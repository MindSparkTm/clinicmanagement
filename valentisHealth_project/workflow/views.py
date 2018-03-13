from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Message
from .forms import MessageForm
from .models import WorkflowManager


class MessageListView(ListView):
    model = Message
    template_name = 'workflow/workflow.html'

    def get_context(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)
        context['inbox'] = WorkflowManager.inbox(self.request.user)
        context['sent'] = WorkflowManager.sent(self.request.user)
        context['unread_count'] = WorkflowManager.inbox_unread_count(self, self.request.user)

        return context


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'workflow/workflow.html'

    def get_context(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)
        context['inbox'] = WorkflowManager.inbox(self.request.user)
        context['sent'] = WorkflowManager.sent(self.request.user)
        context['unread_count']  = WorkflowManager.inbox_unread_count(self, self.request.user)

        return context


class MessageDetailView(DetailView):
    model = Message
    template_name = 'workflow/workflow.html'


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'workflow/workflow.html'

