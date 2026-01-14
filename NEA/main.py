import pygame.key
import time
from orbtals import *
from maytrixes import *
from sys import exit


def draw(orbs, faces, matrices, X_TABLE, Y_TABLE, numElec, atom_structure_l, short_arrangment_l, long_arrangment_l, periodicTable, periodicTableRect, atomStructure, atomStructureRect, elecChart, eleChartRect ):
    numElec = numElec//2
    #print(numElec)
    #print(numElec)

    atom_surface = font.render(atom_structure_l[numElec], False, (255, 255, 255))
    shortArr_surface = font.render(short_arrangment_l[numElec], False, (255, 255, 255))
    longArr_surface = font.render(long_arrangment_l[numElec], False, (255, 255, 255))

    Window.fill(BLACK)
    Window.blit(periodicTable, periodicTableRect)
    Window.blit(atomStructure[numElec], atomStructureRect[numElec])
    Window.blit(elecChart[numElec], eleChartRect[numElec])
    Window.blit(atom_surface, (10, 350))
    Window.blit(longArr_surface, (960, 650))
    Window.blit(shortArr_surface, (960, 700))
    if 10 >= numElec >= 0:
        orbs[0].Draw_node(matrices[0], faces[0], 35)
        #print(matrices[0])
    if 18 >= numElec  >= 2:
        orbs[0].Draw_node(matrices[0], faces[0], 65)
    if 30 >= numElec >= 4 :
        orbs[1].Draw_node(matrices[1], faces[1], 49)
    if 31 >= numElec >= 5 :
        orbs[2].Draw_node(matrices[2], faces[2], 49)
    if 32 >= numElec >= 6 :
        orbs[3].Draw_node(matrices[3], faces[3], 49)
    if 36 >= numElec >= 10 :
        orbs[0].Draw_node(matrices[0], faces[0], 85)
    if 48 >= numElec >= 12 :
        orbs[1].Draw_node(matrices[1], faces[1], 53)
    if 49 >= numElec >= 13 :
        orbs[2].Draw_node(matrices[2], faces[2], 53)
    if 50 >= numElec >= 14 :
        orbs[3].Draw_node(matrices[3], faces[3], 53)
    if numElec >= 18:
        orbs[0].Draw_node(matrices[0], faces[0], 105)
    if numElec >= 20:
        orbs[4].Draw_node(matrices[4], faces[4], 55)
    if numElec >= 21:
        orbs[5].Draw_node(matrices[5], faces[5], 55)
    if numElec >= 22:
        orbs[6].Draw_node(matrices[6], faces[6], 55)
    if numElec >= 23:
        orbs[7].Draw_node(matrices[7], faces[7], 55)
        orbs[8].Draw_node(matrices[8], faces[8], 55)
    if numElec >= 30:
        orbs[1].Draw_node(matrices[1], faces[1], 57)
    if numElec >= 31:
        orbs[2].Draw_node(matrices[2], faces[2], 57)
    if numElec >= 32:
        orbs[3].Draw_node(matrices[3], faces[3], 57)
    if numElec >= 36:
        orbs[0].Draw_node(matrices[0], faces[0], 125)
    if numElec >= 38:
        orbs[4].Draw_node(matrices[4], faces[4], 61)
    if numElec >= 39:
        orbs[5].Draw_node(matrices[5], faces[5], 61)
    if numElec >= 40:
        orbs[6].Draw_node(matrices[6], faces[6], 61)
    if numElec >= 40:
        orbs[7].Draw_node(matrices[7], faces[7], 60)
        orbs[8].Draw_node(matrices[8], faces[8], 60)
    if numElec >= 48:
        orbs[1].Draw_node(matrices[1], faces[1], 65)
    if numElec >= 49:
        orbs[2].Draw_node(matrices[2], faces[2], 65)
    if numElec >= 50:
        orbs[3].Draw_node(matrices[3], faces[3], 65)




    pg.display.update()


def relative_calc(orbs):
    mouse_angle = (0, 0)
    keyboard_angle = (0, 0)
    mouse_angle = pg.mouse.get_rel()
    for orb in orbs:
        orb.angle_set(mouse_angle)
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pg.K_a]:
        keyboard_angle = (-10, keyboard_angle[0])
    if keys_pressed[pg.K_d]:
        keyboard_angle = (10, keyboard_angle[1])
    if keys_pressed[pg.K_w]:
        keyboard_angle = (keyboard_angle[0], -10)
    if keys_pressed[pg.K_s]:
        keyboard_angle = (keyboard_angle[1], 10)
    if pg.mouse.get_pressed()[0]:
        return keyboard_angle[0] + mouse_angle[0], keyboard_angle[1] + mouse_angle[1]
    return keyboard_angle


def wrap_mouse():
    mouse_pos = pg.mouse.get_pos()
    #print(mouse_pos)
    if mouse_pos[0] > WIN_WIDTH:
        pg.mouse.set_pos(0, mouse_pos[1])
    elif mouse_pos[0] < 0:
        pg.mouse.set_pos(WIN_WIDTH, mouse_pos[1])
    if mouse_pos[1] > WIN_HEIGHT:
        pg.mouse.set_pos(mouse_pos[0], 0)
    elif mouse_pos[1] < 0:
        pg.mouse.set_pos(mouse_pos[0], WIN_HEIGHT)


def Element_selecter(cell_bounds_l, elecNumber, eventType, key):
    selectorPos = pg.mouse.get_pos()
    if eventType == pg.MOUSEBUTTONDOWN and selectorPos[1] >= cell_bounds_l[0][1]:

        for i in range(1, len(cell_bounds_l), 2):
            #print(i)
            if (cell_bounds_l[i-1][0] <= selectorPos[0] <= cell_bounds_l[i][0]) and (cell_bounds_l[i-1][1] <= selectorPos[1] <= cell_bounds_l[i][1]):
                elecNumber = i
    #if eventType == pg.KEYDOWN:
    if key == pg.K_RIGHT and elecNumber//2+1 < 54:
        elecNumber += 2


    elif key == pg.K_LEFT and elecNumber > 1:
        # print("left")
        elecNumber -= 2
            #print(elecNumber)

    return elecNumber



def main():
    elecNum = 1
    TABLE_X = 5
    TABLE_Y = 400
    CELL_WIDTH, CELL_HEIGHT = [635*1.5/18, 232*1.5/5]
    ELEMENTBOUNDS = [[TABLE_X, TABLE_Y], [TABLE_X+CELL_WIDTH,TABLE_Y+CELL_HEIGHT],
    [TABLE_X + CELL_WIDTH*17, TABLE_Y] , [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT],
    [TABLE_X, TABLE_Y +CELL_HEIGHT], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT], [TABLE_X+ CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH *13, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*2],
    [TABLE_X, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*3],
    [TABLE_X, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*4],
    [TABLE_X, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*5],
    [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*5]]


    start_time = time.time()

    orbs = []
    matrices = []
    ogmats = []
    normals = []
    textures = []
    faces = []
    matmakers = []
    longOrb , shortOrb , atom = orb_vertex_pos("assets/elements.txt").Atom_load()
    #print(longOrb)
    #print(shortOrb)
    #print(atom)


    orbs.append(orb_vertex_pos("assets/s_orb.obj", BLUE_LINE, BLUE_FILL))
    orbs.append(orb_vertex_pos("assets/py_orb.obj", PURPLE_LINE, PURPLE_FILL))
    orbs.append(orb_vertex_pos("assets/pz_orb.obj", PURPLE_LINE, PURPLE_FILL))
    orbs.append(orb_vertex_pos("assets/px_orb.obj", PURPLE_LINE, PURPLE_FILL))
    orbs.append(orb_vertex_pos("assets/dxy_orb.obj", GREEN_LINE, GREEN_FILL))
    orbs.append(orb_vertex_pos("assets/dxz_orb.obj", GREEN_LINE, GREEN_FILL))
    orbs.append(orb_vertex_pos("assets/dyz_orb.obj", GREEN_LINE, GREEN_FILL))
    orbs.append(orb_vertex_pos("assets/dz2_orb.obj", GREEN_LINE, GREEN_FILL))
    orbs.append(orb_vertex_pos("assets/dx-2y-2_orb.obj", GREEN_LINE, GREEN_FILL))


    periodicTableImage = pg.image.load("assets/periodic.png")
    periodicTable = pg.transform.scale(periodicTableImage, (635 * 1.5, 232 * 1.5))
    periodicTableRect = periodicTable.get_rect(x=TABLE_X, y=TABLE_Y)


    atomStructureList = []
    atomStructureRectList = []
    for i in range(0, 54):
        image = (pg.image.load("assets/bohr/" + str(i) + ".png"))
        atomStructureList.append(pg.transform.scale(image, (1000 / 3, 1000 / 3)))
        atomStructureRectList.append(atomStructureList[i].get_rect(x=10, y=0))


    elecChartList = []
    elecChartRectList = []
    for i in range(0, 54):
        image = (pg.image.load("assets/electron charts/" + str(i) + ".png"))
        elecChartList.append(pg.transform.scale(image, (900 / 2.4, 1500 / 2.4)))
        elecChartRectList.append(elecChartList[i].get_rect(x=960, y=0))



    for i in range(len(orbs)):
        ogmat, normal, texture, face = orbs[i].Vert_load()
        ogmats.append(ogmat)
        normals.append(normal)
        textures.append(texture)
        faces.append(face)
        matmakers.append(matrix())


    end_time = time.time()
    print("Loaded orbitals in " + str(end_time - start_time) + " seconds")



    clock = pg.time.Clock()
    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000

        wrap_mouse()
        angle = relative_calc(orbs)
        ngmatrices = []



        #elecNum = Key_element_arrow(elecNum)

        pg.display.set_caption("electron orbital simulation")                #str(clock.get_fps())




        keyspressed = pg.key.get_pressed()
        for event in pg.event.get():

            if event.type == pg.QUIT or keyspressed[pg.K_ESCAPE]:
                running = False
                pg.quit()
                exit()
            if event.type == pg.KEYUP and event.key == pg.K_j:
                angle = (0,(pi/6)/delta_time*10)
            elif event.type == pg.KEYUP and event.key == pg.K_k:
                angle = ((pi/6)/delta_time*10,0)

            for index in range(len(matmakers)):
                ngmatrices.append(matmakers[index].Rotate_X(ogmats[index], (angle[1] * delta_time) / 10))
                ngmatrices[index] = (matmakers[index].Rotate_Y(ngmatrices[index], (angle[0] * delta_time) / 10))

            for index in range(len(ogmats)):
                ogmats[index] = ngmatrices[index]

            if event.type == pg.KEYDOWN:
                elecNum = Element_selecter(ELEMENTBOUNDS, elecNum, event.type, event.key)

            if event.type == pg.MOUSEBUTTONDOWN:
                elecNum = Element_selecter(ELEMENTBOUNDS, elecNum, event.type, None)

        draw(orbs, faces, ogmats, TABLE_X, TABLE_Y, elecNum, atom, shortOrb, longOrb, periodicTable, periodicTableRect, atomStructureList ,atomStructureRectList, elecChartList, elecChartRectList  )

        pg.display.flip()


if __name__ == "__main__":
    main()


"""ngmatrix_px = matmaker_px.Rotate_X(ogMat_px, angle[1] / 100)
        ngmatrix_px = matmaker_px.Rotate_Y(ngmatrix_px, angle[0] / 100)
        ngmatrix_py = matmaker_py.Rotate_X(ogMat_py, angle[1] / 100)
        ngmatrix_py = matmaker_py.Rotate_Y(ngmatrix_py, angle[0] / 100)
        ngmatrix_pz = matmaker_pz.Rotate_X(ogMat_pz, angle[1] / 100)
        ngmatrix_pz = matmaker_pz.Rotate_Y(ngmatrix_pz, angle[0] / 100)
        ngmatrix_dxy = matmaker_dxy.Rotate_X(ogMat_dxy, angle[1] / 100)
        ngmatrix_dxy = matmaker_dxy.Rotate_Y(ngmatrix_dxy, angle[0] / 100)
        ngmatrix_dxz = matmaker_dxz.Rotate_X(ogMat_dxz, angle[1] / 100)
        ngmatrix_dxz = matmaker_dxz.Rotate_Y(ngmatrix_dxz, angle[0] / 100)
        ngmatrix_dyz = matmaker_dyz.Rotate_X(ogMat_dyz, angle[1] / 100)
        ngmatrix_dyz = matmaker_dyz.Rotate_Y(ngmatrix_dyz, angle[0] / 100)
        ngmatrix_dz2 = matmaker_dz2.Rotate_X(ogMat_dz2, angle[1] / 100)
        ngmatrix_dz2 = matmaker_dz2.Rotate_Y(ngmatrix_dz2, angle[0] / 100)
        ngmatrix_dxxyy = matmaker_dxxyy.Rotate_X(ogMat_dxxyy, angle[1] / 100)
        ngmatrix_dxxyy = matmaker_dxxyy.Rotate_Y(ngmatrix_dxxyy, angle[0] / 100)"""

"""ogMat_s = ngmatrix_s
        ogMat_px = ngmatrix_px
        ogMat_py = ngmatrix_py
        ogMat_pz = ngmatrix_pz
        ogMat_dxy = ngmatrix_dxy
        ogMat_dxz = ngmatrix_dxz
        ogMat_dyz = ngmatrix_dyz
        ogMat_dz2 = ngmatrix_dz2
        ogMat_dxxyy = ngmatrix_dxxyy"""

'''HYDROGEN = [TABLE_X, TABLE_Y], [TABLE_X+CELL_WIDTH,TABLE_Y+CELL_HEIGHT]
HELIUM = [TABLE_X + CELL_WIDTH*18, TABLE_Y] , [TABLE_X + CELL_WIDTH*19, TABLE_Y + CELL_HEIGHT]
LITHIUM = [TABLE_X, TABLE_Y +CELL_HEIGHT], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*2]
BERYLLIUM = [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*2]
BORON = [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT], [TABLE_X+ CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*2]
CARBON = [TABLE_X + CELL_WIDTH *14, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*2]
NITROGEN = [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*2]
OXYGEN = [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*2]
FLOURINE = [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*2]
NEON = [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT], [TABLE_X + CELL_WIDTH*19, TABLE_Y + CELL_HEIGHT*2]
SODIUM = [TABLE_X, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*3]
MAGNESIUM = [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*3]
ALUMINIUM = [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*3]
SILICON = [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*3]
PHOSPHORUS = [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*3]
SULFUR = [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*3]
CHLORINE = [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*3]
ARGON = [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*2], [TABLE_X + CELL_WIDTH*19, TABLE_Y + CELL_HEIGHT*3]
POTASSIUM = [TABLE_X, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*4]
CALCIUM = [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*4]
SCANDIUM = [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*4]
TITANIUM = [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*4]
VANADIUM = [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*4]
CHROMIUM = [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*4]
MANGANESE = [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*4]
IRON = [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*4]
COBALT = [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*4]
NICKEL = [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*4]
COPPER = [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*4]
ZINC = [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*4]
GALLIUM = [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*4]
GERMANIUM = [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*4]
ARSENIC = [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*4]
SELENIUM = [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*4]
BROMINE = [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*4]
KRYPTON = [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*3], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*4]
RUBIDIUM = [TABLE_X, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*5]
STRONTIUM = [TABLE_X + CELL_WIDTH, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*5]
YITTRIUM = [TABLE_X + CELL_WIDTH*2, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*5]
ZIRCONIUM = [TABLE_X + CELL_WIDTH*3, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*5]
NIOBIUM = [TABLE_X + CELL_WIDTH*4, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*5]
MOLYBDENUM = [TABLE_X + CELL_WIDTH*5, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*5]
TECHNETIUM = [TABLE_X + CELL_WIDTH*6, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*5]
RUTHENIUM = [TABLE_X + CELL_WIDTH*7, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*5]
RHODIUM = [TABLE_X + CELL_WIDTH*8, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*5]
PALLADIUM = [TABLE_X + CELL_WIDTH*9, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*5]
SILVER = [TABLE_X + CELL_WIDTH*10, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*5]
CADMIUM = [TABLE_X + CELL_WIDTH*11, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*5]
INDIUM = [TABLE_X + CELL_WIDTH*12, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*5]
TIN = [TABLE_X + CELL_WIDTH*13, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*5]
ANTIMONY = [TABLE_X + CELL_WIDTH*14, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*5]
TELLURIUM = [TABLE_X + CELL_WIDTH*15, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*5]
IODINE = [TABLE_X + CELL_WIDTH*16, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*5]
XENON = [TABLE_X + CELL_WIDTH*17, TABLE_Y + CELL_HEIGHT*4], [TABLE_X + CELL_WIDTH*18, TABLE_Y + CELL_HEIGHT*5]
ELEMENTS = [HYDROGEN, HELIUM, LITHIUM, BERYLLIUM, BORON, CARBON, NITROGEN, OXYGEN, FLOURINE, NEON,
            SODIUM, MAGNESIUM, ALUMINIUM, SILICON, PHOSPHORUS, SULFUR, CHLORINE, ARGON,
            POTASSIUM, CALCIUM, SCANDIUM, TITANIUM, VANADIUM, CHROMIUM, MANGANESE, IRON, COBALT, NICKEL, COPPER, ZINC, GALLIUM, GERMANIUM, ARSENIC, SELENIUM, BROMINE, KRYPTON,
            RUBIDIUM, STRONTIUM, YITTRIUM, ZIRCONIUM, NIOBIUM, MOLYBDENUM, TECHNETIUM, RUTHENIUM, RHODIUM, PALLADIUM, SILVER, CADMIUM, INDIUM, TIN, ANTIMONY, TELLURIUM, IODINE, XENON]'''

'''for i in range(len(cell_bounds_l)):
            while (2*i + 1) <= 54:
                if selectorPos[0] >= cell_bounds_l[2*i][0] and selectorPos[0] <= cell_bounds_l[2*i + 1][0] and selectorPos[1] >= cell_bounds_l[i][1] and selectorPos[1] <= cell_bounds_l[i+1][1]:
                    elecNumber = i + 1
                else:
                    pass'''


'''def Key_element_arrow(elecNumber):
    for event in pg.event.get():
        if event.type == pg.KEYUP:
            key = pg.key.name(event.key)
            if key == "right" and elecNumber < 54:
                elecNumber += 1
                print(elecNumber)

            elif key == "left" and elecNumber > 1:
                elecNumber -= 1
                print(elecNumber)

    """if key[pg.K_RIGHT] and elecNumber < 54:
        elecNumber += 1
        print("re")
        print(elecNumber)

    if key[pg.K_LEFT] and elecNumber > 1:
        elecNumber -= 1
        print("not re")
        print(elecNumber)"""

    return elecNumber
'''


'''for i in range(len(orbs)):
    orbs[i].Draw_node(matrices[i], faces[i])

orb1.Draw_node(face1, matrix1, normal1)
orb2.Draw_node(face2, matrix2, normal2)
orb3.Draw_node(face3, matrix3, normal3)
orb4.Draw_node(face4, matrix4, normal4)
orb5.Draw_node(face5, matrix5, normal5)
orb6.Draw_node(face6, matrix6, normal6)
orb7.Draw_node(face7, matrix7, normal7)
orb8.Draw_node(face8, matrix8, normal8)'''