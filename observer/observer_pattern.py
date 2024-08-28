from typing import List
from abc import ABC, abstractmethod

'''
1. publisher interface
2. subscriber interfaces
3. concrete publisher
4. concrete subscriber
5. Constructor injection
'''

# 1. Subscriber Interface
class SubscriberInterface(ABC):

    @abstractmethod
    def notify(self) -> None:
        pass

# 2. Publisher Interface
class PublisherInterface(ABC):

    @abstractmethod
    def publish(self) -> None:
        pass

    @abstractmethod
    def add_subscriber(self, subscriber: SubscriberInterface) -> None:
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: SubscriberInterface) -> None:
        pass

# 3. Concrete Publisher
class IphoneAlert(PublisherInterface):
    def __init__(self, subscribers: List[SubscriberInterface]=None) -> None:
        self.stock: int = 0
        self.subscribers: List[SubscriberInterface] =  subscribers if subscribers else []

    def publish(self) -> None:
        for subscriber in self.subscribers:
            subscriber.notify()

    def add_stock(self, new_stock: int) -> None:
        if self.stock == 0 and new_stock > 0:
            self.publish()

        self.stock += new_stock

    def add_subscriber(self, subscriber: SubscriberInterface) -> None:
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: SubscriberInterface) -> None:
        self.subscribers.remove(subscriber)

# 4. Concrete Subscriber
class EmailAlert(SubscriberInterface):
    def __init__(self, mail: str) -> None:
        self.mail = mail
    
    def notify(self) -> None:
        print(f'Email alert sent to {self.mail}.')

class PhoneAlert(SubscriberInterface):
    def __init__(self, number: str) -> None:
        self.number = number
    
    def notify(self) -> None:
        print(f'SMS alert sent to {self.number}.')

# Example Usage
if __name__ == "__main__":

    # Create subscribers
    email_subscriber1 = EmailAlert("example1@example.com")
    email_subscriber2 = EmailAlert("example2@example.com")
    phone_alert1 = PhoneAlert("123-456-7890")

    # Initializing and adding subscribers to the publisher
    iphone_alert = IphoneAlert([email_subscriber1, email_subscriber2])
    iphone_alert.add_subscriber(phone_alert1)

    # Trigger a stock update and notification
    iphone_alert.add_stock(10)
