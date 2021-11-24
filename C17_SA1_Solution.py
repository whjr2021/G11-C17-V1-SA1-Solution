# Import pygame and time modules
import pygame
import time
# Initialize pygame
pygame.init() 

screen = pygame.display.set_mode((550, 400))
pygame.display.set_caption("City Runner Game")

# Create image loading function here
def image_load(location, length, width):
    img = pygame.image.load(location).convert_alpha()
    img_scaled = pygame.transform.smoothscale(img,(length,width))
    return img_scaled
      
# Create text display function here
def text_display(size,text,r,g,b,x,y):
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, (r,g,b))
    screen.blit(text, (x,y))

# Define coin display function here
def coin_display(x):
    screen.blit(coin,(70*(x+1),210))
        
bgImg = image_load("background.png",800,400)
char = image_load("character.png",40,90)
coin = image_load("coin.png",50,50)

# All variables required to track backround, character, and coin positions are defined here
bgx = 0
charx = 10
chary = 210
x = 0

# Variables required to track money collected and time elapsed are defined here
money = 0
total_time = 10

# Game loop
carryOn = True
# Create first time point here
t1 = time.time()
while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                carryOn = False  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    charx += 10
                    bgx -= 1
                if charx >= 500:
                    charx = 10
                    bgx = 0
                    x = 0
                    coin_display(x)

        # Display the background, character and coins here
        screen.blit(bgImg,(bgx,0))
        coin_display(x)
        screen.blit(char,(charx,chary))
        
        char_rect = char.get_rect(topleft=(charx,chary))
        coin_rect = coin.get_rect(topleft=(70*(x+1), 210))
        if coin_rect.collidepoint(char_rect.x,char_rect.y):
            money += 1000
            x += 1
            coin_display(x)
        
        # Display "Money Collected" text along with "money" variable value here 
        text_display(32,"Money Collected: "+ str(money), 255, 255, 255, 10, 10)
       
        t2 = time.time()
        time_elapsed = t2 - t1
        time_left = round((total_time - time_elapsed))
        text_display(32,"Time Left: "+ str(time_left) + " Seconds", 255, 255, 255, 290, 10)
     
        if time_elapsed >= 10:
            pygame.time.wait(2000)
            # Code to close the game here
            screen.fill((100,100,255))
            font = pygame.font.Font(None, 34)
            text_display(44,"Money collected: " + str(money),255,255,255,120,180)
            pygame.display.flip()
            pygame.time.wait(2000)
            break
    
        pygame.display.flip()
pygame.quit()