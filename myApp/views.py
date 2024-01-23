from django.shortcuts import render,redirect
from django.views.generic import View
from myApp.models import Movie
from django import forms
# Create your views here.

class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        return render(request,"movie_list.html",{"data":qs})
    
class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        # print(kwargs)
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})
    
class MovieDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")
    
class MovieForm(forms.Form):
    name=forms.CharField()
    language=forms.CharField()
    genre=forms.CharField()
    run_time=forms.IntegerField()
    director=forms.CharField()
    actors=forms.CharField()
    year=forms.IntegerField()

class MovieCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MovieForm()
        return render(request,"movie_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MovieForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Movie.objects.create(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form})
        # data={k:v for k,v in request.POST.items()}
        # data.pop("csrfmiddlewaretoken")
        # Movie.objects.create(**data) # unpack the dictionary
        # return redirect("movie-list")
    