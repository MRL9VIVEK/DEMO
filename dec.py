def announce(f):
    def wrapper():
        print("new world")
        f()
        print("old world")
        return wrapper
@announce
def hello():
    print("hello")
    