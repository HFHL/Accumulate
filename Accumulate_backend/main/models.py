from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 添加related_name参数来解决冲突
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="user_perm",
    )


class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words')
    english_word = models.CharField(max_length=100)
    chinese_translation = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_word} - {self.chinese_translation}"


class Sentence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentences')
    english_sentence = models.TextField()
    chinese_sentence = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_sentence} / {self.chinese_sentence}"
