import pygame
import math

# مقداردهی اولیه
#"color flames" animation.
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# رنگ‌های نورها (قرمز، سبز، آبی، زرد)
colors = [(255, 0, 0), (0, 200, 0), (0, 128, 255), (255, 255, 0)]
radius = 100
center = (WIDTH // 2, HEIGHT // 2 - 50)  # انتقال مرکز انیمیشن به بالاتر
angle_offset = math.pi / 2  # برای چرخش متقارن

time = 0
running = True
final_size = 100  # اندازه نهایی برای لوگو ویندوز

# تنظیمات فونت
font = pygame.font.SysFont("Arial", 26)  # فونت کمی ریزتر
small_font = pygame.font.SysFont("Arial", 14)  # فونت ریزتر
pygame.display.set_caption("ویندوز 7 - انیمیشن لوگو")

while running:
    screen.fill((0, 0, 0))
    dt = clock.tick(60) / 1300.0  # بر حسب ثانیه
    time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حرکت دایره‌ها به سمت مرکز و انیمیشن نورها
    for i in range(4):
        angle = angle_offset * i
        progress = min(time / 2.0, 1)  # حرکت از 0 تا 1
        x = center[0] + math.cos(angle) * radius * (1 - progress)
        y = center[1] + math.sin(angle) * radius * (1 - progress)

        # درخشش نورها
        glow_radius = 30 * (1 - progress) + 10
        alpha = int(255 * (1 - progress))
        surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (*colors[i], alpha), (glow_radius, glow_radius), int(glow_radius))
        screen.blit(surface, (x - glow_radius, y - glow_radius))

        # رسم دایره اصلی
        pygame.draw.circle(screen, colors[i], (int(x), int(y)), 15)

    # افکت نورانی هنگام تبدیل
    if 2 < time < 2.3:
        flash_progress = (time - 2) / 0.3
        flash_alpha = int(255 * (1 - flash_progress))
        flash_radius = 30 + 100 * (1 - flash_progress)
        flash_surface = pygame.Surface((flash_radius * 2, flash_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(flash_surface, (255, 255, 255, flash_alpha), (flash_radius, flash_radius), int(flash_radius))
        screen.blit(flash_surface, (center[0] - flash_radius, center[1] - flash_radius))
        
    if 2.1 < time < 2.2:
        flash_progress = (time - 2) / 0.3
        flash_alpha = int(255 * (1 - flash_progress))
        flash_radius = 60 + 100 * (1 - flash_progress)
        flash_surface = pygame.Surface((flash_radius * 2, flash_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(flash_surface, (255, 255, 255, flash_alpha), (flash_radius, flash_radius), int(flash_radius))
        screen.blit(flash_surface, (center[0] - flash_radius, center[1] - flash_radius))
        
    if 2.2 < time < 2.1:
        flash_progress = (time - 2) / 0.3
        flash_alpha = int(255 * (1 - flash_progress))
        flash_radius = 100 + 100 * (1 - flash_progress)
        flash_surface = pygame.Surface((flash_radius * 2, flash_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(flash_surface, (255, 255, 255, flash_alpha), (flash_radius, flash_radius), int(flash_radius))
        screen.blit(flash_surface, (center[0] - flash_radius, center[1] - flash_radius))
        
    if 2.3 < time < 2.1:
        flash_progress = (time - 2) / 0.3
        flash_alpha = int(255 * (1 - flash_progress))
        flash_radius = 150 + 100 * (1 - flash_progress)
        flash_surface = pygame.Surface((flash_radius * 2, flash_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(flash_surface, (255, 255, 255, flash_alpha), (flash_radius, flash_radius), int(flash_radius))
        screen.blit(flash_surface, (center[0] - flash_radius, center[1] - flash_radius))

    # تبدیل دایره‌ها به لوگوی ویندوز
    if time > 2:
        progress = min((time - 2) / 3, 1)
        logo_size = final_size * progress
        if logo_size > final_size:
            logo_size = final_size

        rect_size = logo_size / 2
        # رسم ۴ مربع رنگی
        pygame.draw.rect(screen, colors[0], (center[0] - logo_size / 2, center[1] - logo_size / 2, rect_size, rect_size))  # قرمز
        pygame.draw.rect(screen, colors[1], (center[0], center[1] - logo_size / 2, rect_size, rect_size))               # سبز
        pygame.draw.rect(screen, colors[2], (center[0] - logo_size / 2, center[1], rect_size, rect_size))               # آبی
        pygame.draw.rect(screen, colors[3], (center[0], center[1], rect_size, rect_size))                               # زرد

    # متن "Starting Windows..."
    text_start = font.render("Starting Windows...", True, (255, 255, 255))
    screen.blit(text_start, (WIDTH // 2 - text_start.get_width() // 2, HEIGHT - 100))

    # متن "PEYMAN-X Corporation (c)"
    text_microsoft = small_font.render("(c) PEYMAN-X Corporation", True, (255, 255, 255))
    screen.blit(text_microsoft, (WIDTH // 2 - text_microsoft.get_width() // 2, HEIGHT - 40))

    pygame.display.flip()

pygame.quit() 
