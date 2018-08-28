from django.shortcuts import render
from django.views import View


class HomePage(View):

    @staticmethod
    def get(request):
        #form = LoginForm()
        return render(request, 'home_page.html', {
            #'form': form,
        })

class About(View):

    @staticmethod
    def get(request):
        #form = LoginForm()
        return render(request, 'abouts.html', {
            #'form': form,
        })

class Laws(View):

    @staticmethod
    def get(request):
        #form = LoginForm()
        return render(request, 'laws.html', {
            #'form': form,
        })

