from django.shortcuts import render
from catalogo.models import BlogPost
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def buscador_posts(request):
    query = request.GET.get('q', '')

    resultados = BlogPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).order_by('id')

    paginator = Paginator(resultados,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'blog_posts': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'buscador/buscador_posts.html', context)