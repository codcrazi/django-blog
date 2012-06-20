from posts.models import *
from django.contrib import admin

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)





