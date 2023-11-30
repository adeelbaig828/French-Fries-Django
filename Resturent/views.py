from django.shortcuts import render



def HandlePageNotFound404(request,exception,template_name="404.html"):
    return render(request,template_name)

def Page404(request):
    return render(request,"404.html")