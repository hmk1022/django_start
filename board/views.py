# from django.shortcuts import render

# def index(request):
#     context = {
#         'title': 'Board list',
#         'board_list': [
#             {'no':1, 'title': '목록1' },
#             {'no':2, 'title': '목록2' },
#             {'no':3, 'title': '목록3' },
#             {'no':4, 'title': '목록4' },
#             {'no':5, 'title': '목록5' }
#         ]
#     }
#     return render(request, 'board/index.html', context)
# index: 게시글 목록

# detail: 게시글 제목 선택 시 상세 페이지 이동

# write: 게시글 목록에서 "글쓰기" 버튼 클릭 시 쓰기 페이지 이동

# write_board: 쓰기 페이지에서 새로운 글을 등록 시에 submit 처리 

# create_reply: 상세 페이지에서 댓글 등록 시에 submit 처리

# POST 데이터 전송(저장) 후 HttpResponseRedirect 를 사용하여 사용자가 뒤로 가기를 했을때 두번 POST 전송 처리 되지 않게 한다.


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.db import connection

from .models import Board

def index(request):
    all_boards = Board.objects.all().order_by("-pub_date") # 모든 데이터 조회, 내림차순(-표시) 조회
    return render(request, 'board/index.html', {'title':'Board List', 'board_list':all_boards})

# def detail(request, board_id):
#     board = Board.objects.get(id=board_id)
#     return render(request, 'board/detail.html', {'board': board})

def detail(request, board_id):
    # book1 = get_object_or_404(Book, code=code)
    # book2 = Book.objects.get(code=code)

    try:
        cursor = connection.cursor()

        strSql = "SELECT b.hp, b.age, CASE WHEN b.sex = '01'THEN '남성'WHEN b.sex = '02'THEN '여성' ELSE '성별을 알 수 없음' END as sex, b.pub_date, a.name FROM board_board b LEFT JOIN (SELECT code, name from author) a on a.code = b.author WHERE id = (%s)"
        result = cursor.execute(strSql, (board_id,))
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        board = {'hp': datas[0][0],
                'age': datas[0][1],
                'sex': datas[0][2],
                'pub_date': datas[0][3],
                'name': datas[0][4]}

    except:
        connection.rollback()
        print("Failed selecting in BookListView")


    return render(request, 'board/detail.html', {'board': board})

def write(request):
    return render(request, 'board/write.html')

def write_board(request):
    b = Board(hp=request.POST['hp'], sex=request.POST['sex'], age=request.POST['age'], author=request.POST['author'], pub_date=timezone.now())
    b.save()
    return HttpResponseRedirect(reverse('board:index'))

# def create_reply(request, board_id):
#     b = Board.objects.get(id = board_id)
#     b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
#     return HttpResponseRedirect(reverse('board:detail', args=(board_id,)))    