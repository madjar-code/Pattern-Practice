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
