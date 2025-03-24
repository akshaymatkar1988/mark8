import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Db.mongo import customer_collection
from User.IUser import IUser
from User.models.User import User
from bson import ObjectId


class Customer(IUser):

    customers = customer_collection

    @staticmethod
    def serialize_customer(customer):
        firstname = customer.get("firstname", None)
        lastname = customer.get("lastname", None)
        age = customer.get("age", 0)
        return {
            "id": str(customer["_id"]),
            "username": customer["username"],
            "firstname": firstname,
            "lastname": lastname,
            "age": age,
        }

    def create(self, data):

        if data:
            new_customer = User().from_dict(data)
            result = self.customers.insert_one(new_customer.to_dict())
            return {"message": "Customer added", "id": str(result.inserted_id)}
        else:
            return {"message": "missing something"}

    def read(self):
        customers = self.customers.find()
        return {
            "customers": [
                Customer.serialize_customer(customer) for customer in customers
            ]
        }

    def delete(self, id):
        obj_id = ObjectId(id)
        customer = self.customers.delete_one({"_id": obj_id})
        if customer.deleted_count == 1:
            return {"message": f"Customer {id} deleted successfully"}
        return {"message": f"Customer {id} not found"}

    def update(self, id, value_to_update):
        obj_id = ObjectId(id)
        customer = self.customers.find_one({"_id": obj_id})
        if customer:
            result = self.customers.update_one(
                {"_id": obj_id}, {"$set": value_to_update}
            )
            if result.modified_count > 0:
                return {"message": "Customer updated"}
            return {"message": "No changes made"}

        return {"message": "Customer not found"}
