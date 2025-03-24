from User.customer import Customer
from flask import Blueprint, request, jsonify

customer_blueprint = Blueprint("customer", __name__)
customer = Customer()


@customer_blueprint.route("/add", methods=["POST"])
def add_customer():
    data = request.json
    result = customer.create(data)
    return jsonify(result)


@customer_blueprint.route("/", methods=["GET"])
def get_customers():
    result = customer.read()
    return jsonify(result)


@customer_blueprint.route("/update", methods=["PATCH"])
def update_customer():
    data = request.json
    id = data["id"]
    value_to_update = data["update"]
    result = customer.update(id, value_to_update)
    return jsonify(result)


@customer_blueprint.route("/delete", methods=["DELETE"])
def delete_customer():
    id = request.json["id"]

    result = customer.delete(id)
    return jsonify(result)
