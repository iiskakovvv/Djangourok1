from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def contact(request):
    a = """<h1><center>Name: Adi Number</center></h1>
     <h2><center>+77778815252</center></h2>
     <h2><center><a href = 'https://github.com/iiskakovvv'>Githab</a></center> </h2>
     <h2><center><a href ='https://www.instagram.com/iiskakovvv/'>Instagram</a></center> </h2>
    
     
    """
    return HttpResponse(a)
def info(request):
    a = """<h1>Зомби-эпидемия захлестнула планету. 
    Шериф Рик Граймс путешествует с семьей и небольшой группой выживших в поисках безопасного места.
    Но постоянный страх смерти каждый день приносит тяжелые потери, заставляя товарищей по несчастью чувствовать глубины человеческой жестокости. Рик пытается спасти близких и понимает, что всепоглощающий страх людей может быть опаснее ходячих мертвецов.</h1>
    """
    return HttpResponse(a)