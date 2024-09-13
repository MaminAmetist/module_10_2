# Потоки на классах
# Задача "За честь и отвагу!"
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.coint = 0
        self.company = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while range(self.company):
            sleep(1)
            self.coint += 1
            self.company -= self.power
            print(f'{self.name} сражается {self.coint} дней(дня), осталось {self.company} воинов')
        print(f'{self.name} одержал победу спустя {self.coint} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thr_1 = Thread(target=first_knight.run)
thr_2 = Thread(target=second_knight.run)

thr_1.start()
thr_2.start()

thr_1.join()
thr_2.join()

print('Все битвы закончились!')

