from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('views/home.html')


@app.route('/blog-feed/', methods=["GET", "POST"])
def blog_feed():
	return render_template('views/blog-feed.html')


@app.route('/blog-post/<int:pk>')
def blog_post(pk):
	return render_template('views/blog-post.html')


@app.route('/dashboard/', methods=["GET", "POST"])
def dashboard():
	return render_template('views/dashboard.html')


if __name__ == '__main__':
	app.run()
