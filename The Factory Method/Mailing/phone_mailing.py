from abc import ABC, abstractmethod

from typing import (
    NamedTuple,
    Optional,
)


class User(NamedTuple):
    name: str
    phone: Optional[str]


users = [
    User(name="evan", phone="+111111111"),
    User(name="alex", phone="+222222222"),
    User(name="george", phone="+333333333")
]


class Message(ABC):
    @abstractmethod
    def send_message(self):
        pass


class PhoneMessage(Message):
    def __init__(self, text: str, recipient: User) -> None:
        self.message_text: str = text
        self.recipient: User = recipient

    def send_message(self) -> None:
        """Send message to phone"""
        try:
            # code to message sending
            print('Phone message sent')
        except:
            print('Problems sending a phone message')

