from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from .models import Transation, Elements, Category
from .form import Transation_Form, Element_Form, Category_Form
import datetime
from django.contrib import messages # Learn about this class =============

# Create your views here.


def home(request):
    #content = "<html><body>Hello World</body></html>"
    #return HttpResponse(content)
    content = {}
    content['date'] = datetime.datetime.now()
    content['list'] = ["t1", "t2", "t3"]

    return render(request, "contas/home.html", content)



class test(View):
    def get(self, request):
        content = "<html><body> Hello World </body></html>"
        return HttpResponse(content)
    

#===========================================================

class list_items(View):
    def get(self, request):

        search = request.GET.get('search')
        if search:
            data_page = Transation.objects.filter(category=search)

        else: 
            data = dict()
            data = Transation.objects.all()

            paginator = Paginator(data, 2)  # paginator will divide the data in two parts, according the number we pass by.

            page = request.GET.get('page') # It will get the current page

            data_page = paginator.get_page(page) # data_page receive all the data of the page sended.

        return render(request, 'contas/list.html',{'transation': data_page, 'msg-search': search})

    

#===========================================================

class Insert(View):
    def post(self, request):

        #form variable receive tha validation of the Form Class, Form Class is create based on Models
        # We always validate the request response with the form Class(It checks all the fields already) , to compare if all the fields are correctly filled

        form = Transation_Form(request.POST or None)
        if form.is_valid():
            description= form.cleaned_data["description"]
            value = form.cleaned_data["value"]
            category = form.cleaned_data["category"]
            observation = form.cleaned_data["observation"]
            db = Transation(description=description, value=value, category=category, observation=observation)
            db.save()
            #form.save()
            #return render(request, "contas/form.html", {"data": form})
            return HttpResponseRedirect("/list/")
            #return redirect("url_list")
    
    def get(self, request):
        form = dict()
        form['form'] = Transation_Form()
        form['action'] = "Create"
        form['cat'] = Category.objects.all()
        return render(request, "contas/create.html", form)


#===========================================================

class Update(View):
    def get(self, request, pk):
        #form = dict()
        user = Transation.objects.get(pk=pk)
        category = Category.objects.all()
        #form['form'] = Transation_Form(instance=transation)
        action = 'Update'
        return render(request, "contas/form.html", {"transation": user, "cat": category, "action": action})

    def post(self, request, pk):

        # Taking just one model from database according the pk variable
        transation = Transation.objects.get(pk=pk)

        #Saving the result on the right instance of model
        form = Transation_Form(request.POST or None, instance=transation)

        if form.is_valid():
            form.save()
            return redirect("url_list")
        else:
            #form = Transation_Form()
            #form = dict()
            user = Transation.objects.get(pk=pk)
            category = Category.objects.all()
            #form['form'] = Transation_Form(instance=transation)
            action = 'Update'
            return render(request, "contas/form.html", {'transation': user, "cat": category, "action": action})
        



#===========================================================



class Delete(View):
    def get(self, request,pk):
        form = dict()
        transation = Transation.objects.get(pk=pk)
        form['form'] = Transation_Form(instance=transation)
        form['action'] = 'Delete'
        return render(request, "contas/form.html", form)

    def post(self, request, pk):
        transation = Transation.objects.get(pk=pk)
        form = Transation_Form(request.POST, instance=transation)
        if form.is_valid():
            transation.delete()
            return redirect("url_list")
        



class Element(View):
    def get(self, request):
        form = Elements.objects.all()
        return render(request, "contas/form-element.html", {"elements": form})

    def post(self, request):
        data = Elements.objects.all()
        for item in data:
            if request.POST.get('c' + str(item.id)) == 'clicked':
                item.state = True
            else:
                item.state = False
        item.save()

        return redirect("url_list")




class Create(View):
    def get(self, request):
        form = Category_Form()
        return render(request, "contas/create_category.html",{"form": form})

    def post(self, request):
        form = Category_Form(request.POST)
        if form.is_valid():
            print("Valid")
            n = form.cleaned_data["name"]
            t = Category(name=n)
            t.save()
            request.user.category.add(t) # Add the information on the current user logged on the same register, added on user column
            return redirect("/")
        else:
            print('invalid')
            return redirect('/create/')


class view(View):
    def get(self, request):
        if request.user.is_authenticated:           
            return render(request, "contas/view.html", {})

    def post(self, request):
        pass


class index(View):
    def get(self, request, pk):
        user_obj = Category.objects.get(id=pk)

        if user_obj in request.user.category.all():
            pass
            # Show the information
            return render(request, "contas/view.html", {"data": user_obj})



    def post(self, request, id):
        pass