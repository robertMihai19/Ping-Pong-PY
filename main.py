import pygame

pygame.init()
pygame.display.init()

width=600
height=400

def redraw_window(minge_x, minge_y, player1_y, player2_y, win):
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 255, 255), ((minge_x, minge_y), (15, 15)))
    pygame.draw.rect(win, (255, 255, 255), ((0, player1_y), (15, 100)))
    pygame.draw.rect(win, (255, 255, 255), ((width - 15, player2_y ), (15, 100)))
    pygame.display.update()

def main():
    win=pygame.display.set_mode((width, height))
    win.fill((0,0,0))
    move_minge = 15
    run=True
    move=0.05
    minge_x = width / 2
    minge_y = height / 2
    stanga=-1
    sus=-1
    player1_y=height/2-50
    player2_y=height/2-50
    COOLDOWN=0
    while run==True:
        redraw_window(minge_x, minge_y, player1_y, player2_y, win)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_y-move>0:
            player1_y-=move
        if keys[pygame.K_s] and player1_y+move+100<height:
            player1_y+=move
        if keys[pygame.K_UP] and player2_y-move>0:
            player2_y-=move
        if keys[pygame.K_DOWN] and player2_y+move+100<height:
            player2_y+=move

        if COOLDOWN==0:
            minge_y = minge_y + sus * move_minge
            minge_x = minge_x + stanga * move_minge
            COOLDOWN=200
            if minge_y<=0:
                minge_y=0
                sus=sus*(-1)
            if minge_y>height-15:
                minge_y=height-15
                sus=sus*(-1)
            if (minge_x<10 and minge_y>=player1_y and minge_y<=player1_y+100 ) or (minge_x>=width-15 and minge_y>=player2_y-30 and minge_y<=(player2_y+115)):
                stanga=stanga*(-1)
                minge_x=minge_x+move_minge*stanga
                minge_y=minge_y+move_minge*sus

        if COOLDOWN!=0:
            COOLDOWN-=1
        if minge_x<0 or minge_x>width:
            run=False

main()