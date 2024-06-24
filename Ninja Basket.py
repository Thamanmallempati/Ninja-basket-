import pygame
pygame.init()
import random
x = 800
y = 800

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Ninja Basket")
clock = pygame.time.Clock()

Red = (255,0,0)

bg_image = pygame.image.load("download(2).jpg")
bg_image = pygame.transform.scale(bg_image,(x,y))

font_style = pygame.font.SysFont(None,30)




def score(msg,colour):
    msg = font_style.render("Score:"+str(msg),True,colour)
    screen.blit(msg,(10,10))
Score = 0

f_w,f_h = 30,30
f_speed = 10
f_x = random.randint(0,x-f_w)
f_y = 0

food = pygame.image.load("download__1_-removebg-preview (2).png")
food = pygame.transform.scale(food,(f_w,f_h))
food1 = pygame.image.load("download-removebg-preview.png")
food1 = pygame.transform.scale(food1,(f_w,f_h))
food2 = pygame.image.load("istockphoto-804495812-612x612-removebg-preview.png")
food2 = pygame.transform.scale(food2,(f_w,f_h))

fruits = []

def mul_fruits():
    f_type = random.choice([food,food1,food2])
    fr_x = random.randint(0,x-f_w)
    fr_y = 0
    return{'type':f_type,'x':fr_x,'y':fr_y}

red = (255,0,0)

basket_w,basket_h = 100,50
basket_x = (x - basket_w)//2
basket_y = y - basket_h - 10
basket_s = 20



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT) and (basket_x < x - basket_w):
                basket_x += basket_s
            if (event.key == pygame.K_LEFT) and (basket_x > 0) :
                basket_x -= basket_s

        # Create new fruits
    if random.random() < 0.05:
        fruits.append(mul_fruits())

    for fruit in fruits:
        fruit['y'] += f_speed

        if (basket_x < fruit['x'] < basket_x + basket_w and basket_y < fruit['y'] < basket_y + f_w):
            fruits.remove(fruit)
            Score += 1
        elif fruit['y'] > y:
            fruits.remove(fruit)




    screen.blit(bg_image,(0,0))
    pygame.draw.rect(screen,red,(basket_x,basket_y,basket_w,basket_h))

    for fruit in fruits:
        if fruit['type'] == food:
            screen.blit(food,(fruit['x'],fruit['y']))
        if fruit['type'] == food1:
            screen.blit(food1,(fruit['x'],fruit['y']))
        if fruit['type'] == food2:
            screen.blit(food2,(fruit['x'],fruit['y']))

    score(Score,Red)

    pygame.display.update()
    clock.tick(30)