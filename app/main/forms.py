from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    title = StringField('Title of Your Blog Post', validators=[Required()])
    description = TextAreaField('Type in Your Blog Description', render_kw={'class': 'form-control', 'rows': 5},
                                validators=[Required()])
    submit = SubmitField('Add a Blog Post', render_kw={'class': 'btn btn-primary'})