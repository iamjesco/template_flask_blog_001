from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models.FORMS import PostForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blogdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "srh834jty3wre98()763k7"
db = SQLAlchemy(app)

from models.DATABASE import Post


@app.route('/')
def home():
	return render_template('views/home.html')


@app.route('/blog-feed/', methods=["GET", "POST"])
def blog_feed():
	all_posts = Post.query.all()
	return render_template('views/blog-feed.html', all_posts=all_posts)


@app.route('/blog-post/<int:pk>')
def blog_post(pk):
	return render_template('views/blog-post.html')


@app.route('/dashboard/', methods=["GET", "POST"])
def dashboard():
	form = PostForm()
	if form.validate_on_submit():
		title = request.form.get('title')
		body = request.form.get('body')
		form_data = Post(title=title, body=body)
		db.session.add(form_data)
		db.session.commit()
		return redirect(url_for('dashboard'))
	return render_template('views/dashboard.html', form=form)


if __name__ == '__main__':
	app.run()
