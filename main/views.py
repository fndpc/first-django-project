from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/main.html')
def water(request):
    return render(request, 'main/water.html')
def forests(request):
    return render(request, 'main/forests.html')
def deserts(request):
    return render(request, 'main/deserts.html')
