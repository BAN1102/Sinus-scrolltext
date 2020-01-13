#
#       Scrolltext
#
#       To do:   angle, rolling
#
#

from pygame import *
import pygame
pygame.init()
pygame.font.init()

#       Variables

winwidth = 1920
winheight = 1080
scrollttf = pygame.font.Font("From Cartoon Blocks.ttf", 155)
screen = pygame.display.set_mode((winwidth, winheight), FULLSCREEN | DOUBLEBUF)
pygame.mouse.set_visible(False)
screen.fill((0, 0, 0))
pygame.display.update()


#       Classes

class Scrolltext():  # Add every letter from the text string as a object and move
    #    them across the screen.
    #    Letters can move fast, slow, jump, change color and angle.
    #    Sinus scrollers are the goal

    def __init__(self, x, y, speed, txt, color, width, repeat):

        self.x = x
        self.y = y
        self.speed = 0 - speed
        self.txt = txt
        self.color = textcolor[color]
        self.i = color
        self.width = width
        self.repeat = repeat
        self.textcount = len(textcolor)

    def move(self):

        if self.x <= -65:
            if self.repeat == 1:
                self.x = winwidth + 65
            if self.repeat == 0:
                scrolltext.remove(self)
        label = scrollttf.render(self.txt, 1, (self.color, 0, 255 - self.color))
        screen.blit(label, (self.x - int(self.color / 2), self.y - (self.color * 2)))
        self.x += self.speed
        self.i += 1
        if self.i == self.textcount:
            self.i = 0
        self.color = textcolor[self.i]


# Main

text = "Just a short text to show of my scroller. It was made a while back and i have yet to use it......."
textcolor = [128, 136, 143, 151, 159, 167, 174, 182, 189, 196, 202, 209, 215, 220, 226, 231,
             235, 239, 243, 246, 249, 251, 253, 254, 255, 255, 255, 254, 253, 251, 249, 246,
             243, 239, 235, 231, 226, 220, 215, 209, 202, 196, 189, 182, 174, 167, 159, 151,
             143, 136, 128, 119, 112, 104, 96, 88, 81, 73, 66, 59, 53, 46, 40, 35,
             29, 24, 20, 16, 12, 9, 6, 4, 2, 1, 0, 0, 0, 1, 2, 4,
             6, 9, 12, 16, 20, 24, 29, 35, 40, 46, 53, 59, 66, 73, 81, 88,
             96, 104, 112, 119, 128]
clock = pygame.time.Clock()
scrolltext = []
textwith = 0
for i in range(0, len(text)):
    width, height = scrollttf.size(text[i])
    scrolltext.append(Scrolltext(winwidth + textwith, winheight - 155, 4, text[i], i, width - 10, 1))
    textwith += width - 10

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        running = False

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for i in scrolltext:
        i.move()

    pygame.display.update()

pygame.quit()
