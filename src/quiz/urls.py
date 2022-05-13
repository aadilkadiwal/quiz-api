from django.urls import path
from rest_framework import routers
from . import api as quiz_api
from . import views as quiz_view

router = routers.DefaultRouter()

router.register('categorys', quiz_api.CategoryModelViewSet, basename='categorys')
router.register('questions', quiz_api.QuestionModelViewSet, basename='questions')
router.register('answers', quiz_api.AnswerModelViewSet, basename='answer')

urlpatterns = [
    path('', quiz_view.dashboard, name='home-page'),
]
