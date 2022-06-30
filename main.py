from flask import Flask
from flask_restful import  Api , Resource
import mysql.connector


app = Flask (__name__)
api = Api(app)

db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot"  ,
    database = "real_estate")
mycursor = db.cursor()


class HelloWorld(Resource):

    def get(self , name):

        #depending on the number of argument ,
        #select things to do.


        query = "select * from final_agent where name REGEXP '" +name+"*'"
        mycursor.execute(query)
        rows = mycursor.fetchall()

        #return rows with that data on it
        return {"data" :rows}

    def post(self):
        return {"data" : "Posted"}

api.add_resource(HelloWorld , "/getvalue/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)

