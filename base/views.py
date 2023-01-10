from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm
# from django.http import JsonResponse
# import json
# Create your views here.

# stud=[
#     { 'id':1,'var':'this new topic'},
#     { 'id':2,'var':'today is day one from scracth'},
#     { 'id':3,'var':'today is day two'},
# ]

def hom(request):
    print(request.method)
    stud=Room.objects.all()
    context={'stud':stud}
    return render(request,'hom.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    # for i in stud:
    #     if i['id']==int(pk):
    #         room=i
    contxt={'room':room}
    return render(request,'room.html',contxt)

def createroom(request):
    form=RoomForm()
    if request.method=="POST":
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hom')
    context={'form':form}
    # return JsonResponse(json.loads( '{ "name":"John", "age":30, "city":"New York"}'))
    return render(request,'form_room.html',context)

def updateroom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.method == "POST":
        form=RoomForm(request.POST,instance=room)
        if form.is_vaild():
            form.save()
            return redirect("hom")

    context={'form': form}
    return render(request,"form_room.html",context)


def delroom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('hom')
    return render(request,'del.html',{'obj':room})

