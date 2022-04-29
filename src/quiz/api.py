from rest_framework import viewsets
from . import serializers as quiz_serializers
from . import models as quiz_models

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = quiz_models.Category.objects.all()
    serializer_class = quiz_serializers.CategorySerializer

class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = quiz_models.Question.objects.all()
    serializer_class = quiz_serializers.QuestionSerializer    

class AnswerModelViewSet(viewsets.ModelViewSet):
    queryset = quiz_models.Answer.objects.all()
    serializer_class = quiz_serializers.AnswerSerializer    