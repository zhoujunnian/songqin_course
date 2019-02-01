def endsign(func):
    def wrapper():
        return func()  + ' !!'
    return wrapper

def endsign2(func):
    def wrapper():
        return func()  + ' ##'
    return wrapper

@endsign2
@endsign
def hello():
    return 'hello'

hello =endsign(hello)
hello =endsign2(hello)

print(hello())

