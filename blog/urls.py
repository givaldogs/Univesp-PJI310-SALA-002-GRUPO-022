from django.urls import path
from blog.views import index, post, page, created_by, category


app_name = 'blog'



urlpatterns = [
     path('', index, name='index'),
     path('post/', post, name='post'),
     path('post/<slug:slug>/', post, name='post'),
     path('page/', page, name='page'),
     path('page/<slug:slug>/', page, name='page'),
     path('created_by/<int:author_pk>/', created_by, name='created_by'),
     path('category/<slug:slug>/', category, name='category'),

]