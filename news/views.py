# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Article

from.forms import StartForm

def index(request):
    latest_article_list = Article.objects.order_by('created_date')[:10]

    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")
        hondurasian = request.POST.get("hondurasian")
        like_country_No_doubt = request.POST.get("like_country_No_doubt")
        love_Fun = request.POST.get("love_Fun")
        testForm = "Hello, {0}!".format(hondurasian) + \
                   " You are {0}".format(like_country_No_doubt) + \
                   " Our Friend, {0}".format(name) + \
                   ". You will get {0}".format(love_Fun) + \
                   " pleasure from Our Country and This website!"
        context = {'latest_article_list': latest_article_list, 'text': testForm}

        return render(request, 'news/index2.html', context)
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     # age = request.POST.get("age")
    #     hondurasian = request.POST.get("hondurasian")
    #     like_country_no_doubt = request.POST.get("like_country_no_doubt")
    #     # love_Fun = request.POST.get("love_Fun")
    #     testForm = "Welcome, Dear {0}".format(hondurasian) + " Friend, {0}".format(name)

    # elif request.method == "POST":
    #     name = request.POST.get("name")
    #     # age = request.POST.get("age")
    #     hondurasian = request.POST.get("hondurasian")
    #     like_country_no_doubt = request.POST.get("like_country_no_doubt"==False)
    #     # love_Fun = request.POST.get("love_Fun")
    #     testForm = "Puck you and your belongings, {0}".format(hondurasian) + "! And Get Out of here, {0}".format(name)

    else:
        testForm = StartForm()
        context = {'latest_article_list': latest_article_list, 'form': testForm}

        return render(request, 'news/index.html', context)



def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'news/detail.html', {'article': article})

def base_list(request):
    return render(request, "news/base_list.html", {'base_list': 'base_list'})

def navy(request):
    return render(request, "news/navy.html", {'navy': 'navy'})

def army(request):
    return render(request, "news/army.html", {'army': 'army'})

def airforce(request):
    return render(request, "news/airforce.html", {'airforce': 'airforce'})

def animals(request):
    return render(request, "news/animals.html", {'animals': 'animals'})

def one(request):
    list_leaders = {"drive": "Let to drive, Guys!", "happy": "Be happy!"}
    return render(request, "news/one.html", list_leaders)

def drive(request):
    yoyoyo = {}

def two(request):
    return render(request, "news/two.html", {'health': 'health'})

def three(request):
    return render(request, "news/three.html", {'culture': 'culture'})

def four(request):
    return render(request, "news/four.html", {'holiday': 'holiday'})

def five(request):
    totalLove = {"love": "Love each other!", "leaves":"And love leaves!"}
    return render(request, "news/five.html", totalLove)

def six(request):
    return render(request, "news/six.html", {'happy': 'happy'})

