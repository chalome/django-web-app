from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.models import Band
# Create your views here.

def hello(request):
    bands=Band.objects.all()
    # return HttpResponse("<center><h1 style='color:green'>Hello world,this is Django<h1/><br><img src='../merchex/pic.jpg'></center>")
    # return HttpResponse(f"""<center><h1 style='color:green'>Hello world,this is Django<h1/><br>
    #                     <h1> my favorites Bands are:<h1><br>
    #                     <ul>
    #                    <li>{bands[0].name}</li>
    #                    <li>{bands[1].name}</li>
    #                    <li>{bands[2].name}</li>
    #                     </ul>
    #                     """)
    return render(request,'listings/hello.html',{'bands':bands})


def about(request):
    
    return render(request,'listings/about.html')


    
