import pygame
from pygame.constants import WINDOWSHOWN
pygame.init()

winWidth = 1280
winHeight = 720
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("PyPong")

paddleWidth = 20
paddleHeight = 60
# Player 1 paddle position and dimensions
p1X = 0
p1Y = winHeight/2
p1Paddle = (p1X, p1Y, paddleWidth, paddleHeight)
p1Score = 0

# Player 2 paddle position and dimensions
p2X = winWidth - 20
p2Y = winHeight/2
p2Paddle = (p2X, p2Y, paddleWidth, paddleHeight)
p2Score = 0

# Ball position and dimensions
ballX = winWidth/2
ballY = winHeight/2
ballCenter = (ballX, ballY)
ballVX = 10 #ball velocity - 10 pixels per frame
ballVY = 0
ballRadius = 5 
rgbColour = (255,255,255)

# Middle Line
lineX = winWidth/2
lineY = 0
lineWidth = 10
lineHeight = winHeight
lineDimensions = (lineX, lineY, lineWidth, lineHeight)


# Colours
white = (200, 200, 200)

def draw_game():
    p1Paddle = (p1X, p1Y, paddleWidth, paddleHeight)
    p2Paddle = (p2X, p2Y, paddleWidth, paddleHeight)
    window.fill((0,0,0))
    pygame.draw.rect(window, rgbColour, p1Paddle)
    pygame.draw.rect(window, rgbColour, p2Paddle)
    pygame.draw.rect(window, rgbColour, lineDimensions)
    pygame.draw.circle(window, rgbColour, ballCenter, ballRadius)
    # pygame.display.update()
    p1DisplayScore()
    p2DisplayScore()
    pygame.display.flip()

def p1DisplayScore():
    font = pygame.font.Font(None, 30)
    text = font.render("P1 Score: "+str(p1Score), True, white)
    textX = ((winWidth/2) - 200)
    textY = 30
    window.blit(text, (textX,textY))
    

def p2DisplayScore():
    font = pygame.font.Font(None, 30)
    text = font.render("P2 Score: "+str(p2Score), True, white)
    textX = ((winWidth/2) + 150)
    textY = 30
    window.blit(text, (textX,textY))

# Everything that needs repeated checking - in the while 'run' while loop
run = True
firstIteration = True
while run:
    pygame.time.delay(50) #50 milliseconds a frame

    ballX = ballX - ballVX
    ballY = ballY + ballVY
    ballCenter = (ballX, ballY)
    # If player pressed up or down
    keyPressed = pygame.key.get_pressed()
    # Player 1 w & s for up and down keys
    if keyPressed[pygame.K_w] and p1Y != 0:
        p1Y -=10
    if keyPressed[pygame.K_s] and p1Y != winHeight - 40:
        p1Y +=10

    # Player 2 for up and down keys
    if keyPressed[pygame.K_UP] and p2Y != 0 :
        p2Y -=10
    if keyPressed[pygame.K_DOWN] and p2Y != winHeight - 40:
        p2Y +=10

    #### Points System ####
    if ballX == 0:
        p1Score +=1
        p1DisplayScore()
        pygame.display.flip()

    if ballX == winWidth:
        p2Score +=1
        p2DisplayScore()
        pygame.display.flip()
    
    # If the ball hits the left paddle
    if ballX == paddleWidth and ballY + ballRadius > p1Y and ballY - ballRadius < p1Y + paddleHeight:
        ballVX = -10
        if keyPressed[pygame.K_w] and p1Y != 0:
            ballVY -=10
        if keyPressed[pygame.K_s] and p1Y != winHeight - 40:
            ballVY +=10

    # If the ball hits the right paddle
    if ballX == winWidth - paddleWidth and ballY+ballRadius > p2Y and ballY - ballRadius < p2Y + paddleHeight:
        ballVX = +10
        if keyPressed[pygame.K_UP] and p2Y != 0 :
            ballVY -=10
        if keyPressed[pygame.K_DOWN] and p2Y != winHeight - 40:
            ballVY +=10

    if ballY <= 0:
        ballVY = +10
    if ballY >= winHeight:
        ballVY = -10
    
    ballCenter = (ballX + ballVX, ballY)
    draw_game()

    # Quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False