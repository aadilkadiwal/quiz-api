from rest_framework import serializers
from . import models as quiz_models

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Category
        fields = ['name', 'description', 'image']

class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=50)

    def create(self, validated_data):
        category_name = validated_data.pop("category")
        category_id = quiz_models.Category.objects.get(name=category_name)
        return super().create({**validated_data, "category": category_id})    

    class Meta:
        model = quiz_models.Question
        fields = ['category', 'question', 'level']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = quiz_models.Answer
        fields = ['question', 'answer', 'is_right']                 