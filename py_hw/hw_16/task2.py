class Boss:
    def __init__(self, id_, name, company):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker) and worker not in self.workers:
            self.workers.append(worker)
            worker._boss = self

class Worker:
    def __init__(self, id_, name, company, boss=None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss
            boss.add_worker(self)
        else:
            raise ValueError("This person is not a boss!")

boss = Boss(1, "Steve", "Apple")
worker = Worker(2, "John", "Apple", boss)
print(f"{worker.name}'s boss is {worker.boss.name}")
