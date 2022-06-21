from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_required, current_user
from .models import Task
from . import db
import random
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        task = request.form.get("task_py")
        new_task = Task(data=task, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added!", category="success")
    tasks = []
    for i in current_user.tasks:
        tasks.append([i.data, i.id, str(i.done)])
    new_task = Task(data="Temp", user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    start = new_task.id
    db.session.delete(new_task)
    db.session.commit()
    print(start)
    return render_template("home.html", user=current_user, tasks=tasks, start=start)


@views.route("/delete-task", methods=["POST"])
@login_required
def delete_task():
    taskID = request.form.get("taskID_py")
    task = Task.query.get(taskID)
    if task:
        db.session.delete(task)
        db.session.commit()
    return jsonify({})


@views.route("/do-task", methods=["POST"])
@login_required
def do_task():
    taskID = request.form.get("taskID_py")
    task = Task.query.get(taskID)
    if request.form.get("done") == "done":
        task.done = True
        db.session.commit()
    else:
        task.done = False
        db.session.commit()
    return jsonify({})


@views.route("/learn-latin", methods=["GET", "POST"])
@login_required
def learn_latin():
    return render_template("learn_latin.html", user=current_user)
