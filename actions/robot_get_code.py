from imports.imports import *

password = password
encoded_password = quote(password)
user_name = user_name
db_name = db_name
phone_Shalev = '972000000125'
phone_Omri = '972000000444'
phone_Elon = 'Insert phone here'
phone_Mark = 'Insert phone here'
phone_Lior = 'Insert phone here'
phone_Aviv = 'Insert phone here'





# Function to create MongoDB connection
def create_mongo_connection(user_name, encoded_password, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    return client


# Function to test the MongoDB connection
def test_connection(db):
    try:
        db.command("ping")
        print("Connected to MongoDB.")
    except Exception as e:
        print("Error connecting to MongoDB:", e)


def create_mongo_db(client, db_name):
    # Connect to MongoDB using the given credentials and return the database object
    db = client[db_name]
    return db


def close_connection(client):
    client.close()


# --------------------------


def get_loginCode(db, phone):
    collection = db['users']
    document = collection.find_one({'phone': phone})
    if document:
        value = document.get('loginCode', 'NoValue')
        print(f'Login code is: {value}')
        return int(value)
    else:
        print('Invalid phone number.')
        return None

def full():
        client = create_mongo_connection(user_name, encoded_password, db_name)
        db = create_mongo_db(client, db_name)
        test_connection(db)
        login_code = get_loginCode(db, phone_Shalev)
        return login_code














