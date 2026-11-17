from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('location/', views.location, name='location'),
    path('catalog/', views.catalog, name='catalog'),
    path('suppliers/', views.suppliers, name='suppliers'),

    
    path('tovary/', views.TovarListView.as_view(), name='tovar_list'),
    path('tovary/add/', views.TovarCreateView.as_view(), name='tovar_add'),
    path('tovary/<int:pk>/', views.TovarDetailView.as_view(), name='tovar_detail'),
    path('tovary/<int:pk>/edit/', views.TovarUpdateView.as_view(), name='tovar_edit'),
    path('tovary/<int:pk>/delete/', views.TovarDeleteView.as_view(), name='tovar_delete'),


    path('postavshiki/', views.PostavchikListView.as_view(), name='postavchik_list'),
    path('postavshiki/add/', views.PostavchikCreateView.as_view(), name='postavchik_add'),
    path('postavshiki/<int:pk>/', views.PostavchikDetailView.as_view(), name='postavchik_detail'),
    path('postavshiki/<int:pk>/edit/', views.PostavchikUpdateView.as_view(), name='postavchik_edit'),
    path('postavshiki/<int:pk>/delete/', views.PostavchikDeleteView.as_view(), name='postavchik_delete'),


    path('clienti/', views.ClientiListView.as_view(), name='clienti_list'),
    path('clienti/add/', views.ClientiCreateView.as_view(), name='clienti_add'),
    path('clienti/<int:pk>/', views.ClientiDetailView.as_view(), name='clienti_detail'),
    path('clienti/<int:pk>/edit/', views.ClientiUpdateView.as_view(), name='clienti_edit'),
    path('clienti/<int:pk>/delete/', views.ClientiDeleteView.as_view(), name='clienti_delete'),


    path('cotrudniki/', views.CotrudnikiListView.as_view(), name='cotrudniki_list'),
    path('cotrudniki/add/', views.CotrudnikiCreateView.as_view(), name='cotrudniki_add'),
    path('cotrudniki/<int:pk>/', views.CotrudnikiDetailView.as_view(), name='cotrudniki_detail'),
    path('cotrudniki/<int:pk>/edit/', views.CotrudnikiUpdateView.as_view(), name='cotrudniki_edit'),
    path('cotrudniki/<int:pk>/delete/', views.CotrudnikiDeleteView.as_view(), name='cotrudniki_delete'),


    path('zakazi/', views.ZakaziListView.as_view(), name='zakazi_list'),
    path('zakazi/add/', views.ZakaziCreateView.as_view(), name='zakazi_add'),
    path('zakazi/<int:pk>/', views.ZakaziDetailView.as_view(), name='zakazi_detail'),
    path('zakazi/<int:pk>/edit/', views.ZakaziUpdateView.as_view(), name='zakazi_edit'),
    path('zakazi/<int:pk>/delete/', views.ZakaziDeleteView.as_view(), name='zakazi_delete'),
]