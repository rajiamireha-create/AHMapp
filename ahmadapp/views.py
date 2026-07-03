from django.shortcuts import render ,redirect
from ahmadapp.models import ahmadapptask
from ahmadapp.form import ahmadapptaskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
    
def index(request):
    context = {
        "index":"welcome to index page",
        "ahmad":"welcome to ahmad page",
    }
    return render(request,'index.html',context)
    
    
@login_required
def pending_task(request,task_id):
    task_obj = ahmadapptask.objects.get(pk=task_id)
    if task_obj.manager == request.user:      
       task_obj.done = False
       task_obj.save()
       return redirect('ahmadapp')  
    else: 
        messages.error(request,'You Cannot Do Anywith This Task')
        return redirect('ahmadapp')
@login_required
def completed_task(request,task_id):
    task_obj = ahmadapptask.objects.get(id=task_id)
    task_obj.done = True
    task_obj.save()
    return redirect('ahmadapp')
@login_required
def edit_task(request,task_id):
  if request.method == "POST":
        task_obj = ahmadapptask.objects.get(id=task_id)
        form = ahmadapptaskform(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request,'Task edited Successfully')
        return redirect('ahmadapp')
  else:
         task_obj = ahmadapptask.objects.get(id=task_id)
         return render(request,'edit.html',{'task_obj':task_obj})
@login_required     
def delete_task(request,task_id):
    
    task = ahmadapptask.objects.get(id=task_id)
    if task.manager == request.user:
        task.delete()
        messages.success(request,'Task Deleted Successfully')
        return redirect('ahmadapp')
    else:
        messages.error(request,'You Cannot Delete This Task')
        return redirect('ahmadapp')


@login_required
def ahmadapp(request):
    
    
    if request.method == "POST":    
        form = ahmadapptaskform(request.POST or None)
        if form.is_valid():
            isinstance = form.save(commit=False)    
            isinstance.manager = request.user
            isinstance.save()
        messages.success(request,'Task Added Successfully')
        return redirect('ahmadapp')
    else:       
        all_tasks = ahmadapptask.objects.filter(manager = request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('page') 
        all_tasks = paginator.get_page(page)
        return render(request, 'ahmadapp.html',{'all_tasks':all_tasks})
    
    
    
    
@login_required
def home(request):
    context = {
        "home":"welcome to home page"
    }
    return render(request,'home.html',context)

@login_required
def contact(request):
    context = {
        "contact":"welcome to contact page"
    }
    return render(request,'contact.html',context)
@login_required
def pricing(request):
    context = {
        "pricing":"welcome to pricing page"
    }
    return render(request,'pricing.html',context)




def features(request,):
    if request.method == "POST":    
        form = ahmadapptaskform(request.POST or None)
        if form.is_valid():
            form.save()
    messages.success(request,'We Processing Your Request Continue With The app Dont worry ')

    return render(request,'features.html')
