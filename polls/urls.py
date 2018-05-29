from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
	path('',views.IndexView.as_view(),name='index'), #e.g. /polls/
	path('<int:pk>/',views.DetailView.as_view(),name='detail'), #e.g. /polls/6/
	path('<int:pk>/results/',views.ResultsView.as_view(),name='results'), #e.g. /polls/6/results/
	path('<int:question_id>/vote/',views.vote,name='vote'), #e.g. /polls/6/vote/

]