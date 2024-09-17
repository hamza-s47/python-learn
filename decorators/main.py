def dec(func):
    def wrap():
        func()
        print("From Decorator")
        return 2
    return wrap

@dec
def abc():
    print("Normal Func")

abc()
print(abc())  # added 2 also