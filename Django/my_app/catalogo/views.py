from django.shortcuts import render
from catalogo.models import BlogPost

# Create your views here.
def blog_list(request):

    blog = BlogPost.objects.all()
    context_catalogo_blogs = {
        'blog_posts': blog
    }

    return render(request, 'catalogo/blog_list.html', context_catalogo_blogs)

