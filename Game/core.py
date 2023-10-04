from random import randint


class Creature:
    def __init__(self, name, atk, armor, hp, min_damage, max_damage):
        if type(name) != str:
            raise TypeError("Имя должно быть строкой!")
        else:
            self.name = name
        if atk < 1 or atk > 30 or type(atk) != int:
            raise TypeError("Атака должна быть целым числом диапазоне от 1 до 30!")
        else:
            self.atk = atk
        if armor < 1 or armor > 30 or type(armor) != int:
            raise TypeError("Защита должна быть целым числом диапазоне от 1 до 30!")
        else:
            self.armor = armor
        if hp < 0 or type(hp) != int:
            raise TypeError("Здоровье должно быть натуральным числом!")
        else:
            self.hp = hp
        if min_damage < 0 or max_damage < 0 or type(min_damage) != int or type(max_damage) != int:
            raise TypeError("Урон должен быть диапазоном натуральных чисел!")
        else:
            # Будем считать, что диапазон урона мб задан в произвольном порядке
            self.min_damage = min(min_damage, max_damage)
            self.max_damage = max(max_damage, min_damage)

    def _income_damage(self, atk, min_damage, max_damage):
        n = atk - self.armor + 1
        flag = 0
        for i in range(n):
            if randint(1, 6) > 4:
                flag = 1
                break
        if flag == 1:
            self.hp -= randint(min_damage, max_damage)
            # При подсчёте будем считать, что если после битвы хп оказалось меньше 0, то оно будет равнятся 0
            if self.hp < 0: self.hp = 0
            print('{} получил урон и теперь имеет {} хп!'.format(self.name, self.hp))
        else:
            print('{} не получил урона!'.format(self.name))

    def attack(self, creature):
        creature._income_damage(self.atk, self.min_damage, self.max_damage)


class Player(Creature):
    def __init__(self, name, atk, armor, hp, min_damage, max_damage):
        Creature.__init__(self, name, atk, armor, hp, min_damage, max_damage)
        # Задаём параметры максимального хп и количества хилок для игрока
        self.max_hp = hp
        self.heals = 4

    def healing(self):
        if self.heals != 0:
            self.hp += self.max_hp * 0.3
            self.heals -= 1
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print('{} восстановил {} хп, теперь у него {} хп!'.format(self.name, self.max_hp * 0.3, self.hp))
        else:
            print('{} израсходовал все хилки'.format(self.name))


class Monster(Creature):
    def __init__(self, name, atk, armor, hp, min_damage, max_damage):
        Creature.__init__(self, name, atk, armor, hp, min_damage, max_damage)


class Fight:
    def __init__(self, creature1, creature2):
        self.creature1 = creature1
        self.creature2 = creature2

    def battle(self, creature1, creature2):
        if creature1.atk < creature2.armor and creature2.atk < creature1.armor:
            print(
                'Существа не могут атаковать друг друга, т.к. обоим не хватает атаки, чтобы пробить броню друг друга!')
            exit()
        if creature1.atk < creature2.armor:
            print(
                '{} не может получить урон, так как атака врага, равная {}, меньше, чем броня защищающегося, равная {}'.format(
                    creature2.name, creature1.atk, creature2.armor))
        else:
            creature1.attack(creature2)
        if creature2.hp <= 0:
            print('{} победил!'.format(creature1.name))
            return
        if creature2.atk < creature1.armor:
            print(
                '{} не может получить урон, так как атака врага, равная {}, меньше, чем броня защищающегося, равная {}'.format(
                    creature1.name, creature2.atk, creature1.armor))
        creature2.attack(creature1)
        if creature1.hp <= 0:
            print('{} победил!'.format(creature2.name))
            return
