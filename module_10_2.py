# Потоки на классах
# Задача "За честь и отвагу!"
from threading import Thread
from time import sleep

class Knight(Thread):
    COMPANY = 100
    COUNT = 0
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while range(self.COMPANY):
            if self.COMPANY >= self.power:
                sleep(1)
                self.COUNT += 1
                self.COMPANY -= self.power
                print(f'{self.name} сражается {self.COUNT} дней(дня), осталось {self.COMPANY} воинов')
        print(f'{self.name} одержал победу спустя {self.COUNT} дней(дня)!')
        return

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thr_1 = Thread(target=first_knight.run)
thr_2 = Thread(target=second_knight.run)

thr_1.start()
thr_2.start()

thr_1.join()
thr_2.join()

print('Все битвы закончились!')
