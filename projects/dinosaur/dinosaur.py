import pygame
pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Dinosaur')
WHITE = ('#ffffff')
BLACK = ('#000000')
# tọa độ và tốc độ vật
background_x = 0
background_y = 0
dinosaur_x = 0
dinosaur_y = 220
tree_x = 550
tree_y = 227
x_velocity = 5
y_velocity = 7
# điểm
score = 0
font1 = pygame.font.SysFont('san', 20)
font2 = pygame.font.SysFont('san', 45)
# load file
background = pygame.image.load('background.jpg')
dinosaur = pygame.image.load('dinosaur.png')
tree = pygame.image.load('tree.png')
sound1 = pygame.mixer.Sound('tick.wav')
# sound2 = pygame.mixer.Sound('sound.mp3')

clock = pygame.time.Clock()
jump = False
pausing = False
running = True

while running:
    # pygame.mixer.Sound.play(sound2)
    clock.tick(60)
    screen.fill(WHITE)
    # vẽ nền
    background1_rect = screen.blit(background, (background_x, background_y))
    background2_rect = screen.blit(background, (background_x + 600, background_y))
    background_x -= x_velocity
    score_txt = font1.render("Score = " + str(score), True, BLACK)
    screen.blit(score_txt, (5, 5))
    if background_x  + 600 <= 0:
        background_x = 0
    # vẽ cây
    tree_rect = screen.blit(tree, (tree_x, tree_y))
    tree_x -= x_velocity
    if tree_x <= -20:
        tree_x = 550
        score += 1 
    # vẽ dinosaur
    dinosaur_rect = screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
    if 220 >= dinosaur_y >= 80:
        if jump == True:
            dinosaur_y -= y_velocity
    else:
        jump = False
    if dinosaur_y < 220:
        if jump ==False:
            dinosaur_y += y_velocity
    if dinosaur_rect.colliderect(tree_rect):
        pygame.mixer.Sound.play(sound1)
        pausing = True
        gameover_txt = font2.render(f"GAME OVER with {score} points", True, BLACK)
        screen.blit(gameover_txt, (112, 125))
        x_velocity = 0
        y_velocity = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dinosaur_y == 220:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
                if pausing :
                    score = 0
                    background_x = 0
                    background_y = 0
                    dinosaur_x = 0
                    dinosaur_y = 220
                    tree_x = 550
                    tree_y = 227
                    x_velocity = 5
                    y_velocity = 7
                    pausing = False
    pygame.display.flip()
pygame.quit()