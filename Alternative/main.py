import pygame
import math

# مقداردهی اولیه
pygame.init()
WIDTH, HEIGHT = 640, 480
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
font = pygame.font.SysFont("Arial", 28)  # فونت کمی ریزتر
small_font = pygame.font.SysFont("Arial", 14)  # فونت ریزتر برای متن "Microsoft Corporation (c)"
pygame.display.set_caption("ویندوز 7 - انیمیشن لوگو")

while running:
    screen.fill((0, 0, 0))
    dt = clock.tick(60) / 1000.0  # بر حسب ثانیه
    time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حرکت دایره‌ها به سمت مرکز و انیمیشن نورها
    for i in range(4):
        angle = angle_offset * i
        progress = min(time / 2.0, 1)  # حرکت دایره‌ها از 0 تا 1
        x = center[0] + math.cos(angle) * radius * (1 - progress)
        y = center[1] + math.sin(angle) * radius * (1 - progress)

        # نورهایی که از پشت حرکت می‌کنند
        glow_radius = 30 * (1 - progress) + 10  # بزرگتر شدن به تدریج
        alpha = int(255 * (1 - progress))  # کاهش شدت رنگ به مرور

        # رسم نور با درخشش
        surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, (*colors[i], alpha), (glow_radius, glow_radius), glow_radius)
        screen.blit(surface, (x - glow_radius, y - glow_radius))

        # رسم دایره مرکزی
        pygame.draw.circle(screen, colors[i], (int(x), int(y)), 15)

    # اگر دایره‌ها به مرکز رسیدن، شروع به ترکیب شدن کن
    if time > 2:  # وقتی که به دو ثانیه رسید
        # تبدیل دایره‌ها به مستطیل‌ها (لوگوی ویندوز ۷)
        progress = min((time - 2) / 3, 1)  # از ۰ تا ۱ تغییر می‌کنه

        # محاسبه ابعاد جدید برای مستطیل‌ها
        rect_size = final_size / 2  # اندازه هر مستطیل
        distance_from_center = final_size * 0.5 * (1 - progress)  # فاصله از مرکز برای مستطیل‌ها

        # رسم ۴ مستطیل برای لوگوی ویندوز ۷
        pygame.draw.rect(screen, colors[0], (center[0] - distance_from_center, center[1] - distance_from_center, rect_size, rect_size))  # قرمز
        pygame.draw.rect(screen, colors[1], (center[0] + distance_from_center, center[1] - distance_from_center, rect_size, rect_size))  # سبز
        pygame.draw.rect(screen, colors[2], (center[0] - distance_from_center, center[1] + distance_from_center, rect_size, rect_size))  # آبی
        pygame.draw.rect(screen, colors[3], (center[0] + distance_from_center, center[1] + distance_from_center, rect_size, rect_size))  # زرد

    # نمایش متن "Starting Windows..."
    text_start = font.render("Starting Windows...", True, (255, 255, 255))
    screen.blit(text_start, (WIDTH // 2 - text_start.get_width() // 2, HEIGHT - 100))  # انتقال به پایین

    # نمایش متن "Microsoft Corporation (c)"
    text_microsoft = small_font.render("PEYMAN-X Corporation (c)", True, (255, 255, 255))
    screen.blit(text_microsoft, (WIDTH // 2 - text_microsoft.get_width() // 2, HEIGHT - 40))  # پایین‌تر از متن اصلی

    pygame.display.flip()

pygame.quit()
