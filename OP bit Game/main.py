# Work in progress

import pygame

pygame.init()

def main():
    running,c = True,False
    screen = pygame.display.set_mode((1300,690))
    pygame.display.set_caption('The witcher_bitGame')
        
    while running:
        m = pygame.mouse.get_pos()
        for event in pygame.event.get():
            et_mouse = (event.type == pygame.MOUSEBUTTONDOWN)
        
            if (event.type == pygame.QUIT) or c: running = False                

main()
pygame.quit()
