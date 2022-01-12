from django.db import models

# 블로그 게시불 정보 1개를 저장할 객체
class Post(models.Model):
    # 게시불 제목을 저장할 속성
    # CharField: 글자 수의 제한이 있는 문자열\
    # max_length = 300: 글자 수는 300 글자까지 저장
    title = models.CharField(max_length=30)

    writer = models.CharField(max_length=30)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[id=" + str(self.id) + ",title=" + self.title+ ",writer=" + self.writer + ", content=" + self.content + ",created_at=" + str(self.created_at)+"]"
