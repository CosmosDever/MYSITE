from django.shortcuts import render

# Create your views here.
def landing_page(request):
    # Template is resolved via app directories; no need to include the full path
    return render(request, 'main/landing.html')