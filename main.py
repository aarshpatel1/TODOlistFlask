from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import datetime

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
class Todos(db.Model):
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


@app.route("/", methods=["GET", "POST"])
def home():
    all_todos = db.session.execute(db.select(Todos)).scalars().all()
    form = AddTodo()
    if form.validate_on_submit():
        new_todo = Todos(
            todo=form.todo.data,
            description="",
            date=datetime.now().strftime("%d-%m-%Y"),
            time=datetime.now().strftime("%H:%M:%S")
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("todo.html", form=form, todos=all_todos)


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    delete = db.get_or_404(Todos, todo_id)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
