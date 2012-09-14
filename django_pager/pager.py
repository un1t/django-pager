# coding: utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(queryset, page, per_page):
    paginator = Paginator(queryset, per_page)
    
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    
    return objects
