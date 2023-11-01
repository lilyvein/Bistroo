from django.urls import path
from . import views

app_name = 'app_admin'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),  # homepage
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category_detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail')
]