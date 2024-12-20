import pygame
from abc import ABC, abstractmethod
import config
from ball import Ball # импорт Ball из файла ball
from racket import RacketAuto, RacketManual, Racket # импорт RacketAuto, RacketManual, Racket из файла racket
from score import Score # импорт Score из файла score
#ABC - абстрактный класс(нельзя создать экземпляр)

class Scene(ABC):
    @abstractmethod
    def __init__(self, game):
        self.game = game
        self.keys_pressed = None
        self.all_sprites = pygame.sprite.Group()

    def handle_events(self) -> None:
        '''обрабатывает события'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.game.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.is_running = False

                
        self.keys_pressed = pygame.key.get_pressed()

    def update(self):
        self.all_sprites.update()

    def render(self):
        '''отрисовывает обьекты на екране'''
        self.all_sprites.draw(self.game.screen)
        pygame.display.flip()


class GameplayScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.all_rackets = pygame.sprite.Group()

        # левая ракетка
        x_left = self.game.window_width // 10
        self.racket_left = RacketManual(x_left, pygame.K_w, pygame.K_s, self)

        # правая ракетка
        x_right = self.game.window_width // 10 * 9 - Racket.width
        self.racket_right = RacketAuto(x_right, self)

        # мяч
        self.ball = Ball(self)

        #левое табло 
        self.score_left = Score(int(self.game.window_width * 0.25), 100, self)

        #правое табло
        self.score_right = Score(int(self.game.window_width * 0.75), 100, self)

    def render(self):
         '''отрисовывает обьекты на екране'''
         self.all_sprites.draw(self.game.screen)
         pygame.display.flip()

class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        pass

    def render(self):
         '''отрисовывает обьекты на екране'''
         self.all_sprites.draw(self.game.screen)
         pygame.display.flip()