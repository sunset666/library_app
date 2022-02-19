from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    purchased = DateField('Purchase Date', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Book')
