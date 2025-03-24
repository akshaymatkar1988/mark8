from pymongo import MongoClient

mongoUri = "mongodb://localhost:27017/userservice"
mclient = MongoClient(mongoUri)
db = mclient.mark8
customer_collection = db.customers
