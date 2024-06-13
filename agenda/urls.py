from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('submit/', views.TalkSubmitView.as_view(), name='talks-submit'),
    path('edit/<int:pk>/', views.TalkEditView.as_view(), name='talks-edit'),
    path('', views.TalkListView.as_view(), name='talks-list'),
    path('<int:pk>/', views.TalkDetailView.as_view(), name='talks-detail'),
]
