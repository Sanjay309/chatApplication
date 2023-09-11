from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/<str:group_name>/', login_required(views.group), name='group'),
    path('groups/', views.GroupList.as_view(template_name='chatApp/group_list.html'),name='groups'),
    path('groups/create/', views.GroupCreate.as_view(template_name='chatApp/group_form.html'),name='group-create'),
    path('groups/update/<int:pk>/', views.GroupUpdate.as_view(template_name='chatApp/group_form.html'),name='group-update'),
    path('groups/delete/<int:pk>/', views.GroupDelete.as_view(template_name='chatApp/group_confirm_delete.html'),name='group-delete'),
]