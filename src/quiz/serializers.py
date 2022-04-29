from rest_framework import serializers
from . import models as quiz_models

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Category
        fields = ['name',]

class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=50)

    class Meta:
        model = quiz_models.Question
        fields = ['category', 'question', 'level',]

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=500)

    class Meta:
        model = quiz_models.Answer
        fields = ['question', 'answer', 'is_right',]                 