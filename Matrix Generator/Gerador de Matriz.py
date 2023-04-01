import subprocess
import pygame
import time
import os

pygame.init()

bar = ''
if os.name == 'nt': 
    bar = "\\"
    open_arq = 'explorer'
else: 
    bar = '/'
    open_arq = 'open'

def testButton(rect, mouse):
    if (rect.topleft[0] <= mouse[0] <= rect.topright[0]) and (rect.topleft[1] <= mouse[1] <= rect.bottomright[1]): return True
    else: return False

def testButtons(listB, mouse):
    rects = []
    for count in range(len(listB)): 
        rects.append(testButton(listB[count], mouse))
    return rects
        
def colorButtons(status, d):
    c = []
    for Rect in range(len(status)): c.append(d[Rect][int(status[Rect])])
    return c

def insertText(test,tBox,event,dMaxL,blk):
    for keyTeste in range(len(test)):
        if event.type == pygame.KEYDOWN and test[keyTeste]:
            if event.key == pygame.K_BACKSPACE: tBox[keyTeste] = tBox[keyTeste][: - 1]
            elif len(tBox[keyTeste]) < dMaxL[keyTeste] and event.unicode not in blk: tBox[keyTeste] += event.unicode
    return tBox

def TestStatus(status,et_mouse,rgb,tBox,m,tx,mod_t):
    Drgb = {'r':0, 'g':1, 'b':2}
    if status[0] and et_mouse: tBox[Drgb[rgb]] = str(int(tBox[Drgb[rgb]]) + 1)
    if status[1] and et_mouse: tBox[Drgb[rgb]] = str(int(tBox[Drgb[rgb]]) - 1)

    if status[2]: 
        if et_mouse: mod_t[Drgb[rgb]], tBox[Drgb[rgb]] = True, ''
    else: mod_t[Drgb[rgb]] = False
    if (status[3] and et_mouse): tBox[Drgb[rgb]] = str(((m[0] - (tx + 170) - 25)*255)//155)
    return tBox,mod_t

def testmatrixClick(mat,tamX,tamY,m,et_mouse):
    for a in range(tamY):
        for b in range(tamX):
            if testButton(mat[a][b],m) and et_mouse: 
                return True,b,a
    return False,0,0

def fontVector(vector_size):
    vector_font = [] 
    for a in vector_size:
        vector_font.append(pygame.font.Font('freesansbold.ttf', a))
    return vector_font

def linkBox(r,g,b,tBox):
    list_rgb = [r,g,b]
    for a in range(len(list_rgb)):
        try: list_rgb[a] = int(tBox[a])
        except ValueError: 
            if tBox[a] == '': list_rgb[a] = 0
            else: tBox[a] = str(list_rgb[a])    
        if list_rgb[a] < 0: tBox[a], list_rgb[a] = "0", 0
        if list_rgb[a] > 255: tBox[a], list_rgb[a] = "255", 255
    return list_rgb[0],list_rgb[1],list_rgb[2],tBox

def convert2RGB(hexa):
    if len(hexa) < 7:
        for a in range(7 - len(hexa)): hexa += '0'
    if hexa[0] == '#':
        try: R, G, B = int(hexa[1:3], base=16), int(hexa[3:5], base=16), int(hexa[5:7], base=16) 
        except ValueError: R, G, B = 0, 0, 0
        return [str(R), str(G), str(B), hexa]
    else: return ['0', '0', '0', hexa]

def convert2hex(r, g, b):
    r, g, b = hex(r)[2:4], hex(g)[2:4], hex(b)[2:4]
    if len(r) == 1: r = '0' + r
    if len(g) == 1: g = '0' + g
    if len(b) == 1: b = '0' + b
    return "#" + r + g + b

def createRect(tx, ty, L):
    R = []
    for r in L: R.append(pygame.Rect(tx + r[0], ty + r[1], r[2], r[3]))
    return R

def genRectmatrix(dx,dy,tamX,tamY,t,e,data):
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

def drawRect(screen, colorL, RectsL):
    for count in range(len(RectsL)):
        pygame.draw.rect(screen,colorL[count],RectsL[count])

def drawText(screen,tt,font,ft,pos,ct,notList):
    T, TP = [], []
    for tp in range(len(tt)):
        T = font[ft[tp]].render(tt[tp], True, ct[tp])
        TP = T.get_rect()
        if tp not in notList: TP.center = pos[tp].center
        else:TP.center = pos[tp]
        screen.blit(T, TP)
def drawmatrixColor(tamX,tamY,color_mat,screen,Mat,limX,b):
    for colun in range(tamY):
        for line in range(limX-tamX,limX):
            if color_mat[colun][line] != (0,0,0) or b:
                pygame.draw.rect(screen, color_mat[colun][line], Mat[colun][line-(limX-tamX)])

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    try: pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    except: pygame.draw.rect(shape_surf, (0,0,0), shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def drawPrevmatrixColor(tamX,tamY,color_mat,screen,Mat):
    for colun in range(tamY):
        for line in range(tamX):
            if color_mat[colun][line] != (0,0,0):
                draw_rect_alpha(screen,concate_tu(color_mat[colun][line],75),Mat[colun][line])

def saveColor(r, g, b, font, tx, ty, screen):
    file = open("color_saved.txt", 'r+')    
    f = str((r, g, b)) + '\n'
    Lines = file.readlines()
    if f in Lines: txt_saveok = 'Color Already Saved.'   
    else: 
        txt_saveok = 'Color Saved Successfully.'
        file.write(f)
    file.close

    running_wsave = True
    tx, ty = tx + 100, ty + 33
    d,dt = {0:[(50,50,50),(255,0,0)]},{0: [(180,180,180),(255,255,255)]}
    ft,tt,ct = [2,2,2],[txt_saveok,'Save','X'],[(180,180,180),(180,180,180)]
    Rect_winSAVE,Color_LIST = [(-1, -1, 202, 127),(0, 25, 200, 100),(0, 0, 200, 25),(150, 0, 50, 25)],[(0, 0, 0),(30, 30, 30),(50, 50, 50)]
    Rect_winSAVE = createRect(tx,ty,Rect_winSAVE)

    while running_wsave:
        m = pygame.mouse.get_pos()
        status = testButtons([Rect_winSAVE[0],Rect_winSAVE[3]], m)
        for event in pygame.event.get():
            et_mouse = event.type == pygame.MOUSEBUTTONDOWN
            if event.type == pygame.QUIT: return True
            if (status[1] and et_mouse) or (not(status[0]) and et_mouse): running_wsave = False

        ct2 = colorButtons([status[1]],dt)
        Color_LIST2 = colorButtons([status[1]],d)
        
        drawRect(screen, Color_LIST+Color_LIST2, Rect_winSAVE)
        drawText(screen,tt,font,ft,Rect_winSAVE[1:],ct+ct2,[])
        pygame.display.update()
    return False

def selectColor(red,green,blue,screen, font, tx, ty):
    running_color_select = True

    rects,y = [(-1,-1,402,192),(0, 0, 400, 25), (15, 40, 94, 91)],[40,75,110]
    but = [(355, 40, 20, 20), (170, 40, 20, 20), (125, 40, 40, 20), (195, 40, 155, 20), (355, 75, 20, 20), (170, 75, 20, 20), (125, 75, 40, 20), (195, 75, 155, 20), (355, 110, 20, 20), (170, 110, 20, 20), (125, 110, 40, 20), (195, 110, 155, 20), (255, 145, 120, 30), (175, 145, 75, 30), (95, 145, 75, 30), (15, 145, 75, 30), (350, 0, 50, 25), (0, 25, 400, 165)]
    rects,but = createRect(tx, ty, rects),createRect(tx, ty, but)
    
    ft, dt,d = [],{},{}
    for c in range(len(but)-1):
        ft.append(2)
        dt[c] = [(140,140,140),(255,255,255)]        
        if c == 2: dt[c] = [(150,0,0),(255,0,0)]
        if c == 6: dt[c] = [(0,150,0),(0,255,0)]
        if c == 10: dt[c] = [(0,0,150),(0,0,255)]
        if c == 16: d[c] = [(30,30,30),(255,0,0)] 
        else: d[c] = [(60,60,60),(90,90,90)]   
    ft = ft + [2,2,2,2]
 
    tBox = [str(red), str(green), str(blue), ''] 
    mod_b,mod_t, mod_hexa, close = [False, False, False],[False, False, False], False, False
    color_select_satus = False
   
    et_mouse = False
   
    while running_color_select:
        m = pygame.mouse.get_pos()
        status = testButtons(but, m)

        for event in pygame.event.get():
            et_mouse = pygame.mouse.get_pressed()[0]    
            if event.type == pygame.QUIT: color_select_satus, running_color_select, close = False, False, True
            tBox,mod_t = TestStatus(status[0:4],et_mouse,"r",tBox,m,tx,mod_t)
            tBox,mod_t = TestStatus(status[4:8],et_mouse,"g",tBox,m,tx,mod_t)
            tBox,mod_t = TestStatus(status[8:12],et_mouse,"b",tBox,m,tx,mod_t)
            
            if status[12] and et_mouse: mod_hexa = True
            elif not(status[12]) and et_mouse: mod_hexa = False
            
            if status[13] and et_mouse:
                status[13] = False
                if saveColor(red, green, blue, font, tx, ty, screen): 
                    color_select_satus, running_color_select, close = False, False, True
            
            if (status[14] and et_mouse) or (status[16] and et_mouse) or (not(status[17]) and et_mouse): 
                color_select_satus, running_color_select, close = False, False, False
            
            if status[15] and et_mouse: 
                color_select_satus, running_color_select, close = True, False, False

            dMaxL = {0: 3, 1:3, 2:3, 3:7}
            test = mod_t + [mod_hexa]           
            tBox = insertText(test,tBox,event,dMaxL,[])
        red,green,blue,tBox = linkBox(red,green,blue,tBox)
        if not(running_color_select): break
        if mod_hexa: tBox = convert2RGB(tBox[3])
        else: tBox[3] = convert2hex(red, green, blue)

        Butcolor = colorButtons(status[:-1], d)
        drawRect(screen, [(0,0,0),(30,30,30)],rects[:-1])  
        pygame.draw.rect(screen,(40,40,40),but[len(but)-1])    
        drawRect(screen, Butcolor, but[:-1])
        pygame.draw.rect(screen,(red,green,blue),rects[len(rects)-1])

        c = (red,green,blue) 
        color = [(red,0,0),(0,green,0),(0,0,blue)]
        for bar in range(3): pygame.draw.rect(screen, color[bar], (tx + 195, ty + y[bar], (c[bar]*155)/255, 20))

        ct = colorButtons(status[:-1],dt) + [(255,0,0),(0,255,0),(0,0,255),(140,140,140)]
        tt = ['+','-',('0' if tBox[0] == '' else tBox[0]),'', '+','-',('0' if tBox[1] == '' else tBox[1]),'','+','-',('0' if tBox[2] == '' else tBox[2]),'',tBox[3],"Save","Cancel","Ok","X","R","G","B",'Select Color']    
        drawText(screen,tt,font,ft,but[:-1]+[(tx+385,ty+50),(tx+385,ty+85),(tx+385,ty+120)]+[rects[1]],ct,[17,18,19])
        pygame.display.update()

    return (red, green, blue, color_select_satus, close)

def SelectOP_anim(x,y,screen, font, tt):
    n = len(tt)
    tam = ((n*30)+((n+1)*5))
    y = y - tam 
             
    c, Running_opW,op = False, True, 0
    but,ft, b_OnOff, bt_OnOff = [],[],{},{}
    Rects = [(x-1,y-1,102,tam+2), (x,y,100,tam)]  
    y += 5
    for a in range(n):
        ft.append(2)
        but.append((x+5,y+(a*30)+(5*a),90,30))
        b_OnOff[a],bt_OnOff[a] = [(60,60,60),(90,90,90)],[(140,140,140),(255,255,255)]
   
    Rects, but = createRect(0, 0, Rects),createRect(0, 0, but)

    while Running_opW:
        m = pygame.mouse.get_pos()
        status = testButtons(but, m)
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            if (event.type == pygame.QUIT): c, Running_opW,op = True, False, 0
            if not(testButton(Rects[0],m)) and et_mouse: Running_opW,op = False, 0
            for s in range(len(status)):
                if status[s] and et_mouse: Running_opW,op = False, s+1

        colorR = [(0,0,0),(35,35,35)]
        colorB = colorButtons(status, b_OnOff)
        ct = colorButtons(status, bt_OnOff)
        drawRect(screen, colorR+colorB, Rects+but)
        drawText(screen,tt,font,ft,but,ct,[])
        pygame.display.update()
    return c,op

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
                    txts = [arq.split(bar)[1] for arq in arquivos if arq.lower().endswith(".txt")] 
                    if (name + ".txt") not in txts:
                        return c,True,name
                    else:
                        c,op = alert((818/2)-170,(373/2)-80,font,screen,["Export as", "There is already animation" ,"saved with this name"],["Replace","Keep"])
                        if op == 0: return c,False,"" 
                        elif op == 1:
                            os.remove("saved_anim{}.txt".format(bar,name)) 
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

def loadIn(dx,dy,screen,font):
    c,RunningLoadIN,sel = False,True,0
    caminhos = [os.path.join("saved_anim", nome) for nome in os.listdir("saved_anim")]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    txts = [arq.split(bar)[1] for arq in arquivos if arq.lower().endswith(".txt")] # win vs ubu
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

def concate_tu(t1,t2):
    t1 = list(t1)
    t1.append(t2)
    return tuple(t1)

def sign(a):
    if a < 0: return -1
    if a == 0: return 0
    if a > 0: return 1

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

def changeColorCircle(mainMat,x,y,color):
    try:
        if x >= 0 and y >= 0: mainMat[int(y)][int(x)] = color
        return mainMat
    except IndexError:
        return mainMat

def readDataSaved(tamX, tamY):
    matrix,cont,arqName = [], 0, "color_saved.txt"
    try:
        with open(arqName,'r') as file: lines = file.readlines()
    
    except FileNotFoundError:
        with open(arqName,'w') as file: file.close()
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
        matrix.append(colun)

    while len(lines) > 0:
        for ncolor in range(tamY):
            try:
                dataReaded = lines[0]
                lines.pop(0)
            except: dataReaded = '(0, 0, 0)\n'
            dataReaded = list(map(int,(dataReaded.strip('\n'))[1:-1].split(", ")))
            matrix[ncolor].append((dataReaded[0],dataReaded[1],dataReaded[2]))
    return matrix

def export_Mat(matrix, name):
    t = "saved_anim/" + name + ".txt"
    with open(t,"w") as f:
        for third_d in matrix:
            for second_d in third_d:
                for firt_d in second_d:
                    f.write("(" + ', '.join(map(str,firt_d)) + ")-")
                f.write("\n")
            f.write("# new Layer\n")

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

def drawLine(mainmatrix,P1,P2,color):
    x1,y1,x2,y2 = P1[0],P1[1],P2[0],P2[1]
    x,y = x1,y1
    deltaX,deltaY = abs(x2-x1),abs(y2-y1)
    S1,S2 = sign(x2-x1),sign(y2-y1)
    
    if deltaY > deltaX:
        temp,interchange = deltaX,1
        deltaX,deltaY = deltaY,temp

    else: interchange = 0
    e = (2 * deltaY) - deltaX 
    a = 2 * deltaY 
    b = (2 * deltaY) - (2 * deltaX)
    mainmatrix[y][x] = color

    for i in range(1,deltaX+1):
        if e < 0:
            if interchange == 1: y = y + S2
            else: x = x + S1
            e = e + a
        else:
            y = y + S2
            x = x + S1
            e = e + b
        mainmatrix[y][x] = color
    return mainmatrix

def drawCircle(mainmatrix,P1,P2,color,full):
    X_center, Y_center = P1[0], P1[1]
    r = ((P2[0]-X_center)**2 + (P2[1]-Y_center)**2)**0.5 
    
    extrem_p1,extrem_p2,extrem_p3,extrem_p4 = (X_center-r, Y_center-r),(X_center+r, Y_center-r),(X_center-r, Y_center+r),(X_center+r, Y_center+r)
    
    x = r
    y = 0

    mainmatrix = changeColorCircle(mainmatrix,(x + X_center), (y + Y_center),color)
    mainmatrix = changeColorCircle(mainmatrix,(-x + X_center), (y + Y_center),color)
    mainmatrix = changeColorCircle(mainmatrix,(y + X_center), (x + Y_center),color)
    mainmatrix = changeColorCircle(mainmatrix, (y + X_center), (-x + Y_center),color)    

    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + (2 * y) + 1
        else:        
            x -= 1
            P = P + (2 * y) - (2 * x) + 1
        if (x < y): break
        mainmatrix = changeColorCircle(mainmatrix,(x + X_center),(y + Y_center), color)    
        mainmatrix = changeColorCircle(mainmatrix,(-x + X_center), (y + Y_center), color)   
        mainmatrix = changeColorCircle(mainmatrix,(x + X_center), (-y + Y_center), color)   
        mainmatrix = changeColorCircle(mainmatrix,(-x + X_center), (-y + Y_center), color)  
        if x != y:
            mainmatrix = changeColorCircle(mainmatrix,(y + X_center), (x + Y_center), color)  
            mainmatrix = changeColorCircle(mainmatrix,(-y + X_center), (x + Y_center), color) 
            mainmatrix = changeColorCircle(mainmatrix,(y + X_center), (-x + Y_center), color)  
            mainmatrix = changeColorCircle(mainmatrix,(-y + X_center), (-x + Y_center), color)

    if full:
        extrem_p1,extrem_p2,extrem_p3 = (X_center-r, Y_center-r),(X_center+r, Y_center-r),(X_center-r, Y_center+r)

        for yt in range(int(extrem_p2[0]-extrem_p1[0])):
            for xt in range(int(extrem_p3[1]-extrem_p1[1])):
                rn = ((extrem_p1[0] + xt - X_center)**2 + (extrem_p1[1]+yt - Y_center)**2)**0.5        
                if rn <= r: changeColorCircle(mainmatrix,extrem_p1[0] + xt, extrem_p1[1]+yt, color)
    return mainmatrix

def drawSquare(main_matrix,Pg1,Pg2,color,full):
    p1,p2,p3,p4 = Pg1,(Pg2[0],Pg1[1]),(Pg1[0],Pg2[1]),Pg2    
       
    if full:
        l = [p1,p2,p3,p4]
        l.sort(key = lambda x: (x[0],x[1]))

        pe1 = l[0]
        pe2 = l[-1]    

        for yt in range(pe1[1], pe2[1]+1):
            for xt in range(pe1[0],pe2[0]+1):
                main_matrix[yt][xt] = color

    else:
        main_matrix = drawLine(main_matrix,p1,p2,color) 
        main_matrix = drawLine(main_matrix,p1,p3,color) 
        main_matrix = drawLine(main_matrix,p3,p4,color) 
        main_matrix = drawLine(main_matrix,p2,p4,color) 
    return main_matrix
        
def main(tamX, tamY):
    cwd = os.getcwd()
    path_dir = cwd + bar + "saved_anim"

    if tamX < 30: tamX = 30
    if tamY < 12: tamY = 12

    lx = 30+(tamX*20)+((tamX-1)*3) + 10
    ly = 30+(tamY*20)+((tamY-1)*3) + 10
    d = tamX-30
    r,g,b = 0,0,0

    try:    
        os.mkdir(path_dir)
    except FileExistsError:
        print('Fail')
    
    running,change, removC, anim,c,in_load,full = True, False, False, False, False,False,False
    current_frame,tam,opp,Tool = -1,-1,0,0
    Point, main_matrix,indexC,option = [],[],3,0
    clock, frame_rate, tamXC, tamYC = time.time(),5 ,3, 6

    name = 'New Animation'
    screen = pygame.display.set_mode((lx+90,ly + 60))

    font = [25, 20, 15]
    font = fontVector(font)

    colorsr = pygame.Rect(728,178,60,124.5)
    Rects = (lx+1, 31, 58, 58), (lx, 30, 60, 60)
    but = [(lx, 105, 60, 60),(30,ly,50,30),(85, ly, 100, 30),(190,ly,100,30),(295,ly,100,30),(400,ly,30,30),(435,ly,30,30),(470,ly,30,30),(lx-105,ly,100,30),(lx,ly,28,30),(lx+33,ly,28,30),(lx - 222,ly,80,30),(lx - 137,ly,27,30)]
    tool_op = {0: "Tools", 1:"Color Dtc",2:"Line",3:"Square",4:"Circle"}

    but_OnOff = {}
    for y in range(len(but)):
        but_OnOff[y] = [(60,60,60),(90,90,90)]

    but = createRect(0, 0, but)
    Rects = createRect(0, 0, Rects)
    rects_m = genRectmatrix(30,30,tamX,tamY,20,3,False)
    rects_sc = genRectmatrix(lx+1,178,tamXC,tamYC,17,4.5,False) 
    tt = ["Add","Arq","New Frame","Duplicate","Remove","<",">","","Rmv. Color","<",">","",""]

    ct2,ft2 = [],[]
    for x in range(len(but)):
        ct2.append((150,150,150))
        ft2.append(2)
    ft,ct,pos = [1] + ft2,[(255,255,255)] + ct2,[(56,17)] + but
    
    while running: 
        pygame.display.set_caption('Animation Generator: ' + name)
        save_mat = readDataSaved(tamXC,tamYC)

        if option == 4: option, in_load = 1, True

        if option == 1: 
            if not(change):
                if in_load:
                    c,t,mat_rol, tam,n = loadIn((818/2)-115,(373/2)-117.5,screen,font)
                    if t: main_matrix,name = mat_rol, n
                    current_frame,change,in_load = 0,False,False 
                else:
                    main_matrix = [genRectmatrix(0,0,tamX,tamY,0,0,True)]
                    current_frame,tam = 0,0
                    name,change = 'New Animation',False
            
            else:
                try: comp = (import_Mat(name) != main_matrix)
                except: comp = False

                if not comp: c,opp = alert((818/2)-170,(373/2)-80,font,screen,["New Animation", "Changes were not saved." ,"What do you want to do"],["Discard","Save"])
                else: c,opp = False, 1

                if opp == 1: 
                    if in_load:
                        c,t,mat_rol, tam,n = loadIn((818/2)-115,(373/2)-117.5,screen,font)
                        if t: main_matrix,name = mat_rol,n
                        current_frame,change,in_load = 0,False,False
                    else: 
                        main_matrix = [genRectmatrix(0,0,tamX,tamY,0,0,True)]
                        current_frame,tam = 0,0
                        name,change = 'New Animation',False
                    opp = 0
                if opp == 2: option = 2
                
        if option == 2:
            if name != 'New Animation':
                os.remove("saved_anim/{}.txt".format(name)) 
                export_Mat(main_matrix, name)
                change = False
            else: option = 3

        if option == 3:
            c,t,n = saveAsAnim((818/2)-145,(373/2)-95,font,screen)
            if t:
                name,change = n, False 
                export_Mat(main_matrix, name)

        if opp == 2:
            if in_load:
                c,t,mat_rol, tam,n = loadIn((818/2)-115,(373/2)-117.5,screen,font) 
                if t: main_matrix,name,change = mat_rol,n,False
                current_frame,in_load = 0,False
            else: 
                main_matrix = [genRectmatrix(0,0,tamX,tamY,0,0,True)]
                current_frame,tam = 0,0
                name,change = 'New Animation',False
            opp = 0

        if option == 5:
            subprocess.Popen([open_arq,path_dir])

        if (option > 0) and (option <= 5): option = 0  

        tt[11] = tool_op[Tool]
        m = pygame.mouse.get_pos()
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
            status = testButtons(but, m)

            if (event.type == pygame.QUIT) or (c): running = False
            if not(testButton(colorsr,m)) and et_mouse and removC: removC = False
    

            test,changed_X,changed_Y = testmatrixClick(rects_m,tamX,tamY,m,et_mouse)
            if test and (not anim) and Tool == 1:
                r,g,b = main_matrix[current_frame][changed_Y][changed_X] 
            
            elif test and (not anim):
                change = True
                if(event.button == 3): main_matrix[current_frame][changed_Y][changed_X] = (0, 0, 0)
                else:
                    main_matrix[current_frame][changed_Y][changed_X-d] = (r, g, b)

            if test and (not anim) and (2 <= Tool <= 4):
                if(event.button == 3): 
                    if len(Point) > 0:
                        Point.pop(0)
                else: Point.append((changed_X,changed_Y)) 

                if len(Point) == 2:
                    
                    if Tool == 2: main_matrix[current_frame] = drawLine(main_matrix[current_frame],Point[0],Point[1],(r,g,b))
                    if Tool == 3: main_matrix[current_frame] = drawSquare(main_matrix[current_frame],Point[0],Point[1],(r,g,b),full)
                    if Tool == 4: main_matrix[current_frame] = drawCircle(main_matrix[current_frame],Point[0],Point[1],(r,g,b),full)
                    Point = []
                   
                    
            testC,changed_XC,changed_YC = testmatrixClick(rects_sc,tamXC,tamYC,m,et_mouse)
            if testC:
                if removC:
                    changedColorSave(save_mat[changed_YC][changed_XC+(indexC-tamXC)])
                else:
                    color_to_change = save_mat[changed_YC][changed_XC+(indexC-tamXC)]             
                    r,g,b = color_to_change[0],color_to_change[1],color_to_change[2]

            if status[0] and et_mouse and (not anim):
                r1,g1,b1,s,c = selectColor(r,g,b,screen,font,lx - 339,105)
                if s: r,g,b = r1,g1,b1

            if status[1] and et_mouse and (not anim):
                c,option = SelectOP_anim(30,ly+30,screen,font, ["New","Export","Export as","Load","Folder"])

            if (status[2] and et_mouse and (not anim)) or tam == -1:
                main_matrix.insert(current_frame+1,genRectmatrix(0,0,tamX,tamY,0,0,True))
                current_frame += 1
                tam+=1
                if tam != 0:
                    change = True

            if status[3] and et_mouse and (not anim):
                main_matrix.insert(current_frame+1,doubleFrame(main_matrix[current_frame]))
                current_frame += 1
                tam+=1
                change = True
            
            if status[4] and et_mouse and (not anim):
                if len(main_matrix) > 1:
                    tam -=1
                    main_matrix.pop(current_frame)
                    if current_frame>tam: current_frame=0
                else:
                    main_matrix.pop(current_frame)
                    main_matrix.append(genRectmatrix(0,0,tamX,tamY,0,0,False))
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
                if removC: removC = False
                else: removC = True
            
            if status[9] and et_mouse and indexC > tamXC: 
                indexC -= 1 
            
            if status[10] and et_mouse and indexC < len(save_mat[0]):  
                indexC+=1 

            if status[11] and et_mouse and (not anim):
                if Tool != 0:
                    Tool = 0
                else:
                    c,Tool = SelectOP_anim(lx-222,ly+30,screen,font,["Color Dtc","Line","Square","Circle"])
                    Point = []

            if status[12] and et_mouse and (not anim):
                if full: full = False
                else: full = True

        if c: break
        screen.fill((37,37,37))

        if anim:
            if time.time() - clock >= (1/frame_rate):
                if current_frame == tam: current_frame = 0
                else: current_frame += 1
                clock = time.time()

        colorR = [(0,0,0),(r,g,b)] 
        colorB = colorButtons(status, but_OnOff)
        drawmatrixColor(tamX,tamY,main_matrix[current_frame],screen,rects_m,30,True) 
        
        if len(main_matrix) > 1 and not(anim): 
            if (current_frame != 0): drawPrevmatrixColor(tamX,tamY,main_matrix[current_frame-1],screen,rects_m)
            else: drawPrevmatrixColor(tamX,tamY,main_matrix[-1],screen,rects_m)

        drawmatrixColor(tamX,tamY,main_matrix[current_frame],screen,rects_m,30,False)    
        drawmatrixColor(tamXC,tamYC,save_mat,screen,rects_sc,indexC,True)
        drawRect(screen, colorR+colorB, Rects+but)
        drawText(screen,[str(current_frame+1) + ' of ' + str(tam+1)] + tt, font, ft, pos, ct, [0])
        
        if anim:
            pygame.draw.rect(screen,(150,150,150),(480,ly+9,4,14))
            pygame.draw.rect(screen,(150,150,150),(486.5,ly+9,4,14))
        else: pygame.draw.polygon(screen,(150,150,150),[[480, ly+10],[490,ly+15],[480,ly+20]])
        if full: pygame.draw.rect(screen,(150,150,150),(lx-132,ly+5,17,20),0) 
        else: pygame.draw.rect(screen,(150,150,150),(lx-132,ly+5,17,20),2)
        if removC: pygame.draw.circle(screen, (255, 0, 0),[lx-105, ly], 5) 
        
        if Tool == 2 or Tool == 3 or Tool == 4:
            if len(Point) == 1: pygame.draw.rect(screen,(150,150,150),(508,ly+25,35,2))
            elif len(Point) == 2: pygame.draw.rect(screen,(150,150,150),(545,ly+25,35,2))


        pygame.display.update()

main(30,12)
pygame.quit