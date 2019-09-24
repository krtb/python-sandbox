from user import User 
# from user file, import user class that is in camel case

# create variable and set equal to User class instance. instead of (id), has value of NONE, let PSQL handle
my_user = User('kurt@kurt.me', 'Kurt', 'Bauer', None) # calls init method and allows it to define the properties, __init__()


print(my_user)
