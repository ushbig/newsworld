from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import  ForeignKey, Integer,String ,Column
from os import environ

app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    __tablename__ = "blogpost"
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)
    Author = db.Column(db.String(20), nullable=False) 

    def __repr__(self):
        return 'Blogpost' +  str(self.id)



@app.route('/')
def hello():
    return "hello world"
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method =='POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['Author']
        new_post = BlogPost(title = post_title, content= post_content, Author= post_author )
        db.session.add(new_post)
        db.session.commit()
        
        return redirect('/posts')
    else:
        all_posts= BlogPost.query.all( )
    return render_template('post.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.Author = request.form['Author']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html' , post =post)

@app.route('/posts/new', methods=['GET','POST'])
def new_post():
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.Author = request.form['Author']
        new_post = BlogPost(title =post_title, content=post_content, Author=post_author )
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html' )
if __name__ == "__main__":
    app.run(debug= True)
    