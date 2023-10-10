import pygame
pygame.init()
import win32com.client as win
import random
import os
say=win.Dispatch('SAPi.spVoice')

os.chdir("snake-project")
#defining color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
pink=(255,0,255)
blue=(0,0,255)
sky_blue=(0,255,255)
yellow=(255,255,0)
green=(0,255,0)

#defining the variables for height and width of the display 
screen_height=600
screen_width=900

#creating game display
game_window=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Vaibhav's snake game")  #giving the name to the game


#creating a clock for the game
clock=pygame.time.Clock()



#plot the snake in the game display
def plot_snk(game_window,color,snk_lst,snake_size):
    # print(snk_lst) #printing the list of coordinates wherever snake is going
    for x,y in snk_lst:
        #creating the head of the snake
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

 

#selecting font
font1=pygame.font.SysFont(None, 55)#selcting system font with sysfont and by passing arguments None will give it the system 
# and 55 is the size of the font

#creating function to display text on screen
def disp_text(text,color,x,y): #text=what you want to print, color=which color, x,y=coordinates on x and y axis
    screen_text=font1.render(text,True,color) #using render function by passing text,antialiasing='boolean' value,color as parameters
    game_window.blit(screen_text,[x,y])  #using blit function which will update the screen

#creating game loop function
def gameloop():

    #opening high_score.txt file
    with open('hiscore.txt','r') as f:
        hiscore=f.read()

    #creating neccesary variables

    exit_game=False
    game_over=False

    #creating the velocity for the snake
    velocity_x=2
    velocity_y=2

    #defining the size of the snake at the begining of the game
    snake_x=45  #position of snake at x axis
    snake_y=55  #position of snake at y axis
    snake_size=20

    #defining the frame per second for the game
    fps=45

        # for increasing length of the snake
    snk_lst=[]  #list of coordinates
    snk_len=1

    #dimensions and size the food
    food=20 
    food_x=random.randint(5,screen_width/2)  #position of food in x axis and starting randint from 5 so that it wont display at the score area 
    food_y=random.randint(5,screen_height/2)  #position of food in y axis

    #making variable for score
    score=0
    #creating game loop
    while not exit_game:  #running the loop till exit_game not became TRUE
      
      #what has to happen when the game gets over
        if game_over:
            #to over writing the highscore whenever it is broken
            with open('hiscore.txt','w') as f:
                f.write(str(hiscore))  #typcasting high score because it is in string when it gets broke

            game_window.fill(white)  #it will fill all the display with white color
            disp_text('game over! press enter to continue',red,100,300) #using disp_text function for displaying the text that game is over
            #100 is given width for the text and 300 is given height


            #to handle the exit_game event and to restart the game using enter key
            for event in pygame.event.get():  #to get the events or to handle the events
                if event.type==pygame.QUIT:  #gonna be used to quit the game
                    exit_game=True    
                if event.type==pygame.KEYDOWN: #making the key
                    if event.key==pygame.K_RETURN:   #using this for press enter button
                        gameloop()  #whenever enter button will be pressed the game will restart
        else:
            for event in pygame.event.get():  #to get the events or to handle the events
                if event.type==pygame.QUIT:  #gonna be used to quit the game
                    exit_game=True    

                #defining the movement for the arrow keys
                
                if event.type==pygame.KEYDOWN:  #making the event.key
                    
                    if event.key==pygame.K_RIGHT:  #for right arrow key to move snake in right
                        # snake_x = snake_x+10   #moving the snake position by the value of 10
                        velocity_x = 5  #velocity gonna be increase for right side so that it can move toward right side till another key got pressed
                        velocity_y = 0  #we have to set the velocity for y axis on 0 so that it wont move diagonally

                    elif event.key==pygame.K_LEFT:  #for left arrow key to move snake in left
                        velocity_x = -5  #velocity gonna be decrease on x axis so that it can move toward left side till another key got pressed
                        velocity_y = 0   #we have to set the velocity for y axis on 0 so that it wont move diagonally

                    elif event.key==pygame.K_UP:  #for UP arrow key to move the snake in upward direction
                        velocity_y = -5  #velocity gonna be decrease on y axis so that it can move toward upper side till another key got pressed
                        velocity_x = 0   #we have to set the velocity for x axis on 0 so that it wont move diagonally

                    elif event.key==pygame.K_DOWN:  #for down arrow key to move the snake in downward direction
                        velocity_y = 5  #velocity gonna be increase on y axis so that it can move toward down side till another key got pressed
                        velocity_x = 0  #we have to set the velocity for x axis on 0 so that it wont move diagonally

        # moving the snake's position by adding velocity into it
            snake_x=snake_x + velocity_x
            snake_y=snake_y + velocity_y

            #creating score for the game
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:  #using abs function for getting the absolute value
                #here we are taking absolute value because whenever snake comes near to atleast 5 unit distance on the x axis and y axis or we can say less than 6
                #so score will get increase and food will get another place in the display
                score = score + 10
                # print('score:-',score) #used to print the score in the terminal not on the game display
                food_x=random.randint(0,screen_width/2)  #position of food in x axis after snake eats the food
                food_y=random.randint(0,screen_height/2)  #position of food in y axis after snake eats the food

                snk_len= snk_len + 3  #increasing the length of the snake

                #to check wheather the current score is greater than high score or not
                if score>int(hiscore):
                    hiscore=score  #if it get greater than the high score then high score will became current score


            game_window.fill(green)    #using colors for the display window


            #displaying the score and high score on the game display
            disp_text(f"score:-{score} high score:- {hiscore}",black,5,5) #using disp_text function by passing text string,color,x axis coordinates,y axis coordinates
            
            #creating the food for the snake
            pygame.draw.rect(game_window,yellow,[food_x,food_y,food,food])

            #storing the coordinates for x and y in the list head to start the game
            head=[]
            head.append(snake_x) #taking coordinates for x axis and appending them in head
            head.append(snake_y) #taking coordinates for y axis and appending them in head
            snk_lst.append(head)  #putting all those coordinates in snk_lst from head
            
            #deleting the head of the snake whenever the length of snake  list is greater than length of snake's length
            if len(snk_lst)>snk_len:  #we are using it beacuse the length of snake will increase whenever it will move 
                del snk_lst[0]  #so to stop that we have to delete it immediately so that length of snake wont get increase untill it eats bthe food
            
            #to end the game whenever collision gets occur within the snake's body
            if head in snk_lst[:-1]: #to check the condition including all the elements except the last element means excluding the head 
                #if head is avilble in the list the the game will get over
                game_over=True

            #to end the game whenever the collision occur with wall
            if snake_x>screen_width or snake_x<0 or snake_y<0 or snake_y>screen_height:
                game_over= True
                # print('game over') #used to print game over in the terminal

            #to create the snake
            plot_snk(game_window,red,snk_lst,snake_size)

        pygame.display.update()   #updating the changes
        clock.tick(fps)   #setting the frames per second in the game using game clock

    # say.speak(f'score is {score}')

    #to quit the game
    pygame.quit()
    quit()

gameloop()