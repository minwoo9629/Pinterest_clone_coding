from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp import views

app_name = "accountapp"
urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create/', views.AccountCreateView.as_view(), name="create"),
    path('detail/<int:pk>', views.AccountDetailView.as_view(), name="detail"),
    path('update/<int:pk>', views.AccountUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', views.AccountDeleteView.as_view(), name="delete"),
]