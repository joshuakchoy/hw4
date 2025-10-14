from time import ctime

def timestamp(func):
    def wrapper(*args, **kwargs):
        print(ctime())
        return func(*args, **kwargs)
    return wrapper