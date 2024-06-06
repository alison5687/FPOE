from django.contrib import admin
from .models.post import Post
from .models.hilo import Hilo
admin.site.register(Post)
admin.site.register(Hilo)