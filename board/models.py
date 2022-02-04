from django.db import models

class Board(models.Model):
    """
        board_no: 설문조사 번호
        addr: 사는곳
        sex: 성별
        author: 좋아하는 작가(다중 선택가능)
        create_date: 설문 조사일
    """
    board_no =  models.BigAutoField(primary_key= True)
    addr = models.CharField(max_length=100)
    sex = models.CharField(max_length=3)
    age = models.CharField(max_length=3)
    author = models.CharField(max_length=3)
    hp = models.CharField(max_length=20)
    ##like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.hp

# class Reply(models.Model):
#     """
#         reply: Reply -> Board 연결관계
#         comment: 댓글내용
#         rep_date: 작성일
#     """
#     reply = models.ForeignKey(Board, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=200)
#     rep_date = models.DateTimeField()

#     def __str__(self):
#         return self.comment