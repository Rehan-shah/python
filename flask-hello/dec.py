

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"

    return wrapper

def make_unde(func):
    def wrapper():
        return f"<em>{func()}</em>"

    return wrapper

