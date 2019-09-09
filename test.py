#importing the pygame library
import pygame
import random
import timeit

class Planet:
    k = 0.1
    planets = []
    def __init__(self, mass, x = 100, y= 100):
        self.x = int(x)
        self.y = int(y)
        self.mass = float(mass)
        self.r = 0

        Planet.planets.append(self)

    def findLine(self, point):
        self.dx = self.x - point.x
        self.dy = self.y - point.y

        self.dt = (self.dx ** 2 + self.dy ** 2) ** (1.0 / 2)

        return self

    def hitDetect(self, point):
        self.detect = False
        if self.x - int(self.r) < int(point.x) < int(self.x) + int(self.r):
            if self.y - int(self.r) < point.y < int(self.y) + int(self.r):
                y_min = -1*(abs((point.x - self.x)**2 - self.r ** 2)**(1.0/2)) + self.y
                y_max = abs((point.x - self.x)**2 - self.r ** 2)**(1.0/2) + self.y
                if y_min < point.y < int(y_max):
                    self.detect = True
        return self


def generateCoord(Planet):  # generates coordinates of all planets
    Planet.planets[0].x = 400
    Planet.planets[0].y = 200
    x_lim = [200, [100,50][len(Planet.planets) > 7]][len(Planet.planets) > 5]
    y_lim = [100, [80, 50][len(Planet.planets) > 7]][len(Planet.planets) > 5]
    for i in range(1, len(Planet.planets)):

        # makes sure that generated coodrinates do not overlap with other planets
        reset = True
        while reset:
            Planet.planets[i].x = random.randint(50, 850)
            Planet.planets[i].y = random.randint(50, 450)
            reset = False
            for j in range(0, i):
                distance_x = abs(Planet.planets[j].x - Planet.planets[i].x)
                distance_y = abs(Planet.planets[j].x - Planet.planets[i].x)
                if distance_x <= x_lim and distance_y <= y_lim:
                    reset = True  # resets coordinates if overlap found

    return Planet

#Rocket object which stores relevant information (methods, functions, variables) about
# Point mass object in the simulation
class Point:  # object influenced by planetary masses
    thrust = 0.015 #thrust constant

    #Initializes object
    def __init__(self, vy, vx, planets, x=0, y=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.planets = planets


        self.thrustUpPressed, self.thrustDownPressed = False, False
        self.thrustForwardPressed, self.thrustBackPressed = False, False

    #Timer initialization
    def startTimer(self):
        self.startPos = timeit.default_timer()
        self.StartVel = timeit.default_timer()

    #Calculates net acceleration from planetary bodies
    def netAcc(self):  # finds net acceleration caused by planetary masses
        self.ax = 0
        self.ay = 0

        #Calculates acceleration in terms of each planetary body and
        #Adds to x and y components of the rocket's acceleration
        for i in self.planets:
            i.findLine(self)
            self.ax += (i.dx * Planet.k * i.mass) / (i.dt ** 2)
            self.ay += (i.dy * Planet.k * i.mass) / (i.dt ** 2)

        return self

    # Calculates and controls the change in velocity of the rocket (just speed)
    def changeVel(self):  # changes velocity of object
        t = timeit.default_timer() - self.StartVel #Calculates idle time

        #Calculates final velocity for both components
        v2x = self.accTotalx * (t) + self.vx
        v2y = self.accTotaly * (t) + self.vy

        #Limits the speed of the velocity
        if abs(v2x) > 4:
            v2x = [-4,4][v2x > 4]

        if abs(v2y) > 4:
            v2y = [-4,4][v2y > 4]

        #Updates initial velocity with its final velocity
        self.vx = v2x
        self.vy = v2y

        #Resets timer value
        self.startVel = timeit.default_timer()

        return self

    #Calcualtes change of position of the rocket
    def changePos(self):  # changes position of object
        t = timeit.default_timer() - self.startPos

        #Calculating the change in position in terms of adding
        # net acceleration and velocity (based on components)
        p2x = 0.5 * self.accTotalx * (t) ** 2 + self.vx + self.x
        p2y = 0.5 * self.accTotaly * (t) ** 2 + self.vy + self.y

        #Updates position
        self.x = p2x
        self.y = p2y

        #Resets timer value
        self.startPos = timeit.default_timer()

        return self

    #Calculates acceleration due to thrust and adds to net acceleration
    def thrustAcc(self):  # Adds thrust acceleration to net gravitational acceleration
        #Initializes total acceleration as acceleration from gravitational pull of planets
        self.accTotalx = self.ax
        self.accTotaly = self.ay

        #Adds acceleration from the thrust constant provided by user input to the total acceleration
        if self.thrustForwardPressed: self.accTotalx += Point.thrust
        if self.thrustBackPressed: self.accTotalx -= Point.thrust
        if self.thrustDownPressed: self.accTotaly += Point.thrust
        if self.thrustUpPressed: self.accTotaly -= Point.thrust

        return self

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
            elif event.key == pygame.K_PERIOD:#if . is pressed '.' is added to temporary list
                self.lis.append(".")

#creating a font that is used throughout all text
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#Set the width and height of the screen [width, height])
size = (900, 504)
screen = pygame.display.set_mode(size)

#Creating boolean variables required for the code
carryOn = True
start = True
button = False
timer_disabled = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#creating all variables that will be needed for the code
screen_change = 0
input_num = 0
num_planets = []
mass = []
all_mass = []
radius = []
all_radius = []
x_velocity = []
y_velocity = []
plan_x_list = []
plan_y_list = []

for i in range(10):
    plan_x = random.randint(0, 800)
    plan_x_list.append(plan_x)
    plan_y = random.randint(0, 400)
    plan_y_list.append(plan_y)

#loading in images
background = pygame.image.load("start.png")
welcome = pygame.image.load("Welcome!.png")
select = pygame.image.load("Selection.png")
green_box = pygame.image.load("green box.png")
planet_details = pygame.image.load("Copy of dazzle (3).png")
ship_details = pygame.image.load("Ship.png")
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
game_over = pygame.image.load("Game Over.png")
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

    #creating the starting sreen
    if screen_change == 0: #the initial value of screen change is 0
        #blitting in the original background screen
        screen.blit(background, [0,0])

        #changing screen if player presses any key
        if screen_change == 0 and event.type == pygame.KEYUP:
            if not button:
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
        screen.blit(welcome, [0, 0])

        # changing screen if player presses any key
        if screen_change == 1 and event.type == pygame.KEYUP:
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
            input = user_input(num_planets)
            input.events()

            #deletes last nuber if backspace is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    num_planets = num_planets[:-1]

            # printing the user input
            display_num_planets = myfont.render("".join(num_planets), False, (255, 255, 255))
            screen.blit(display_num_planets, (423, 171))

            #checking if input is good and moving on
            number_of_planets = "".join(num_planets)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #if number is negative the screen will close and will give warning
                    if "-" in number_of_planets or number_of_planets == '':
                        print "Invalid input! Number of planets must be positive!" #warning
                        num_planets = [] #resets input
                    #if number is > 10 warning is given and screen closes
                    elif int(number_of_planets) > 10:
                        print "Invalid Input! Maximum of 10 planets!" #warning
                        num_planets = []
                    #making sure that pressing a key does not change multiple screens
                    elif not button: #initially button is false and will only change if it is false
                        screen_change = 3 #change screen
                        input_num = 1 #indicating that the input will change
                        number_of_planets = int(number_of_planets)
                    button = True # until button is pressed down screen will not change
            else:
                button = False #once let go screen can be changed

    #taking user input for mass and radius of each planet
    if screen_change == 3:
        screen = pygame.display.set_mode(size)

        # The name of the window
        pygame.display.set_caption("Space Simulation; Selection of Planets")

        # This is to set the background screen
        screen.blit(planet_details, [0, 0])

        #initially setting up a temporary variable
        if start:
            temp = number_of_planets
            start = False

        #taking inputs for all planets
        if temp > 0:
            #printing the number of the planet that the player is entering information for
            show_planet = (number_of_planets - temp) + 1
            display_planet = myfont.render(str(show_planet), False, (255, 255, 255))
            screen.blit(display_planet, (540, 17))

            #taking user input for mass
            if input_num == 1:

                #blitting the green box to indicate user input
                screen.blit(green_box, (372, 124))

                #getting user input buy initializing a class tha does this
                input_mass = user_input(mass)
                input_mass.events()

                # if backspace is pressed last number is taken off
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        mass = mass[:-1]

                # printing the user input
                display_mass = myfont.render("".join(mass), False, (255, 255, 255))
                screen.blit(display_mass, (387, 125))

                # checking if input is good and moving on
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # if number is negative the screen will close and will give warning
                        if "-" in "".join(mass):
                            print "Invalid input! mass of planet must be positive!"  # warning
                            mass = []  # reset input
                        # making sure that pressing a key does not change multiple screens
                        elif not button:  # initially button is false and will only change if it is false
                            temp -= 1 # indicating that the input will change
                            planet_mass = float("".join(mass))
                            new_planet = Planet(planet_mass)
                            mass = [] #resetting temp. variable for the next planet

                            #Assigns image and radius to planet object based on mass input
                            if 0 < new_planet.mass <= 0.5:
                                new_planet.img = planet_blue
                                new_planet.r = 9

                            elif new_planet.mass <= 3:
                                new_planet.img = planet_yellow
                                new_planet.r = 12

                            elif new_planet.mass <= 6:
                                new_planet.img = planet_red
                                new_planet.r = 15

                            elif new_planet.mass > 6:
                                new_planet.img = planet_brown
                                new_planet.r = 21


                        button = True  # until button is pressed down screen will not change
                else:
                    button = False  # once let go screen can be changed



        #once all planet inuts are done this changes the screen
        if temp == 0:
            screen_change += 1
            input_num = 3
            temp -= 1

    #taking user input for x and y velocities of the space ship
    if screen_change == 4:
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
            input_x_velocity = user_input(x_velocity)
            input_x_velocity.events()

            # if backspace is pressed last number is taken off
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x_velocity = x_velocity[:-1]

            # printing the user input
            display_x_velocity = myfont.render("".join(x_velocity), False, (255, 255, 255))
            screen.blit(display_x_velocity, (227, 125))

            # checking if input is good and moving on
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not button:
                        input_num = 4
                        x_velocity = int("".join(x_velocity))
                    button = True  #until button is pressed down screen will not change
            else:
                button = False #once let go, screen will change

        #taking user iput for y-velocity
        if input_num == 4:

            #blitting a green box to indicate user input
            screen.blit(green_box, (212, 294))

            # putting user input
            input_y_velocity = user_input(y_velocity)
            input_y_velocity.events()

            # if backspace is pressed last number is taken off
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    y_velocity = y_velocity[:-1]

            # printing the user input
            display_y_velocity = myfont.render("".join(y_velocity), False, (255, 255, 255))
            screen.blit(display_y_velocity, (227, 295))

            # printing the user input for x-velocity for reference
            display_x_velocity = myfont.render(str(x_velocity), False, (255, 255, 255))
            screen.blit(display_x_velocity, (227, 125))

            # checking if input is good and moving on
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not button:  #initially button is false and will only change if it is false
                        screen_change = 5 #changing input
                        y_velocity = int("".join(y_velocity))

                        #initializes player object
                        player = Point(y_velocity, x_velocity, Planet.planets)
                    button = True  #until button is pressed down screen will not change
            else:
                button = False #once let go, screen will change

    #Simulation Phase
    if screen_change == 5:
        screen.blit(star_sky, (0,0))

        #Initiates timer
        if timer_disabled:
            generateCoord(Planet) #generates coordinates for all planets
            player.startTimer()
            timer_disabled = False


        #Collects user input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.thrustUpPressed = True

            if event.key == pygame.K_DOWN:
                player.thrustDownPressed = True

            if event.key == pygame.K_LEFT:
                player.thrustBackPressed = True

            if event.key == pygame.K_RIGHT:
                player.thrustForwardPressed = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                player.thrustUpPressed = False

            if event.key == pygame.K_DOWN:
                player.thrustDownPressed = False

            if event.key == pygame.K_LEFT:
                player.thrustBackPressed = False

            if event.key == pygame.K_RIGHT:
                player.thrustForwardPressed = False

        #Pastes the specific rocket images based on what key was pressed
        screen.blit(rocket, (player.x, player.y))
        if player.thrustUpPressed:
            screen.blit(rocket_thrust_down, (player.x, player.y))
        if player.thrustDownPressed:
            screen.blit(rocket_thrust_up, (player.x, player.y))
        if player.thrustBackPressed:
            screen.blit(rocket_thrust_right, (player.x, player.y))
        if player.thrustForwardPressed:
            screen.blit(rocket_thrust_left, (player.x, player.y))

        #Searches through each planet list and then pastes the planet picture
        #Along with determining whether the rocket hits the planet zone
        for i in Planet.planets:

                screen.blit(i.img, (i.x, i.y))
                i.hitDetect(player)

                #If rocket hits a planet zone, it's game over!
                if i.detect:
                    screen_change = 6

        #Calling calculation methods for rocket class instance
        player.netAcc()
        player.thrustAcc()
        player.changeVel() 
        player.changePos()

        #Displays acceleration and velocity on screen
        acc_x_display = myfont.render('Acc_x: ' + str(player.accTotalx), False, (255, 255, 255))
        acc_y_display = myfont.render('Acc_y: '+ str(player.accTotaly), False, (255, 255, 255))

        vel_x_display = myfont.render('Vel_x: ' + str(player.vx), False, (255, 255, 255))
        vel_y_display = myfont.render('Vel_y: ' + str(player.vy), False, (255, 255, 255))

        screen.blit(acc_x_display, (500,20))
        screen.blit(acc_y_display, (500, 50))

        screen.blit(vel_x_display, (500, 420))
        screen.blit(vel_y_display, (500, 450))

    #Switches over screen to the screen that states "Game over!"
    if screen_change == 6:
        screen.blit(game_over, (0,0))
        if event.type == pygame.KEYDOWN:
            carryOn = False

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()