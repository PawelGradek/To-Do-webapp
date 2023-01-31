from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('list-of-all',views.listofallelems,name='list-of-all'),
    path('edit-to-do/<int:id>',views.edit,name='edit-to-do'),
    path('update/<int:id>',views.update,name='update')
]