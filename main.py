from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)




class VideoModel(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100) , nullable = False)
    views = db.Column(db.Integer , nullable = False)
    likes = db.Column(db.Integer , nullable = False)

    def __repr__(self):
        return f"Video(name = {name} , views = {views} , likes = {likes} "


# db.create_all()
# you create it once and then rempove it.



#required when a put object is created so that it it created
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name" , type = str , help = "Name of the video is required" , required= True)
video_put_args.add_argument("views" , type = int , help = "Views of the video")
video_put_args.add_argument("likes" , type = int , help = "Likes on the video")
videos = {}



video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name" , type = str , help = "Name of the video is required")
video_update_args.add_argument("views" , type = int , help = "Views of the video")
video_update_args.add_argument("likes" , type = int , help = "Likes on the video")

def abort_if_video_id_doesnt_exist(video_id):
    print("i am here")
    if video_id not in videos:
        abort(404 , message ="Video id not valid...")

def abort_if_video_already_exists(video_id):
    if video_id in videos:
        abort(409 , message = "Video already exists with that id")



resource_fields = {
    'id' : fields.Integer ,
     'name' : fields.String ,
    'views' : fields.Integer ,
    'likes' : fields.Integer
}
# resource field is a way to define how a object should be serialized and should be returned

class Video(Resource):

    @marshal_with(resource_fields) #serialized into the json format
    def get(self , video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404 , message = 'Could not get id')
        return result

    @marshal_with(resource_fields) #serialized into json fomrat
    def put(self , video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409 , message= 'Video id taken')
        video = VideoModel(id=video_id , name = args['name'] , views = args['views'] , likes = args['likes'])
        # videos[video_id] = args #store value in video_id
        db.session.add(video)
        db.session.commit()
        return video

    @marshal_with(resource_fields)
    def patch(self , video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404 , message = "Video does not exist , cannot update")

        if args['name']:  #if args in name
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']


        db.session.commit()

        return result

    def delete (self , video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return " " , 204






api.add_resource(Video , "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

