from django.db import models
from core.models import AbstractBaseSet

class Category(AbstractBaseSet):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='category', default='defaultcategory.jpg')

    def __str__(self):
        return self.name

class Question(AbstractBaseSet):
    class Difficulty(models.TextChoices):
        BEGINNER = "BEGINNER"
        INTERMEDIATE = "INTERMEDIATE"
        ADVANCE = "ADVANCE"
        EXPERT = "EXPERT"

    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    level = models.CharField(choices=Difficulty.choices, max_length=12)

    def __str__(self):
        return self.question

class Answer(AbstractBaseSet):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_right = models.BooleanField(default=False)