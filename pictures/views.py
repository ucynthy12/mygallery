from django.shortcuts import render,redirect
from .models import Image,Location,Category
# Create your views here.

def pictures(request):
    album = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'all-photos/album.html',{'album':album,'locations':locations})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(name=location)
    album = Image.objects.filter(location=selected_location.id)
    return render(request,'all-photos/location.html',{'location':selected_location,'locations':locations,'album':album})
    
def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        category = request.GET.get("photos")
        searched_photos = Image.search_image(category)
        message = f"{category}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_photos})

    else:
        message = "You haven't searched for any image in this category"
        return render(request, 'all-photos/search.html', {"message": message})
        

