from django.shortcuts import render
from .forms import LearnForm
from django.contrib.auth.decorators import login_required

from .models import learn
from django.http import HttpResponse
from django.core.paginator import Paginator
from taggit.models import Tag

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

def blog(request):
    blog_list = learn.objects.all()
    paginator = Paginator(blog_list, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'learn': page_obj}
    return render(request,'learn/blog.html', context)


def blog_detail(request, pk):
    blog_detail= learn.objects.get(id=pk)
    context = {'learn': blog_detail}  # here the name goes to the templete
    return render(request, 'learn/single-blog.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    posts = learn.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)
