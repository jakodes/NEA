from sprite_object import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'Sprites/static sprites/'
        self.animated_sprite_path = 'Sprites/animated sprites/'
        add_sprite = self.add_sprite
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'blue_light/0.png', pos=(3.5, 4.75),
                                  animation_time=225))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'blue_light/0.png', pos=(3.5, 3.25),
                                  animation_time=225))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'green_light/0.png', pos=(4.5, 4.75),
                                  animation_time=225))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'green_light/0.png', pos=(4.5, 3.25),
                                  animation_time=225))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
