from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app.forms import LoginForm, RegistrationForm, BookForm
from app import app, db
from app.models import User, Book


@app.route('/')
@app.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    books = Book.query.filter_by(user_id=current_user.id).paginate(page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=books.next_num) if books.has_next else None
    prev_url = url_for('index', page=books.prev_num) if books.has_prev else None
    return render_template('index.html', title='Home', books=books.items, next_url=next_url, prev_url=prev_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data, purchased=form.purchased.data,
                    notes=form.notes.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        flash('Congratulations, you added a new book!')
        return redirect(url_for('index'))
    return render_template('book_add.html', title='Register', form=form)
