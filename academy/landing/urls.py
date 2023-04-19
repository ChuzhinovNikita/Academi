from django.urls import path
from . import views

urlpatterns = [
    # path(route, view.name, url_name)
    # route - строка которая содержит url. Именно с ней маршрутизатор сапоставляет url с запроса
    # view - функция определённого route. Будет автоматически запущена если какойто из route подошел с url запроса
    # url_name - имя нашего route который необходимо использовать при создании ссылки, вместо указывания полного пути
    path('home/', views.home, name='home'),
    path('greeting/', views.greeting, name='greeting'),
    # создаём юрл 'course/<int:pk>' где pk - это уникальный идентификатор
    # важно чтобы параметр функции назывался точно так же как и в urls.py
    path('course/<int:pk>', views.course, name='course'),
    path('check_leads/', views.check_leads, name='check_leads'),
]