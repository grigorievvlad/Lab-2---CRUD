from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tovar, Postavchik, Clienti, Cotrudniki, Zakazi
from .forms import TovarForm, PostavchikForm, ClientiForm, CotrudnikiForm, ZakaziForm


def first_view(request):
    return render(request, 'first.html')

def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def location(request):
    return render(request, 'location.html')


def catalog(request):
    return render(request, 'catalog.html')


def suppliers(request):
    return render(request, 'suppliers.html')

class TovarListView(ListView):
    model = Tovar
    template_name = 'tovar/tovar_list.html'
    context_object_name = 'tovary'


class TovarDetailView(DetailView):
    model = Tovar
    template_name = 'tovar/tovar_detail.html'
    context_object_name = 'tovar'


class TovarCreateView(CreateView):
    model = Tovar
    form_class = TovarForm
    template_name = 'tovar/tovar_form.html'
    success_url = reverse_lazy('tovar_list')


class TovarDeleteView(DeleteView):
    model = Tovar
    template_name = 'tovar/tovar_confirm_delete.html'
    success_url = reverse_lazy('tovar_list')


class TovarUpdateView(UpdateView):
    model = Tovar
    form_class = TovarForm
    template_name = 'tovar/tovar_form.html'
    success_url = reverse_lazy('tovar_list')


class PostavchikListView(ListView):
    model = Postavchik
    template_name = 'postavchik/postavchik_list.html'
    context_object_name = 'postavshiki'


class PostavchikDetailView(DetailView):
    model = Postavchik
    template_name = 'postavchik/postavchik_detail.html'
    context_object_name = 'postavchik'


class PostavchikCreateView(CreateView):
    model = Postavchik
    form_class = PostavchikForm
    template_name = 'postavchik/postavchik_form.html'
    success_url = reverse_lazy('postavchik_list')


class PostavchikDeleteView(DeleteView):
    model = Postavchik
    template_name = 'postavchik/postavchik_confirm_delete.html'
    success_url = reverse_lazy('postavchik_list')


class PostavchikUpdateView(UpdateView):
    model = Postavchik
    form_class = PostavchikForm
    template_name = 'postavchik/postavchik_form.html'
    success_url = reverse_lazy('postavchik_list')


class ClientiListView(ListView):
    model = Clienti
    template_name = 'clienti/clienti_list.html'
    context_object_name = 'clienti'


class ClientiDetailView(DetailView):
    model = Clienti
    template_name = 'clienti/clienti_detail.html'
    context_object_name = 'client'


class ClientiCreateView(CreateView):
    model = Clienti
    form_class = ClientiForm
    template_name = 'clienti/clienti_form.html'
    success_url = reverse_lazy('clienti_list')


class ClientiDeleteView(DeleteView):
    model = Clienti
    template_name = 'clienti/clienti_confirm_delete.html'
    success_url = reverse_lazy('clienti_list')


class ClientiUpdateView(UpdateView):
    model = Clienti
    form_class = ClientiForm
    template_name = 'clienti/clienti_form.html'
    success_url = reverse_lazy('clienti_list')


class CotrudnikiListView(ListView):
    model = Cotrudniki
    template_name = 'cotrudniki/cotrudniki_list.html'
    context_object_name = 'cotrudniki'


class CotrudnikiDetailView(DetailView):
    model = Cotrudniki
    template_name = 'cotrudniki/cotrudniki_detail.html'
    context_object_name = 'cotrudnik'


class CotrudnikiCreateView(CreateView):
    model = Cotrudniki
    form_class = CotrudnikiForm
    template_name = 'cotrudniki/cotrudniki_form.html'
    success_url = reverse_lazy('cotrudniki_list')


class CotrudnikiDeleteView(DeleteView):
    model = Cotrudniki
    template_name = 'cotrudniki/cotrudniki_confirm_delete.html'
    success_url = reverse_lazy('cotrudniki_list')


class CotrudnikiUpdateView(UpdateView):
    model = Cotrudniki
    form_class = CotrudnikiForm
    template_name = 'cotrudniki/cotrudniki_form.html'
    success_url = reverse_lazy('cotrudniki_list')


class ZakaziListView(ListView):
    model = Zakazi
    template_name = 'zakazi/zakazi_list.html'
    context_object_name = 'zakazi'


class ZakaziDetailView(DetailView):
    model = Zakazi
    template_name = 'zakazi/zakazi_detail.html'
    context_object_name = 'zakaz'


class ZakaziCreateView(CreateView):
    model = Zakazi
    form_class = ZakaziForm
    template_name = 'zakazi/zakazi_form.html'
    success_url = reverse_lazy('zakazi_list')


class ZakaziDeleteView(DeleteView):
    model = Zakazi
    template_name = 'zakazi/zakazi_confirm_delete.html'
    success_url = reverse_lazy('zakazi_list')


class ZakaziUpdateView(UpdateView):
    model = Zakazi
    form_class = ZakaziForm
    template_name = 'zakazi/zakazi_form.html'
    success_url = reverse_lazy('zakazi_list')