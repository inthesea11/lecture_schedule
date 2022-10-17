from django.urls import path
from .views import SubjectListView, SubjectCreateView, SubjectDetailView, SubjectUpdateView, SubjectDeleteView

urlpatterns = [
    path('', SubjectListView.as_view(), name='list'),
    path('add/', SubjectCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', SubjectDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', SubjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='delete'),
]