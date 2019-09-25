from user import User 
# from user file, import user class that is in camel case

# create variable and set equal to User class instance. instead of (id), has value of NONE, let PSQL handle
my_user = User.load_from_db_by_email('kurt@kurt.me')

print(my_user)
