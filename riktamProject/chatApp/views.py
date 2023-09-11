from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Chat
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def group(request, group_name):
    print("group name", group_name)
    group = Group.objects.filter(name = group_name).first()
    chats = []
    if group:
        chats = Chat.objects.filter(group = group)
    else:
        group = Group(name = group_name)
        group.save()
    return render(request, 'chatApp/group_2.html', {'groupname' : group_name, 'chats': chats})

class GroupList(LoginRequiredMixin, ListView):
    model = Group
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['groups'] = context['groups'].filter(user=self.request.user)
        context['groups'] = context['groups']
        return context

class GroupCreate(CreateView):
    model = Group
    fields = ['name']
    success_url = reverse_lazy('groups')
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The group was created successfully.")
        return super(GroupCreate,self).form_valid(form)
    
class GroupUpdate(UpdateView):
    model = Group
    fields = ['name']
    success_url = reverse_lazy('groups')
    
    def form_valid(self, form):
        messages.success(self.request, "The group was updated successfully.")
        return super(GroupUpdate,self).form_valid(form)
    
class GroupDelete(DeleteView):
    model = Group
    context_object_name = 'group'
    success_url = reverse_lazy('groups')
    
    def form_valid(self, form):
        messages.success(self.request, "The group was deleted successfully.")
        return super(GroupDelete,self).form_valid(form)