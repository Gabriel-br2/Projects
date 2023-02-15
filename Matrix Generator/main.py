# To do: 

# Ferramentas: Linha, quadrado, quadrado preenchido, circulo, circulo preenchido, detect color 
# Otimização


import pygame
import time
import os
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
    ft,tt = [2,2,2,2], ["New","Export","Export as","Load"]        
    Rects, but = [(29,196,102,148), (30,197,100,146)],[(35,202,90,30),(35,237,90,30),(35,273,90,30),(35,308,90,30)]    
    b_OnOff = {0: [(60,60,60),(90,90,90)], 1: [(60,60,60),(90,90,90)], 2: [(60,60,60),(90,90,90)], 3:[(60,60,60),(90,90,90)]}    
    bt_OnOff = {0: [(140,140,140),(255,255,255)], 1:[(140,140,140),(255,255,255)],2: [(140,140,140),(255,255,255)],3:[(140,140,140),(255,255,255)]}
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

        colorR = [(0,0,0),(35,35,35)]
        colorB = colorButtons(status, b_OnOff)
        ct = colorButtons(status, bt_OnOff)
        drawRect(screen, colorR+colorB, Rects+but)
        drawText(screen,tt,font,ft,but,ct,[])
        pygame.display.update()
    return c,op

def export_Mat(matriz, name):
    t = "saved_anim/" + name + ".txt"
    with open(t,"w") as f:
        for third_d in matriz:
            for second_d in third_d:
                for firt_d in second_d:
                    f.write("(" + ', '.join(map(str,firt_d)) + ")-")
                f.write("\n")
            f.write("# new Layer\n")

def alert(dx,dy,font,screen,tt,ops):
    ft = [2,2,2,2,2,2,2]
    Cr = [(0,0,0),(30,30,30),(40,40,40)] 
    c, Running_AlSaved,op = False, True, 0
    bt = ["X",ops[0],ops[1],"Cancel"] 
    B_onOff = {0:[(30,30,30),(255,0,0)], 1:[(60,60,60),(90,90,90)], 2:[(60,60,60),(90,90,90)] , 3:[(60,60,60),(90,90,90)]}
    Rects,buttons = [(-1,-1,342,162),(0,0,340,25),(0,25,340,135)],[(290,0,50,25),(10,105,100,35),(120,105,100,35),(230,105,100,35)]
    bt_onOff = {0:[(180,180,180),(255,255,255)],1:[(140,140,140),(255,255,255)],2:[(140,140,140),(255,255,255)],3:[(140,140,140),(255,255,255)]}
    Rects,buttons = createRect(dx, dy, Rects),createRect(dx, dy, buttons)    
    pos,colorRt = [Rects[1], (dx+170,dy+55),(dx+170,dy+75)],[(140,140,140),(140,140,140),(140,140,140)]
    while Running_AlSaved:
        m = pygame.mouse.get_pos()
        status = testButtons(buttons, m)
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            if (event.type == pygame.QUIT): c, Running_AlSaved = True, False
            for a in range(4):
                if status[a] and et_mouse: op,Running_AlSaved = a,False
        colorB = colorButtons(status, B_onOff)
        colorBt = colorButtons(status, bt_onOff)
        drawRect(screen, Cr+colorB, Rects+buttons)
        drawText(screen, tt + bt, font, ft, pos + buttons,colorRt + colorBt,[1,2])
        pygame.display.update()
    return c,op

def saveAsAnim(dx,dy,font,screen):
    cx,c,Running_SaveA,testName = False, False,True,False
    name = ''
    ft = [1,2,2,2,2,2]
    Rects = [(0, 0, 290, 190), (1, 1, 288, 25),(1, 26, 288, 163)]
    Rects = createRect(dx, dy, Rects)
    tt,pos =["Name of Animation: ","Export as"],[(145+dx,55+dy),Rects[1]]
    colorR,colorRT = [(0,0,0),(30,30,30),(40,40,40)],[(140,140,140),(140,140,140)]
    Buttons = [(240, 1, 48, 25),(20,85,250,35), (20,130,120,35), (150,130,120,35)]
    b_OnOff = {0: [(30,30,30),(255,0,0)],1: [(200,200,200),(255,255,255)], 2:[(60,60,60),(90,90,90)],3:[(60,60,60),(90,90,90)]}
    bt_OnOff = {0: [(180,180,180),(255,255,255)],1:[(50,50,50),(0,0,0)], 2: [(140,140,140),(255,255,255)], 3:[(140,140,140),(255,255,255)]}
    Buttons = createRect(dx, dy, Buttons)  
    while Running_SaveA:
        m = pygame.mouse.get_pos()
        status = testButtons(Buttons, m)
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            if (event.type == pygame.QUIT): c, Running_SaveA = True, False
            if (status[0] and et_mouse) or (not(testButton(Rects[0], m)) and et_mouse) or (status[3] and et_mouse): cx, Running_SaveA = True,False
            if status[1] and et_mouse: testName = True
            if not(status[1]) and et_mouse: testName = False 
            if status[2] and et_mouse and (name != ""):  
                if name == "" or cx: return c,False,name
                else:
                    caminhos = [os.path.join("saved_anim", nome) for nome in os.listdir("saved_anim")]
                    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
                    txts = [arq.split("\\")[1] for arq in arquivos if arq.lower().endswith(".txt")]
                    if (name + ".txt") not in txts:
                        return c,True,name
                    else:
                        c,op = alert((818/2)-170,(373/2)-80,font,screen,["Export as", "There is already animation" ,"saved with this name"],["Replace","Keep"])
                        if op == 0: return c,False,"" 
                        elif op == 1:
                            os.remove("saved_anim\\{}.txt".format(name))
                            return c, True, name
                        elif op == 2:
                            t = 1
                            while (name + ".txt") in txts:
                                if t == 1: name = name + "({})".format(t)
                                else: name = name[:-3] + "({})".format(t) 
                                t += 1
                            return c, True, name            
            name  = insertText([testName],[name],event,[28],["!","=","/",":", "?", "*","<",">","|"])[0]
        colorB = colorButtons(status, b_OnOff)
        btt = ["X",name,"OK","Cancel"]
        colorBT = colorButtons(status, bt_OnOff)
        drawRect(screen, colorR+colorB, Rects+Buttons)
        drawText(screen, tt + btt, font, ft, pos + Buttons, colorRT + colorBT, [0])
        pygame.display.update()
    return c, False, "" 

def import_Mat(name):
    t = "saved_anim/" + name + ".txt"
    with open(t,"r") as f:
        list = f.readlines()
        list = "".join(list[:-1]).split("# new Layer\n")
        for third_d in range(len(list)):
            list[third_d] = "".join(list[third_d][:-1]).split("\n")
            for second_d in range(len(list[third_d])):
                list[third_d][second_d] = "".join(list[third_d][second_d][:-1]).split("-")
                for first_d in range(len(list[third_d][second_d])):
                    list[third_d][second_d][first_d] = tuple(map(int,list[third_d][second_d][first_d][1:-1].split(",")))
    return list

def loadIn(dx,dy,screen,font):
    c,RunningLoadIN,sel = False,True,0
    caminhos = [os.path.join("saved_anim", nome) for nome in os.listdir("saved_anim")]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    txts = [arq.split("\\")[1] for arq in arquivos if arq.lower().endswith(".txt")]
    txts = [arq.split(".")[0] for arq in txts]
    if len(txts) < 8: txts += ["" for t in range(5-len(txts))]

    ft = [2,2,2,2,2,2,2,2,2,2,2]
    d3_onoff = {0:[(60,60,60),(90,90,90)]}
    dtt = {0:[(180,180,180),(255,255,255)]}
    d2_onoff = {0:[(180,180,180),(255,255,255)]}
    tt = ["Load Anim",'up','dw.','Ok','cancel','X']
    Rect = [(-1,-1,232,267),(0,0,230,265),(0,0,230,25)]     
    colorR,Tab,Tab2 = [(0,0,0),(40,40,40),(30,30,30)],[(20,45,150,30)],[(20,45,150,30)]
    B = [(180,135,30,30),(180,170,30,30),(20,205,90,30), (120,205,90,30), (180,0,50,25)]
    d_onoff  = {0:[(60,60,60),(90,90,90)],1:[(60,60,60),(90,90,90)],2:[(60,60,60),(90,90,90)],3:[(60,60,60),(90,90,90)],4:[(30,30,30),(255,0,0)],5: [(180,180,180),(255,255,255)]}
    dt_onOff = {0:[(140,140,140),(255,255,255)],1:[(140,140,140),(255,255,255)],2:[(140,140,140),(255,255,255)],3:[(140,140,140),(255,255,255)],4:[(140,140,140),(255,255,255)],5:[(140,140,140),(255,255,255)]} 

    for a in range(1,5):
        Tab.append((Tab[0][0],Tab[a-1][1]+30,Tab[0][2],Tab[0][3]))
        Tab2.append((Tab2[0][0],Tab2[a-1][1]+30,Tab2[0][2],Tab2[0][3]))
        d2_onoff[a],d3_onoff[a],dtt[a] = [(180,180,180),(255,255,255)],[(60,60,60),(90,90,90)],[(180,180,180),(255,255,255)]

    Tab,Tab2 = createRect(dx, dy, Tab),createRect(dx,dy, Tab2)
    Rect,Buttons = createRect(dx, dy, Rect),createRect(dx, dy, B)    
    lim_in, lim_pos = 0,5

    while RunningLoadIN:
        strin = txts[lim_in:lim_pos]
        m = pygame.mouse.get_pos()
        status,statust = testButtons(Buttons, m),testButtons(Tab,m)
        gstatus = status + statust
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            if (event.type == pygame.QUIT): c, RunningLoadIN = True, False
            if gstatus[0] and et_mouse and (lim_in > 0):
                lim_in -= 1
                lim_pos -= 1
            
            if gstatus[1] and et_mouse and (lim_pos < len(txts)):
                lim_in += 1
                lim_pos += 1

            if gstatus[2] and et_mouse:
                try:
                    l = import_Mat(strin[sel])
                    return c, True, l, len(l)-1,strin[sel]
                except:
                    print("Fail")

            if (gstatus[3] and et_mouse) or (gstatus[4] and et_mouse): c, RunningLoadIN = False, False
            
            for t in range(5):
                if gstatus[5:10][t] and et_mouse:
                    d2_onoff[sel] = [(180,180,180),(255,255,255)]
                    d3_onoff[sel] = [(60,60,60),(90,90,90)]
                    dtt[sel] = [(180,180,180),(255,255,255)]
                    sel = t
                    d2_onoff[sel] = [(255,255,255),(255,255,255)]
                    d3_onoff[sel] = [(90,90,90),(90,90,90)]
                    dtt[sel] = [(255,255,255),(255,255,255)]

        color_but = colorButtons(status, d_onoff)
        color_tbut = colorButtons(status, dt_onOff) 
        colortab = colorButtons(statust, d2_onoff)
        color2tab = colorButtons(statust, d3_onoff)
        colotTtab = colorButtons(statust, dtt)

        drawRect(screen, colorR+color_but+color2tab, Rect+Buttons+Tab2) 
        for b in range(5): pygame.draw.rect(screen,colortab[b],Tab[b],2)
        drawText(screen, tt+strin, font, ft, [Rect[2]] + Buttons + Tab, [(140,140,140)] + color_tbut + colotTtab, [])
        pygame.display.update()
    return c,False,[],0,""         

def drawPauseBut(screen, anim, color):
    if anim:
        pygame.draw.rect(screen,color,(480,322,4,14))
        pygame.draw.rect(screen,color,(486.5,322,4,14))
    else:
        pygame.draw.polygon(screen,color,[[480, 323],[490,328],[480,333]])

def main():
    r,g,b = 0,0,0
    change, removC, anim,c,in_load = False, False, False,False,False
    current_frame,tam,opp = -1,-1,0
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
        ct2.append((150,150,150))
        ft2.append(2)
    ft,ct,pos = [1] + ft2,[(255,255,255)] + ct2,[(56,17)] + but
    tt = ["Add","Arq","New Frame","Duplicate","Remove","<",">","","Rmv. Color","<",">"]
    while running:
        
        pygame.display.set_caption('Animation Generator: ' + name)
        save_mat = readDataSaved(tamXC,tamYC)

        if option == 4: option, in_load = 1, True

        if option == 1: 
            if not(change):
                if in_load:
                    c,t,mat_rol, tam,n = loadIn((818/2)-115,(373/2)-117.5,screen,font)
                    if t: main_matriz,name = mat_rol, n
                    current_frame,change,in_load = 0,False,False 
                else:
                    main_matriz = [genRectMatriz(0,0,tamX,tamY,0,0,True)]
                    current_frame,tam = 0,0
                    name,change = 'New Animation',False
            
            else:
                try: comp = (import_Mat(name) != main_matriz)
                except: comp = False

                if comp: c,opp = alert((818/2)-170,(373/2)-80,font,screen,["New Animation", "Changes were not saved." ,"What do you want to do"],["Discard","Save"])
                else: c,opp = False, 1

                if opp == 1: 
                    if in_load:
                        c,t,mat_rol, tam,n = loadIn((818/2)-115,(373/2)-117.5,screen,font)
                        if t: main_matriz,name = mat_rol,n
                        current_frame,change,in_load = 0,False,False
                    else: 
                        main_matriz = [genRectMatriz(0,0,tamX,tamY,0,0,True)]
                        current_frame,tam = 0,0
                        name,change = 'New Animation',False
                    opp = 0
                if opp == 2: option = 2
                
        if option == 2:
            if name != 'New Animation':
                os.remove("saved_anim\\{}.txt".format(name))
                export_Mat(main_matriz, name)
                change = False
            else: option = 3

        if option == 3:
            c,t,n = saveAsAnim((818/2)-145,(373/2)-95,font,screen)
            if t:
                name,change = n, False 
                export_Mat(main_matriz, name)

        if opp == 2:
            if in_load:
                c,t,mat_rol, tam,n = loadIn((818/2)-115,(373/2)-117.5,screen,font) 
                if t: main_matriz,name,change = mat_rol,n,False
                current_frame,in_load = 0,False
            else: 
                main_matriz = [genRectMatriz(0,0,tamX,tamY,0,0,True)]
                current_frame,tam = 0,0
                name,change = 'New Animation',False
            opp = 0

        if (option > 0) and (option <= 4): option = 0  

        m = pygame.mouse.get_pos()
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            status = testButtons(but, m)

            if (event.type == pygame.QUIT) or (c): running = False
            if not(testButton(colorsr,m)) and et_mouse and removC: removC = False
    
            test,changed_X,changed_Y = testMatrizClick(rects_m,tamX,tamY,m,et_mouse)
            if test and (not anim):
                change = True
                if(event.button == 3): main_matriz[current_frame][changed_Y][changed_X] = (0, 0, 0)
                else: main_matriz[current_frame][changed_Y][changed_X] = (r, g, b)

            testC,changed_XC,changed_YC = testMatrizClick(rects_sc,tamXC,tamYC,m,et_mouse)
            if testC:
                if removC:
                    changedColorSave(save_mat[changed_YC][changed_XC+(indexC-tamXC)])
                else:
                    color_to_change = save_mat[changed_YC][changed_XC+(indexC-tamXC)]             
                    r,g,b = color_to_change[0],color_to_change[1],color_to_change[2]

            if status[0] and et_mouse and (not anim):
                r1,g1,b1,s,c = selectColor(r,g,b,screen,font,388,105)
                if s: r,g,b = r1,g1,b1

            if status[1] and et_mouse and (not anim):
                c,option = SelectSLN_Anim(screen,font)

            if (status[2] and et_mouse and (not anim)) or tam == -1:
                main_matriz.insert(current_frame+1,genRectMatriz(0,0,tamX,tamY,0,0,True))
                current_frame += 1
                tam+=1
                if tam != 0:
                    change = True

            if status[3] and et_mouse and (not anim):
                main_matriz.insert(current_frame+1,doubleFrame(main_matriz[current_frame]))
                current_frame += 1
                tam+=1
                change = True
            
            if status[4] and et_mouse and (not anim):
                if len(main_matriz) > 1:
                    tam -=1
                    main_matriz.pop(current_frame)
                    if current_frame>tam: current_frame=0
                else:
                    main_matriz.pop(current_frame)
                    main_matriz.append(genRectMatriz(0,0,tamX,tamY,0,0,False))
                change = True

            if status[5] and et_mouse and (not anim):
                if current_frame == 0: current_frame = tam
                else: current_frame -= 1

            if status[6] and et_mouse and (not anim):
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
        screen.fill((37,37,37))

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
        drawPauseBut(screen,anim,(150,150,150)) 
        
        if removC: pygame.draw.circle(screen, (255, 0, 0),[622, 313], 5) 
        
        pygame.display.update()

main()
