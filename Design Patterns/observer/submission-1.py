class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.observers = []
        self.itemName = itemName
        self.stock = stock

    def subscribe(self, observers: Observer) -> None:
        self.observers.append(Observer)

    def unsubscribe(self, observers: Observer) -> None:
        self.observers.remove(Observer)

    def updateStock(self, newStock: int) -> None:
        if newStock > 0 :
            stock = newStock

        for Observer in observers :
            observer.countNotifications()
        
