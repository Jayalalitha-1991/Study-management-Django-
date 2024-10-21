from django.urls import path
from .views import StudyListView, StudyCreateView, StudyUpdateView, StudyDeleteView, StudyDetailView

urlpatterns = [
    path('', StudyListView.as_view(), name='study-list'),
    path('create/', StudyCreateView.as_view(), name='study-create'),
    path('<int:pk>/update/', StudyUpdateView.as_view(), name='study-update'),
    path('<int:pk>/delete/', StudyDeleteView.as_view(), name='study-delete'),
    path('<int:pk>/view/', StudyDetailView.as_view(), name='study-detail'),

]