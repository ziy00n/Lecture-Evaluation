from django.urls import path
from . import views

urlpatterns = [
    path("create_eval/<int:num>", views.create, name="create_eval"), # 강의평 작성하기
    path("delete_eval/<int:eval_id>", views.delete, name="delete_eval"), # 강의평 삭제하기
]