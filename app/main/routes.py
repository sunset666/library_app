from flask import request, url_for, render_template, flash, redirect, current_app
from flask_login import login_required, current_user

from app import db
from app.auth.email import send_email
from app.main import bp
from app.main.forms import BookForm, ShareBookForm
from app.models import Book


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    books = Book.query.filter_by(user_id=current_user.id)
    form = ShareBookForm()
    return render_template('index.html', title='Home', books=books, form=form)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data, purchased=form.purchased.data,
                    notes=form.notes.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        flash('Congratulations, you added a new book!')
        return redirect(url_for('main.index'))
    return render_template('main/book_add.html', title='Register', form=form)


@bp.route('/share', methods=['POST'])
@login_required
def share_library():
    form = ShareBookForm()
    if form.validate_on_submit():
        books = Book.query.filter_by(user_id=current_user.id)
        html = render_template('email/shared_library.html', books=books)
        subject = "%s has shared this library with you" % current_user
        send_email(subject=subject, sender=current_app.config['MAIL_SENDER'], recipients=[form.email.data],
                   html_body=html)
        flash('Congratulations, you shared your library with %s' % form.email.data)
    return redirect(url_for('main.index'))

