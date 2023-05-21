from abc import ABC, abstractmethod

from typing import (
    TypedDict,
    NamedTuple,
    Optional,
    Sequence,
)


class User(TypedDict):
    name: str
    phone: Optional[str]
    email: Optional[str]


class TextData(NamedTuple):
    subject: Optional[str]
    text: str


users: Sequence[User] = [
    User(name="evan", phone="+111111111"),
    User(name="alex", phone="+222222222"),
    User(name="george", phone="+333333333"),
    User(name="sam", email="test1@test.com"),
    User(name="simon", email="test2@test.com"),
    User(name="stan", email="test3@test.com"),
]

TEXT_DATA = TextData(subject='About Weather',
                     text='Wonderful weather!')


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
            print(f'Phone message sent to {self.recipient.name}')
        except:
            print('Problems sending a phone message')


class EmailMessage(Message):
    def __init__(self, subject: str, text: str,
                 recipient: User) -> None:
        self.subject: str = subject
        self.message_text: str = text
        self.recipient: User = recipient

    def send_message(self) -> None:
        """Send message to email"""
        try:
            # code to message sending
            print(f'Email message sent to {self.recipient.name}')
        except:
            print('Problems sending an email message')


def sending_factory(recipient: User,
                    text_data: TextData) -> Message:
    if recipient.get('phone', None):
        message = PhoneMessage(text=text_data.text,
                               recipient=recipient)
    elif recipient.get('email', None):
        message = EmailMessage(subject=text_data.subject,
                               text=text_data.text,
                               recipient=recipient)
    else:
        print('No contacts')
    return message


def sending_messages() -> None:
    for user in users:
        message = sending_factory(recipient=user,
                                  text_data=TEXT_DATA)
        if message:
            message.send_message()


if __name__ == '__main__':
    sending_messages()
