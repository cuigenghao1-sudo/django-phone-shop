from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Магазин смартфонов</h1><p>Главная страница магазина.</p>")


def phones(request):
    return HttpResponse("<h1>Каталог смартфонов</h1><p>Список доступных смартфонов.</p>")


def phone_detail(request):
    return HttpResponse("<h1>Информация о смартфоне</h1><p>Подробная информация о выбранном смартфоне.</p>")


def about(request):
    return HttpResponse("<h1>О магазине</h1><p>Информация о магазине смартфонов.</p>")


def contacts(request):
    return HttpResponse("<h1>Контакты</h1><p>Контактная информация магазина.</p>")