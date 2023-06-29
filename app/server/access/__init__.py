import motor.motor_asyncio
from decouple import config


# MONGO_DETAILS = "mongodb://localhost:27017/"
MONGO_DETAILS = config('MONGODB_URL')

mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = mongodb_client['Books']
book_collection = database.get_collection("books")

def shut_db_client():
    mongodb_client.close()
    

