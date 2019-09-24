import psycopg2

class User:
    #pass = if we didn't want our user to do anything
    # self = currently bound object
    def __init__(self, email, first_name, last_name, id): # add args/props of user object, id goes last
        # init method = allows for definition of props stores in each object, provide with some values
        self.email = email
        self.first_name = first_name # set props passed into class to be a property of this class
        self.last_name = last_name
        self.id = id
        
    
    def __repr__(self): #without it would only get type and memory address
        return "<User {}>".format(self.email) # allows your to print the user object with less code

    def save_to_db(self): # add method to save user to database
        # change to with/as connection:, psycopg2 not comes with connect and close functions
        with psycopg2.connect(user='kurt', password='password', database='learning_python', host='localhost') as connection:
        #cursor, retrieves data and reads row by row, have to open this
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s,%s,%s)',
                    (self.email, self.first_name, self.last_name)
                ) #does almost the same thing as the format method