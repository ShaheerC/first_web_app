from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('/home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')

def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio(request):
    image_urls = []
    for i in range (5):
        random_number = randint(0, 100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me(request):
    skill_list = ['HTML','CSS','Python','Django','JavaScript','NodeJS']
    interest_list = ['Reading','Gaming','Sci Fi','Eating','MMA']
    context = {'Skills': skill_list, 'Interests': interest_list}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites(request):
    fav_links = ['Google']
    context = {'Favourites': fav_links}
    response = render(request, 'fav_links.html', context)
    return HttpResponse(response)