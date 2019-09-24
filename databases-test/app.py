from user import User 
# from user file, import user class that is in camel case

# create variable and set equal to User class instance. instead of (id), has value of NONE, let PSQL handle
my_user = User('three@three.me', 'three', 'threethree', None) # calls init method and allows it to define the properties, __init__()
my_user.save_to_db()

print(my_user)
