from django.urls import path
from . import views

app_name = 'blog'  # creates a namespace for this app

urlpatterns = [
    path('', views.index, name='index'),  # display the index.html file at the root URL
    path('blog/', views.BlogView.as_view(), name='blog'),  # display the list of blog posts at the /blog/ URL
    path('about/', views.about, name='about'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='detail'),  # display the detail of a blog post at the /blog/<id>/ URL

]
'''
urlpatterns = [
    # /blog/
    path('', views.index, name='index'),  # for function-based view

    # /blog/<blog pk number>
    path('<int:pk>', views.PostDetailView.as_view(), name='detail')
]
'''
