from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/', 
        views.BlogPostCrearLista.as_view(),
        name='blogpost-view-crear'
    ),

    # blogposts/id del BlogPost
    path('blogposts/<int:pk>', 
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name='update'
    ),

    # custom BlogPost
    path('blogposts/custom', 
        views.BlogPostLista.as_view(),
        name='blogpost-view-custom'
    )
]
