from django.conf import settings
from django.db import models
from django.utils import timezone

# class Post(models.Model): 모델(객체) 정의


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # def 함수/메서드 정의, publish 메소드 이름
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__ string 값을 되돌려 줌
    def __str__(self):
        return self.title
