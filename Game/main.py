from core import *

player = Player("and3Rlex", 30, 30, 100, 1, 25)
monster = Monster("БОТ Стив", 30, 30, 100, 1, 25)

fight = Fight(player, monster)

while player.hp != 0 and monster.hp != 0:
    fight.battle(player, monster)
    # Применение хилки - когда у игрока осталось меньше какого-то процента от максимального хп:
    if player.hp < player.max_hp * 0.8:
        player.healing()


monster2 = Monster("БОТ Акула", 30, 30, 100, 1, 25)
monster3 = Monster("БОТ Владимир", 30, 30, 100, 1, 25)

fight2 = Fight(monster3, monster2)

while monster2.hp != 0 and monster3.hp != 0:
    fight2.battle(monster2, monster3)