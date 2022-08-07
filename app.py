import os
from flask import Flask, render_template, flash
from forms import RecordForm, RemoveRecordForm, UpdateRecordForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'securityKey'
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# define our models
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(64), nullable=False)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = RecordForm()
    if form.validate_on_submit():
        record = Record.query.filter_by(name=form.name.data).first()
        if record is None:
            record = Record(name=form.name.data,
                            email=form.email.data,
                            phone=form.phone.data,
                            address=form.address.data)
            db.session.add(record)
            db.session.commit()

            name = form.name.data
            form.name.data = ''
            form.email.data = ''
            form.phone.data = ''
            form.address.data = ''
            flash(name + "'s record was successfully submitted")
        else:
            flash('Student\'s grade was already submitted')

    return render_template('add.html', form=form)


@app.route('/view')
def view():
    records = Record.query.all()
    return render_template('view.html', records=records)


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    remove_form = RemoveRecordForm()
    if remove_form.validate_on_submit():
        record = Record.query.filter_by(phone=remove_form.phone.data).first()
        name = record.name
        Record.query.filter_by(phone=remove_form.phone.data).delete()
        db.session.commit()

        flash(name + "'s record was successfully removed!")
    return render_template('remove.html', remove_form=remove_form)

@app.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateRecordForm()
    if form.validate_on_submit():
        record = Record.query.filter_by(id=form.id.data).first()
        record.name = form.name.data
        record.phone = form.phone.data
        record.email = form.email.data
        record.address = form.address.data
        db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.phone.data = ''
        form.email.data = ''
        form.address.data = ''
        flash(name + "'s record has been updated")

    return render_template('update.html', form=form)


if __name__ == '__main__':
    app.run()
