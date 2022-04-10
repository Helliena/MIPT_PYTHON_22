from view import Cat, Button, Cursor
import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#Game parameters
screen_width = 900
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("sprites_data/background.png")
pygame.mouse.set_visible(False)
night = pygame.image.load("sprites_data/night.png")

#Cat
cat = Cat(450, 670)
cat_group = pygame.sprite.Group()
cat_group.add(cat)

#Activities
play = Button(150, 915, "sprites_data/play.png")
feed = Button(480, 915, "sprites_data/food.png")
sleep = Button(750, 915, "sprites_data/sleep.png")
buttons_group = pygame.sprite.Group()
buttons_group.add(play)
buttons_group.add(feed)
buttons_group.add(sleep)

#Cursor
cursor = Cursor()
cursor_group = pygame.sprite.Group()
cursor_group.add(cursor)

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in buttons_group if s.rect.collidepoint(pos)]
            for sp in clicked_sprites:
                if sp == play:
                    cat.play()
                if sp == feed:
                    cat.feed()
                if sp == sleep:
                    cat.sleep()

    pygame.display.flip()
    screen.blit(background, (0, 0))

    cat_group.update(screen)
    cat_group.draw(screen)

    if cat.is_sleeping:
        screen.blit(night, (0, 0))
    
    buttons_group.draw(screen)

    cursor.update()
    cursor_group.draw(screen)

    clock.tick(30)