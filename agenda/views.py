from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Talk
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages  # Import messages

class TalkSubmitView(LoginRequiredMixin, CreateView):
    model = Talk
    fields = ['title', 'abstract', 'track']
    template_name = 'edit.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Submit talk for consideration'
        context['button_text'] = 'Submit talk'
        return context

    def form_valid(self, form):
        form.instance.speaker = self.request.user
        messages.success(self.request, f'Thank you for submitting "{form.instance.title}" for consideration.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add an error message for unsuccessful form submissions
        messages.error(self.request, 'Submission failed. Please check your form for errors.')
        return super().form_invalid(form)

class TalkEditView(LoginRequiredMixin, UpdateView):
    model = Talk
    fields = ['title', 'abstract', 'track']
    template_name = 'edit.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update talk'
        context['button_text'] = 'Update'
        return context

    def form_valid(self, form):
        messages.success(self.request, f'Thank you for updating "{form.instance.title}".')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add an error message for unsuccessful form updates
        messages.error(self.request, 'Update failed. Please check your form for errors.')
        return super().form_invalid(form)

class TalkListView(ListView):
    model = Talk
    template_name = 'list.html'
    context_object_name = 'talks'

class TalkDetailView(DetailView):
    model = Talk
    template_name = 'detail.html'
    context_object_name = 'talk'
