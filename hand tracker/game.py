import pygame as py
py.init()
s_width=700
s_height = 500

py.display.set_caption('Brick Breaker')
screen = py.display.set_mode((s_width,s_height))

run = True
slider_x = s_width/2
slider_y = 470
mouse_x=0
mouse_y=0
while True:
    for event in py.event.get():
        if event.type==py.QUIT:
            run = False

        if event.type== py.MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            if mouse_x<slider_x :
                slider_x -= 30
            if mouse_x>slider_x and slider_x<530:
                slider_x += 30
    screen.fill((0,0,0))
    py.draw.rect(screen,(255,255,255),( slider_x,slider_y,150,15),)
    py.display.update()

py.quit()
