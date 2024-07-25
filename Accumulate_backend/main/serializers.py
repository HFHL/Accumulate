from rest_framework import serializers
from .models import User, Word, Sentence


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'user', 'english_word', 'chinese_translation', 'date']


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['id', 'user', 'english_sentence', 'chinese_sentence', 'date']
