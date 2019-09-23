#create user class
class User:
    #pass = if we didn't want our user to do anything
    # self = currently bound object
    def __init__(self, email, first_name, last_name, id): # add args/props of user object, id goes last
        # init method = allows for definition of props stores in each object
        super().__init__(*args, **kwargs)