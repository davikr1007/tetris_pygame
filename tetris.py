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

def is_valid_position(new_x, new_y, new_rotation):
    """블록이 보드 내에 있는지 확인"""
    block_shape = current_block[new_rotation]
    for row_index, row in enumerate(block_shape):
        for col_index, cell in enumerate(row):
            if cell:
                board_x = new_x + col_index
                board_y = new_y + row_index
                if board_x < 0 or board_x >= ROW_CELL_COUNT:  # 왼쪽/오른쪽 벽 체크
                    return False
                if board_y >= COL_CELL_COUNT:  # 바닥 체크
                    return False
    return True

def handle_movement(event):
    """블록 이동 처리 (벽 충돌 방지)"""
    global block_x, block_y

    if event.key == pygame.K_LEFT:  # 왼쪽 이동
        if is_valid_position(block_x - 1, block_y, rotation):
            block_x -= 1
    elif event.key == pygame.K_RIGHT:  # 오른쪽 이동
        if is_valid_position(block_x + 1, block_y, rotation):
            block_x += 1
    elif event.key == pygame.K_DOWN:  # 아래 이동
        if is_valid_position(block_x, block_y + 1, rotation):
            block_y += 1
    elif event.key == pygame.K_UP:  # 회전
        handle_rotation()

    print(f"블록 좌표 - X: {block_x}, Y: {block_y}, 회전: {rotation}")

def handle_rotation():
    """블록 회전 처리 (벽 충돌 방지)"""
    global rotation, block_x

    new_rotation = (rotation + 1) % 4  # 90도 회전

    # 1. 회전이 가능한지 먼저 체크
    if is_valid_position(block_x, block_y, new_rotation):
        rotation = new_rotation  # 회전 적용
    else:
        # 2. 벽을 넘으면 이동하면서 회전 (Wall Kick 적용)
        if is_valid_position(block_x - 1, block_y, new_rotation):
            block_x -= 1
            rotation = new_rotation
        elif is_valid_position(block_x + 1, block_y, new_rotation):
            block_x += 1
            rotation = new_rotation
        elif is_valid_position(block_x - 2, block_y, new_rotation):
            block_x -= 2
            rotation = new_rotation
        elif is_valid_position(block_x + 2, block_y, new_rotation):
            block_x += 2
            rotation = new_rotation

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
