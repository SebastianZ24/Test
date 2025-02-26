from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import Note, User
import json
#failas skirtas route

views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        elif len(note) >100:
            flash('Note is too long!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
        note = json.loads(request.data)
        noteId = note['noteId']
        note = Note.query.get(noteId)
        if note:
            if note.user_id==current_user.id:
                db.session.delete(note)
                db.session.commit()

        return jsonify({})

