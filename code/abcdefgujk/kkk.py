import pygame
import sys

# 초기화
pygame.init()

# 화면 만들기
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("나의 첫 파이게임")

# 색 정의
WHITE = (211,211,211)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.display.flip()









