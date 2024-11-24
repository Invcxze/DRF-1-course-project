from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('shop', include('shop.urls'))
]
