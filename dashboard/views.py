from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from users.models import User


class DashBoardView(TemplateView):
    template_name = 'dashboard.html'


    def get_context_data(self):
        context = super(DashBoardView, self).get_context_data()
        users = User.objects.all().exclude(id=self.request.user.id).select_related('user_profile').prefetch_related('roles')
        context.update({'users': users})
        return context
