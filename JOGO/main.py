import random,time                                        
from tkinter import image_types                                
from tkinter.constants import S, W, X, Y
from typing import Optional                                                    
from graphics import *                                     

l_global,movs = [1000,650],[15, 4]    

win = GraphWin( "Star Wars", l_global[0], l_global[1])              
win.setBackground("black")

def win_lose(t):          
    if t == 'lose_': LR = [Rectangle(Point(200,150),Point(800,500)),Rectangle(Point(210,160),Point(790,490)),Rectangle(Point(410,390),Point(590,460)),Text(Point(500,225),"Você Perdeu!"),Text(Point(500,425),"Voltar ao Menu"),Text(Point(500,300),"A falta do habilidoso piloto Han Solo foi grande."),Text(Point(500,325),"A lendaria Millenniun Falcon foi destruída."),Text(Point(500,350),"Tente novamente, e que A FORÇA ESTEJA COM VOCÊ!")]
    elif t == 'win': LR = [Rectangle(Point(200,150),Point(800,500)),Rectangle(Point(210,160),Point(790,490)),Rectangle(Point(410,390),Point(590,460)),Text(Point(500,225),"Você Ganhou!"),Text(Point(500,425),"Voltar ao Menu"),Text(Point(500,275),"Você é um excelente piloto"), Text(Point(500,300),"e conseguiu escapar do campo de asteorides"),Text(Point(500,325),"Agora vc pode livremente seguir sua jornada até JAKKU"),Text(Point(500,350),"Que a FORÇA ESTEJA COM VOCÊ!")]
    
    for a in range(len(LR)):
        if a == 0: LR[a].setFill('black')
        elif a == 1 or a == 2: LR[a].setOutline("yellow") 
        elif a >= 3 :
            LR[a].setTextColor("yellow")
            LR[a].setFace('courier')
            if a == 3: LR[a].setSize(30)
            else: LR[a].setSize(12)
            LR[a].setStyle('bold')
        LR[a].draw(win)
        
    while True:
        x,y = win.getMouse().getX(), win.getMouse().getY()
        if (210 < x < 790) and (160 < y < 490): break
    for e in range(len(LR)): LR[e].undraw()
    
def VIDA(v,vida_total):                                             
    P = 288 - (288//vida_total*v-vida_total)
    if P > 288: return Point(288,42)
    else: return Point(P,42)

def pause():                                                        
    L_P = [Rectangle(Point(0,0),Point(400,650)),Rectangle(Point(10,10),Point(390,640)),Text(Point(180,625),"Gabriel R. Souza - 150888 - v1.2"),Image(Point(200,110),"resource/pause/logo.png"),Image(Point(200,345),"resource/pause/start(0).png"),Image(Point(200,345),"resource/pause/start(1).png"),Image(Point(200,480),"resource/pause/exit(0).png"),Image(Point(200,480),"resource/pause/exit(1).png")]
    
    L_P[0].setFill("black")
    L_P[1].setOutline("yellow")
    L_P[2].setTextColor("yellow")
    L_P[2].setFace("courier")

    for a in range(len(L_P)):
        if a != 5 and a != 7: L_P[a].draw(win)
    
    while True:
        x,y = win.getMouse().getX(), win.getMouse().getY()   
  
        if (62 < x < 335) and (316 < y < 376):
            L_P[5].draw(win)
            time.sleep(0.5)
            for e in range(len(L_P)): L_P[e].undraw()                                            
            return 0
                                                                     
        elif (66 < x < 340) and (455 < y < 508):                                 
            L_P[7].draw(win)                                               
            time.sleep(0.5)  
            for i in range(len(L_P)): L_P[i].undraw()                                                        
            return 1                                                         

def hit_test(oq,mil_x,mil_y,ast_x,ast_y,ast_t):                                                                  
    if oq == 'mil':                                                        
        Pos_M,L_q1,R_M = (mil_x-20,mil_y),[],40                                           
        Pos_MR = [(mil_x,mil_y-20),(mil_x+50,mil_y+20),(mil_x+50,mil_y-20),(mil_x,mil_y+20)]

        if ast_t == "Ast2":                           
            Pos_at,L_q2 = [(ast_x+30,ast_y+27),(ast_x-35,ast_y-30),(ast_x-35,ast_y+27),(ast_x+30,ast_y-30)],[]

            for a in range(4):                                                                
                L_q2.append(pow(pow((Pos_M[0]-Pos_at[a][0]),2) + pow((Pos_M[1]-Pos_at[a][1]),2),0.5) < R_M)
                L_q1.append(Pos_MR[0][0] < Pos_at[a][0] < Pos_MR[3][0] and Pos_MR[3][1] < Pos_at[a][1] < Pos_MR[0][1])
       
            return any(L_q2) or any(L_q1)                                   

        else:                                                                               
            if ast_t == "Ast1": Pos_at,R_at = (ast_x,ast_y),12              
            if ast_t == "Ast3": Pos_at,R_at = (ast_x,ast_y+1),27           
            if ast_t == "Ast4": Pos_at,R_at = (ast_x,ast_y),12             
            CC = pow(pow((Pos_M[0]-Pos_at[0]),2) + pow((Pos_M[1]-Pos_at[1]),2),0.5) < R_M + R_at
            for a in range(4): L_q1.append(pow(pow((Pos_MR[a][0]-Pos_at[0]),2) + pow((Pos_MR[a][1]-Pos_at[1]),2),0.5) < R_at)

            return CC or any(L_q1)                                        

    elif oq == "shot":                                                     
        Pos_tiro,R_M = (mil_x,mil_y),12                                    

        if ast_t == "Ast2":
            Pos_at,R_at = (ast_x,ast_y),35
            return pow(pow((Pos_tiro[0]-Pos_at[0]),2) + pow((Pos_tiro[1]-Pos_at[1]),2),0.5) < R_M + R_at            
            
        else:
            if ast_t == "Ast1": Pos_at,R_at = (ast_x,ast_y),12                  
            if ast_t == "Ast3": Pos_at,R_at = (ast_x,ast_y+1),27            
            if ast_t == "Ast4": Pos_at,R_at = (ast_x,ast_y),12
            return pow(pow((Pos_tiro[0]-Pos_at[0]),2) + pow((Pos_tiro[1]-Pos_at[1]),2),0.5) < R_M + R_at

def hit(P_explo):                                                                                                
    for a in range(1,5):                                                   
        img = Image(P_explo,"resource/explosao/explo{}.png".format(a))     
        img.draw(win)         
        time.sleep(0.075)
        img.undraw()

def Milenium(Pos_in_milenium):                                     
    millennium_img = Image(Pos_in_milenium, "resource/millennium.png")     
    millennium_img.draw(win)
    return millennium_img                                                  

L_vida = []
def Asteroide(Qt_ast,Pos_mil,vida,vida_total,i,it):                              
    img_vida = Image(Point(150,25),"resource/life_bar.png")
    n_file,pos_vel = ["Ast1","Ast2","Ast3","Ast4"], [0.75, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1]                                
    t_ast,pos_ast_y,vel_ast,img_ast = [],[],[],[]                          

    for a in range(Qt_ast):                                                
        t_ast.append(n_file[random.randrange(0,4)])                        
        pos_ast_y.append(random.randrange(0,l_global[1]))                   
        vel_ast.append(pos_vel[random.randrange(0,8)])                     
        img_ast.append(Image(Point(1100,pos_ast_y[a]),"resource/ast/{}.png".format(t_ast[a])))       
        img_ast[a].draw(win)                                               

    millennium_img = Milenium(Pos_mil)
    img_vida.draw(win)

    s,tiro,vida,bs = [],0,vida,0                                    
    while True:
                                                         
        if len(L_vida) == 0:
            L_vida.append(Rectangle(Point(11,32),VIDA(vida,vida_total)))
            L_vida[0].setFill("Red")
            L_vida[0].draw(win)

        elif len(L_vida) == 1:
            L_vida.append(Rectangle(Point(11,32),VIDA(vida,vida_total)))  
            L_vida[0].undraw()
            del(L_vida[0])
            L_vida[0].setFill("Red")
            L_vida[0].draw(win)
        
        for e in range(Qt_ast):
            if img_ast[e].getAnchor().getX() > -100: img_ast[e].move(-vel_ast[e],0)
            elif e not in s: s.append(e)
            
        key = win.checkKey()                                                                        
        if key == "w" and millennium_img.getAnchor().getY() >= 35: millennium_img.move(0,-movs[0])  
        elif key == "a"  and millennium_img.getAnchor().getX() >= 50: millennium_img.move(-movs[0],0)  
        elif key == "s" and millennium_img.getAnchor().getY() <= 615: millennium_img.move(0,movs[0])
        elif key == "d" and millennium_img.getAnchor().getX() <= 950: millennium_img.move(movs[0],0)
       
        elif key == "Escape":                                              
            if pause() == 1:
                for a in range(Qt_ast): img_ast[a].undraw()
                millennium_img.undraw()
                img_vida.undraw()
                return -2000000000000000,0

        elif key == "space":
            tiro += 1
            if bs == 1: shoot.undraw()
            shoot = Image(millennium_img.getAnchor(),"resource/laser.png") 
            shoot.draw(win)
            bs = 1                                           
            
        if tiro >= 1:
            C = False                                                     
            shoot.move(movs[1],0)
            for a in range(Qt_ast):
                if hit_test("shot",shoot.getAnchor().getX(),shoot.getAnchor().getY(),img_ast[a].getAnchor().getX(),img_ast[a].getAnchor().getY(),t_ast[a]):
                    hit(Point(img_ast[a].getAnchor().getX(),img_ast[a].getAnchor().getY()))
                    shoot.undraw()
                    bs = 0
                    C,K = True,a
                    break                                                   
            if shoot.getAnchor().getX() >= 1100:
                shoot.undraw()
                bs = 0
                C,K = False,0
                tiro = 0                                                   

            if C:
                img_ast[K].undraw()
                del(t_ast[K],pos_ast_y[K],vel_ast[K],img_ast[K])
                Qt_ast -= 1

        key = win.checkKey()
        
        o = 0
        while o <= Qt_ast-1: 
            MP,AP = millennium_img.getAnchor(),img_ast[o].getAnchor()                                    
            if hit_test("mil",MP.getX(), MP.getY(), AP.getX(), AP.getY(), t_ast[o]):
                img_ast[o].undraw()
                hit(AP)
                del(t_ast[o],pos_ast_y[o],vel_ast[o],img_ast[o])
                Qt_ast -= 1
                vida += 1
                if vida == vida_total:
                    L_vida[0].undraw()
                    for i in range(5): hit(MP)
                    millennium_img.undraw()
                    img_vida.undraw()
                    for a in range(Qt_ast): img_ast[a].undraw()
                    return -3000000000000000,0
            else: o += 1

        if len(s) == Qt_ast:
            A = millennium_img.getAnchor()
            millennium_img.undraw()
            img_vida.undraw()
            L_vida[0].undraw()
            if bs == 1:
                shoot.undraw()
                bs = 0
            for a in range(Qt_ast): img_ast[a].undraw()    
            return A,vida

def fase_asteroides(num_rd,vida_total):                             
    P_m = Point(l_global[0]//2,l_global[1]//2)
                              
    for i in range(num_rd+1):                                                 
        Qt_ast = random.randrange(8,13)                                    
        if P_m == -2000000000000000: break
        if P_m == -3000000000000000:
            win_lose('lose_')
            break
        if i == 0: P_m,v = Asteroide(Qt_ast,P_m,0,vida_total,i,num_rd)
        else: P_m,v = Asteroide(Qt_ast,P_m,v,vida_total,i,num_rd)
        if i == num_rd: A = 1
        else: A = 0
    if A == 1: win_lose('win')
    Menu_inicial()

def animacao():
    Lis = [Text(Point(500,295),"A long time ago in a galaxy far,"),Text(Point(500,355),"far away....                                ")]
    time.sleep(2)

    for a in range(2):
        Lis[a].setSize(35)
        Lis[a].setTextColor(color_rgb(22,192,186))
        Lis[a].draw(win)

    time.sleep(7)
    for e in range(2): Lis[e].undraw()

    time.sleep(2)

    Wall = Image(Point(500,325),"resource/fundo.PNG")
    Wall.draw(win)

    T = Text(Point(935,640),"Esc - Pular")
    T.setFace('courier')
    T.setStyle('bold')
    T.setTextColor(color_rgb(246,228,30))

    L_T = [Image(Point(500,325),"resource/pause/logo.png"),Text(Point(500,665),"Jogo Especial"),Text(Point(500,715),"MILLENNIN FALCON"),Text(Point(500,780),"A  ditadura imperial,  finalmente"),Text(Point(500,815),"caiu. O imperador e seu mais leal"),Text(Point(500,850),"servo,     Darth Vader,     estão"),Text(Point(500,885),"mortos,   e o  sol  da  esperança"),Text(Point(500,920),"brilha    sobre     a     galaxia"),Text(Point(500,955),"novamente.                       "),Text(Point(500,1025),"Mas  os  braços  remanescentes do"),Text(Point(500,1060),"império    seguem  e  a  luta  na"),Text(Point(500,1095),"rebelião continua.               "),Text(Point(500,1165),"Irving  (você), conhece a lenda:"),Text(Point(500,1200),"Luke,  Leia  e  Han,  e  sobre a"),Text(Point(500,1235),"lendaria Milleniun Falcon. Ele a"),Text(Point(500,1270),"encontrou     com    um    homem"),Text(Point(500,1305),"chamado   Ducan  que  se  gabava"),Text(Point(500,1340),"por  te-lo  roubado e então  sem"),Text(Point(500,1375),"pensar duas vezes a roubou.     "),Text(Point(500,1445),"Quem sabe o  que a força  guarda"),Text(Point(500,1480),"para o futuro desta nave?       ")]
    L_T[0].draw(win)
    
    for a in range(1,len(L_T)):
        L_T[a].setFace('courier')
        L_T[a].setStyle('bold')
        L_T[a].setTextColor(color_rgb(246,228,30)) 
        if a == 1: L_T[a].setSize(30)
        elif a == 2: L_T[a].setSize(25)
        else: L_T[a].setSize(18)
        L_T[a].draw(win)
    
    time.sleep(3)

    T.draw(win)
    while L_T[20].getAnchor().getY() >= -100:
        key = win.checkKey()                                                                        
        if key == "Escape": break  
        for e in range(len(L_T)): L_T[e].move(0,-0.125)
    for i in range(len(L_T)): L_T[i].undraw()
    T.undraw()                                                 
    Menu_inicial()

def Menu_inicial():                                                
    Rf = Rectangle(Point(0,0),Point(l_global[0],l_global[1]))
    Lm = Line(Point(500,250),Point(500,600))
    LR = [Rectangle(Point(10,10),Point(990,640)),Rectangle(Point(605,365),Point(665,425)),Rectangle(Point(535,435),Point(595,495)),Rectangle(Point(605,435),Point(665,495)),Rectangle(Point(675,435),Point(735,495)),Rectangle(Point(510,540),Point(760,600)),Rectangle(Point(605,260),Point(665,320))]
    LI = [Image(Point(500,110),"resource/pause/logo.png"),Image(Point(250,345),"resource/pause/start(0).png"),Image(Point(250,345),"resource/pause/start(1).png"),Image(Point(250,480),"resource/pause/exit(0).png"),Image(Point(250,480),"resource/pause/exit(1).png")]
    LT = [Text(Point(210,625),"Gabriel R. Souza - 150888 - v1.2"),Text(Point(875,460),"Movimentação"),Text(Point(826,570),"Tiro"),Text(Point(832,290),"Pause"),Text(Point(635,395),"W"),Text(Point(565,465),"A"),Text(Point(635,465),"S"),Text(Point(705,465),"D"),Text(Point(635,570),"SPACE"),Text(Point(635,290),"ESC")]
                                                                 
    Rf.setFill("black")
    Lm.setFill("yellow")

    for a in range(len(LR)): LR[a].setOutline("yellow")
    
    for e in range(len(LT)):
        LT[e].setTextColor("yellow")
        LT[e].setFace("courier")
        if e <= 7 and e > 0: LT[e].setSize(20)
        else: LT[e].setSize(15)
        
    L = LR + LI + LT
    L.insert(0,Lm)
    L.insert(0,Rf)    
    
    for i in range(len(L)):
        if i != 11  and i != 13: L[i].draw(win)    

    while True:
        x,y = win.getMouse().getX(),win.getMouse().getY()

        if (112 < x < 381) and (320 < y < 368):     
            L[11].draw(win)
            time.sleep(0.5)
            for o in range(len(L)): L[o].undraw()
            fase_asteroides(30,2)
            break

        if (113 < x < 385) and (453 < y < 504):     
            L[13].draw(win)
            time.sleep(0.5)
            for u in range(len(L)): L[u].undraw()
            win.close()
            return -1000000000

def inicio():                                                      
    R = Rectangle(Point(0,0),Point(l_global[0],l_global[1]))
    L_ini = [Text(Point(500,300),"FURG - C3"),Text(Point(500,325),"Algoritmos para Engenharia de Automação"),Text(Point(500,350),"Prof. Marcelo Malheiros"),Text(Point(500,300),"PRIMEIRO PROJETO"),Text(Point(500,325),"Gabriel Rocha de Souza"),Text(Point(500,350),"Matrícula - 150888")]
    R.setFill("black")
    for a in range(6):
        L_ini[a].setTextColor("white")
        L_ini[a].setFace("courier")
        L_ini[a].setStyle("bold")
    R.draw(win)
    for e in range(3): L_ini[e].draw(win)
    time.sleep(5)
    for i in range(6):
        if i < 3: L_ini[i].undraw()
        else: L_ini[i].draw(win)
    time.sleep(5)
    R.undraw()
    for o in range(3,6): L_ini[o].undraw() 
    animacao()
    
inicio()