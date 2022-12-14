from django.core.paginator import Paginator
from django.conf import settings


def page_content(query, request):
    paginator = Paginator(query, settings.POSTS_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'page_obj': page_obj,
    }
