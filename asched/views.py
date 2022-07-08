from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def mainpage(request):
   return render(request,'mainpage.html')

def Commissioning(request):
   if request.method =="POST":
         cl_surname = request.POST['cl_surname']
         cl_firstname = request.POST['cl_firstname']   
         cl_middlename = request.POST['cl_middlename']   
         cl_email = request.POST['cl_email']   
         cl_contact = request.POST['cl_contact'] 
         item = clientbasicinfo(cl_surname = cl_surname,
         cl_firstname = cl_firstname,
         cl_middlename = cl_middlename,
         cl_email = cl_email,
         cl_contact = cl_contact,
         )
         item.save()

   else:
      return render(request,'commission.html')
   itemone = clientbasicinfo.objects.all()
   return render(request,'commission.html',{'itemone':itemone})

#edit#

def edit(request,biid):
   item= clientbasicinfo.objects.get(id = biid)
   itemone = clientbasicinfo.objects.all()
   return render(request,'commission.html',{'item':item,
      'itemone':itemone,
      })

#update#
def update(request,biid):
    itemone = clientbasicinfo.objects.get(id=biid)
    itemone.cl_surname = request.POST['cl_surname']
    itemone.cl_firstname = request.POST['cl_firstname']
    itemone.cl_middlename = request.POST['cl_middlename']
    itemone.cl_email = request.POST['cl_email']
    itemone.cl_contact = request.POST['cl_contact']

    itemone.save()
    return redirect('mainpage')


#delete#
def Delete_BasicInfo(request,biid):
   item = clientbasicinfo.objects.get(id=biid)
   item.delete()
   return render(request,'commission.html')


def clientInfo(request):
   itemone = clientbasicinfo.objects.all()
   return render(request,'basic_info.html',{'itemone':itemone})


def authorInfo(request):
   return render(request, 'authorinfo.html')


def porartstyle(request):
   if request.method =="POST":
         shot = request.POST['shot']
         shot_price = request.POST['shot_price']
         art= request.POST['art']
         art_price = request.POST['art_price']
         color = request.POST['color']
         color_price = request.POST['color_price']
         sizes = request.POST['sizes']
         size_price = request.POST['size_price']
         item = portraitshot(shot = shot,
         shot_price = shot_price,
         art = art,
         art_price = art_price,
         color = color,
         color_price = color_price,
         sizes = sizes,
         size_price = size_price,
         )
         item.save()
   else:
      return render(request,'artstyle.html')
   itemthree = portraitshot.objects.all()
   return render(request,'artstyle.html',{'itemthree':itemthree})

def comsTwo(request):
   if request.method =="POST":
         currentdatetime = request.POST['currentdatetime']
         fileformat = request.POST['fileformat']
         background = request.POST['background']
         item = clientattribute(currentdatetime = currentdatetime,
         fileformat = fileformat,
         background = background,
         )
         item.save()
   else:
      return render(request, 'comstwo.html')
   itemtwo = clientattribute.objects.all()
   return render(request,'comstwo.html',{'itemtwo':itemtwo})

   

