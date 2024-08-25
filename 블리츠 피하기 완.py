import pygame
import random

pygame.init()

# 화면 크기 설정
screen_width = 1920
screen_height = 1080
pygame.display.set_mode((screen_width, screen_height))

# 초기 설정
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))


#다시시작
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)

def play_again():
    # play again 이라고 하는 box를 출력 -> 변경 필요
    text = bigfont.render('Play again?', 13, (0, 0, 0))
    textx = SCREEN_WIDTH / 2 - text.get_width() / 2
    texty = SCREEN_HEIGHT / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                               (textx_size + 10, texty_size +
                                                10)))

    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                       SCREEN_HEIGHT / 2 - text.get_height() / 2))

    
    clock = pygame.time.Clock() # 시간을 계산하는 변수
    pygame.display.flip()   # 재시작?

    in_main_menu = True

    while in_main_menu:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                main()

                           
# FPS
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("블리츠 피하기")

# 배경 이미지 불러오기 
background = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/블리츠 피하기/소환사의 협곡.jpg")

def main():

    # 메인 캐릭터 스프라이트 불러오기
    character = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/블리츠 피하기/티모.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width / 2) - (character_width / 2) 
    character_y_pos = screen_height - character_height

    to_x = 0
    to_y = 0

    chracter_speed = 0.9

    # 적 캐릭터
    enemy = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/블리츠 피하기/블리츠.png")
    enemy_size = enemy.get_rect().size
    print(enemy_size)
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_x_pos = 1
    enemy_y_pos = 0
    enemy_speed = 10

    # 승리 스크린
    victory = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/블리츠 피하기/victory1.jpg")


    # 폰트 정의
    game_font = pygame.font.Font(None, 100)

    total_time = 5

    start_ticks = pygame.time.get_ticks()

    # 이벤트 루프
    running = True 
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False 
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:
                    to_x -= chracter_speed 
                elif event.key == pygame.K_RIGHT:
                    to_x += chracter_speed
                elif event.key == pygame.K_UP:
                    to_y -= chracter_speed
                    
                elif event.key == pygame.K_DOWN:
                    to_y += chracter_speed
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

        character_x_pos += to_x * dt 
        character_y_pos += to_y * dt

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width 

        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        enemy_y_pos += enemy_speed
        if enemy_y_pos > screen_height:
            enemy_y_pos = 0 
            enemy_x_pos = random.randint(100, screen_width - enemy_width)

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos
        enemy_rect.top = enemy_y_pos

        if character_rect.colliderect(enemy_rect):
            # 실패화면 띄워야 함.
            play_again()


        screen.blit(background, (0, 0))
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) 
        
        # 타이머 
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 

        timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))
        screen.blit(timer, (220, 120))
        
        if total_time - elapsed_time <= 0:
            screen.blit(victory, (600, 300))
            play_again()


        pygame.display.update()

    pygame.time.delay(1000)

    pygame.quit()   

main()