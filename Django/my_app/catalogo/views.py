from django.shortcuts import render

# Create your views here.
def blog_list(request):
    blog = [
        {
            'title': 'Crear un entorno virtual en Python',
            'author': 'MGC',
            'date': '2022-01-15',
            'content': 'Contenido sobre como crear un entorno virtual en Python con windwos, linux y mac.',
            'url': 'https://misael-gomez-cuautle.super.site/blog-personal-1/projects/entorno-virtual-en-python'
        },
        {
            'title': 'Comandos básicos de Linux',
            'author': 'MGC',
            'date': '2025-12-20',
            'content': 'Comandos Linux del libro Linux Basic for Hackers.',
            'url': 'https://github.com/misaelgocu/cmd-linux'
        },
        {
            'title': 'Librerías o módulos en Python',
            'author': 'MGC',
            'date': '2024-03-10',
            'content': 'Forma de instalar librerías o módulos en Python usando pip.',
            'url': 'https://misael-gomez-cuautle.super.site/blog-personal-1/projects/libreras-o-mdulos-en-python'
        },
        {
            'title': 'Aprendiendo Django',
            'author': 'MGC',
            'date': '2024-06-05',
            'content': 'Proyecto de blog personal usando el framework Django.',
            'url': 'https://misael-gomez-cuautle.super.site/blog-personal-1/projects/aprendiendo-django'
        }
    ]

    context_catalogo_blogs = {
        'blog_posts': blog
    }

    return render(request, 'catalogo/blog_list.html', context_catalogo_blogs)

