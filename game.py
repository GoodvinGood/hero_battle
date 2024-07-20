import random
from hero import Hero

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!\n")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            if not self.player.is_alive():
                print("Компьютер победил!")
            elif not self.computer.is_alive():
                print("Игрок победил!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
