from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)        # 제목(최대 길이 200)
    pub_date = models.DateTimeField()               # 작성일
    text = models.TextField()                       # 본문내용
    slug = models.SlugField(max_length=40, unique=True,
                            allow_unicode=True, null=True)

    def __str__(self):                              # 객체의 제목을 반환
        return self.title
