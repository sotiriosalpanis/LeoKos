from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv()
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')
mongo_table = os.getenv('MONGO_DB_TABLE')
mongo_url = f'mongodb+srv://{mongo_username}:{mongo_password}@leo-kos.rw1tg.mongodb.net/?retryWrites=true&w=majority'
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = client[mongo_table]
