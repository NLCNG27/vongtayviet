from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, '../templates/home.html')

def contact_view(request):
    return render(request, '../templates/contact.html') 

def job_listing_view(request):
    return render(request, '../templates/job_listing.html')

