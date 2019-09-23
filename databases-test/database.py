#create user class
class User:
    #pass = if we didn't want our user to do anything
    def __init__(self, *args, **kwargs):
        # init method = allows for definition of props stores in each object
        super().__init__(*args, **kwargs)