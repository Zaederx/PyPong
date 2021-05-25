import pygame
pygame.init()

winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption("PyPong")

# Player 1 paddle position and dimensions
p1X = 0
p1Y = winHeight/2
p1Paddle = (p1X,p1Y, 20, 40)
p1Score = 0

# Player 2 paddle position and dimensions
p2X = winWidth - 20
p2Y = winHeight/2
p2Paddle = (p2X,p2Y, 20, 40)
p2Score = 0

# Ball position and dimensions
ballX = winWidth/2
ballY = winHeight/2
ballCenter = (ballX,ballY)
ballV = 1 #ball velocity
ballRadius = 5 
rgbColour = (100,100,100)

def draw_game():
    p1Paddle = (p1X,p1Y, 20, 40)
    p2Paddle = (p2X,p2Y, 20, 40)
    window.fill((0,0,0))
    pygame.draw.rect(window, rgbColour, p1Paddle)
    pygame.draw.rect(window, rgbColour, p2Paddle)
    pygame.draw.circle(window, rgbColour, ballCenter, ballRadius )
    pygame.display.update()


# Everything that needs repeated checking - in the while 'run' while loop
run = True
while run:
    pygame.time.delay(50)

    # If player pressed up or down
    keyPressed = pygame.key.get_pressed()
    # Player 1 w & s for up and down keys
    if keyPressed[pygame.K_w]:
        p1Y -=10
    if keyPressed[pygame.K_s]:
        p1Y +=10

    # Player 2 for up and down keys
    if keyPressed[pygame.K_UP]:
        p2Y -=10
    if keyPressed[pygame.K_DOWN]:
        p2Y +=10

    draw_game()

    # Quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False