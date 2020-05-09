from typing import Optional


def get_userid(email:str) -> Optional[int]:
    if email == 'exists@example.com':
        return 1
    return None


if __name__ == '__main__':
    print(get_userid("exists@example.com"))
    print(get_userid("other@example.com"))

