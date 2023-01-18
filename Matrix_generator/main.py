import pygame
from color_select import *

pygame.init()

def generate_data_color_matrix_new(tamX,tamY):
    Matrix = []
    for colun in range(tamY):
        Line = []
        for line in range(tamX):
            Line.append((0,0,0))
        Matrix.append(Line)
    return Matrix

def generate_matrix_color(dx,dy,tamX,tamY):
    rects_m = []
    x,y = dx,dy
    for colun in range(tamY):
        Line = []
        for line in range(tamX):
            Line.append(pygame.Rect(x,y,20,20))
            x += 23
        rects_m.append(Line)
        y +=23
        x = dx
    return rects_m

def draw_matrix_color(tamX,tamY,cm,screen,Mat):
    for colun in range(tamY):
        for line in range(tamX):
            pygame.draw.rect(screen, cm[colun][line], Mat[colun][line])
            
def test_matrix_button(mat,tamX,tamY,m,et_mouse):
    for a in range(tamY):
        for b in range(tamX):
            if test_button(mat[a][b],m) and et_mouse:
                return True,a,b
    return False,0,0 
    
def duplicate_frame_one_to_one(main_mat):
    Ret = []
    for a in range(len(main_mat)):
        ret_l = []
        for b in range (len(main_mat[a])):
            ret_l.append(main_mat[a][b])
        Ret.append(ret_l)
    return Ret

















def main():
    main_matrix = []
    current_frame = -1
    tam = -1

    tamX, tamY = 30, 12

    running = True
    screen = pygame.display.set_mode([1000,500])
    pygame.display.set_caption('Animation Genetor: ')

    main_color = pygame.Rect(728, 31, 58, 58)
    main_colorborder = pygame.Rect(727, 30, 60, 60)
    button_colorselect = pygame.Rect(727, 100, 60, 60)
    button_new_frame = pygame.Rect(30, 313, 100, 30)
    but_duplicateframe = pygame.Rect(135,313,100,30)
    but_front = pygame.Rect(275,313,30,30)
    but_back = pygame.Rect(240,313,30,30)

    rects_m = generate_matrix_color(30,30,tamX,tamY)
    rects_sc = generate_matrix_color(900,400,2,5) 

    font = [25, 20, 15]
    font = font_vector(font)

    r,g,b = 0,0,0

    c = False

    save_mat = generate_data_color_matrix_new(2,5)

    while running:
        m = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (c): 
                running = False

            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)

            if test_button(button_colorselect,m) and et_mouse:
                r1,g1,b1,s,c = select_color(r,g,b,screen,font,300,130)
                if s: r,g,b = r1,g1,b1
                
            if (test_button(button_new_frame,m) and et_mouse) or tam == -1:
                main_matrix.insert(current_frame+1,generate_data_color_matrix_new(tamX,tamY))
                current_frame += 1
                tam+=1


            if test_button(but_duplicateframe,m) and et_mouse:
                main_matrix.insert(current_frame+1,duplicate_frame_one_to_one(main_matrix[current_frame]))
                current_frame += 1
                tam+=1

            if test_button(but_back,m) and et_mouse:
                if current_frame == 0: current_frame = tam
                else: current_frame -= 1

            if test_button(but_front,m) and et_mouse:
                if current_frame == tam: current_frame = 0
                else: current_frame += 1

            test,changed_X,changed_Y = test_matrix_button(rects_m,tamX,tamY,m,et_mouse)
            if test: main_matrix[current_frame][changed_X][changed_Y] = (r, g, b) 

        if c: break

        screen.fill((50, 50, 50))

        str_to_txt = str(current_frame+1) + ' of ' + str(tam+1) 
        txt = font[1].render(str_to_txt,True,(255,255,255))
        screen.blit(txt, (30,7))

        draw_matrix_color(tamX,tamY,main_matrix[current_frame],screen,rects_m)
        draw_matrix_color(2,5,save_mat,screen,rects_sc)

        pygame.draw.rect(screen, (0 , 0, 0), main_colorborder)
        pygame.draw.rect(screen, (r, g, b), main_color)
        pygame.draw.rect(screen, (70, 70, 70), button_colorselect)
        pygame.draw.rect(screen, (70, 70, 70), but_front)
        pygame.draw.rect(screen, (70, 70, 70), but_back)
        pygame.draw.rect(screen, (70, 70, 70), but_duplicateframe)
        pygame.draw.rect(screen, (70, 70, 70), button_new_frame)
        
        pygame.display.update()

main()
