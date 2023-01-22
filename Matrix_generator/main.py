import pygame
from color_select import *

pygame.init()

def genRectMatriz(dx,dy,tamX,tamY,t,e,data):
    rects_m = []
    x,y = dx,dy
    for colun in range(tamY):
        Line = []
        for line in range(tamX):
            if data: Line.append((0,0,0))
            else: Line.append(pygame.Rect(x,y,t,t))
            x += t+e
        rects_m.append(Line)
        y +=t+e
        x = dx
    return rects_m

def drawMatrizColor(color_mat,screen,Mat):
    for colun in range(len(color_mat)):
        for line in range(len(color_mat[colun])):
            pygame.draw.rect(screen, color_mat[colun][line], Mat[colun][line])
            
def testMatrizClick(mat,tamX,tamY,m,et_mouse):
    for a in range(tamY):
        for b in range(tamX):
            if testButton(mat[a][b],m) and et_mouse: 
                return True,a,b
    return False,0,0 
    
def doubleFrame(main_mat):
    Ret = []
    for a in range(len(main_mat)):
        ret_l = []
        for b in range (len(main_mat[a])):
            ret_l.append(main_mat[a][b])
        Ret.append(ret_l)
    return Ret

def readDataSaved(tamX, tamY):
    matriz = [] 
    cont = 0
    arqName = "color_saved.txt"
    file = open(arqName,'r')
    lines = file.readlines()
    for Y in range(tamY):
        colun = []
        for X in range(tamX):
            try: data_count = lines[cont]
            except: data_count = '(0,0,0)\n'
            data_count = data_count.split(',')
            data_count = data_count[0].split('(') + data_count[1:]
            data_count = data_count[1:len(data_count)-1] + data_count[len(data_count)-1].split(')')
            data_count = list(map(int,data_count[0:len(data_count)-1]))
            colun.append((data_count[0],data_count[1],data_count[2]))
            cont += 1
        matriz.append(colun)
    return matriz

def main():
    main_matriz = []
    current_frame = -1
    tam = -1

    tamX, tamY = 30, 12

    running = True
    screen = pygame.display.set_mode([1000,500])
    pygame.display.set_caption('Animation Genetor: ')

    main_color = pygame.Rect(728, 31, 58, 58)
    main_colorborder = pygame.Rect(727, 30, 60, 60)
    button_colorselect = pygame.Rect(727, 105, 60, 60)
    button_new_frame = pygame.Rect(30, 313, 100, 30)
    but_duplicateframe = pygame.Rect(135,313,100,30)
    but_front = pygame.Rect(275,313,30,30)
    but_back = pygame.Rect(240,313,30,30)

    rects_m = genRectMatriz(30,30,tamX,tamY,20,3,False)
    rects_sc = genRectMatriz(728,178,3,6,17,4.5,False) 
        
    font = [25, 20, 15]
    font = fontVector(font)

    r,g,b = 0,0,0

    c = False

    while running:
        save_mat = readDataSaved(3,6)
        m = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (c): 
                running = False

            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)

            if testButton(button_colorselect,m) and et_mouse:
                r1,g1,b1,s,c = selectColor(r,g,b,screen,font,300,130)
                if s: r,g,b = r1,g1,b1
                
            if (testButton(button_new_frame,m) and et_mouse) or tam == -1:
                main_matriz.insert(current_frame+1,genRectMatriz(0,0,tamX,tamY,0,0,True))
                current_frame += 1
                tam+=1


            if testButton(but_duplicateframe,m) and et_mouse:
                main_matriz.insert(current_frame+1,doubleFrame(main_matriz[current_frame]))
                current_frame += 1
                tam+=1

            if testButton(but_back,m) and et_mouse:
                if current_frame == 0: current_frame = tam
                else: current_frame -= 1

            if testButton(but_front,m) and et_mouse:
                if current_frame == tam: current_frame = 0
                else: current_frame += 1

            test,changed_X,changed_Y = testMatrizClick(rects_m,tamX,tamY,m,et_mouse)
            if test: main_matriz[current_frame][changed_X][changed_Y] = (r, g, b) 

        if c: break

        screen.fill((50, 50, 50))

        str_to_txt = str(current_frame+1) + ' of ' + str(tam+1) 
        txt = font[1].render(str_to_txt,True,(255,255,255))
        screen.blit(txt, (30,7))
        
        drawMatrizColor(main_matriz[current_frame],screen,rects_m)
        drawMatrizColor(save_mat,screen,rects_sc)

        pygame.draw.rect(screen, (0 , 0, 0), main_colorborder)
        pygame.draw.rect(screen, (r, g, b), main_color)
        pygame.draw.rect(screen, (70, 70, 70), button_colorselect)
        pygame.draw.rect(screen, (70, 70, 70), but_front)
        pygame.draw.rect(screen, (70, 70, 70), but_back)
        pygame.draw.rect(screen, (70, 70, 70), but_duplicateframe)
        pygame.draw.rect(screen, (70, 70, 70), button_new_frame)
        
        pygame.display.update()

main()