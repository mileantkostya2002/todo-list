from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, Tag
from .forms import TaskForm, TagForm

class TaskListView(generic.ListView):
    model = Task
    template = "tasks/task_list.html"
    context_object_name = "tasks"
    queryset = Task.objects.prefetch_related('tags')


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task-list')

class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")

class TaskToggleStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('task:todo-list')

class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tasks/tag_list.html'

class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'tasks/tag_form.html'
    success_url = reverse_lazy('todo:tag-list')
    form_class = TagForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = 'tasks/tag_confirm_delete.html'
    success_url = reverse_lazy('todo:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")