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

def get_block_width():
    """현재 블록의 실제 가로 크기 계산"""
    max_width = 0
    for row in current_block[rotation]:
        width = sum(row)  # 1이 있는 개수만 카운트
        max_width = max(max_width, width)
    return max_width

def get_block_height():
    """현재 블록의 실제 세로 크기 계산"""
    max_height = 0
    for col in range(len(current_block[rotation][0])):  # 블록의 각 열을 확인
        col_height = sum(row[col] for row in current_block[rotation])  # 세로 방향으로 1 개수 세기
        max_height = max(max_height, col_height)
    return max_height

def handle_movement(event):
    """블록 이동 처리"""
    global block_x, block_y  # 블록 위치 변수 사용
    block_width = get_block_width()  # 현재 블록의 실제 가로 크기
    block_height = get_block_height()  # 현재 블록의 실제 세로 크기

    if event.key == pygame.K_LEFT:  # 왼쪽 이동
        if block_x > 0:
            block_x -= 1
    elif event.key == pygame.K_RIGHT:  # 오른쪽 이동
        if block_x + block_width < ROW_CELL_COUNT:
            block_x += 1
    elif event.key == pygame.K_DOWN:  # 아래로 한 칸 이동
        if block_y + block_height < COL_CELL_COUNT:  # 블록 높이를 고려한 제한
            block_y += 1
    print(f"블록 좌표 - X: {block_x}, Y: {block_y}")

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
            elif event.type == pygame.KEYDOWN:
                handle_movement(event)  # 키 입력 처리

        pygame.display.flip()
        clock.tick(60)  # 초당 60 프레임 설정

    pygame.quit()

if __name__ == "__main__":
    main()
