from django.shortcuts import render
from .models import contact
from django.http import HttpResponse
from django.core.paginator import Paginator


# Create your views here.

def show_contact(request):
    contact_list = contact.objects.all()
    paginator = Paginator(contact_list, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'contact': page_obj}
    return render(request,'contact/faculty_member.html', context)
