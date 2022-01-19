from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):

    pass

logout = LogoutView.as_view()