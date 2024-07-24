from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource,reqparse, fields, marshal_with, abort
from datetime import datetime,timezone

app = Flask(__name__)
api =Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///text.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique =True, nullable= True)
    posts = db.relationship('PostModel', backref= 'author', lazy=True) 
    def __repr__(self):
        return f' {self.username}'
    
class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime,nullable=False, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id'), nullable=False)
    
    def __repr__(self):
        return f'{self.title}'


    
User_args = reqparse.RequestParser()
User_args.add_argument('username', type=str, required=True, help='Username is required')

post_args = reqparse.RequestParser()
post_args.add_argument('title', type=str, required=True, help='Title is required')
post_args.add_argument('content', type=str, required=True, help='Content is required')
post_args.add_argument('user_id', type=int, required=True, help='user_id is required')


userfields = {"id": fields.Integer, "username": fields.String}

postFields = {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String,
    "created_at": fields.DateTime,
    "author": fields.String(attribute="author.username")}



class Users(Resource):
    @marshal_with(userfields)
    def get(self):
        users = UserModel.query.all()
        return users,200
    
    @marshal_with(userfields)
    def post(self):
        args = User_args.parse_args()
        username =args["username"]
        newuser = UserModel(username =username)
        db.session.add(newuser)
        db.session.commit()
        return newuser, 201
    

class User(Resource):
    @marshal_with(userfields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message=f"User with {id} not found")
        return user
    
    @marshal_with(userfields)
    def patch(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message=f"User with {id} not found")
        args = User_args.parse_args()
        user.username=args["username"]
        db.session.commit()
        return user,200
    
    @marshal_with(userfields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message =f"User with {id} not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users,200

class Posts(Resource):
    @marshal_with(postFields)
    
    def get(self):
        posts = PostModel.query.all()
        return posts,200
    
    @marshal_with(postFields)
    def post(self):
        args =post_args.parse_args()
        title = args["title"]
        content = args["content"]
        user_id = args["user_id"]
        user =UserModel.query.get(user_id)
        if not user:
            return {"message" : "user not found"},404
        newpost = PostModel(title=title, content=content,user_id=user_id)
        db.session.add(newpost)
        db.session.commit()
        return newpost, 201
    
class post(Resource):
    @marshal_with(postFields)
    def get(self, id):
        post = PostModel.query.filter_by(id=id).first()
        if not post:
            abort(404, message=f"Post with ID {id} not found")
        return post, 200
    
    @marshal_with(postFields)
    def patch(self, id):
        post = PostModel.query.filter_by(id=id).first()
        if not post:
            abort(404, message=f"Post with ID {id} not found")
        args = post_args.parse_args()
        post.title = args["title"]
        post.content = args["content"]
        db.session.commit()
        return post,200
    
    



api.add_resource(Users,"/users/")
api.add_resource(User,"/users/<int:id>")
api.add_resource(Posts,"/posts/")
api.add_resource(post,"/posts/<int:id>")

@app.route('/')
def home():
    return "hello world!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run( debug=True)
 