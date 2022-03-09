from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
	title = StringField('', validators=[DataRequired('Please enter title')], render_kw={"placeholder": "Title"})
	body = CKEditorField('', validators=[DataRequired('Please enter content')])
	category = SelectField('', validators=[DataRequired('Please choose a category')],
	                       choices=[('', 'Choose a category'), ('news', 'news'), ('tech', 'tech'), ('personal', 'personal')])





