from flask import Blueprint, render_template, abort
from LearnMappings import Grade3Mapper

learn_bp = Blueprint('learn', __name__)

@learn_bp.route('/Learn')
def learn_index():
    return render_template('LearnPage.html', section='content')

@learn_bp.route('/Learn/Primary_Grade_3_Mathematics')
def p3_notes():
    return render_template('Notes/P3_Notes.html', section='content')

@learn_bp.route('/Learn/Primary_Grade_4_Mathematics')
def p4_notes():
    return render_template('Notes/P4_Notes.html', section='content')

@learn_bp.route('/Learn/Primary_Grade_5_Mathematics')
def p5_notes():
    return render_template('Notes/P5_Notes.html', section='content')

@learn_bp.route('/Learn/Primary_Grade_6_Mathematics')
def p6_notes():
    return render_template('Notes/P6_Notes.html', section='content')

@learn_bp.route('/Learn/Primary-Grade-3/<topic>/<subtopic>')
@learn_bp.route('/Learn/Primary-Grade-3/<subtopic>', defaults={'topic': ''})
def primary3_dynamic(subtopic: str, topic: str):
    try:
        filename, data = Grade3Mapper.getMapping(subtopic, topic=topic)
    except KeyError:
        abort(404)
    return render_template('Notes/Primary3' + filename, **data)
