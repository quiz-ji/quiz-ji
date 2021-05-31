try:
    from django.conf.urls import url , path
except ImportError:
    from django.urls import re_path as url , path
from .views import *
urlpatterns = [

   
    path('createcategory',createcategory, name = 'createcategory'),
    path('admin/quiz/subcategory/add/',createsubcategory, name = 'createsubcategory'),
    path('createexam',addexam, name = 'createexam'),
    path('tfque',tfque, name = 'tfque'),
    path('mcque',mcque, name = 'mcque'),
    path('importquecsv',importquecsv, name = 'importquecsv'),
    path('importstudentcsv',importstudentcsv, name = 'importstudentcsv'),
    path('quizmarking/',view=QuizMarkingList.as_view(),name='quiz_marking'),
    path('quizlist/',view=QuizListView.as_view(),name='quiz_index'),
    path('progress/',view=QuizUserProgressView.as_view(),name='quiz_progress'),
    path('password/', change_password, name='change_password'),
    url(r'^(?P<slug>[\w-]+)/$',view=QuizDetailView.as_view(),name='quiz_start_page'),
    url(r'^(?P<quiz_name>[\w-]+)/take/$',view=QuizTake.as_view(),name='quiz_question'),
    url(r'^marking/(?P<pk>[\d.]+)/$',view=QuizMarkingDetail.as_view(),name='quiz_marking_detail'),






    path('quizmarking/',view=QuizMarkingList.as_view(),name='quiz_marking'),
  
]
