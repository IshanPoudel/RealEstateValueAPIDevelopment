from flask import Flask , request
from flask_restful import  Api , Resource , reqparse , abort
import mysql.connector


app = Flask (__name__)
api = Api(app)

db = mysql.connector.connect(host="localhost" ,
    user = "root" ,
    passwd="rootroot"  ,
    database = "real_estate")
mycursor = db.cursor()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type = str , help = "Name of the video is required" , required= True)
video_put_args.add_argument("views" , type = int , help = "Views of the video")
video_put_args.add_argument("likes" , type = int , help = "Likes on the video")
videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    print("i am here")
    if video_id not in videos:
        abort(404 , message ="Video id not valid...")

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

class Video(Resource):

    def get(self , video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(selfself , video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args #store value in video_id

        return videos[video_id] , 201


api.add_resource(HelloWorld , "/getvalue/<string:name>")
api.add_resource(Video , "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

