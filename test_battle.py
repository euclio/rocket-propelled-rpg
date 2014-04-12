from rprpg.battle.scene import Scene
from rprpg.battle.entity import Player, Enemy
from rprpg.render.spritesheet import SpriteSheet

def main():
    spritesheet = SpriteSheet('rprpg/assets/biker.png')
    entities = [Player(spritesheet), Enemy(spritesheet)]
    battle = Scene(entities)
    battle.start()


if __name__ == '__main__':
    main()
