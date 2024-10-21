from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Study
import logging

#logger = logging.getLogger(__name__)


logger = logging.getLogger(__name__)

def study_list(request):
    try:
        studies = Study.objects.filter(is_deleted=False)
        return render(request, 'studies/study_list.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error retrieving study list: {e}")
        return render(request, 'error.html', {'message': 'Error retrieving study list.'})


class StudyListView(ListView):
    model = Study
    template_name = 'studies/study_list.html'
    context_object_name = 'studies'

class StudyCreateView(CreateView):
    model = Study
    template_name = 'studies/study_form.html'
    fields = ['name', 'description', 'phase', 'sponsor_name']
    success_url = reverse_lazy('study-list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Study created successfully.')
            logger.info(f"Study created: {self.object}")
            return response
        except Exception as e:
            logger.error(f"Error creating study: {str(e)}")
            messages.error(self.request, 'Error creating study.')
            return super().form_invalid(form)

class StudyUpdateView(UpdateView):
    model = Study
    template_name = 'studies/study_form.html'
    fields = ['name', 'description', 'phase', 'sponsor_name']
    success_url = reverse_lazy('study-list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Study updated successfully.')
            logger.info(f"Study updated: {self.object}")
            return response
        except Exception as e:
            logger.error(f"Error updating study: {str(e)}")
            messages.error(self.request, 'Error updating study.')
            return super().form_invalid(form)

class StudyDeleteView(DeleteView):
    model = Study
    template_name = 'studies/study_confirm_delete.html'
    success_url = reverse_lazy('study-list')

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(self.request, 'Study deleted successfully.')
            logger.info(f"Study deleted: {self.object}")
            return response
        except Exception as e:
            logger.error(f"Error deleting study: {str(e)}")
            messages.error(self.request, 'Error deleting study.')
            return self.render_to_response(self.get_context_data())

class StudyDetailView(DetailView):
    model = Study
    template_name = 'studies/study_detail.html'