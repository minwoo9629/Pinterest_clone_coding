from django.urls import path
from projectapp import views
app_name = "projectapp"

urlpatterns = [
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='detail'),
    path('list/', views.ProjectListView.as_view(), name='list'),
]

