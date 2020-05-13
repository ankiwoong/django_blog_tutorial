from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)        # 제목(최대 길이 200)
    pub_date = models.DateTimeField()               # 작성일
    text = models.TextField()                       # 본문내용
    # slug : URL의 구성요소로 웹사이트의 특정 페이지를 가리키는 사람이 읽기 쉬운 형식의 식별자
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):                              # 객체의 제목을 반환
        return self.title
