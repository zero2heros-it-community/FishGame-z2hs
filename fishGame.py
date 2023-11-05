
import pygame, random

# Package Starting
pygame.init()

# window Size
width, height = 600, 750
window = pygame.display.set_mode((width, height))

# Background Sound and FeedSound
pygame.mixer.music.load("backgroundFon.mp3")
pygame.mixer.music.play(-1, 0.0)       # -1 oyun baslar baslamaz müzik calmaya basla- taki 0.0 yani oyun kapanana kadar
feedSound = pygame.mixer.Sound("feedSound.mp3")
levelUp = pygame.mixer.Sound("feedSound.mp3")

# Frames per Second ayarlari
fast = 10    # piksel
time = pygame.time.Clock()
FPS = 27

# Karakter ve Yem Ayarlari
fish = pygame.image.load("fish1-image.png")
fishCoordinate = fish.get_rect()
fishCoordinate.topleft = (width / 2, height / 2)

feed = pygame.image.load("feed.png")
feedCoordinate = feed.get_rect()
feedCoordinate.topleft = (150, 150)

# Background picture
background = pygame.image.load("background1.jpg")

# Score degiskeni icin tanimlama
font = pygame.font.SysFont("consolas", 64)
score = 0


status = True

while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    window.blit(background, (0,0))
    window.blit(fish, fishCoordinate)
    window.blit(feed, feedCoordinate)

    scoreTable = font.render("Score:" + str(score), True, (255, 0, 0), (0, 0, 255))
    scoreTable_coordinate = scoreTable.get_rect()
    scoreTable_coordinate.topleft = (20, 20)
    pygame.draw.line(window, (255,0,255), (0,90), (600,90),3)

    window.blit(scoreTable, scoreTable_coordinate)

    button = pygame.key.get_pressed()
    if button[pygame.K_LEFT] and fishCoordinate.left > 0:
        fishCoordinate.x -= fast
    elif button[pygame.K_RIGHT] and fishCoordinate.right < width:
        fishCoordinate.x += fast
    elif button[pygame.K_UP] and fishCoordinate.top > 0:
        fishCoordinate.y -= fast
    elif button[pygame.K_DOWN] and fishCoordinate.bottom < height:
        fishCoordinate.y += fast

    if score > 7:
        fish = pygame.image.load("fish2-image.png")
        background = pygame.image.load("background2.jpg")
        if button[pygame.K_LEFT] and fishCoordinate.left > 0:
            fishCoordinate.x -= fast
        elif button[pygame.K_RIGHT] and fishCoordinate.right < width:
            fishCoordinate.x += fast
        elif button[pygame.K_UP] and fishCoordinate.top > 0:
            fishCoordinate.y -= fast
        elif button[pygame.K_DOWN] and fishCoordinate.bottom < height:
            fishCoordinate.y += fast

    if fishCoordinate.colliderect(feedCoordinate):
        feedSound.play()
        feedCoordinate.x = random.randint(0, width - 32)
        feedCoordinate.y = random.randint(0, height - 32)
        score += 1

    pygame.display.update()
    time.tick(FPS)


