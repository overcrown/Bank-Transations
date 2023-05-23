from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .forms import RegisterUser

# Libraries to create and authenticate the user



# Create your views here.


class register(View):

    def get(self, request):
        if request.user.is_authenticated:
            print('You are in')
        else:
            print('You are out')
        form = RegisterUser()
        return render(request, "register/register.html", {"form": form})

    def post(self, request):
        forms = RegisterUser(request.POST or None)
        if forms.is_valid():
            forms.save()
            print('Saved')
        else:
            return redirect('/register')
        return redirect('/list')