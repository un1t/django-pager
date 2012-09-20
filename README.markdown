# django-pager

Pagination. If you have many pages, only 11 will be shown. 
For example you have 100 pages. 

**1** 2 3 4 5 6 7 8 ... 98 99 100

1 2 3 ... 71 72 **73** 74 75 ... 98 99 100

1 2 3 ... 93 94 95 96 97 98 **99** 100

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
        return render('list.html', {"contacts": contacts})


list.html
    
    {% include 'django_pager/pager.html' with objects=contacts %}


### Run tests

    PYTHONPATH=. python django_pager/tests.py



