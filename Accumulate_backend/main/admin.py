from django.contrib import admin
from .models import User, Word, Sentence
# Register your models here.


admin.site.register(User)
admin.site.register(Word)
admin.site.register(Sentence)
