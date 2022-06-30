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

    def get(self ):

        query = "select * from final_agent order by agent_id desc limit 50"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        return {"data" :rows}

    def post(self):
        return {"data" : "Posted"}

api.add_resource(HelloWorld , "/getvalue")


if __name__ == "__main__":
    app.run(debug=True)

