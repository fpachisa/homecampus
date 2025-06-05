from flask import Blueprint, render_template, request, flash, redirect, url_for

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/Contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('first_name')
        comment = request.form.get('comment')
        email = request.form.get('email')
        # In a real application an email would be sent here
        print(f"Feedback from {name} <{email}>: {comment}")
        flash('Thank you for your feedback!!')
        return redirect(url_for('contact.contact'))
    return render_template('Contact.html')
