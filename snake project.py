# import modules necessary for the game 
import random 

# used ranndom becuse show the food in the screan randomly 
import curses

# initialize the curses library to create our screan
screan = curses.initscr()

# Hide the mouse cursor
curses.curs_set(0)

# getmax screan height and width 
screan_height , screan_width = screan.getmaxyx()


# create a new widow 
window = curses.newwin(screan_height,screan_width,0,0)

# Allow window to recive input from keyboard 
window.keypad(1)

# set the delay for updating the screan 
window.timeout(130)

# set the x,y coordinates of the initial postion of snake's head 
snake_x = screan_width // 4 
snake_y = screan_height // 2

# define the initial position of snake body
snake = [
    [snake_y,snake_x],
    [snake_y,snake_x-1],
    [snake_y,snake_x-2],        
]

# create the food in the middle window 
food = [screan_height//2,screan_width //2] 

# add food by using PI character from curses module 
window.addch(food[0], food[1], curses.ACS_PI)

# set initial movement direction to right 
key = curses.KEY_RIGHT

# create  main game loop that loops forever untill player loses or quits the game 
while True :
# get the next key pressd by user 
    next_key = window.getch() 
# if user doesn't input anything, Key remains same, else key will be set to the new preesed key 
# with Pythonic way to write if condition :       
    key = key if next_key == -1  else next_key 

# check if snake collided with the walls or itself 
    if snake[0][0] in [0, screan_height] or snake[0][1] in [0,screan_width] or snake[0] in snake[1:] :

        curses.endwin() # closeing the window
        quit() # exit the program
# set the new position of snake  head based on the direction  
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN : 
        new_head[0] += 1 
    elif key == curses.KEY_UP : 
        new_head[0] -= 1 
    elif key == curses.KEY_RIGHT : 
        new_head[1] += 1 
    elif key == curses.KEY_LEFT : 
        new_head[1] -= 1

# insert the new head to the frist position of snake list 
        snake.insert(0, new_head)         
# check the snake eat food ?
        if snake[0] == food :
            food = None # remove food of snake ate it 

# while food is removed , generate new food in a random place on screan             
            while food is None :
                new_food = [ 
                    random.randint(1, screan_height-1) , 
                    random.randint(1, screan_width-1)  
                ]
# set the food to new food if new food genrated is not in snake body and add it to screan 
                food = new_food if new_food not in snake else None
            window.addch(food[0], food[1],curses.ACS_PI) 
# otherwise ramove the last seqmant of snake body         
        else :
            tail = snake.pop()  
            window.addch(tail[0], tail[1],' ')               
        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)