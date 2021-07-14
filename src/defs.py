import random
class enemy:
  def __init__(name,hp, damage, attack1, attack2,attack3,namee):
    enemy.namee = namee
    enemy.hp = random.randint(hp-3,hp+5)
    enemy.damage = random.randint(damage-5,damage+5)
    enemy.attack1 = attack1
    enemy.attack2 = attack2
    enemy.attack3 = attack3
