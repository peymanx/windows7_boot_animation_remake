import pygame
import math

# مقداردهی اولیه
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Windows 98 Boot Animation")  # تغییر عنوان پنجره
clock = pygame.time.Clock()

# رنگ‌های نوار پایین و پس‌زمینه
background_color = (0, 0, 0)
blue_color = (0, 0, 255)
text_color = (255, 255, 255)

# تنظیمات فونت
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 14)

# تنظیمات Pixel Blitting
pixel_size = 5  # اندازه پیکسل برای blitting
blit_speed = 1  # سرعت حرکت پیکسل‌ها

# موقعیت نوار پایین صفحه
bar_height = 25
bar_top = HEIGHT - bar_height

# بارگذاری تصویر پس‌زمینه
bg_image = pygame.image.load("win98.jpg")  # نام فایل تصویر پس‌زمینه را وارد کنید
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))  # تغییر سایز تصویر به اندازه صفحه

time = 0
running = True
progress = 0  # درصد پیشرفت
loading_text = "Please Wait..."

while running:
    screen.fill(background_color)
    
    # نمایش تصویر پس‌زمینه
    screen.blit(bg_image, (0, 0))

    dt = clock.tick(60) / 1000.0  # بر حسب ثانیه
    time += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # شبیه‌سازی انیمیشن بارگذاری با Pixel Blitting
    for i in range(0, WIDTH, pixel_size):
        # ایجاد افکت حرکت پیکسل‌ها در نوار پایین
        if i < progress:
            pygame.draw.rect(screen, blue_color, (i, bar_top, pixel_size, bar_height))

    # نمایش متن "Starting Windows..."
    text_start = font.render("Starting Windows...", True, text_color)
    screen.blit(text_start, (WIDTH // 2 - text_start.get_width() // 2, HEIGHT // 3))

    # نمایش متن "Microsoft Corporation (c)"
    text_microsoft = small_font.render("Microsoft Corporation (c)", True, text_color)
    screen.blit(text_microsoft, (WIDTH // 2 - text_microsoft.get_width() // 2, HEIGHT - 40))

    # پیشرفت بارگذاری
    progress = int((time % 5) * blit_speed * WIDTH)  # سرعت پیشرفت با توجه به زمان

    # افکت Pixel Blitting در نوار پایین
    pygame.display.flip()

pygame.quit()
