import pygame

# 화면 크기
ROW_CELL_COUNT = 10 # 가로 10칸
COL_CELL_COUNT = 20 # 세로 20칸

CELL_SIZE = 30  # 한 칸 크기

DISPLAY_WIDTH, DISPLAY_HEIGHT = 300, 600  # 가로 10칸, 세로 20칸 (각 블록 30x30)

# 색상 설정
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
WHITE = (255, 255, 255)

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Tetris Board")

def draw_board():
    """10x20 보드 그리기"""
    screen.fill(BLACK)  # 배경을 검은색으로 설정
    for row in range(20):  # 세로 20칸
        for col in range(10):  # 가로 10칸
            pygame.draw.rect(screen, GREY, 
                            (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 
                            1)  # 회색 테두리로 보드 그리기

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)  # 화면 초기화
        draw_board()  # 보드 그리기
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)  # 초당 60 프레임 설정

    pygame.quit()

if __name__ == "__main__":
    main()
