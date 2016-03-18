from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from .forms import UserProfileForm, ContactForm
from models import UserProfile
from helpers import email_helper



def index(request):
	return render_to_response('index.html', RequestContext(request))


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name','')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            email_helper.contact_us_email(contact_name, contact_email, form_content)
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })



    return render_to_response('contact.html', RequestContext(request, {'form': form}))

def twitter_feed(request):
    return render_to_response('twitter_feed.html', RequestContext(request))

def code_of_conduct(request):
    return render_to_response('code_of_conduct.html', RequestContext(request))


def open_source(request):
    return render_to_response('open_source.html', RequestContext(request))
    
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/profile.html') 
    return render(request, 'login.html')


@login_required
def profile(request):
    form = UserProfileForm()
    print(str(request.user))
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        print(form.data)
        if form.is_valid():
            print("valid")
            userprofile = form.save(commit=False)
            # userprofile.user = request.user.username
            userprofile.save()
        else:
            messages.error(request, form.errors)
            print("failed")
    return render(request, "profileform.html", RequestContext(request, {'form': form, 'profile': profile}))

@login_required
def ladynerds(request):
    ladynerds = UserProfile.objects.all()
    context_dict = {'ladynerds':ladynerds}
    return render_to_response('ladynerds.html', RequestContext(request, context_dict))

@login_required
def resources(request):
    return render_to_response('resources.html', RequestContext(request))

@login_required
def faq(request):
    return render_to_response('faq.html', RequestContext(request))
