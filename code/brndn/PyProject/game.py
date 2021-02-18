'''
=-=-= Python Project 15 Feb 2021 =-=-=
=-=-=-=-=-= A PyGame Game -=-=-=-=-=-=
=-=-=-=-=- Composer: brndn =-=-=-=-=-=
'''

import pygame as pg
pg.init()

Z = 50 #100
walls_on = False #True
movement = 'mouse' #'keys'
hole_mode = 'norm' #'chain' #'infinite'
enemy_delay = 100

X = Z
Y = Z
window = pg.display.set_mode((1100,600))
pg.display.set_caption("Game")
fps = 60
donut_image = pg.image.load('donut.png')
donut = pg.transform.scale(donut_image,(X,Y))
manatee_image = pg.image.load('manatee.png')
manatee = pg.transform.scale(manatee_image,(X,Y))
donuthole_image = pg.image.load('donuthole.png')
donuthole = pg.transform.scale((donuthole_image),(X//2,Y//2))
hole_velocity = X/5
player_velocity = X/10
pg.mouse.set_visible(False)
bkgrnd = pg.transform.scale(pg.image.load('background.jpg'),(1100,600))
wall_image = pg.transform.scale(pg.image.load('wall.jpg'),(20,20))
life_font = pg.font.SysFont('ariel',50,True)
score_font = pg.font.SysFont('ariel',50,True)
walls = []
if walls_on == True:
    level = [
        'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                    wwwwwwwwwwwww                    w',
        'w                    w           w                    w',
        'w                    w           w                    w',
        'w                    w           w                    w',
        'w                    w           w                    w',
        'w                    wwwwwwwwwwwww                    w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'w                                                     w',
        'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'
        ]
else:level = []

for y,row in enumerate(level):
    for x,col in enumerate(row):
        if col == 'w':
            walls.append(pg.Rect(x*20,y*20,20,20))

def draw_window(player,enemies,holes,life,score):
    window.blit(bkgrnd,(0,0))
    for wall in walls:
        #wall = pg.Rect(x*20,y*20,20,20)
        window.blit(wall_image,(wall.x,wall.y))
        #pg.draw.rect(window,(0,0,0),wall)
    life_text = life_font.render('Life: ' + str(life),1,(255,255,255))
    window.blit(life_text,(275,20))
    score_text = score_font.render('Score: ' + str(score),1,(255,255,255))
    window.blit(score_text,(600,20))
    window.blit(donut,(player.x,player.y))
    for enemy in enemies:
        window.blit(manatee,(enemy.x,enemy.y))
    for direction, hole in holes:
        window.blit(donuthole,(hole.x,hole.y))
    pg.display.update()
    

def main():
    player = pg.Rect(500,500,X,Y)
    life = 5
    score = 0
    holes = []
    enemies = [pg.Rect(30,30,X,Y)]
   
    step_size = 4
    loopcount = 1
    clock = pg.time.Clock()

    run = True
    while run:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            #if event.type == pg.MOUSEMOTION:
            if movement == 'mouse':
                mx, my = pg.mouse.get_pos()
            #    dmx, dmy = pg.mouse.get_rel()
                player.center = (mx,my)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    holes.append(('up',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_s:
                    holes.append(('down',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_a:
                    holes.append(('left',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_d:
                    holes.append(('right',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_q:
                    holes.append(('upleft',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_e:
                    holes.append(('upright',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_z:
                    holes.append(('downleft',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_c:
                    holes.append(('downright',pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
                if event.key == pg.K_SPACE:
                    holes.append(('space', pg.Rect(player.x+X/4,player.y+Y/4,X/2,Y/2)))
        for direction, hole in holes:
            if direction == 'up':
                hole.y -= hole_velocity
            elif direction == 'down':
                hole.y += hole_velocity
            elif direction == 'left':
                hole.x -= hole_velocity
            elif direction == 'right':
                hole.x += hole_velocity
            elif direction == 'upleft':
                hole.y -= hole_velocity
                hole.x -= hole_velocity
            elif direction == 'upright':
                hole.y -= hole_velocity
                hole.x += hole_velocity
            elif direction == 'downleft':
                hole.y += hole_velocity
                hole.x -= hole_velocity
            elif direction == 'downright':
                hole.y += hole_velocity
                hole.x += hole_velocity
            
        for direction, hole in holes:
            for wall in walls:
                if hole.colliderect(wall):
                    try:
                        holes.remove((direction,hole))
                    except ValueError:
                        pass
        if movement == 'keys':                
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                player.y -= player_velocity
            if keys[pg.K_DOWN]:
                player.y += player_velocity
            if keys[pg.K_LEFT]:
                player.x -= player_velocity
            if keys[pg.K_RIGHT]:
                player.x += player_velocity
            for wall in walls:
                if player.colliderect(wall):
                    if keys[pg.K_UP]:
                        player.y += player_velocity
                    if keys[pg.K_DOWN]:
                        player.y -= player_velocity
                    if keys[pg.K_LEFT]:
                        player.x += player_velocity
                    if keys[pg.K_RIGHT]:
                        player.x -= player_velocity


        for enemy in enemies:
            player_vector = pg.math.Vector2(*(player.x,player.y))
            enemy_vector = pg.math.Vector2(*(enemy.x,enemy.y))
            new_enemy_vector = pg.math.Vector2(*(enemy.x,enemy.y))
            distance = enemy_vector.distance_to(player_vector)
            step_size = 4
            for wall in walls:
                wall_vector = pg.math.Vector2(*(wall.x,wall.y))
                if enemy.colliderect(wall):
                    step_size -= 5
                #if enemy.colliderect(wall) == False:
                    
            if distance > 0:
                direction_vector = (player_vector - enemy_vector) / distance
                step_distance = min(distance, step_size)
                new_enemy_vector = enemy_vector + direction_vector * step_distance
                enemy.x,enemy.y = new_enemy_vector
            
            if player.colliderect(enemy):
                enemies = []
                life -= 1
            
            if hole_mode == 'infinite':
                for direction, hole in holes:
                    if hole.colliderect(enemy):
                        try:
                            enemies.remove(enemy)
                            score += 1
                            if direction == 'space':
                                holes.remove((direction,hole))
                        except ValueError:
                            pass
                    if hole.x < 0 or hole.x > 1100 or hole.y < 0 or hole.y > 600:
                        holes.remove((direction,hole))

            if hole_mode == 'chain':
                for direction, hole in holes:
                    if hole.colliderect(enemy):
                        try:
                            score += 1
                            enemies.remove(enemy)
                            holes.remove((direction,hole))
                            holes.extend([
                                ('up',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('down',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('left',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('right',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('upleft',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('upright',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('downleft',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('downright',pg.Rect(hole.x,hole.y,X/2,Y/2))
                                ])
                        except ValueError:
                            pass
            if hole_mode == 'norm':
                for direction, hole in holes:
                    if hole.colliderect(enemy) and direction != 'space':
                        try:
                            enemies.remove(enemy)
                            holes.remove((direction,hole))
                            score += 1
                        except ValueError:
                            pass
                    if hole.colliderect(enemy) and direction == 'space':
                        try:
                            enemies.remove(enemy)
                            holes.remove((direction,hole))
                            holes.extend([
                                ('up',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('down',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('left',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('right',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('upleft',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('upright',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('downleft',pg.Rect(hole.x,hole.y,X/2,Y/2)),
                                ('downright',pg.Rect(hole.x,hole.y,X/2,Y/2))
                                ])
                        except ValueError:
                            pass

        
        if loopcount % enemy_delay == 0:  
            enemies.append(pg.Rect(30,30,X,Y))
        if life <= 0:
            score = 0
            life = 5
        draw_window(player,enemies,holes,life,score)
        loopcount += 1
    

if __name__=="__main__":
    main()

'''
*Boss manatee
--giant manatee
--manapede
*Powerups
--chain reaction
--appear/collect
--stronger shot
*Map
--walls
'''