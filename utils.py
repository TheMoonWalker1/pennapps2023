from pymongo import MongoClient
def get_db_handle():
    client = MongoClient('mongodb+srv://db:<password>@pennapps2023.jadeitb.mongodb.net/?retryWrites=true&w=majority')
    db = client['pennapps2023']
    return db, client