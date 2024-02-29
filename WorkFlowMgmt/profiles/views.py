from django.shortcuts import render


def main_page(request):
    return render(request, 'profiles/main_page.html')