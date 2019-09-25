from user import User 
# from user file, import user class that is in camel case

# create variable and set equal to User class instance. instead of (id), has value of NONE, let PSQL handle
my_user = User('test', 'test@test.com', 'testtest', None)
my_user.save_to_db()
print(my_user)
