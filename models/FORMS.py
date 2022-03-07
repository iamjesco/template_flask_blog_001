from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired('Please enter title')])
	body = TextAreaField('Body', validators=[DataRequired('Please enter content')])





