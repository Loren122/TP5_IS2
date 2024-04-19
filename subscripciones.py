from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, id: str) -> None:
        pass

class ConcreteObserver(Observer):
    def __init__(self, id: str):
        self.id = id

    def update(self, id: str) -> None:
        if self.id == id:
            print(f"Observer {self.id}: Reacted to the event")

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, id: str) -> None:
        pass

class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """
    _observers = []

    def attach(self, observer: Observer) -> None:
        print(f"Subject: Attached an observer with id {observer.id}.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, id: str) -> None:
        print(f"Subject: Notifying observers about id {id}...")
        for observer in self._observers:
            observer.update(id)

# Ejemplo de uso
subject = ConcreteSubject()

observer1 = ConcreteObserver("1454")
observer2 = ConcreteObserver("wasd")
observer3 = ConcreteObserver("5555")
observer4 = ConcreteObserver("zxcv")

subject.attach(observer1)
subject.attach(observer2)
subject.attach(observer3)
subject.attach(observer4)

ids = ["1454", "pato", "qwer", "ghrw", "zxcv", "5555", "qrst", "wasd"]
for id in ids:
    subject.notify(id)
