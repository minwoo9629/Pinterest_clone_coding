from django.urls import path
from subscribeapp import views
app_name = 'subscribeapp'

urlpatterns =[
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
]