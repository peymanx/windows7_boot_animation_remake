import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# رنگ‌ها
BG_COLOR = (0, 0, 128)        # پس‌زمینه آبی تیره
TEXT_COLOR = (255, 255, 255)  # متن سفید
BAR_COLOR = (0, 120, 215)     # آبی ویندوزی
BOX_WIDTH = 30
BOX_HEIGHT = 10

# فونت
font = pygame.font.SysFont("Arial", 24)

# محل قرارگیری نوار بارگذاری
bar_x = WIDTH // 2 - 100
bar_y = HEIGHT // 2 + 50

# تنظیمات مستطیل‌های انیمیشن
box_count = 5
spacing = 10
speed = 100  # پیکسل بر ثانیه
offset = 0.0

while True:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # نوشتن متن بوت
    text = font.render("Windows 2000 Professional", True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))

    # انیمیشن مستطیل‌ها
    offset += speed * dt
    total_width = (BOX_WIDTH + spacing) * box_count
    for i in range(box_count):
        x = (bar_x + i * (BOX_WIDTH + spacing) + int(offset)) % total_width
        pygame.draw.rect(screen, BAR_COLOR, (x + bar_x, bar_y, BOX_WIDTH, BOX_HEIGHT))

    pygame.display.flip()
