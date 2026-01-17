from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    # Usamos DateField para coincidir con tu formato YYYY-MM-DD
    date = models.DateField(verbose_name="Fecha de publicación")
    content = models.TextField(verbose_name="Contenido o Resumen")
    url = models.URLField(max_length=500, verbose_name="Enlace externo")
    # Añadimos imagen opcional para que la UI de Bootstrap brille
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL de Imagen", default="logo.png" )

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-date'] # Los más recientes primero por defecto

    def __str__(self):
        return self.title