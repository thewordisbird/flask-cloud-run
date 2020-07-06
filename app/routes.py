from flask import Blueprint, render_template, request

from .forms import SearchForm

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    search = request.args.get('search', None)
    form = SearchForm(data={'search': search})
    
    data = [
        {
            'name': 'Justin Bird',
            'phone': '(818) 667-5884',
            'email': 'justin.h.bird@gmail.com'
        },
        {
            'name': 'Scott Dushane',
            'phone': '(818) 648-9298',
            'email': 'sdushane@gmail.com'
        }
    ]
    
    if search:
        results = [d for d in data if search in d['name']]
    else:
        results = None
    return render_template('index.html', form=form, results=results)