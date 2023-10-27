import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(Counter.rounds):
            Counter.counter += 1

# Создание и запуск двух потоков
thread1 = Counter()
thread2 = Counter()
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Counter value:", Counter.counter)
