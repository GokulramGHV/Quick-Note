from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
from datetime import datetime
#from sqlalchemy.sql import func


views = Blueprint('views', __name__)


@views.route('/notes', methods=['GET', 'POST'])
@login_required
def home():
    notes = Note.query.filter_by(user_id = current_user.id).order_by(Note.date.desc()).all()
    l = []
    for res in notes:
        l.append((res.data,str(res.date),res.id))
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id,date=datetime.utcnow() + timedelta(hours=5, minutes=30))
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("home.html", userNotes=l,count=len(l),text="none", user=current_user)


@views.route('/delete-note/<int:id>',methods=['GET','POST'])
def deleteNote(id):
    note = Note.query.get(id)
    if note:
        if note.user_id == current_user.id:
            print(note.data)
            db.session.delete(note)
            db.session.commit()
    
    return redirect(url_for('views.home'))


@views.route('/edit-note/<int:id>', methods=['GET','POST'])
def update(id):
    note = Note.query.get_or_404(id)

    if request.method == 'POST':
        note.data = request.form['note']
        note.date = datetime.utcnow() + timedelta(hours=5, minutes=30)

        try:
            db.session.commit()
            return redirect(url_for('views.home'))
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', text=note.data,user=current_user)
    
@views.route('/',methods=['GET','POST'])
def start_page():
    return render_template('start_page.html',user=current_user)

    


    