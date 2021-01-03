from django.urls import path
from profileapp import views
app_name = "profileapp"

urlpatterns = [
    path('create/', views.ProfileCreationView.as_view(), name='create'),
    path('update/<int:pk>', views.ProfileUpdateView.as_view(), name='update'),
]

