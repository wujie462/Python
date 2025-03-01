import pygame
from .. import constants as C
from . import coin
pygame.font.init()


class Info:
    def __init__(self, state):
        self.state = state
        self.creat_state_labels()
        self.creat_info_labels()
        self.flash_coin=coin.FlashingCoin()

    def creat_state_labels(self):
        self.state_labels=[]
        if self.state == 'main_menu':
            self.state_labels.append((self.creat_labels('1 PLAYER GAME'),(272,360)))
            self.state_labels.append((self.creat_labels('2 PLAYER GAME'),(272,405)))
            self.state_labels.append((self.creat_labels('TOP - '),(290,465)))
            self.state_labels.append((self.creat_labels('000000'),(400,465)))

    def creat_info_labels(self):
        self.info_labels=[]
        self.info_labels.append((self.creat_labels('MARIO'),(75,30)))
        self.info_labels.append((self.creat_labels('WORLD'),(450,30)))
        self.info_labels.append((self.creat_labels('TIME'),(625,30)))
        self.info_labels.append((self.creat_labels('000000'),(75,55)))
        self.info_labels.append((self.creat_labels('x00'),(300,55)))
        self.info_labels.append((self.creat_labels('1 - 1'),(480,55)))


    # 什么字,多大,缩放多少
    def creat_labels(self, label, size=40, width_scale=1.25, height_scale=1):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label, 1, (255, 255, 255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image, (int(rect.width*width_scale),
                                                           int(rect.height*height_scale)))
        
        return label_image

    def update(self):
        self.flash_coin.update()

    def draw(self, surface):
        for label in self.state_labels:
            surface.blit(label[0],label[1])
        for label in self.info_labels:
            surface.blit(label[0],label[1])
            surface.blit(self.flash_coin.image,self.flash_coin.rect)