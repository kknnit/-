from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from App.models import Dog, Cat, User


def index(request):
    return HttpResponse('index')


def dog(request):
    dog=Dog()
    dog.age=8
    dog.name='阿黄'
    dog.save()
    return HttpResponse('添加成功')
def cat(request):
    cat=Cat()
    cat.name='阿白'
    cat.color='白色'
    cat.save()
    return HttpResponse('添加成功')


def testst(request):
    name='张三'
    return render(request,'testst.html',context=locals())


def upload(request):
    if request.method=='GET':
        return render(request,'upload.html')
    elif request.method=='POST':
        icon=request.FILES.get('icon')

        for part in icon.chunks():
            with open('/home/admin_/.virtualenvs/django/day06/static/upload/time.jpg','wb') as fp:
                fp.write(part)
                fp.close()


        return HttpResponse('上传成功')

    return HttpResponse('ok')


def uploaddjango(request):
    if request.method=='GET':
        return render(request,'uploaddjango.html')
    elif request.method=='POST':
        icon=request.FILES.get('icon')
        user=User()
        user.u_icon=icon
        user.save()
        return HttpResponse('上传成功')
    return HttpResponse('ok')


def getimage(request):
    # id=request.GET.get('id')
    user=User.objects.get(pk=1)
    icon=user.u_icon
    context={
        'icon':'/static/upload/'+icon.url
    }

    return render(request,'getimage.html',context=context)