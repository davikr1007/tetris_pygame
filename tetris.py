import pygame
import random
from blocks import Blocks  # 블록 데이터 가져오기

# 화면 크기
ROW_CELL_COUNT = 10 # 가로 10칸
COL_CELL_COUNT = 20 # 세로 20칸
CELL_SIZE = 30  # 한 칸 크기

DISPLAY_WIDTH, DISPLAY_HEIGHT = 300, 600  # 가로 10칸, 세로 20칸 (각 블록 30x30)

# 색상 설정
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)  # 블록 색상

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Tetris")

# 블록 초기 위치
block_x = 3 # 가로 4번째 칸에서 시작
block_y = 0  # 맨 위에서 시작
current_block = random.choice(list(Blocks.BLOCKS.values()))  # 랜덤 블록 선택
rotation = 0  # 초기 회전 상태

def draw_board():
    """10x20 보드 그리기"""
    screen.fill(BLACK)  # 배경을 검은색으로 설정
    for row in range(20):  # 세로 20칸
        for col in range(10):  # 가로 10칸
            pygame.draw.rect(screen, GREY, 
                            (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 
                            1)  # 회색 테두리로 보드 그리기

def draw_block():
    """블록 그리기"""
    for row_index, row in enumerate(current_block[rotation]):
        for col_index, cell in enumerate(row):
            if cell:  # 1인 경우만 그림
                x = (block_x + col_index) * CELL_SIZE
                y = (block_y + row_index) * CELL_SIZE
                # 블록 채우기
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
                # 테두리 추가
                pygame.draw.rect(screen, GREY, (x, y, CELL_SIZE, CELL_SIZE), 1)
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)  # 화면 초기화
        draw_board()  # 보드 그리기
        draw_block()  # 블록 그리기

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)  # 초당 60 프레임 설정

    pygame.quit()

if __name__ == "__main__":
    main()
