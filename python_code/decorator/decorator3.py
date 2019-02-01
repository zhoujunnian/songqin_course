def endsign(tail):
    def innerOne(func):
        def wrapper():
            return func()  + ' ' + tail
        return wrapper
    return innerOne

@endsign('333')
def hello():
    return 'hello'
# hello = endsign('333') (hello)

print(hello())

