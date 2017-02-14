"""
Admin file for the blog!
"""


from django.contrib import admin
from .models import Post


admin.site.register(Post)
