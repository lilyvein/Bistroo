from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView) # vaated mida kasutame
from app_admin.models import Category
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'app_admin/index.html'


class CategoryCreateView(CreateView):
    template_name = 'app_admin/category_form_create.html'
    model = Category
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('app_admin:category_list')


class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.order_by('number')  # Result ordered by name
    context_object_name = 'categories'  # default object_list now teacher


class CategoryCreateView(CreateView):
    template_name = 'app_admin/category_form_create.html'
    model = Category
    fields = '__all__'  # All fields into form
    success_url = reverse_lazy('app_admin:category_list')


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    template_name = 'app_admin/category_update.html'
    model = Category
    fields = ['number', 'name']  # update only this fields
    success_url = reverse_lazy('app_admin:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('app_admin:category_list')
