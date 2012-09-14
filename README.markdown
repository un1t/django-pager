# django-pager

Pagination.

## Installation
    
    pip install django-pager

## Configuration

settings.py

    INSTALLED_APPS = (
        ...
        'django_pager',
    )



## Usage 

views.py

from django_pager import paginate

def listing(request):
    qs = Contact.objects.all()
    page = request.GET.get('page', 1)
    contacts = paginate(qs, page, 10)
    return render_to_response('list.html', {"contacts": contacts})


list.html
    
    {% include 'django_pager/pager.html' with objects=contacts %}





