from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp import views

app_name = "accountapp"
urlpatterns = [
    path('', views.hello, name="hello"),
    path('create/', views.AccountCreateView.as_view(), name="create"),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('detail/<int:pk>', views.AccountDetailView.as_view(), name="detail"),
]