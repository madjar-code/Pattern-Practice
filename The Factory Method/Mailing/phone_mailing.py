from abc import ABC, abstractmethod

from typing import (
    NamedTuple,
    Optional,
    Sequence,
)


class User(NamedTuple):
    name: str
    phone: Optional[str]


users: Sequence[User] = [
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


def sending_messages() -> None:
    for user in users:
        phone_message = PhoneMessage(
            text='Wonderful weather', recipient=user)
        phone_message.send_message()


if __name__ == '__main__':
    sending_messages()
