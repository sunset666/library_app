from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class BookForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    purchased = DateField('Purchase Date', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save Book')


class ShareBookForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Share Library')
