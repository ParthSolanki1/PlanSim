#importing the pygame library
import pygame
import random

#initiallizing pygame libraries and text libraries
pygame.init()
pygame.font.init()

#class for user_input
class user_input:
    """
    This is a class that takes user input from the player. On screen user input is not coded within pygame,
    therefore this class is used inorder to take user input from the player
    """
    #initialiing the class and asking for a temporary list that the user input is stored in
    def __init__(self, lis):
        self.lis = lis

    #this is a method in this class that takes key presses (on numbers) made by the user and
    #places in the temporary list
    def events(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: #if 1 is pressed '1' is added to temporary list
                self.lis.append("1")
            elif event.key == pygame.K_2: #if 2 is pressed '2' is added to temporary list
                self.lis.append("2")
            elif event.key == pygame.K_3: #if 3 is pressed '3' is added to temporary list
                self.lis.append("3")
            elif event.key == pygame.K_4:#if 4 is pressed '4' is added to temporary list
                self.lis.append("4")
            elif event.key == pygame.K_5:#if 5 is pressed '5' is added to temporary list
                self.lis.append("5")
            elif event.key == pygame.K_6:#if 6 is pressed '6' is added to temporary list
                self.lis.append("6")
            elif event.key == pygame.K_7:#if 7 is pressed '7' is added to temporary list
                self.lis.append("7")
            elif event.key == pygame.K_8:#if 8 is pressed '8' is added to temporary list
                self.lis.append("8")
            elif event.key == pygame.K_9:#if 9 is pressed '9' is added to temporary list
                self.lis.append("9")
            elif event.key == pygame.K_0:#if 0 is pressed '0' is added to temporary list
                self.lis.append("0")
            elif event.key == pygame.K_MINUS:#if - is pressed '-' is added to temporary list
                self.lis.append("-")

#creating a font that is used throughout all text
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#Set the width and height of the screen [width, height])
size = (900, 504)
screen = pygame.display.set_mode(size)

#Creating boolean variables required for the code
carryOn = True #allows screen to stay up until player presses close or invalid input is entered
start = True #allows a temporary list to be created at a particular time
button = False #used so that pressing a key will not activate all the other functions

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#creating all variables that will be needed for the code
screen_change = 0 #variable that determines if screen needs to be changed
input_num = 0     #variable that determines if the input needs to change
num_planets = []  #list that temporarily holds number of planets
mass = []         #list that temporarily holds mass of planets
all_mass = []     #list that holds all masses of all planets
radius = []       #list that temporarily holds radius of planets
all_radius = []   #list that holds the radius' of all planets
x_velocity = []    #list that temporarily holds x-velocity of the ship
y_velocity = []   #list that temporarily holds y-velocity of the ship
plan_x_list = []
plan_y_list = []

for i in range(10):
    plan_x = random.randint(0, 800)
    plan_x_list.append(plan_x)
    plan_y = random.randint(0, 400)
    plan_y_list.append(plan_y)

#loading in images
background = pygame.image.load("start.png")      #1st screen
welcome = pygame.image.load("Welcome!.png")      #the intro screen
select = pygame.image.load("Selection.png")      #the number of planets screen
green_box = pygame.image.load("green box.png")   #the input box
planet_details = pygame.image.load("planet.png") #the planet mass and radius screen
ship_details = pygame.image.load("Ship.png")     #the ships veloity screen
star_sky = pygame.image.load("star_sky.jpg")
planet_blue = pygame.image.load("planet_blue.png")
planet_red = pygame.image.load("planet_red.png")
planet_brown = pygame.image.load("planet_brown.png")
planet_yellow = pygame.image.load("planet_yellow.png")
rocket = pygame.image.load("rocket.png")
rocket_thrust_left = pygame.image.load("thrust_left.png")
rocket_thrust_right = pygame.image.load("thrust_right.png")
rocket_thrust_down = pygame.image.load("thrust_down.png")
rocket_thrust_up = pygame.image.load("thrust_up.png")

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

    #creating the starting sreen
    if screen_change == 0: #the initial value of screen change is 0
        #blitting in the original background screen
        screen.blit(background, [0,0])

        #changing screen if player presses any key
        if screen_change == 0 and event.type == pygame.KEYUP:
            #initially the boolean variable 'button' is false
            if not button:
                #changes the screen
                screen_change += 1

            #as loong as key is pressed 'button' will be True
            #so that it doesn't change screen until a key is pressed again
            button = True
        else:
            #after key is let go, you can change screen again
            button = False

    #displaying an instruction/welcome screen
    if screen_change == 1:
        # The name of the window
        pygame.display.set_caption("Space Simulation")

        # This is to set the welcome screen
        screen.blit(welcome, [0, 0])

        # changing screen if player presses any key
        if screen_change == 1 and event.type == pygame.KEYUP:
            # initially the boolean variable 'button' is false
            if not button:
                #changes screen
                screen_change += 1

            # as loong as key is pressed 'button' will be True
            # so that it doesn't change screen until a key is pressed again
            button = True
        else:
            # after key is let go, you can change screen again
            button = False

    #displaying screen in which you can choose number of planets
    if screen_change == 2:
        #setting size of screen
        screen = pygame.display.set_mode(size)

        # The name of the window
        pygame.display.set_caption("Space Simulation; Number of planets")

        #blitting the background
        screen.blit(select, [0, 0])

        #taking user input for number of planets
        if input_num == 0:
            #blitting a green box tha indicates user input
            screen.blit(green_box, [406, 170])

            # putting user input
            input = user_input(num_planets) #initializing class
            input.events() #calling the method

            #deletes last nuber if backspace is pressed
            if event.type == pygame.KEYDOWN: #checks if key is pressed down
                if event.key == pygame.K_BACKSPACE: #cheks if the key is backspace
                    num_planets = num_planets[:-1] #deletes last letter

            # printing the user input
            display_num_planets = myfont.render("".join(num_planets), False, (255, 255, 255)) #rendering text
            screen.blit(display_num_planets, (423, 171)) #blitting text

            #checking if input is good and moving on
            number_of_planets = "".join(num_planets) #turns the temporary list into a string number in permanent variable
            if event.type == pygame.KEYDOWN: #checks if key is pressed
                if event.key == pygame.K_SPACE: #checks if key is spaebar
                    #if number is negative the screen will close and will give warning
                    if "-" in number_of_planets:
                        print "Invalid input! Number of planets must be positive!" #warning
                        carryOn = False #closing screen
                    #if number is > 10 warning is given and screen closes
                    if int(number_of_planets) > 10:
                        print "Invalid Input! Maximum of 10 planets!" #warning
                        carryOn = False #closing screen
                    #making sure that pressing a key does not change multiple screens
                    if not button: #initially button is false and will only change if it is false
                        screen_change = 3 #change screen
                        input_num = 1 #indicating that the input will change
                        number_of_planets = int(number_of_planets) #turning the number of planets to integer
                    button = True # until button is pressed down screen will not change
            else:
                button = False #once let go screen can be changed

    #taking user input for mass and radius of each planet
    if screen_change == 3:
        # setting size of screen
        screen = pygame.display.set_mode(size)

        # The name of the window
        pygame.display.set_caption("Space Simulation; Selection of Planets")

        # This is to set the background screen
        screen.blit(planet_details, [0, 0])

        #initially setting up a temporary variable
        if start:
            temp = number_of_planets #temp variable = number of planets
            start = False #this is so the temporary variable is not recreated

        #taking inputs for all planets
        if temp > 0:
            #printing the number of the planet that the player is entering information for
            show_planet = (number_of_planets - temp) + 1 #finding the number
            display_planet = myfont.render(str(show_planet), False, (255, 255, 255)) #redering number
            screen.blit(display_planet, (540, 17)) #blitting number

            #taking user input for mass
            if input_num == 1:

                #blitting the green box to indicate user input
                screen.blit(green_box, (372, 124))

                #getting user input buy initializing a class tha does this
                input_mass = user_input(mass) #initializing the class
                input_mass.events() #method that does this

                # if backspace is pressed last number is taken off
                if event.type == pygame.KEYDOWN:  # checks is key is pressed
                    if event.key == pygame.K_BACKSPACE:  # checks if the key is backspace
                        mass = mass[:-1]  # delets last number

                # printing the user input
                display_mass = myfont.render("".join(mass), False, (255, 255, 255)) #rendering input
                screen.blit(display_mass, (387, 125)) #printing text

                # checking if input is good and moving on
                if event.type == pygame.KEYDOWN:  # checks if key is pressed
                    if event.key == pygame.K_SPACE:  # checks if key is spaebar
                        # if number is negative the screen will close and will give warning
                        if "-" in "".join(mass):
                            print "Invalid input! Number of planets must be positive!"  # warning
                            carryOn = False  # closing screen
                        # making sure that pressing a key does not change multiple screens
                        if not button:  # initially button is false and will only change if it is false
                            input_num = 2  # indicating that the input will change
                            all_mass.append(int("".join(mass))) #appending the mass of this planet toall masses of planets list
                            mass = [] #resetting temp. variable for the next planet
                        button = True  # until button is pressed down screen will not change
                else:
                    button = False  # once let go screen can be changed

            #taking user input for radius of all planets
            if input_num == 2:

                # blitting the green box to indicate user input
                screen.blit(green_box, (372, 294))

                # getting user input using a class
                input_radius = user_input(radius) #initiallizing class
                input_radius.events() #running the method

                # if backspace is pressed last number is taken off
                if event.type == pygame.KEYDOWN:  # checks is key is pressed
                    if event.key == pygame.K_BACKSPACE:  # checks if the key is backspace
                        radius = radius[:-1]  # delets last number

                # printing the user input
                display_radius = myfont.render("".join(radius), False, (255, 255, 255)) #rendering text
                screen.blit(display_radius, (387, 295)) #blitting text

                #displaying mass previously entered for referent
                display_mass = myfont.render(str(all_mass[number_of_planets - temp]), False, (255, 255, 255)) # rendering
                screen.blit(display_mass, (387, 125)) # blitting

                # checking if input is good and moving on
                if event.type == pygame.KEYDOWN:  # checks if key is pressed
                    if event.key == pygame.K_SPACE:  # checks if key is spaebar
                        # if number is negative the screen will close and will give warning
                        if "-" in "".join(radius):
                            print "Invalid input! Number of planets must be positive!"  # warning
                            carryOn = False  # closing screen
                        # making sure that pressing a key does not change multiple screens
                        if not button:  # initially button is false and will only change if it is false
                            input_num = 1  # indicating that the input will change
                            all_radius.append(int("".join(radius)))  # appending the radius of this planet to all radius of planets list
                            radius = []  # resetting temp. variable for the next planet
                            temp -= 1 # checkng the mount of planets left
                        button = True  # until button is pressed down screen will not change
                else:
                    button = False  # once let go screen can be changed

        #once all planet inuts are done this changes the screen
        if temp == 0: # checking if all planet inputs are done
            screen_change += 1 # changing screen
            input_num = 3 # indicating new input
            temp -= 1 # making sure that this if loop is not repeated

    #taking user input for x and y velocities of the space ship
    if screen_change == 4:
        # setting size of screen
        screen = pygame.display.set_mode(size)

        # The name of the window
        pygame.display.set_caption("Space Simulation; Velocities")

        # This is to set the background screen
        screen.blit(ship_details, [0, 0])

        #taking x-velocity input
        if input_num == 3:

            #blitting a grn box to indicate user input
            screen.blit(green_box, (212, 124))
            # getting user input using class
            input_x_velocity = user_input(x_velocity) #initiallizing class
            input_x_velocity.events() #starting method

            # if backspace is pressed last number is taken off
            if event.type == pygame.KEYDOWN:  # checks is key is pressed
                if event.key == pygame.K_BACKSPACE:  # checks if the key is backspace
                    x_velocity = x_velocity[:-1]  # delets last number

            # printing the user input
            display_x_velocity = myfont.render("".join(x_velocity), False, (255, 255, 255)) #rendering text
            screen.blit(display_x_velocity, (227, 125)) #printing text

            # checking if input is good and moving on
            if event.type == pygame.KEYDOWN: #checking if key is pressed
                if event.key == pygame.K_SPACE: #checking if the key is spacebar
                    if not button:  #initially button is false and will only change if it is false
                        input_num = 4 #changing input
                        x_velocity = int("".join(x_velocity)) #permanent variable with x-velocity value
                    button = True  #until button is pressed down screen will not change
            else:
                button = False #once let go, screen will change

        #taking user iput for y-velocity
        if input_num == 4:

            #blitting a green box to indicate user input
            screen.blit(green_box, (212, 294))

            # putting user input
            input_y_velocity = user_input(y_velocity) #rendering text
            input_y_velocity.events() #blitting text

            # if backspace is pressed last number is taken off
            if event.type == pygame.KEYDOWN:  # checks is key is pressed
                if event.key == pygame.K_BACKSPACE:  # checks if the key is backspace
                    y_velocity = y_velocity[:-1]  # delets last number

            # printing the user input
            display_y_velocity = myfont.render("".join(y_velocity), False, (255, 255, 255)) #rendering text
            screen.blit(display_y_velocity, (227, 295)) #printing text

            # printing the user input for x-velocity for reference
            display_x_velocity = myfont.render(str(x_velocity), False, (255, 255, 255)) #rendering text
            screen.blit(display_x_velocity, (227, 125)) #blitting text

            # checking if input is good and moving on
            if event.type == pygame.KEYDOWN: #checking if key is pressed
                if event.key == pygame.K_SPACE: #checking if the key is spacebar
                    if not button:  #initially button is false and will only change if it is false
                        screen_change = 5 #changing input
                        y_velocity = int("".join(y_velocity)) #permanent variable with x-velocity value
                    button = True  #until button is pressed down screen will not change
            else:
                button = False #once let go, screen will change


    if screen_change == 5:
        screen.blit(star_sky, (0,0))

        #A certain planet is assigned to a defined range of masses that a player can input
        #Gives an intuitive approach to planet's mass through size
        for i, item in enumerate(all_mass):
            if 0 < item <= 0.5:
                screen.blit(planet_blue, (plan_x_list[i], plan_y_list[i]))
            elif 0.5 < item <= 3:
                screen.blit(planet_yellow, (plan_x_list[i], plan_y_list[i]))
            elif 3 < item <= 6:
                screen.blit(planet_red, (plan_x_list[i], plan_y_list[i]))
            elif item > 6:
                screen.blit(planet_brown, (plan_x_list[i], plan_y_list[i]))
        screen.blit(rocket_thrust_down, (100,100))
        screen.blit(rocket_thrust_right, (200,2000))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()