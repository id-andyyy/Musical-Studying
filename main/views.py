from django.shortcuts import render


def main(request):
    return render(request, 'main/main_page.html', {'title': 'Главная'})
