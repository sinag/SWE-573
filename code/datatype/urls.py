from django.urls import path

from datatype.views import CreateView, DeleteView, UpdateView
from . import views

app_name = 'datatype'
urlpatterns = [
    path('create/<int:community_id>', CreateView.as_view(), name='create'),
    path('<int:community_id>', views.IndexView.as_view(), name='index'),
    path('delete/<int:community_id>/<int:pk>', DeleteView.as_view(), name='delete'),
    path('update/<int:community_id>/<int:pk>', UpdateView.as_view(), name='update'),
]
