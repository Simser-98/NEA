'''import pygame
from math import *
pygame.init()

screen = pygame.display.set_mode([500, 500])
time = 0.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT
            running = False

    screen.fill((255, 255, 255))

    time += 0.001

    pygame.draw.polygon(screen, (0, 255, 255), ((250+sin(time+10)*25,250+cos(time-10)*75),(250+sin(time+20)*320,250+cos(time-20)*125),(250+sin(time+30)*250,250+cos(time-30)*375)))

    pygame.display.flip()

pygame.quit()  '''

'''list = [[0,0,23.7653],
        [0,0,567.86754],
        [0,0,456.8650],
        [0,0,345.76534],
        [0,0,5678.9875]]


for j in range(0,len(list)):
    print(j)
    for i in range(0, len(list) - 1):
        print(list)
        print(i)
        if list[i][2] > list[i + 1][2]:
            print(list[i][2])
            print(list[i + 1][2])
            smal_list = list[i]
            big_list = list[i + 1]
            list[i + 1] = smal_list
            list[i] = big_list
            print(list)
        else:
            pass'''

# initialize a list
'''my_list = [[1,2,3,1,5,4],
           [1,2,4,1,1,9],
           [4,5,1,2,7,9],
           [1,3,4,1,7,3]]

# find length of the list
list_size = len(my_list)
print(list_size)
# declare for loop
for j in range(5):
    for i in range(list_size):

        # check the condition
        if (my_list[i][j] == 1):
            # print the indices
            print(i,j)'''


'''list = [[1,4,6],
           [4,5,7],
           [5,3,1],
           [7,9,0],
           [3,5,2]]

list2 = [[2,5,3],
         [1,4,2],
         [2,3,1],
         [4,2,3],
         [2,3,4]]

for j in range(0,len(list)):
    #print(j)
    for i in range(0, len(list) - 1):
        #print(list)
        #print(i)
        if list[i][2] > list[i + 1][2]:
            #print(list[i][2])
            #print(list[i + 1][2])
            smal_list = list[i]
            big_list = list[i + 1]
            list[i + 1] = smal_list
            list[i] = big_list
            #print(list)
            # find length of the list
            list_size = len(list)
            #print(list_size)
            # declare for loop
            for n in range(3):
                for m in range(list_size):
                    # check the condition
                    if (list2[m][n] == i):
                        list2[m][n] = int(i+1)


                    elif (list2[m][n] == i+1):
                        list2[m][n] = int(i)
        else:
            pass
print(list)
print(list2)'''

"""import pygame

pygame.init()


window = pygame.display.set_mode((500,500))
surface = pygame.Surface((500,500), pygame.SRCALPHA)
surface.fill((255,255,255,128))

running = True
while running:


    pygame.draw.polygon(window, "red", [(50, 50),(250,450), (400,50)])
    window.blit(surface, (0,0))
    pygame.draw.polygon(window, "blue", [(50, 450), (450, 450), (250, 50)])
    window.blit(surface, (0,0))




    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()"""

import pygame

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def draw_circle_alpha(surface, color, center, radius):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)

def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)

pygame.init()
window = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()

background = pygame.Surface(window.get_size())
#ts, w, h, c1, c2 = 50, *window.get_size(), (160, 160, 160), (192, 192, 192)
#tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
#for rect, color in tiles:
    #pygame.draw.rect(background, color, rect)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))

    draw_rect_alpha(window, (0, 0, 255, 127), (55, 90, 140, 140))
    draw_circle_alpha(window, (255, 0, 0, 127), (150, 100), 80)
    draw_polygon_alpha(window, (255, 255, 0, 127),
        [(100, 10), (15, 145), (124, 145)])

    pygame.display.flip()

pygame.quit()
exit()













