from flask import Flask
from flask_restful import Api, Resource, reqparse

app=Flask(__name__)
api = Api(app)

users = [
    {
        "name":"mushtaq",
        "age":23,
        "occupation":"software engineer"
    },
    {
        "name":"saqlain",
        "age":88,
        "occupation":"ias"
    },
    {
        "name":"afnan",
        "age":5,
        "occupation":"roaming"
    }
]


class User(Resource):
    def get(self,name):
        for user in users:
            if(name == user["name"]):
                return user,200
        return "User not found",404
        
    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "user with name {} already exists".format(name),400

        user = {
            "name":name,
            "age":args["age"],
            "occupation":args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"]=args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name":name,
            "age":args["age"],
            "occupation":args["occupation"]
        }

    def delete(self,name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} delted".format(name), 200

api.add_resource(User,"/user/<string:name>")
app.run(debug=True)

