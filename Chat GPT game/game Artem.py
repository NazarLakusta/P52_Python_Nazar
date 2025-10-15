import pygame, random, sys

pygame.init()
W, H = 640, 480
s = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
player = pygame.Rect(W // 2 - 20, H - 60, 40, 40)
bullets = []
enemies = []
score = 0
lives = 3
spawn_timer = 0
speed = 5
shoot_cool = 0
running = True
while running:
    dt = clock.tick(60) / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= int(speed)
    if keys[pygame.K_RIGHT]: player.x += int(speed)
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if shoot_cool <= 0:
            bullets.append(pygame.Rect(player.centerx - 3, player.y - 10, 6, 10))
            shoot_cool = 0.25
    shoot_cool = max(0, shoot_cool - dt)
    spawn_timer += dt
    if spawn_timer > 0.7:
        spawn_timer = 0
        x = random.randint(20, W - 40)
        enemies.append([x, -30, random.choice([1, 1, 2])])
    for b in bullets[:]:
        b.y -= 300 * dt
        if b.y < -20: bullets.remove(b)
    for en in enemies[:]:
        en[1] += 100 * en[2] * dt
        ex, ey = en[0], en[1]
        if ey > H + 40:
            enemies.remove(en)
            lives -= 1
            if lives <= 0: running = False
    for b in bullets[:]:
        for en in enemies[:]:
            er = pygame.Rect(en[0] - 15, en[1] - 15, 30, 30)
            if b.colliderect(er):
                try:
                    bullets.remove(b)
                except:
                    pass
                try:
                    enemies.remove(en)
                except:
                    pass
                score += 10
                break
    for en in enemies[:]:
        er = pygame.Rect(en[0] - 15, en[1] - 15, 30, 30)
        if player.colliderect(er):
            enemies.remove(en)
            lives -= 1
            if lives <= 0: running = False
    if score > 50: speed = 6
    if score > 150: speed = 7
    s.fill((12, 12, 20))
    pygame.draw.rect(s, (50, 200, 80), player)
    for b in bullets: pygame.draw.rect(s, (255, 255, 100), b)
    for en in enemies:
        pygame.draw.circle(s, (200, 60, 60), (int(en[0]), int(en[1])), 16)
    txt = font.render(f"Score: {score}  Lives: {lives}", True, (240, 240, 240))
    s.blit(txt, (10, 10))
    if not running:
        over = font.render(f"Game Over! Final score: {score}", True, (255, 200, 200))
        s.blit(over, (W // 2 - over.get_width() // 2, H // 2))
        pygame.display.flip()
        pygame.time.wait(1500)
        break
    pygame.display.flip()
pygame.quit()
sys.exit()
