from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Talk
from django.contrib.auth.mixins import LoginRequiredMixin

# Create submit talk view
class TalkSubmitView(LoginRequiredMixin, CreateView):
    model = Talk
    fields = ['title', 'abstract', 'track']
    template_name = 'edit.html'
    success_url = '/'

    # Add title and button text to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Submit talk for consideration'
        context['button_text'] = 'Submit talk'
        return context

    def form_valid(self, form):
        form.instance.speaker = self.request.user
        return super().form_valid(form)

# Create update talk view
class TalkEditView(LoginRequiredMixin, UpdateView):
    model = Talk
    fields = ['title', 'abstract', 'track']
    template_name = 'edit.html'
    success_url = '/'

    # Add title and button text to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update talk'
        context['button_text'] = 'Update'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

# Create list view to display talks
# Accept status as a filter
class TalkListView(ListView):
    model = Talk
    template_name = 'list.html'
    context_object_name = 'talks'

# Create detail view
class TalkDetailView(DetailView):
    model = Talk
    template_name = 'detail.html'
    context_object_name = 'talk'
