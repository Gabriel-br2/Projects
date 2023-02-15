import pygame

def testButton(rect, mouse):
    if (rect.topleft[0] <= mouse[0] <= rect.topright[0]) and (rect.topleft[1] <= mouse[1] <= rect.bottomright[1]): return True
    else: return False

def testButtons(listB, mouse):
    rects = []
    for count in range(len(listB)): 
        rects.append(testButton(listB[count], mouse))
    return rects

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

def colorButtons(status, d):
    c = []
    for Rect in range(len(status)): c.append(d[Rect][int(status[Rect])])
    return c

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
                if saveColor(red, green, blue, font, tx, ty, screen): color_select_satus, running_color_select, close = False, False, True
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