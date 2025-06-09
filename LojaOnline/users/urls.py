from django.urls import path
from .views import welcome, login, register
from .sql_services import testar_banco

urlpatterns = [
    path('', welcome, name="welcome"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('testar_bd/', testar_banco)
]
