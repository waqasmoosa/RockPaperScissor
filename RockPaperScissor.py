import pygame,sys
import random


pygame.init()
pygame.font.init()
random.randint(0,3)

screen_width = 800
screen_height = 600

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
YELLOW   = (  255,   216, 59)

img_0 = pygame.image.load("rock.png")
img_1 = pygame.image.load("paper.png")
img_2 = pygame.image.load("scissor.png")

img_list = [img_0, img_1, img_2]

#comp_choice = random.choice(img_list)

comp_score = 0
player_score = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ROCK,PAPER,SCISSOR")

def start_screen():

    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    choice_screen()

        screen.fill(YELLOW)            
        main_font = pygame.font.SysFont("Calibri", 72, True, False)
        sub_font  = pygame.font.SysFont("Calibri", 30, True, False)
        nextscreen_font = pygame.font.SysFont("Calibri", 20, True, False)

        text = main_font.render("Rock,Paper,Scissor", True, WHITE)
        rocktxt = sub_font.render("This Is Rock, Rock can break Scissor", True, WHITE)
        papertxt = sub_font.render("This Is Paper, Paper can wrap the Rock", True, WHITE)
        scissortxt = sub_font.render("This Is Scissor, Scissor can cut Paper", True, WHITE)
        entertxt = nextscreen_font.render("Press Enter For Next Screen", True, WHITE)

        screen.blit(img_0, (50,110))
        screen.blit(img_1, (50,270))
        screen.blit(img_2, (50,450))
    
        screen.blit(text,[140,20])
        screen.blit(rocktxt, [200,170])
        screen.blit(papertxt, [200,330])
        screen.blit(scissortxt, [200,510])
        screen.blit(entertxt, [550,575])
        
        pygame.display.flip()

#RPS CHOICE SCREEN
def choice_screen():

    middle = True

    while middle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_choice = img_list[0]
                    game_screen(player_choice)
                if event.key == pygame.K_2:
                    player_choice = img_list[1]
                    game_screen(player_choice)
                if event.key == pygame.K_3:
                    player_choice = img_list[2]
                    game_screen(player_choice)
                

        screen.fill(YELLOW)
        main_font = pygame.font.SysFont("Calibri", 72, True, False)
        sub_font  = pygame.font.SysFont("Calibri", 20, True, False)
        nextscreen_font = pygame.font.SysFont("Calibri", 40, True, False)

        text = main_font.render("Select Your Choice!", True, WHITE)
        rocktxt = sub_font.render("Press 1, for Rock", True, WHITE)
        papertxt = sub_font.render("Press 2, for Paper", True, WHITE)
        scissortxt = sub_font.render("Press 3, for Scissor", True, WHITE)
        nextscreentxt = nextscreen_font.render("Select the choice to move forward", True, WHITE)

        screen.blit(img_0, (100,250))
        screen.blit(img_1, (350,250))
        screen.blit(img_2, (600,250))

        screen.blit(text,[115,50])
        screen.blit(rocktxt, [100,390])
        screen.blit(papertxt, [340,390])
        screen.blit(scissortxt, [590,390])
        screen.blit(nextscreentxt, [120,500])
        
        pygame.display.flip()

#GAME SCREEN
def game_screen(player_choice):

    state = 0

    comp_choice = random.choice(img_list)
    
    middle = True
    while middle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    welcome_screen()
                if event.key == pygame.K_r:
                    if state == 0:
                        state = 10

        if state == 10:
            choice_screen()

           
        screen.fill(YELLOW)
        screen.blit(comp_choice,[500, 200])
        screen.blit(player_choice, [200,200])
        game_logic(player_choice, comp_choice)
        
        
        pygame.display.flip()

#GAME LOGIC FOR RPS
def game_logic(player_choice, comp_choice):

    start = True
    sub_font = pygame.font.SysFont("Calibri", 50, True, False)
    small_font = pygame.font.SysFont("Calibri", 25, True, False)
    txt1 = sub_font.render("GAME TIE", True, WHITE)
    txt2 = sub_font.render("YOU WIN", True, WHITE)
    txt3 = sub_font.render("YOU LOSE", True, WHITE)
    retry_txt = small_font.render("Press 'R' to Retry", True, WHITE)
    nxt_txt = small_font.render("Press Enter for Next Screen", True, WHITE)


        
    if comp_choice == player_choice:
        screen.blit(txt1, [300,400])
    elif player_choice == img_list[0]:
        if comp_choice == img_list[1]:
            screen.blit(txt3, [300,400])
        else:
            screen.blit(txt2, [300,400])
    elif player_choice == img_list[1]:
        if comp_choice == img_list[2]:
            screen.blit(txt3, [300,400])
        else:
            screen.blit(txt2, [300,400])
    elif player_choice == img_list[2]:
        if comp_choice == img_list[0]:
            screen.blit(txt3, [300,400])
        else:
            screen.blit(txt2, [300,400])

    screen.blit(retry_txt,[15,550])
    screen.blit(nxt_txt,[500,550])

    

#END GAME SCREEN   
def welcome_screen():

    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(YELLOW)        
        main_font = pygame.font.SysFont("Calibri", 115, True, False)
        sub_font = pygame.font.SysFont("Calibri", 40, True, False)
    
        text = main_font.render("WELCOME", True, WHITE)
        text1 = sub_font.render("Made By Waqas Moosa", True, WHITE)
        text2 = sub_font.render("ROCK,PAPER,SCISSOR", True, WHITE)
    
        screen.blit(text, [150,200])
        screen.blit(text1, [210,300])
        screen.blit(text2, [220,350])

        pygame.display.flip()
    

#MAIN PROGRAM
start_screen()
