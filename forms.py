from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField
from wtforms.validators import Length, NumberRange, InputRequired, Email


class RecordForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired("Name required"),
                                           Length(min=2, max=25, message="Name must be between 2 and 25 characters")])
    email = EmailField('Email', validators=[InputRequired("Email required")])
    phone = StringField('Phone Number', validators=[InputRequired("Phone Number required"),
                                                    Length(min=7, max=10, message="Phone Number must be between 7 and 10 characters")])
    address = StringField('Address', validators=[InputRequired("Address required"),
                                                 Length(min=7, max=64, message="Address must be between 7 and 64 characters")])
    submit = SubmitField('Submit')


class RemoveRecordForm(FlaskForm):
    phone = StringField('Phone', validators=[InputRequired("Phone Number required")])
    submit = SubmitField('Submit')


class UpdateRecordForm(FlaskForm):
    id = IntegerField('ID', validators=[InputRequired("ID required"), NumberRange(min=1)])
    name = StringField('Name', validators=[InputRequired("Name required"),
                                           Length(min=2, max=25, message="Name must be between 2 and 25 characters")])
    email = EmailField('Email', validators=[InputRequired("Email required")])
    phone = StringField('Phone Number', validators=[InputRequired("Phone Number required"),
                                                    Length(min=7, max=10,
                                                           message="Phone Number must be between 7 and 10 characters")])
    address = StringField('Address', validators=[InputRequired("Address required"),
                                                 Length(min=7, max=64,
                                                        message="Address must be between 7 and 64 characters")])
    submit = SubmitField('Submit')
