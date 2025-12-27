import pygame
import os
import random

from queue_ds import TrafficQueue

ROAD_COLOR = (35, 35, 35)

GRASS = (34, 139, 34)

WHITE = (255, 255, 255)

YELLOW = (255, 255, 0)

AL2_COLOR = (0, 150, 255)  

AL3_COLOR = (255, 165, 0)


pygame.init()

WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("3-Lane Traffic Simulation (AL1, AL2, AL3)")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 16, bold=True)



queues = {'A': TrafficQueue(), 'B': TrafficQueue(), 'C': TrafficQueue(), 'D': TrafficQueue()}

files = {'A': 'lane_a.txt', 'B': 'lane_b.txt', 'C': 'lane_c.txt', 'D': 'lane_d.txt'}

active_cars = []



class Vehicle:

    def __init__(self, road, lane_type):

        self.road = road

        self.lane_type = lane_type 

        self.finished = False

        # Lane Placement:

        if road == 'A':

            self.pos = [370 if lane_type=='AL2' else 335, -20]; self.vel = [0, 2.5]

        elif road == 'B':

            self.pos = [820, 370 if lane_type=='AL2' else 335]; self.vel = [-2.5, 0]

        elif road == 'C':

            self.pos = [410 if lane_type=='AL2' else 445, 820]; self.vel = [0, -2.5]

        elif road == 'D':

            self.pos = [-20, 410 if lane_type=='AL2' else 445]; self.vel = [2.5, 0]

          self.color = AL2_COLOR if lane_type == 'AL2' else AL3_COLOR



    def move(self, green_light):

        if self.lane_type == 'AL3' or green_light:

            self.pos[0] += self.vel[0]

            self.pos[1] += self.vel[1]

           

                if self.lane_type == 'AL3':

                if self.road == 'A' and self.pos[1] > 330: self.vel = [-2.5, 0]

                if self.road == 'B' and self.pos[0] < 470: self.vel = [0, -2.5]

                if self.road == 'C' and self.pos[1] < 470: self.vel = [2.5, 0]

                if self.road == 'D' and self.pos[0] > 330: self.vel = [0, 2.5]



    def draw(self):

        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], 20, 20))

        pygame.draw.rect(screen, (0,0,0), (self.pos[0], self.pos[1], 20, 20), 1)



def poll_incoming():

    for road, path in files.items():

        if os.path.exists(path):

            with open(path, "r") as f:

                arrivals = f.readlines()

            for _ in arrivals:

               target_lane = 'AL2' if random.random() > 0.3 else 'AL3'

                if target_lane == 'AL2':

                    queues[road].enqueue('v')

                else:

                    active_cars.append(Vehicle(road, 'AL3'))

            open(path, 'w').close()



current_green = 'A'

timer = 0

priority_active = False


while True:

    screen.fill(GRASS)

    poll_incoming()


#  PRIORITY LOGIC 

    if queues['A'].size() > 10:

        current_green = 'A'

        priority_active = True

    elif priority_active and queues['A'].size() < 5:

        priority_active = False

   

    # Normal Rotation
    if not priority_active and timer % 300 == 0:

        roads_list = ['A', 'B', 'C', 'D']

        current_green = roads_list[(roads_list.index(current_green) + 1) % 4]


    pygame.draw.rect(screen, ROAD_COLOR, (300, 0, 200, 800)) 

    pygame.draw.rect(screen, ROAD_COLOR, (0, 300, 800, 200)) 

   
for i in range(0, 800, 40):
 for offset in [333, 366, 433, 466]:

     pygame.draw.line(screen, WHITE, (offset, i), (offset, i+20), 1)

     pygame.draw.line(screen, WHITE, (i, offset), (i+20, offset), 1)

    pygame.draw.line(screen, YELLOW, (400, 0), (400, 800), 2)

    pygame.draw.line(screen, YELLOW, (0, 400), (800, 400), 2)



    if timer % 60 == 0 and queues[current_green].size() > 0:

        active_cars.append(Vehicle(current_green, 'AL2'))

        queues[current_green].dequeue()


 # Traffic Lights 

    light_pos = {'A': (350, 280), 'B': (520, 350), 'C': (450, 520), 'D': (280, 450)}

    for road, pos in light_pos.items():

        col = (0, 255, 0) if road == current_green else (255, 0, 0)

        pygame.draw.circle(screen, col, pos, 15)

        txt = font.render(f"{road} AL2: {queues[road].size()}", True, WHITE)

        screen.blit(txt, (pos[0]-30, pos[1]-45))



  for car in active_cars[:]:

        # Stop at junction if red light

        in_junction = 300 < car.pos[0] < 500 and 300 < car.pos[1] < 500

        can_move = (car.road == current_green) or in_junction

        car.move(can_move)

        car.draw()


        if car.pos[0] < -50 or car.pos[0] > 850 or car.pos[1] < -50 or car.pos[1] > 850:

            active_cars.remove(car)


    if priority_active:

        msg = font.render("!!! PRIORITY MODE: ROAD A !!!", True, YELLOW)

        screen.blit(msg, (310, 20))

   
    screen.blit(font.render("Blue = AL2 (Light)", True, AL2_COLOR), (10, 10))

    screen.blit(font.render("Orange = AL3 (Free Left)", True, AL3_COLOR), (10, 30))



    timer += 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT: pygame.quit(); exit()

    pygame.display.flip()

    clock.tick(30)
