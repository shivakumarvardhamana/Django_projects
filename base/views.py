from urllib import request
from django.utils import timezone
from django.views import View
from django.shortcuts import render,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import test
from django.shortcuts import HttpResponseRedirect,redirect
from django.views.generic.edit import FormView,CreateView
from .form import reviewform
# class uptest(ListView):



#     model = test

#     def get_queryset(self,*args,**kwargs):
#         qs=super(uptest,self).get_queryset(*args,**kwargs)
#         qs=qs.order_by('-id')
#         return qs


# class thakyou(TemplateView):
#     template_name='base/singleview.html'

#     def get_context_data(self, **kwargs):

        
        
#         mod=test.objects.all()
#         cont=super().get_context_data(**kwargs)
#         cont["mess"]=mod
#         return cont

# class sample(TemplateView):
#     template_name='base/temp.html'
#     def get_context_data(self, **kwargs):
        
#         mod=test.objects.all()
#         cont=super().get_context_data(**kwargs)
#         cont["mess"]=mod
#         return cont

# class singleview(DetailView):
#     template_name='base/test_list.html'
#     model=test

# class review(FormView):
#     form_class=reviewform
#     template_name='base/temp.html'
#     success_url='/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class create(CreateView):
#     model=test
#     form_class=reviewform
#     template_name='base/new.html'
#     success_url='/'\
class shiva(View):
    def get(self,request):
        contex={
            'name':'shivakumar'
        }
        request.session
        return render(request,'base/new.html',contex)

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

class favourate(View):
    def post(self,request):
        review_id=request.POST['id']
        request.session["favourrate_review"]=review_id
        
        return HttpResponseRedirect("result/"+review_id+"/")