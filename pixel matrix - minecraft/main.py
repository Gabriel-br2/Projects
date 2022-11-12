from graphics import *

tam_pix_x, tam_pix_y = 10,10
resource = ["resource\lampada_desligada.png","resource\lampada_ligada.png"]
x_max,y_max = list(map(int,input("Entre com valor de X e Y: ").split(" ")))
win = GraphWin("Display Matriz - Minecraft", x_max*tam_pix_x, y_max*tam_pix_y)
lamps_on, Matrix_leds = [], [] 

def Matrix_generator(x,y):
    print("Aguarde a Matrix ser carregada")
    xd,yd = tam_pix_x/2, tam_pix_y/2
    for a in range(y):
        line = []
        for b in range(x):
            line.append(Image(Point(xd,yd),resource[0]))
            line[b].draw(win)
            xd += tam_pix_x
        Matrix_leds.append(line)
        xd = tam_pix_x/2
        yd += tam_pix_y
    print("Matrix Carregada")

def led_change_state(x,y,e):   
    if (x >= 0) and (y >= 0) and (x <= x_max) and (y <= y_max):
        Matrix_leds[y_max-y][x-1].undraw()
        p = Point(Matrix_leds[y_max-y][x-1].getAnchor().getX(), Matrix_leds[y_max-y][x-1].getAnchor().getY())
        
        if e == 0: 
            Matrix_leds[y_max-y][x-1] = Image(p,resource[0])
            if (y_max-y,x-1) in lamps_on: lamps_on.pop((y_max-y,x-1))

        if e == 1: 
            Matrix_leds[y_max-y][x-1] = Image(p,resource[1])
            if (y_max-y,x-1) not in lamps_on: lamps_on.append((y_max-y,x-1))
        
        Matrix_leds[y_max-y][x-1].draw(win)

def clear():
    for a in lamps_on:
        Pt = Point(Matrix_leds[a[0]][a[1]].getAnchor().getX(), Matrix_leds[a[0]][a[1]].getAnchor().getY())
        Matrix_leds[a[0]][a[1]].undraw()
        Matrix_leds[a[0]][a[1]] = Image(Pt,resource[0])
        Matrix_leds[a[0]][a[1]].draw(win)

def sign(a):
    if a < 0: return -1
    if a == 0: return 0
    if a > 0: return 1

def line_Draw(x1,y1,x2,y2):
    x = x1 
    y = y1
    deltaX = abs(x2-x1)
    deltaY = abs(y2-y1)
    S1 = sign(x2-x1)
    S2 = sign(y2-y1)

    if deltaY > deltaX:
        temp = deltaX
        deltaX = deltaY
        deltaY = temp
        interchange = 1 

    else: interchange = 0
    e = (2 * deltaY) - deltaX 
    a = 2 * deltaY 
    b = (2 * deltaY) - (2 * deltaX)
    led_change_state(x,y,1)

    for i in range(1,deltaX+1):
        if e < 0:
            if interchange == 1:
                y = y + S2
            else:
                x = x + S1
            e = e + a
        else:
            y = y + S2
            x = x + S1
            e = e + b
        led_change_state(x,y,1)

def C_Operation(a, b): return a + b   

def Circle_Draw(x_centre, y_centre, r):
    x = r
    y = 0
    led_change_state(C_Operation(x, x_centre), C_Operation(y, y_centre), 1)          
    led_change_state(C_Operation(-x, x_centre), C_Operation(y, y_centre), 1)    
    led_change_state(C_Operation(y, x_centre), C_Operation(x, y_centre), 1)      
    led_change_state(C_Operation(y, x_centre), C_Operation(-x, y_centre), 1) 

    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + (2 * y) + 1
        else:        
            x -= 1
            P = P + (2 * y) - (2 * x) + 1
        if (x < y): break
        led_change_state(C_Operation(x, x_centre), C_Operation(y, y_centre), 1)    
        led_change_state(C_Operation(-x, x_centre), C_Operation(y, y_centre), 1)   
        led_change_state(C_Operation(x, x_centre), C_Operation(-y, y_centre), 1)   
        led_change_state(C_Operation(-x, x_centre), C_Operation(-y, y_centre), 1)  
        if x != y:
            led_change_state(C_Operation(y, x_centre), C_Operation(x, y_centre), 1)  
            led_change_state(C_Operation(-y, x_centre), C_Operation(x, y_centre), 1) 
            led_change_state(C_Operation(y, x_centre), C_Operation(-x, y_centre), 1)  
            led_change_state(C_Operation(-y, x_centre), C_Operation(-x, y_centre), 1)  

def square_Draw(x1,y1,x2,y2):
    line_Draw(x1, y1, x2, y1)
    line_Draw(x1, y1, x1, y2)
    line_Draw(x1, y2, x2, y2)
    line_Draw(x2, y1, x2, y2)

def main():
    Matrix_generator(x_max,y_max)
    while True:
        op = int(input("O que você deseja fazer (1 linha)(2 Circulo)(3 Quadrado)(4 clear)(5 sair): "))
        if op == 1:
            l = list(map(int,input("Entre com os valores x e y dos pontos extremos: ").split(" ")))  
            line_Draw(l[0], l[1], l[2], l[3]) 
        if op == 2:
            l = list(map(int,input("Entre com os valores de x, y e raio: ").split(" ")))
            Circle_Draw(l[0], l[1], l[2])
        if op == 3:
            l = list(map(int,input("Entre com os valores x e y dos pontos extremos: ").split(" ")))
            square_Draw(l[0], l[1], l[2], l[3])
        if op == 4:
            clear()
            lamps_on = []
        if op == 5: break
        
main()