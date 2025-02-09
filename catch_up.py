from pygame import *

#створи вікно гри

window = display.set_mode((700, 500))
display.set_caption("Доганялки")

FPS = 60
clock = time.Clock()
#задай фон сцени

background = transform.scale(
    image.load('background.png'),
    (700, 500)
)


#створи 2 спрайти та розмісти їх на сцені

sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)

sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)

x1 = 100
y1 = 300
x2 = 300
y2 = 300


#оброби подію «клік за кнопкою "Закрити вікно"»

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    keys = key.get_pressed()

    if keys[K_w] and y1 > 5:
        y1 -= 10

    if keys[K_s] and y1 < 395:
        y1 += 10

    if keys[K_a] and x1 > 5:
        x1 -= 10

    if keys[K_d] and x1 < 595:
        x1 += 10



    if keys[K_UP] and y2 > 5:
        y2 -= 10

    if keys[K_DOWN] and y2 < 395:
        y2 += 10

    if keys[K_LEFT] and x2 > 5:
        x2 -= 10

    if keys[K_RIGHT] and x2 < 595:
        x2 += 10

    display.update()
    clock.tick(FPS)
