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
#mx, my = pg.mouse.get_pos()
bkgrnd = pg.transform.scale(pg.image.load('matrixcode.jpg'),(1000,600))


def draw_window(player,enemy,enemies):
    window.blit(bkgrnd,(0,0))
    window.blit(donut,(player.x,player.y))
    for enemy in enemies:
        window.blit(manatee,(enemy.x,enemy.y))

    pg.display.update()
    


def main():
    #mx, my = pg.mouse.get_pos()
    player = pg.Rect(500,200,70,70)
    #enemy = pg.Rect(0,0,70,70)
    enemies = [pg.Rect(0,0,70,70)]
    step_size = 4
    loopcount = 1
    clock = pg.time.Clock()

    run = True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        if event.type == pg.MOUSEMOTION:
            mx, my = pg.mouse.get_pos()
            player.x = mx-45
            player.y = my-45

        for enemy in enemies:
            player_vector = pg.math.Vector2(*(player.x,player.y))
            enemy_vector = pg.math.Vector2(*(enemy.x,enemy.y))
            new_enemy_vector = pg.math.Vector2(*(enemy.x,enemy.y))
            distance = enemy_vector.distance_to(player_vector)
        
            if distance > 0:
                direction_vector = (player_vector - enemy_vector) / distance
                step_distance = min(distance, step_size)
                new_enemy_vector = enemy_vector + direction_vector * step_distance
                enemy.x,enemy.y = new_enemy_vector

            collide = player.colliderect(enemy)
            if collide:
                enemies = [pg.Rect(0,0,70,70)]
        

        if loopcount % 300 == 0:  
            enemies.append(pg.Rect(0,0,70,70))   
        draw_window(player,enemy,enemies)
        loopcount += 1


if __name__=="__main__":
    main()