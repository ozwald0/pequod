from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, TemplateView
from django.views.generic.edit import FormView
from .models import User, user_level, user_status, user_type
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.vanguard.models import products
from .forms import (formUpdateUser, formUserDetail, formUpdateUserlevel, formNewUserLevel, formNewUserStatus, 
                    formUpdateUserStatus, formNewUserType, formUpdateUserType, formNewUser, loginForm)


# Create your views here.

class loginUser(FormView):
    template_name = 'halberd/login.html'
    form_class = loginForm
    success_url = reverse_lazy('halberd_app:halberd_panel')

    def form_valid(self, form):
        user = authenticate(
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password1']
        )
        
        login(self.request, user)
        return super(loginUser, self).form_valid(form)


class newUserView(FormView):
    template_name = "halberd/new_user.html"
    form_class = formNewUser
    success_url = reverse_lazy('halberd_app:users_list')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['names'],
            form.cleaned_data['lastname'],
            form.cleaned_data['lastname2'],
            form.cleaned_data['password1'],
            telephone = form.cleaned_data['telephone'],
            user_level = form.cleaned_data['user_level'],
            user_type = form.cleaned_data['user_type'],
        )
        return super(newUserView, self).form_valid(form)

    #def post(self, request, *args, **kwargs):
    #    self.object = self.get_object()
    #    return super().post(request, *args, **kwargs)

class panelView(LoginRequiredMixin,ListView):
    template_name = "halberd/halberd_home.html"
    model = User
    login_url = reverse_lazy('halberd_app:login')

class usersList(ListView):
    template_name = "halberd/users_list.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = User.objects.search_users(palabra_clave, order)
        return queryset
    

class userDetailView(DetailView):
    model = User
    template_name = "halberd/user_details.html"

    def get_context_data(self, **kwargs):
        context = super(userDetailView, self).get_context_data(**kwargs)
        context['ejemplo'] = "variable de ejemplo"
        return context
    #    return []





    #todo intercepta el guardado a la base de datos y puedes cambiar lo que se requiera
    #def form_valid(self, form):
    #    #logica del proceso
    #    user = form.save(commit=False)
    #    user.fullname = user.lastname + ' ' + user.lastname2
    #    User.save()
    #    return super(newUserView, self).form_valid(form)


class userUpdateView(UpdateView):
    template_name = "halberd/user_update.html"
    model = User
    form_class = formUpdateUser
    success_url = reverse_lazy('halberd_app:users_list')


class altavariosmodelosprueba(FormView):
    template_name = "halberd/vista prueba.html"
    form_class = formUserDetail
    success_url = reverse_lazy('halberd_app:users_list')

    def form_valid(self, form):
        return super(altavariosmodelosprueba, self).form_valid(form)
    

class userLevelView(ListView):
    template_name = "halberd/user_level_view.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = user_level.objects.search_user_level(palabra_clave, order)
        return queryset


class userLevelDetailView(DetailView):
    model = user_level
    template_name = "halberd/user_level_details.html"


class userlevelUpdateView(UpdateView):
    template_name = "halberd/user_level_update.html"
    model = user_level
    form_class = formUpdateUserlevel
    success_url = reverse_lazy('halberd_app:user_level_list')


class newuserlevelView(CreateView):
    model = user_level
    template_name = "halberd/new_user_level.html"
    form_class = formNewUserLevel
    success_url = reverse_lazy('halberd_app:user_level_list')


class userstatusView(ListView):
    template_name = "halberd/user_status_view.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = user_status.objects.search_user_status(palabra_clave, order)
        return queryset
    

class userstatusDetailView(DetailView):
    model = user_status
    template_name = "halberd/user_status_details.html"


class userstatusUpdateView(UpdateView):
    template_name = "halberd/user_status_update.html"
    model = user_status
    form_class = formUpdateUserStatus
    success_url = reverse_lazy('halberd_app:user_status_list')


class newuserstatusView(CreateView):
    model = user_status
    template_name = "halberd/new_user_status.html"
    form_class = formNewUserStatus
    success_url = reverse_lazy('halberd_app:user_level_list')


class userTypeView(ListView):
    template_name = "halberd/user_type_view.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        order = self.request.GET.get("order",'')
        queryset = user_type.objects.search_user_type(palabra_clave, order)
        return queryset
    

class usersTypeDetailView(DetailView):
    model = user_type
    template_name = "halberd/user_type_details.html"


class userTypeUpdateView(UpdateView):
    template_name = "halberd/user_type_update.html"
    model = user_type
    form_class = formUpdateUserType
    success_url = reverse_lazy('halberd_app:user_type_list')


class newusersTypeView(CreateView):
    model = user_type
    template_name = "halberd/new_user_type.html"
    form_class = formNewUserType
    success_url = reverse_lazy('halberd_app:user_type_list')



class logoutUser(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('halberd_app:halberd_panel')
        )