from flask import Flask, request, jsonify, abort, render_template
from models import db, Post, Comment
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    @app.route('/posts', methods=['GET'])
    def get_posts():
        posts = Post.query.all()
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author} for post in posts])

    @app.route('/posts/<int:id>', methods=['GET'])
    def get_post(id):
        post = Post.query.get_or_404(id)
        return jsonify({'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author})

    @app.route('/posts', methods=['POST'])
    def create_post():
        if not request.json or not 'title' in request.json or not 'content' in request.json or not 'author' in request.json:
            abort(400)
        post = Post(title=request.json['title'], content=request.json['content'], author=request.json['author'])
        db.session.add(post)
        db.session.commit()
        return jsonify({'id': post.id}), 201

    @app.route('/posts/<int:id>', methods=['PUT'])
    def update_post(id):
        post = Post.query.get_or_404(id)
        if not request.json:
            abort(400)
        post.title = request.json.get('title', post.title)
        post.content = request.json.get('content', post.content)
        post.author = request.json.get('author', post.author)
        db.session.commit()
        return jsonify({'id': post.id})

    @app.route('/posts/<int:id>', methods=['DELETE'])
    def delete_post(id):
        post = Post.query.get_or_404(id)
        try:
            
            Comment.query.filter_by(post_id=id).delete()
            db.session.delete(post)
            db.session.commit()
            return jsonify({'message': 'Post and associated comments deleted successfully'}), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description="Database error occurred during delete operation")

    @app.route('/posts/<int:post_id>/comments', methods=['GET'])
    def get_comments(post_id):
        post = Post.query.get_or_404(post_id)
        comments = Comment.query.filter_by(post_id=post.id).all()
        return jsonify([{'id': comment.id, 'content': comment.content, 'author': comment.author} for comment in comments])

    @app.route('/posts/<int:post_id>/comments', methods=['POST'])
    def create_comment(post_id):
        post = Post.query.get_or_404(post_id)
        if not request.json or not 'content' in request.json or not 'author' in request.json:
            abort(400)
        comment = Comment(content=request.json['content'], author=request.json['author'], post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        return jsonify({'id': comment.id}), 201
    
    @app.route('/')
    def index():
        return render_template('index.html')


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
