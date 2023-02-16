from django.shortcuts import render
from .forms import LearnForm
from django.contrib.auth.decorators import login_required

from .models import learn
from django.http import HttpResponse
from django.core.paginator import Paginator
from taggit.models import Tag
from django.views.decorators.csrf import ensure_csrf_cookie
from .filters import LearnFilter

# Create your views here.

@login_required
def post_learn(request):
    if request.method=='POST':
        form = LearnForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
    else:
        form = LearnForm()


    context = {'form':form}
    return render(request, 'learn/post_learn.html',context)
@ensure_csrf_cookie
def blog(request):
    blog_list = learn.objects.all()
    myfilter = LearnFilter(request.GET, queryset= blog_list)
    blog_list = myfilter.qs

    paginator = Paginator(blog_list, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'learn': page_obj , 'myfilter' : myfilter}
    return render(request,'blog/blog.html', context)


def blog_detail(request, pk):
    blog_detail= learn.objects.get(id=pk)
    context = {'learn': blog_detail}  # here the name goes to the templete
    return render(request, 'blog/single-blog.html', context)

