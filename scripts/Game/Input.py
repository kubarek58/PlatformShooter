import pygame

class Input:
    up = False
    down = False
    left = False
    right = False
    mouseLeft = False
    mouseRight = False
    Num1 = False
    Num2 = False
    Num3 = False
    Esc = False

    @classmethod
    def checkInputEvents(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cls.Esc = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cls.up = True

                if event.key == pygame.K_s:
                    cls.down = True
                
                if event.key == pygame.K_a:
                    cls.left = True
                
                if event.key == pygame.K_d:
                    cls.right = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    cls.up = False
                
                if event.key == pygame.K_s:
                    cls.down = False
                
                if event.key == pygame.K_a:
                    cls.left = False
                
                if event.key == pygame.K_d:
                    cls.right = False