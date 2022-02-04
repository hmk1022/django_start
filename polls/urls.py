from django.urls import path

from . import views
## 컨트롤러 소스? 서비스?
# http://127.0.0.1:8000/polls로 요청이 오면 views 내부에 index와 연결
urlpatterns = [
    path('', views.index, name='index'),
]
