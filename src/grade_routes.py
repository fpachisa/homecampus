from flask import Blueprint, render_template

# Blueprint handling grade-level pages.
grade_bp = Blueprint('grade', __name__)


@grade_bp.route('/Primary_Grade_3_Mathematics')
def primary_grade_3():
    return render_template('Primary_Grade_3.html')


@grade_bp.route('/Primary_Grade_4_Mathematics')
def primary_grade_4():
    return render_template('Primary_Grade_4.html')


@grade_bp.route('/Primary_Grade_5_Mathematics')
def primary_grade_5():
    return render_template('Primary_Grade_5.html')


@grade_bp.route('/Primary_Grade_6_Mathematics')
@grade_bp.route('/PSLE')
def primary_grade_6():
    return render_template('Primary_Grade_6.html')


@grade_bp.route('/Secondary-1-Grade-7-Mathematics')
@grade_bp.route('/Secondary-1')
def secondary_1():
    return render_template('Grade-7/Grade-7.html')


@grade_bp.route('/Unfinished-Worksheets')
def unfinished_worksheets():
    # Placeholder implementation without database lookups.
    return render_template('Unfinished-Worksheets.html')
