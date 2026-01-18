from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import BlogPost

# Create your views here.
def blog_list(request):

    blog = BlogPost.objects.all().order_by('id')

    paginator = Paginator(blog, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context_catalogo_blogs = {
        'blog_posts': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'catalogo/blog_list.html', context_catalogo_blogs)

