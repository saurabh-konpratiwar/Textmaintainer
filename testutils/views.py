#i have created this file - saurabh
from django.http import *
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    return HttpResponse("hello welcome")
def about(request):
    return HttpResponse("i am sponsor")
#def file(request):
 #   f1 = open("mydata", 'r')
  #  a = f1.read()
   # return HttpResponse("jai shri ram "+a)

def analyze(request):
    #get data from index.html file
    analyzetxt = request.POST.get('analyzetext','default')
    Removepunc = request.POST.get('Removepunc','off')
    capfirst = request.POST.get('capfirst','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    print(analyzetxt,Removepunc,capfirst,newlineremove,spaceremove,charcount)
    analyzeds = ""
    panctuation = '''"’+^'()[]{}<>:,‒–—―…!.«»-‐?‘$’“”;/⁄␠·&@*\\•†‡°¡¿¬#№%‰‱¶′§¨_|¦⁂☞∴‽※'''

    if Removepunc == "on":
        for char in analyzetxt:
            if char not in panctuation:
                analyzeds = analyzeds + char
                param = {'analyzed':analyzeds}
                print(analyzeds)
        return render(request, 'analyze.html', param)

    if capfirst == "on":
        for char in analyzetxt:
            analyzeds = analyzeds + char.upper()
            param = {'analyzed':analyzeds}
            print(analyzeds)
        return render(request, 'analyze.html', param)



    if newlineremove == "on":
        for char in analyzetxt:
            if char != "\n":
                analyzeds = analyzeds + char.upper()
                param = {'analyzed':analyzeds}
                print(analyzeds)
        return render(request, 'analyze.html', param)

    if spaceremove == "on":
        for index,char in enumerate(analyzetxt):
            if analyzetxt[index] == " " and analyzetxt[index+1] == " ":
                pass
            else:
                analyzeds = analyzeds + char
                param = {'analyzed': analyzeds}
                print(analyzeds)
        return render(request, 'analyze.html', param)

    if charcount == "on":
        for index,char in enumerate(analyzetxt):
            analyzeds = index+1
            param = {'analyzed': analyzeds}
        return render(request,'analyze.html',param)


'''def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("removepunc "+request.GET.get('text','default'))
def capfirst(request):
    return HttpResponse("capfirst")
def newlineremove(request):
    return HttpResponse("newlineremove")
def spaceremove(request):
    return HttpResponse("spaceremove")
def charcount(request):
    return HttpResponse("charcount")'''


