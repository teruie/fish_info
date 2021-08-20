from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.views.generic import CreateView

from django.urls import reverse_lazy

from fish.models import Category, Place

from fish.forms import CategoryForm, PlaceForm






class CategoryCreateView(CreateView, LoginRequiredMixin):
    template_name = 'create/category_create.html'
    success_url = reverse_lazy('fish:index')
    form_class = CategoryForm
    model = Category


    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('fish:index')

category_create = CategoryCreateView.as_view()



class PlaceCreateView(CreateView, LoginRequiredMixin):
    template_name = 'create/place_create.html'
    success_url = reverse_lazy('fish:index')
    form_class = PlaceForm
    model = Place


    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('fish:index')

place_create = PlaceCreateView.as_view()