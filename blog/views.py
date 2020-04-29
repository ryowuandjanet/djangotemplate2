from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

def blog_list(request):
    queryset=Post.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,"post_home.html",context)

def blog_detail(request,id=None):
    instance=get_object_or_404(Post,id=id)
    context={
        "instance":instance
    }
    return render(request,"post_detail.html",context)    
    

def blog_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form":form,
    }
    return render(request,"post_form.html",context)    
    
def blog_update(request,id=None):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "instance":instance,
        "title":instance.title,
        "form":form,
    }
    return render(request,"post_form.html",context)  
    
def blog_delete(request,id=None):
    instance=get_object_or_404(Post,id=id)
    if request.method == "POST":
        instance.delete()
        return redirect("post_home")
    context={"instance":instance}
    return render(request,"post_delete.html",context)
