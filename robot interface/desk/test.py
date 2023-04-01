import pygame
import cv2
import numpy

pygame.init()

####################################################################################################

class Txt:
    def __init__(self,font,txt,color):
        self.t = font.render(txt,True,color)
        self.txt_x = self.t.get_size()[0]

    def draw(self,screen,XY):  
        screen.blit(self.t, XY)

    def get_middle(self,x,y):
        rect_tValue = self.t.get_rect()
        rect_tValue.centerx = x
        rect_tValue.centery = y
        return rect_tValue
    
class Slider():
    def __init__(self,name,pos,max,maped_max_min,font):
        self.pos = pos
        self.name = name
        self.font = font
        self.max = max + pos[0]
        self.maped_max_min = maped_max_min
        
        self.calcul = False
        self.is_dragging = False
        self.prev_mouse_state = None              
        
        self.value = 0
        self.middle = (max // 2) + pos[0]
        self.M_pos = self.middle
        self.image = pygame.Surface((25,40),pygame.SRCALPHA)
        self.middle_map = ((maped_max_min[1] -maped_max_min[0])//2)+ maped_max_min[0]
        
        self.rect = self.image.get_rect(topleft = (self.M_pos - 12, self.pos[1]))
        self.draw_surface()

    def draw_surface(self):
        pygame.draw.rect(self.image, (0,0,0), (4,23,17,17))
        pygame.draw.rect(self.image, (50,50,50), (5,24,15,15))
        pygame.draw.rect(self.image, (252,168,3), (10.5,13,4,10))

        t = Txt(self.font[1],str(int(self.value)),(252,168,3))
        r = t.get_middle(12.5,5)
        t.draw(self.image,r)

    def update(self, mouse_pos, chan,t_chan):        
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        if self.rect.collidepoint(mouse_pos) and mouse_pressed: self.is_dragging = True
        elif not mouse_pressed: self.is_dragging = False

        if t_chan:
            chan = map_value(chan, self.maped_max_min, (self.pos[0], self.max))

            if chan > self.max: self.M_pos = self.max
            elif chan < self.pos[0]: self.M_pos = self.pos[0]
            else: self.M_pos = chan

            delta_x = self.M_pos - self.rect.centerx   
            self.rect.move_ip(delta_x, 0)
       
        else:
            if self.is_dragging:
                if self.prev_mouse_state == False:
                    self.rect.centerx = mouse_pos[0]
                else:            
                    if mouse_pos[0] > self.max: self.M_pos = self.max
                    elif mouse_pos[0] < self.pos[0]: self.M_pos = self.pos[0]
                    else: self.M_pos = mouse_pos[0]            

                delta_x = self.M_pos - self.rect.centerx   
                self.rect.move_ip(delta_x, 0)
                
        self.prev_mouse_state = mouse_pressed
        self.value = map_value(self.M_pos, (self.pos[0], self.max), self.maped_max_min)

        self.image.fill((0,0,0,0))
        self.draw_surface()

        return self.value        
    
    def calc(self):
        self.c = [(0,0,0),(60,60,60),(0,0,0),(252,168,3),(252,168,3),(252,168,3),(252,168,3),(252,168,3)]
        self.x = [-16, -15, 0, 0, 0,self.max,self.middle,0]
        self.y = [-11,-10,0,20,20,20,20,0]
        self.tam_x = [self.max-self.pos[0]+31,self.max-self.pos[0]+29,self.max-self.pos[0],self.max-self.pos[0],2,2,2,0]
        self.tam_y = [15+22,15+20,3,2,7.5,7.5,5,3]

        for i in range(8):
            if i < 5: self.x[i] = self.pos[0] + self.x[i]
            if i < 2 or i == 8: self.y[i] = self.pos[1] + self.y[i]
            else: self.y[i] = self.pos[1]+6 + self.y[i]

    def addon(self,screen,font):
        ini_tam,tam = self.middle,self.M_pos-self.pos[0]-(self.max - self.pos[0])//2 

        if tam < 0:
            ini_tam = self.pos[0] + tam + (self.max - self.pos[0])//2
            tam = self.middle - ini_tam
        
        if not self.calcul:
            self.calc()        
            self.calcul = True

        self.x[7],self.tam_x[7] = ini_tam,tam

        for j in range(8):
            if j < 2: br = 5
            else: br = 0
            pygame.draw.rect(screen,self.c[j],(self.x[j],self.y[j]+25.5,self.tam_x[j],self.tam_y[j]),border_radius=br)
        
        a = 0
        txt_str = [str(int(self.maped_max_min[0])), str(int(self.maped_max_min[1])), str(self.middle_map),self.name]
        pos_x = [self.pos[0], self.max+3, self.middle, self.pos[0]]
        
        for t in range(len(txt_str)):
            txt_str[t] = Txt(font[2 if t == 3 else 1],txt_str[t],(252,168,3))
            if t == 3: dpos_y,a = 32.5,txt_str[t].txt_x
            else: dpos_y,a = 68,0
            r = txt_str[t].get_middle(pos_x[t]-a,self.pos[1] + dpos_y)
            txt_str[t].draw(screen,r)
###################################################################################################################################################

def font_m(l,f):
    for tam in range(len(l)): l[tam] = pygame.font.SysFont(f[tam],l[tam])
    return l

def map_value(value, input_iterval, output_iterval):
    maped_value = output_iterval[0] + (value - input_iterval[0]) * (output_iterval[1] - output_iterval[0]) / (input_iterval[1] - input_iterval[0])
    return maped_value

def cam_setup(camera_width,camera_height,video_source):
    cap = cv2.VideoCapture(video_source) 
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)
    return cap

def cam_feed(cap):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = numpy.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.flip(frame, True, False)
    return frame

######################################################################################################################################################

def main(width, height):
    running = True

    screen = pygame.display.set_mode((width, height))
    cap = cam_setup(320,240,0)

    imagem = pygame.image.load('source/framecam.png')
    imagem = pygame.transform.scale(imagem, (350,280))

    font = font_m([24,20,20],[None,None,'Segoe UI'])

    tam = 200
    slider = []
    value = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    pos_zz = [[110,25]]
    min_max_return = (-15,15)
    name = ['Head ','Body ','Rool-L','Rool-R','Pitch-L','Pitch-R']
    for k in range(6):
        if k != 0: pos_zz.append([110,pos_zz[k-1][1] + 80]) 
        slider.append(Slider(name[k], pos_zz[k], tam, min_max_return,font))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        screen.fill((0,0,255))

        pygame.draw.rect(screen,(0,0,0),(-20,13,362,499),2,border_radius=12)
        pygame.draw.rect(screen,(90,90,90),(-20,15,360,495),border_radius=10)
        
        for k1 in range(6):
            slider[k1].addon(screen,font)
            value[k1][0] = slider[k1].update(pygame.mouse.get_pos(),value[k1][1], value[k1][1]!=value[k1][0])
            value[k1][1] = value[k1][0]
            
            screen.blit(slider[k1].image,slider[k1].rect)
            
        print(value)
        
        screen.blit(cam_feed(cap), (860, 270))
        screen.blit(imagem,(845,245))
        
        pygame.display.update()
    
    return cap

cap = main(1200,690)
cap.release()
pygame.quit()
quit()