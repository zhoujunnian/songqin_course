def endsign(func):
    def wrapper():
        return func()  + ' !!'
    return wrapper


def hello():
    return 'hello'

hello = endsign(hello)

print(hello())

