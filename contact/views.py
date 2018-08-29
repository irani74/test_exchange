from django.shortcuts import render, redirect

# Create your views here.
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from contact.forms import ContactForm

from django.views import View

def thanks(request):
    return render_to_response('thanks.html')












def havig(request):

    request.session["fav_color"] = "blue"

    pass


class Member(object):
    pass


def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")












@method_decorator(csrf_exempt, name='havig')

def contact(request):


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #con = get_connection('django.core.mail.backends.console.EmailBackend')
            #send_mail(
                #cd['subject'],
                #cd['message'],
                #cd.get('email', 'noreply@example.com'),
                #['siteowner@example.com'],
                #connection=con
            #)
            return redirect('contact:thanks')
    else:
        form = ContactForm(
            initial={'subject': 'سایت پرداخت ارزی امیر بسیار عالیست!'}

        )

    return render(request, 'contact_form.html', {'form': form})