from django.shortcuts import render,redirect

from .models import MyModelInfo

# Create your views here.
def myformpage(request):
    if request.method == 'POST':
        name_ = request.POST['name']
        email_ = request.POST['email']
        gander_ = request.POST['gender']
        profile_ = request.FILES.get('profile')


        MyModelInfo.objects.create(
            name = name_,
            email = email_,
            gender = gander_,
            profile = profile_
        )
        return redirect('show_mydata')
    return render(request,'master/index.html')

def show_mydata(request):
    get_all_data = MyModelInfo.objects.all()
    context = {
        'mydata':get_all_data
    }
    return render(request,'master/table.html',context)

def edit_page(request,pk):
    get_edit_data = MyModelInfo.objects.get(id=pk)
    context = {
        'getdata':get_edit_data
    }

    return render(request,'master/update.html',context)

def update_mydata(request,pk):
    update_getdata = MyModelInfo.objects.get(id=pk)
    if request.method=='POST':
        update_getdata.name = request.POST['name']
        update_getdata.email = request.POST['email']
        update_getdata.gender = request.POST['gender']
        if 'profile' in request.FILES:
            update_getdata.profile = request.FILES.get('profile')

        update_getdata.save()
        

    return redirect('show_mydata')

def delete_view(request,pk):
    del_data = MyModelInfo.objects.get(id=pk)
    del_data.delete()
    return redirect('show_mydata')
