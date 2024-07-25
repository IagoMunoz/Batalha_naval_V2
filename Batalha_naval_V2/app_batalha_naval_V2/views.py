from django.shortcuts import render

def home(request):
    return render(request, 'https://iagomunoz.github.io/Batalha_naval_V2/login.html')

