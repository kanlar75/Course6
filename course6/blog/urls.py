from django.urls import path
from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]