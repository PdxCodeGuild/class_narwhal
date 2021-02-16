'''
=-=-= Python Project 15 Feb 2021 =-=-=
=-=-=-=-=-= A PyGame Game -=-=-=-=-=-=
=-=-=-=-=- Composer: brndn =-=-=-=-=-=
'''

import pygame as pg
pg.init()

window = pg.display.set_mode((1000,600))
pg.display.set_caption("Game")
fps = 60
donut_image = pg.image.load('donut.png')
donut = pg.transform.scale(donut_image,(100,100))
manatee_image = pg.image.load('manatee.png')
manatee = pg.transform.scale(manatee_image,(100,100))
pg.mouse.set_visible(False)
pg.mouse.set_pos(500,300)
mx, my = pg.mouse.get_pos()

def draw_window(player,enemy):
    window.blit(donut,(player.x,player.y))
    window.blit(manatee,(enemy.x,enemy.y))
    pg.display.update()


def main():
    pg.mouse.set_pos(500,300)
    mx, my = pg.mouse.get_pos()
    player = pg.Rect(mx,my,70,70)
    enemy = pg.Rect(0,0,70,70)
    clock = pg.time.Clock()

    run = True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEMOTION:
                mx, my = pg.mouse.get_pos()
                player.x, player.y = mx, my

        draw_window(player,enemy)


if __name__=="__main__":
    main()
     
