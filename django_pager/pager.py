# coding: utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(queryset, page, per_page, reverse=False):
    paginator = Paginator(queryset, per_page)
    
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    objects.page_ranges = get_page_ranges(objects.number, objects.paginator.num_pages)
    if reverse:
        objects.page_ranges.reverse()
        for r in objects.page_ranges:
            r.reverse()
    return objects

def get_page_ranges(page, num_pages):
    if num_pages <=11:
        return [range(1, num_page+1)]
    elif page <=6:
        return [range(1, 8+1), range(num_pages-2, num_pages+1)]
    elif page > num_pages-6:
        return [range(1, 3+1), range(num_pages-7, num_pages+1)]
    else:
        return [range(1, 3+1), range(page-2, page+2+1), range(num_pages-2, num_pages+1)]

