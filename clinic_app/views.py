from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, DeleteView, DetailView, ListView, UpdateView, CreateView, FormView, View
from models import *


class ListNews(ListView):
    model = News
    template_name_suffix = "_list_all"