from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thequickfoxjumpoverthecrazydog.'
bootstrap = Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    todo: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    time: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250))


# CREATE TABLE
with app.app_context():
    db.create_all()


class AddTodo(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired()])
    add_todo = SubmitField('Add')


@app.route("/")
def home():
    form = AddTodo()
    return render_template("todo.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
