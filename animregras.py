import pygame

SIZE = WIDTH, HEIGHT = 700, 500  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
FPS = 10  # Frames per second


class MySprite(pygame.sprite.Sprite):
    def __init__(self, images):
        super(MySprite, self).__init__()
        # adding all the images to sprite array
        self.images = images
            

        # index value to get the image from the array
        # initially it is 0
        self.index = 0

        # now the image that we will display will be the index from the image array
        self.image = self.images[self.index]

        # creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):
        # when the update method is called, we will increment the index
        self.index += 1

        # if the index is larger than the total images
        if self.index >= len(self.images):
            # we will make the index to 0 again
            self.index = 0

        # finally we will update the image that will be displayed
        self.image = self.images[self.index]


def main2(imagens):
    # initializing pygame
    pygame.init()

    # getting the screen of the specified size
    screen = pygame.display.set_mode(SIZE)

    # creating our sprite object
    my_sprite = MySprite(imagens)

    # creating a group with our sprite
    my_group = pygame.sprite.Group(my_sprite)

    # getting the pygame clock for handling fps
    clock = pygame.time.Clock()

    for i in range (0, 510):
        # if the event is quit means we clicked on the close window button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit the game
                pygame.quit()
                quit()

        # updating the sprite
        my_group.update()

        # filling the screen with background color
        screen.fill(BACKGROUND_COLOR)

        # drawing the sprite
        my_group.draw(screen)

        # updating the display
        pygame.display.update()

        # finally delaying the loop to with clock tick for 10fps
        clock.tick(30)
        
    pygame.time.wait(600)

if __name__ == '__main__':
    main2()
