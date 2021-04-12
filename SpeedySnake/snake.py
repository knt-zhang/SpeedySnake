import pygame
import time
import random
import shelve

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
bright_red = (220, 20, 60)
green = (0, 255, 0)
bright_green = (57, 255, 20)
blue = (50, 153, 213)

dp_width = 600
dp_height = 400

dp = pygame.display.set_mode((dp_width, dp_height))
pygame.display.set_caption('Speedy Snake')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)
menu_font = pygame.font.SysFont("bahnschrift", 35)

def pause():
    loop = 1
    message("Paused, press Space or Esc to continue", black)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    loop = 0
        pygame.display.update()
        clock.tick(60)

def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    dp.blit(value, [0, 0])
    d = shelve.open('score.txt', 'w')
    # replace highest score in array if larger
    # if score > d['score']:
    d['score'] = score
    # else:
    #     d['previous'] = score
    d.close()

def highscore():
    d = shelve.open('score.txt')
    score = d['score']  # displays highest score
    value = font_style.render("High Score: " + str(score), True, black)
    dp.blit(value, [100, 170])

<<<<<<< Updated upstream
    previous = d['previous']    # display recent score
    value_2 = font_style.render("Previous Score: " + str(previous), True, black)
    dp.blit(value_2, [100, 200])
=======
    # previous = d['previous']    # display recent score
    # value_2 = font_style.render("Previous Score: " + str(previous), True, black)
    # dp.blit(value_2, [round(dp_width/6), round(dp_height/4)])
>>>>>>> Stashed changes
    d.close()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dp, black, [round(x[0]), round(x[1]), snake_block, snake_block])
        #@2

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dp.blit(mesg, [round(dp_width/6), round(dp_height/3)])

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(dp, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(dp, ic,(x,y,w,h))

    small_text = pygame.font.SysFont("comicsansms",20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ( round(x+(w/2)), round(y+(h/2)) )
    dp.blit(text_surf, text_rect)

def quit_game():
    pygame.quit()
    quit()

<<<<<<< Updated upstream
=======
def controls():
    instruction = 1
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instruction = 0
                if event.key == pygame.K_SPACE:
                    instruction = 0
              
        dp.fill(white)
        value = font_style.render("Controls: ", True, black)
        dp.blit(value, [round(dp_width/6), round(dp_height/4)])

        value_2 = small_text.render("Use the arrow directional keys to move the snake.", True, black)
        dp.blit(value_2, [round(dp_width/6), round(dp_height/3)])

        value_2 = small_text.render("Press Space or Esc to pause.", True, black)
        dp.blit(value_2, [round(dp_width/6), round(dp_height/2.5)])

        value_3 = small_text.render("Return to menu with Space or Esc", True, black)
        dp.blit(value_3, [round(dp_width/6), round(dp_height/1.5)])

        pygame.display.update()

>>>>>>> Stashed changes
def menu():
    intro = 1
    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quit_game()

        dp.fill(white)
        text_surf, text_rect = text_objects("Speedy Snake", menu_font)
        text_rect.center = (round(dp_width/2), round(dp_height/2))
        dp.blit(text_surf, text_rect)

        #@5
        button("Play", 235, 250, 130, 30, green, bright_green, game_loop)
        button("Temp", 235, 290, 130, 30, red, bright_red, quit_game)
        button("Quit", 235, 330, 130, 30, red, bright_red, quit_game)
        
        pygame.display.update()
        clock.tick(15)

def game_loop():
    game_over = False
    game_close = False

    x1 = dp_width / 2
    y1 = dp_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dp_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dp_height - snake_block) / 10.0) * 10
    #@3



    while not game_over:
        while game_close == True:
            # Losing screen
            dp.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", black)
            highscore()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
<<<<<<< Updated upstream
                    if event.key == pygame.K_c:
=======
                        quit_game()
                    if event.key == pygame.K_m:
                        menu()                        
                    if event.key == pygame.K_SPACE:
>>>>>>> Stashed changes
                        game_loop()
                elif event.type == pygame.QUIT: #@6
                    quit_game()
                        
        for event in pygame.event.get():
            # print (event)
            if event.type == pygame.QUIT: #@1 
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_SPACE:
                    pause()

        if x1 >= dp_width or x1 < 0 or y1 >= dp_height or y1 < 0:
            game_close = True
            #@4

        x1 += x1_change
        y1 += y1_change
        dp.fill(blue)   # background color

        pygame.draw.rect(dp, green, [round(foodx), round(foody), snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        your_score(length_of_snake - 1)

        # pygame.draw.rect(dp, blue, [round(foodx), round(foody), snake_block, snake_block])
        # pygame.draw.rect(dp, black, [round(x1), round(y1), snake_block, snake_block])
        pygame.display.update()

        clock.tick(snake_speed)

        if x1 == foodx and y1 == foody: # snake eats food
            foodx = round(random.randrange(0, dp_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dp_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

    quit_game()

menu()


#1 display Surface quit; Replace if event.type == pygame.quit(): by if event.type == pygame.QUIT:
#2 Fixing DeprecationWarning, an integer is required; by using round(*float*) 
#3 food wasn't respawning or dying, added '/ 10.0) * 10.0'
#4 Lost message wasn't appearing, replaced game_over with game_close
#5 Make sure buttons are within display resolution
#6 Added to quit the game at losing screen by clicking on X