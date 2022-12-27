from django.utils import timezone

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import test
from django.views.generic.edit import FormView,CreateView
from .form import reviewform
class uptest(ListView):



    model = test

    def get_queryset(self,*args,**kwargs):
        qs=super(uptest,self).get_queryset(*args,**kwargs)
        qs=qs.order_by('-id')
        return qs


class thakyou(TemplateView):
    template_name='base/singleview.html'

    def get_context_data(self, **kwargs):

        
        
        mod=test.objects.all()
        cont=super().get_context_data(**kwargs)
        cont["mess"]=mod
        return cont

class sample(TemplateView):
    template_name='base/temp.html'
    def get_context_data(self, **kwargs):
        
        mod=test.objects.all()
        cont=super().get_context_data(**kwargs)
        cont["mess"]=mod
        return cont
class single(TemplateView):
    template_name="base/singleview.html"
    def get_context_data(self, **kwargs):
        cont= super().get_context_data(**kwargs)
        re_id=kwargs["id"]
        print(re_id)
        result=test.objects.get(pk=re_id)
        print(result)
        
        cont['res']=result
        return cont
class singleview(DetailView):
    template_name='base/singleview.html'
    model=test

class review(FormView):
    form_class=reviewform
    template_name='base/temp.html'
    success_url='/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class create(CreateView):
    model=test
    form_class=reviewform
    template_name='base/new.html'
    success_url='/'