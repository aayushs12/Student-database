from django.shortcuts import render,redirect
from crud.models import check, course, crudst,newp
from django.contrib import messages
from crud.forms import stform
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context, loader

def stdisplay(request):
    results=crudst.objects.all()
    return render(request,"Index.html",{"crudst":results})
def stinsert(request):
    if request.method=="POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('stgrade'):
            savest=crudst()
            savest.stname=request.POST.get('stname')
            savest.stemail=request.POST.get('stemail')
            savest.stgrade=request.POST.get('stgrade')    
            if(crudst.objects.filter(stemail=savest.stemail).exists()):
                messages.warning(request,'Email is already in use')
                return redirect('stinsert')
            else:
                savest.save()
                messages.success(request,"The Record "+savest.stname+" Is Saved Successfully")
                return render(request,"Create.html")
    else:
        return render(request,"Create.html")

def stedit(request,stid):
    getstudentdetails=crudst.objects.get(stid=stid)
    return render(request,'edit.html',{"crudst":getstudentdetails})

def stupdate(request,stid):
    stupdate=crudst.objects.get(stid=stid)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
    messages.success(request,"The Student Record has been updated successfully")
    return render(request,"edit.html",{"crudst":stupdate})


def stdel(request,stid):
    delstudent=crudst.objects.get(stid=stid)
    delstudent.delete()
    results=crudst.objects.all()
    return render(request,"Index.html",{"crudst":results})

def stsearch(request):
    dataset = crudst.objects.all()
    return render(request,'idk.html')
 
def stDetailView(request,stid):
    try:
        data = newp.objects.filter(studentid_id=stid)
        newdata=crudst.objects.get(stid=stid)
    except crudst.DoesNotExist:
        raise Http404('Data does not exist') 
    return render(request,'detailview.html',{'data':data,'newdata':newdata})

def stnotsure(request):
    return render(request,'notsure.html')

def cdisplay(request):
    results=course.objects.all()
    return render(request,"course.html",{"course":results})
    
def handleit(request, *args, **argv):
    return render(request, '500.html', status=500)

def sdisplay(request):
    results=newp.objects.all()
    return render(request,"check.html",{"check":results})

def coursedisplay(request,cid):
    details=newp.objects.filter(courseno_id=cid)
    return render(request,'coursedet.html',{"newp":details})