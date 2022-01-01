from typing import List
from django.shortcuts import redirect, render , redirect

# Create your views here.
from django.views.generic import ListView  , DetailView , CreateView
from django.views.generic.edit import FormMixin
from django_filters import filterset
from .models import Property 
from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView


class PropertyList(FilterView):

    model = Property
    #todo  paginations
    paginate_by = 2
    #todo filter
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

   
    
   


class PropertyDetail(FormMixin, DetailView):
    model = Property
    form_class = PropertyBookForm

   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         # todo related hotel filtering by category in property model 
        context["related"] = Property.objects.filter(category=self.get_object().category)[:3]
        return context

    def post(self, request , *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            
            return redirect('property:property_list')


        else:
            print('not valid')
    





class AddListing(CreateView):
    pass