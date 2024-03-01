from django.contrib import admin
from django.urls import path,re_path
from app.views import home, todos,todos_by_status,values,exludes,exludes_f

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('todos/<int:user_id>/', todos, name='todos'),
    path(r'^todos/(?P<status>[CPD])/$', todos_by_status, name='todos_by_status'), #маршрут с регулярным выражением
    path('values/', values, name='values'),    #вывод часть колонок из таблицы
    path('exludes/', exludes, name='exludes'), #исключения по полу
    path('exludes_f/', exludes_f, name='exludes_f'),
]
