from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError


class BookForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    purchased = DateField('Purchase Date', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save Book')

    def validate_purchased(self, purchased):
        today = datetime.today().date()
        if today < purchased.data:
            raise ValidationError("Purchased date can't be in the future")


class ShareBookForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Share Library')
