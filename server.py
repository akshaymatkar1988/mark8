from flask import Flask
from User.controllers.customerController import customer_blueprint

app = Flask(__name__)
app.register_blueprint(customer_blueprint, url_prefix="/api/customers")

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
