from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Host,chatdata
from django.contrib import messages

def index(request):
    return render(request,"chatroom/home.html")

def hostregister(request):
    if request.method == "POST":
        if "hostname" in request.POST:
            username=request.POST["hostname"]
            hostname=request.POST["hostname"]
            roomcode=request.POST["roomcode"]
            host=Host(hostname=request.POST["hostname"],meetcode=request.POST["roomcode"])
            host.save()
            # print("host registered")
            return render(request,"chatroom/chatpage.html",{"username":username,"hostname":hostname,"roomcode":roomcode})
        
        if "username" in request.POST:
            if(Host.objects.filter(meetcode=request.POST["roomcode"]).exists()):
                username=request.POST["username"]
                roomcode=request.POST["roomcode"]
                if Host.objects.filter(hostname=username).exists():
                    hostname=request.POST["username"]
                    return render(request,"chatroom/chatpage.html",{"username":username,"hostname":hostname,"roomcode":roomcode})
                # print("user logged in ")
                return render(request,"chatroom/chatpage.html",{"username":username,"roomcode":roomcode})
            else:
                messages.info(request,"Room Code does not exist")
                return redirect("/")
    
def logout(request):
    if request.method=="POST":
        # hostname=request.POST["hostname"]
        if "roomcode" in request.POST:
            roomcode=request.POST["roomcode"]
            Host.objects.filter(meetcode=roomcode).delete()
    return redirect('/')

def submitmessage(request):
    if request.method=="POST":
        username=request.POST['username']
        roomcode=request.POST['roomcode']
        message=request.POST['message']
        chat=chatdata.objects.create(name=username,message=message,relatehost=Host.objects.get(meetcode=roomcode))
        chat.save()
        data={
            "name":chat.name,
            "message":chat.message,
            "hostname":chat.relatehost.hostname
        }
        if request.is_ajax():
            return JsonResponse(data,status=201)
        
def loadmessages(request,roomcode):
    text=chatdata.objects.filter(relatehost=Host.objects.get(meetcode=roomcode).id)
    list=[]
    for i in range (0,len(text)):
        dict={"name":text[i].name,"message":text[i].message}
        list.append(dict)
    data={
        "list":list
    }
    # for i in range(0,len(text)):
        # print(data['list'][i])
    return JsonResponse(data)