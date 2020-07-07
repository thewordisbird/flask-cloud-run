from flask import Blueprint, render_template, request, redirect, url_for, \
    jsonify

from .forms import SearchForm, ContactInfoForm

from app import firebase

firestore = firebase.firestore()

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    results = firestore.get_collection("contacts")
    return render_template('index.html', results=results)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    form = ContactInfoForm()
    print(form.data)
    print(form.validate())
    print(form.errors)
    if form.validate_on_submit():
        form_data = {
            'name': form.data['name'],
            'phone': form.data['phone'],
            'email': form.data['email']
        }
        firestore.set_document_without_id("contacts", form_data)
        return redirect(url_for('main.index'))    
    return render_template('input_form.html', form=form)

@bp.route('/update/<contact_id>', methods=['POST', 'GET'])
def update(contact_id):
    contact = firestore.get_document(f"contacts/{contact_id}")
    
    form = ContactInfoForm(data=contact)

    if form.validate_on_submit():
        update_data = {
            'name': form.data['name'],
            'phone': form.data['phone'],
            'email': form.data['email']
        }
        firestore.update_document(f"contacts/{contact_id}", update_data)
        return redirect(url_for('main.index'))
    return render_template('input_form.html', form=form)


@bp.route('/delete', methods=['POST'])
def delete():
    req_data = request.get_json()
    contact_id = req_data['contactId']

    firestore.delete_document(f"contacts/{contact_id}")
    
    resp = jsonify({"status": "success"})
    return resp


