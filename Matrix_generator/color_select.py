import pygame

def test_button(r, m):
    if (r.topleft[0] <= m[0] <= r.topright[0]) and (r.topleft[1] <= m[1] <= r.bottomright[1]): return True
    else: return False

def font_vector(vector_size):
    vector_font = [] 
    for a in vector_size:
        vector_font.append(pygame.font.Font('freesansbold.ttf', a))
    return vector_font

def test_all_buttons(l, m):
    r = []
    for c in range(len(l)): r.append(test_button(l[c], m))
    return r

def save(r, g, b, font, tx, ty, screen):
    tx, ty = tx + 100, ty + 33
    file = open("color_saved.txt", 'r + ')    
    f = str((r, g, b)) + '\n'
    Lines = file.readlines()
    if f in Lines: txt_saveok = 'Color Already Saved.'   
    else: 
        txt_saveok = 'Color Saved Successfully.'
        file.write(f)

    file.close

    running_wsave = True
    window_saveborder = pygame.Rect(tx - 1, ty - 1, 202, 127)
    window_saveRect = pygame.Rect(tx, ty + 25, 200, 100)
    window_savBRect = pygame.Rect(tx, ty, 200, 25)
    window_saveExit = pygame.Rect(tx + 150, ty, 50, 25)

    save_title = font[2].render('Save', True, (180, 180, 180))
    save_texit = font[2].render('X', True, (180, 180, 180))
    txt_save = font[2].render(txt_saveok, True, (180, 180, 180))
    
    exit_save = False
    while running_wsave:
        m = pygame.mouse.get_pos()
        for event in pygame.event.get():
            et_mouse = event.type == pygame.MOUSEBUTTONDOWN

            if event.type == pygame.QUIT: 
               return True

            if test_button(window_saveExit, m): exit_save = True
            else: exit_save = False

            if (exit_save and et_mouse) or (not(test_button(window_saveborder, m)) and et_mouse):
                running_wsave = False

        if exit_save: colorsave_exit = (255, 0, 0)
        else: colorsave_exit = (50, 50, 50)

        pygame.draw.rect(screen, (0, 0, 0), window_saveborder)
        pygame.draw.rect(screen, (30, 30, 30), window_saveRect)
        pygame.draw.rect(screen, (50, 50, 50), window_savBRect)
        pygame.draw.rect(screen, colorsave_exit, window_saveExit)

        save_title_rect = save_title.get_rect()
        save_texit_rect = save_texit.get_rect()
        txt_save_rect = txt_save.get_rect()

        save_title_rect.center = window_savBRect.center
        save_texit_rect.center = window_saveExit.center
        txt_save_rect.center = window_saveRect.center
        
        screen.blit(save_texit, save_texit_rect)
        screen.blit(save_title, save_title_rect)
        screen.blit(txt_save, txt_save_rect)

        pygame.display.update()
    return False

def link_BOX(rgb, rgb_box):
    try: rgb = int(rgb_box)
    except ValueError: 
        if rgb_box == '': rgb = 0
        else: rgb_box = str(rgb)
    if rgb < 0: rgb_box, rgb = "0", 0
    if rgb > 255: rgb_box, rgb = "255", 255
    return rgb, rgb_box

def color_test(s):
    color = []
    for a in range(len(s) - 2):
        if s[a]: color.append(((255, 255, 255), (100, 100, 100)))
        else: color.append(((30, 30, 30), (50, 50, 50)))

    if s[16]: color.append(((255, 255, 255), (255, 0, 0)))
    else: color.append(((180, 180, 180), (50, 50, 50)))

    return color

def convert_2RGB(hexa):
    if len(hexa) < 7:
        for a in range(7 - len(hexa)):
            hexa += '0'
    if hexa[0] == '#':
        try: R, G, B = int(hexa[1:3], base=16), int(hexa[3:5], base=16), int(hexa[5:7], base=16) 
        except ValueError: R, G, B = 0, 0, 0
        
        return str(R), str(G), str(B)

    else: 
        return '0', '0', '0'

def convert_2hex(r, g, b):
    r, g, b = hex(r)[2:4], hex(g)[2:4], hex(b)[2:4]

    if len(r) == 1: r = '0' + r
    if len(g) == 1: g = '0' + g
    if len(b) == 1: b = '0' + b

    return "#" + r + g + b

def create_rect(tx, ty, L):
    R = []
    for r in L: R.append(pygame.Rect(tx + r[0], ty + r[1], r[2], r[3]))
    return R

def select_color(red,green,blue,screen, font, tx, ty):
    running_color_select = True

    rects = [(0, 0, 400, 25), (350, 0, 50, 25), (0, 25, 400, 165), (170, 40, 20, 20), (355, 40, 20, 20), (195, 40, 155, 20), (125, 40, 40, 20), (170, 75, 20, 20), (355, 75, 20, 20), (195, 75, 155, 20), (125, 75, 40, 20), (170, 110, 20, 20), (355, 110, 20, 20), (195, 110, 155, 20), (125, 110, 40, 20), (15, 40, 94, 91), (255, 145, 120, 30), (175, 145, 75, 30), (95, 145, 75, 30), (15, 145, 75, 30)]
    rects = create_rect(tx, ty, rects)

#    red, green, blue = 0, 0, 0
    red_tBOX, green_tBOX, blue_tBOX, hex_tBOX = str(red), str(green), str(blue), '' 
    mod_red_b, mod_green_b, mod_blue_b, mod_hexa, close = False, False, False, False, False

    while running_color_select:
        m = pygame.mouse.get_pos()
        status = [rects[4], rects[3], rects[6], rects[5], rects[8], rects[7], rects[10], rects[9], rects[12], rects[11], rects[14], rects[13], rects[16], rects[17], rects[18], rects[19], rects[1], rects[2]]
        status = test_all_buttons(status, m)

        for event in pygame.event.get():
            et_mouse = event.type == pygame.MOUSEBUTTONDOWN

            if event.type == pygame.QUIT: color_select_satus, running_color_select, close = False, False, True

            if (status[16] and et_mouse) or (status[14] and et_mouse) or (not(status[17]) and et_mouse):
                color_select_satus, running_color_select, close = False, False, False

            if status[15] and et_mouse:
                color_select_satus, running_color_select, close = True, False, False

            if status[13] and et_mouse:
                if save(red, green, blue, font, tx, ty, screen): color_select_satus, running_color_select, close = False, False, True

            if status[0] and et_mouse: red_tBOX = str(int(red_tBOX) + 1)
            if status[1] and et_mouse: red_tBOX = str(int(red_tBOX) - 1)

            if status[4] and et_mouse: green_tBOX = str(int(green_tBOX) + 1)
            if status[5] and et_mouse: green_tBOX = str(int(green_tBOX) - 1)
            
            if status[8] and et_mouse: blue_tBOX = str(int(blue_tBOX) + 1)
            if status[9] and et_mouse: blue_tBOX = str(int(blue_tBOX) - 1)

            if status[2]: 
                if et_mouse: mod_red_t, red_tBOX = True, ''
            else: mod_red_t = False

            if status[6]: 
                if et_mouse: mod_green_t, green_tBOX = True, ''
            else: mod_green_t = False

            if status[10]: 
                if et_mouse: mod_blue_t, blue_tBOX = True, ''
            else: mod_blue_t = False

            if status[3] and et_mouse: mod_red_b = True
            elif not(status[3]) and et_mouse: mod_red_b = False

            if status[7] and et_mouse: mod_green_b = True
            elif not(status[7]) and et_mouse: mod_green_b = False

            if status[11] and et_mouse: mod_blue_b = True
            elif not(status[11]) and et_mouse: mod_blue_b = False

            if status[12]:
                if et_mouse: mod_hexa = True
            else: mod_hexa = False
            
            if event.type == pygame.KEYDOWN and mod_red_t:
                if event.key == pygame.K_BACKSPACE: red_tBOX = red_tBOX[: - 1]
                elif len(red_tBOX) < 3: red_tBOX += event.unicode

            if event.type == pygame.KEYDOWN and mod_green_t:
                if event.key == pygame.K_BACKSPACE: green_tBOX = green_tBOX[: - 1]
                elif len(green_tBOX) < 3: green_tBOX += event.unicode
        
            if event.type == pygame.KEYDOWN and mod_blue_t:
                if event.key == pygame.K_BACKSPACE: blue_tBOX = blue_tBOX[: - 1]
                elif len(blue_tBOX) < 3: blue_tBOX += event.unicode

            if event.type == pygame.KEYDOWN and mod_hexa:
                if event.key == pygame.K_BACKSPACE: hex_tBOX = hex_tBOX[: - 1]
                elif len(hex_tBOX) < 7: hex_tBOX += event.unicode

            if mod_red_b: red_tBOX = str(((m[0] - (tx + 170) - 25)*255)//155)
            if mod_green_b: green_tBOX = str(((m[0] - (tx + 170) - 25)*255)//155)
            if mod_blue_b: blue_tBOX = str(((m[0] - (tx + 170) - 25)*255)//155)


        red, red_tBOX = link_BOX(red, red_tBOX)
        green, green_tBOX = link_BOX(green, green_tBOX)
        blue, blue_tBOX = link_BOX(blue, blue_tBOX)
    
        if not(running_color_select): break

        color = color_test(status)

        if mod_hexa: red_tBOX, green_tBOX, blue_tBOX = convert_2RGB(hex_tBOX)
        else: hex_tBOX = convert_2hex(red, green, blue)

        if mod_red_b: color_red_bar = (100, 100, 100)
        else: color_red_bar = color[3][1]
        if mod_green_b: color_green_bar = (100, 100, 100)
        else: color_green_bar = color[7][1]
        if mod_blue_b: color_blue_bar = (100, 100, 100)
        else: color_blue_bar = color[11][1]

        Rects_color = [(50, 50, 50), color[16][1], (30, 30, 30), color[1][1], color[0][1], color_red_bar, color[2][1], color[5][1], color[4][1], color_green_bar, color[6][1], color[9][1], color[8][1], color_blue_bar, color[10][1], (red, green, blue), color[12][1], color[13][1], color[14][1], color[15][1]]
        for d in range(len(Rects_color)):
            pygame.draw.rect(screen, Rects_color[d], rects[d])

        red_bar_c= pygame.Rect(tx + 195, ty + 40, (red*155)/255, 20)
        pygame.draw.rect(screen, (255, 0, 0), red_bar_c)

        green_bar_c= pygame.Rect(tx + 195, ty + 75, (green*155)/255, 20)
        pygame.draw.rect(screen, (0, 255, 0), green_bar_c)

        blue_bar_c= pygame.Rect(tx + 195, ty + 110, (blue*155)/255, 20)
        pygame.draw.rect(screen, (0, 0, 255), blue_bar_c)

        if red_tBOX == '': tr = '0'
        else: tr = red_tBOX
        if green_tBOX == '': tg = '0'
        else: tg = green_tBOX
        if blue_tBOX == '': tb = '0'
        else: tb = blue_tBOX

        T, TP = [], []
        ft = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
        tt = [' - ', ' + ', "R", tr, ' - ', ' + ', "G", tg, ' - ', ' + ', "B", tb, "Ok", "Save", "Cancel", hex_tBOX, 'Select Color', 'X']      
        ct = [color[1][0], color[0][0], (255, 0, 0), (255, 0, 0), color[5][0], color[4][0], (0, 255, 0), (0, 255, 0), color[9][0], color[8][0], (0, 0, 255), (0, 0, 255), color[15][0], color[13][0], color[14][0], color[12][0], (180, 180, 180), color[16][0]]
        pos = [rects[3], rects[4], (tx + 170 + 217, ty + 40 + 11), rects[6], rects[7], rects[8], (tx + 170 + 217, ty + 75 + 11), rects[10], rects[11], rects[12], (tx + 170 + 217, ty + 110 + 11), rects[14], rects[19], rects[17], rects[18], rects[16], rects[0], rects[1]]

        for tp in range(len(tt)):
            T = font[ft[tp]].render(tt[tp], True, ct[tp])
            TP = T.get_rect()
            if tp not in [2, 6, 10]:TP.center = pos[tp].center
            else:TP.center = pos[tp]
            screen.blit(T, TP)
        pygame.display.update()
    return (red, green, blue, color_select_satus, close)