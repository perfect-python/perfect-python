from typing import NewType


UserId = NewType('UserId', int)


def something(user_id:UserId) -> UserId:
    return user_id


if __name__ == '__main__':
    something(UserId(1))
    something(1)
    UserId(1) + 1
    new_user_id:UserId = UserId(1) + UserId(2)

