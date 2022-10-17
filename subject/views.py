from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Subject

class SubjectListView(ListView):
    model = Subject
    paginate_by = 3

# Create your views here.


class SubjectCreateView(CreateView):
    model = Subject
    fields = ['sub_name','department']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class SubjectDetailView(DetailView):
    model = Subject

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = ['sub_name','department']
    template_name_suffix = '_update'

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('list')
