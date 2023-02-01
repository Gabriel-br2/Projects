# To do: 

# Ferramentas: Linha, quadrado, quadrado preenchido, circulo, circulo preenchido 
# Export/Inport/New animação: definir nome sem (!= \ / : " ? * <> |), barra de pesquisa para acessar animação, se overwhite n salvar   
# na saida perguntar se quer salvar
# new mtriz
# salvar como
#salvar

# BUGS
# color select bar click apertado
# cores

import pygame
import time
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

def drawMatrizColor(tamX,tamY,color_mat,screen,Mat,limX,b):
    for colun in range(tamY):
        for line in range(limX-tamX,limX):
            if color_mat[colun][line] != (0,0,0) or b:
                pygame.draw.rect(screen, color_mat[colun][line], Mat[colun][line-(limX-tamX)])

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    try: pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    except: pygame.draw.rect(shape_surf, (0,0,0), shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def concate_tu(t1,t2):
    t1 = list(t1)
    t1.append(t2)
    return tuple(t1)

def drawPrevMatrizColor(tamX,tamY,color_mat,screen,Mat):
    for colun in range(tamY):
        for line in range(tamX):
            if color_mat[colun][line] != (0,0,0):
                draw_rect_alpha(screen,concate_tu(color_mat[colun][line],75),Mat[colun][line])
            
def testMatrizClick(mat,tamX,tamY,m,et_mouse):
    for a in range(tamY):
        for b in range(tamX):
            if testButton(mat[a][b],m) and et_mouse: 
                return True,b,a
    return False,0,0
    
def doubleFrame(main_mat):
    Ret = []
    for a in range(len(main_mat)):
        ret_l = []
        for b in range (len(main_mat[a])):
            ret_l.append(main_mat[a][b])
        Ret.append(ret_l)
    return Ret

def changedColorSave(color):
    arqName = "color_saved.txt"
    color2chan = str((color[0], color[1], color[2])) 
    with open(arqName,"r") as f:
        lines = f.readlines()
    with open(arqName,"w") as f:
        for line in lines:
            if line.strip("\n") != color2chan:
                f.write(line)

def readDataSaved(tamX, tamY):
    matriz,cont,arqName = [], 0, "color_saved.txt"
    with open(arqName,'r') as file: lines = file.readlines()
    for Y in range(tamY):
        colun = []
        for X in range(tamX):
            try: 
                dataReaded = lines[0]
                lines.pop(0)
            except: dataReaded = '(0, 0, 0)\n'
            dataReaded = list(map(int,(dataReaded.strip('\n'))[1:-1].split(", ")))
            colun.append((dataReaded[0],dataReaded[1],dataReaded[2]))
            cont += 1
        matriz.append(colun)

    while len(lines) > 0:
        for ncolor in range(tamY):
            try:
                dataReaded = lines[0]
                lines.pop(0)
            except: dataReaded = '(0, 0, 0)\n'
            dataReaded = list(map(int,(dataReaded.strip('\n'))[1:-1].split(", ")))
            matriz[ncolor].append((dataReaded[0],dataReaded[1],dataReaded[2]))
    return matriz






















def SelectSLN_Anim(screen,font):
    c, Running_SaveSW,op = False, True, 0
    ft,tt = [2,2,2], ["Export","Load","New"]
    Rects, but = [(30,232,100,111), (31,233,98,109)], [(35,273,90,30), (35,308,90,30),(35,237,90,30)]    
    b_OnOff = {0: [(75,75,75),(100,100,100)], 1: [(75,75,75),(100,100,100)], 2: [(75,75,75),(100,100,100)]}    
    bt_OnOff = {0: [(160,160,160),(255,255,255)], 1:[(160,160,160),(255,255,255)],2: [(160,160,160),(255,255,255)]}
    Rects, but = createRect(0, 0, Rects),createRect(0, 0, but)

    while Running_SaveSW:
        m = pygame.mouse.get_pos()
        status = testButtons(but, m)
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            if (event.type == pygame.QUIT): c, Running_SaveSW,op = True, False, 0
            if not(testButton(Rects[0],m)) and et_mouse: Running_SaveSW,op = False, 0
            for s in range(len(status)):
                if status[s] and et_mouse: Running_SaveSW,op = False, s+1

        colorR = [(0,0,0),(55,55,55)]
        colorB = colorButtons(status, b_OnOff)
        ct = colorButtons(status, bt_OnOff)
        drawRect(screen, colorR+colorB, Rects+but)
        drawText(screen,tt,font,ft,but,ct,[])
        pygame.display.update()
    return c,op

















def saveAnim(dx,dy,font,screen):
    c,Running_SaveA = False,True
    
    Rects = [(0, 0, 400, 190), (1, 1, 398, 25),(1, 26, 398, 163)]
    Rects = createRect(dx, dy, Rects)
    tt =[]
    pos = []
    
    
    Buttons = [(350, 1, 48, 25)]

    b_OnOff = {0: [(70,70,70),(255,0,0)]}
    bt_OnOff = {0: [(180,180,180),(255,255,255)]}

    Buttons = createRect(dx, dy, Buttons)

    btt = ["X"]
         
    ft = [2]  

    while Running_SaveA:
        m = pygame.mouse.get_pos()
        status = testButtons(Buttons, m)

        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)

            if (event.type == pygame.QUIT): c, Running_SaveA = True, False
            if (status[0] and et_mouse) or (not(testButton(Rects[0], m)) and et_mouse) : Running_SaveA = False

        colorR = [(0,0,0),(70,70,70),(30,30,30)]
        colorB = colorButtons(status, b_OnOff)

        colorRT = []
        colorBT = colorButtons(status, bt_OnOff)

        drawRect(screen, colorR+colorB, Rects+Buttons)
        drawText(screen, tt + btt, font, ft, pos + Buttons, colorRT + colorBT, [])

        pygame.display.update()
    return c
























def main():
    r,g,b = 0,0,0
    removC, anim,c = False,False,False
    current_frame,tam = -1,-1
    running, main_matriz,indexC,option = True,[],3,0
    clock, frame_rate, tamX, tamY, tamXC, tamYC = time.time(),5, 30, 12, 3, 6

    name = 'New Animation'
    screen = pygame.display.set_mode((818,373))

    font = [25, 20, 15]
    font = fontVector(font)

    colorsr = pygame.Rect(728,178,60,124.5)
    Rects = (728, 31, 58, 58), (727, 30, 60, 60)
    but = [(727, 105, 60, 60),(30,313,50,30),(85, 313, 100, 30),(190,313,100,30),(295,313,100,30),(400,313,30,30),(435,313,30,30),(470,313,30,30),(622,313,100,30),(727,313,28,30) ,(760,313,28,30)]
    
    but_OnOff = {}
    for y in range(len(but)):
        but_OnOff[y] = [(60,60,60),(90,90,90)]

    but = createRect(0, 0, but)
    Rects = createRect(0, 0, Rects)
    rects_m = genRectMatriz(30,30,tamX,tamY,20,3,False)
    rects_sc = genRectMatriz(728,178,tamXC,tamYC,17,4.5,False) 

    ct2,ft2 = [],[]
    for x in range(len(but)):
        ct2.append((180,180,180))
        ft2.append(2)
    ft,ct,pos = [1] + ft2,[(255,255,255)] + ct2,[(56,17)] + but
    tt = ["Add","Arq","New Frame","Duplicate","Remove","<",">","Sp","Rmv. Color","<",">"]

    while running:
        pygame.display.set_caption('Animation Generator: ' + name)

        save_mat = readDataSaved(tamXC,tamYC)
        if option == 1:
            c = saveAnim(0,0,font,screen)

        #if option == 2:
        #if option == 3:
        if option == 1 or option == 2 or option == 3: option = 0 

        m = pygame.mouse.get_pos()
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            status = testButtons(but, m)

            if (event.type == pygame.QUIT) or (c): running = False
            if not(testButton(colorsr,m)) and et_mouse and removC: removC = False
    
            test,changed_X,changed_Y = testMatrizClick(rects_m,tamX,tamY,m,et_mouse)
            if test: 
                if(event.button == 3): main_matriz[current_frame][changed_Y][changed_X] = (0, 0, 0)
                else: main_matriz[current_frame][changed_Y][changed_X] = (r, g, b)

            testC,changed_XC,changed_YC = testMatrizClick(rects_sc,tamXC,tamYC,m,et_mouse)
            if testC:
                if removC:
                    changedColorSave(save_mat[changed_YC][changed_XC+(indexC-tamXC)])
                else:
                    color_to_change = save_mat[changed_YC][changed_XC+(indexC-tamXC)]             
                    r,g,b = color_to_change[0],color_to_change[1],color_to_change[2]

            if status[0] and et_mouse:
                r1,g1,b1,s,c = selectColor(r,g,b,screen,font,388,105)
                if s: r,g,b = r1,g1,b1

            if status[1] and et_mouse:
                c,option = SelectSLN_Anim(screen,font)

            if (status[2] and et_mouse) or tam == -1:
                main_matriz.insert(current_frame+1,genRectMatriz(0,0,tamX,tamY,0,0,True))
                current_frame += 1
                tam+=1

            if status[3] and et_mouse:
                main_matriz.insert(current_frame+1,doubleFrame(main_matriz[current_frame]))
                current_frame += 1
                tam+=1
            
            if status[4] and et_mouse:
                if len(main_matriz) > 1:
                    tam -=1
                    main_matriz.pop(current_frame)
                    if current_frame>tam: current_frame=0
                else:
                    main_matriz.pop(current_frame)
                    main_matriz.append(genRectMatriz(0,0,tamX,tamY,0,0,False))

            if status[5] and et_mouse:
                if current_frame == 0: current_frame = tam
                else: current_frame -= 1

            if status[6] and et_mouse:
                if current_frame == tam: current_frame = 0
                else: current_frame += 1

            if status[7] and et_mouse:
                if anim: anim = False
                else: anim = True

            if status[8] and et_mouse and not(removC): 
                removC = True
            
            if status[9] and et_mouse and indexC > tamXC: 
                indexC -= 1 
            
            if status[10] and et_mouse and indexC < len(save_mat[0]):  
                indexC+=1
            

        




        if c: break
        screen.fill((40, 40, 40))

        if anim:
            if time.time() - clock >= (1/frame_rate):
                if current_frame == tam: current_frame = 0
                else: current_frame += 1
                clock = time.time()

        colorR = [(0,0,0),(r,g,b)] 
        colorB = colorButtons(status, but_OnOff)

        drawMatrizColor(tamX,tamY,main_matriz[current_frame],screen,rects_m,30,True) 
        
        if len(main_matriz) > 1 and not(anim): 
            if (current_frame != 0): drawPrevMatrizColor(tamX,tamY,main_matriz[current_frame-1],screen,rects_m)
            else: drawPrevMatrizColor(tamX,tamY,main_matriz[-1],screen,rects_m)

        drawMatrizColor(tamX,tamY,main_matriz[current_frame],screen,rects_m,30,False)    
        drawMatrizColor(tamXC,tamYC,save_mat,screen,rects_sc,indexC,True)
        drawRect(screen, colorR+colorB, Rects+but)
        drawText(screen,[str(current_frame+1) + ' of ' + str(tam+1)] + tt, font, ft, pos, ct, [0])
        pygame.display.update()
main()