from flask import request, url_for, render_template, flash, redirect, current_app
from flask_login import login_required, current_user

from app import db
from app.main import bp
from app.main.forms import BookForm
from app.models import Book


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    books = Book.query.filter_by(user_id=current_user.id).paginate(page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=books.next_num) if books.has_next else None
    prev_url = url_for('main.index', page=books.prev_num) if books.has_prev else None
    return render_template('index.html', title='Home', books=books.items, next_url=next_url, prev_url=prev_url)


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
    return render_template('book_add.html', title='Register', form=form)
