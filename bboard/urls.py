from django.urls import path

from .views import index, by_rubric

from .views import BbCreateView

from .views import api_rubrics

from .views import api_rubric_detail
urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('api/rubrics/', api_rubrics),
    path('api/rubrics/<int:pk>/', api_rubric_detail),
    path('', index, name='index'),
]
