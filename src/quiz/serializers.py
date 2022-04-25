from rest_framework import serializers
from . import models as quiz_model

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_model.Category
        field = ['name',]

class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=50)

    class Meta:
        model = quiz_model.Question
        field = ['category', 'question', 'level',]

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(max_length=500)

    class Meta:
        model = quiz_model.Answer
        field = ['question', 'answer', 'is_right',]                 