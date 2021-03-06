# -*- coding: utf-8 -*-


from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import gettext_lazy as _

from . import views
from marketing.views import email_list_signup
from shop.sitemaps import CatSitemaps


sitemaps = {
    'cat': CatSitemaps,
}

app_name = 'shop'

urlpatterns = (
    # ex: /
    path('', views.all_produit, name='all_produit'),
    # ex: subscribe/
    path(_('subscribe/'), email_list_signup, name='marketing'),

    # ex: search/
    path(_('search/'), views.search, name='search'),

    # ex: shop/product/
    path(_('shop/product/<slug:slug>/<int:id>/'), views.detail_produit, name='detail_produit'),

    # ex: shop/marque/
    path(_('shop/marque/'), views.all_marques, name='all_marque'),
    path(_('shop/marque/<slug:marque_slug>/'), views.liste_marques, name='listing_marques'),

    # ex: shop/category/
    path(_('shop/category/'), views.all_categorie, name='all_categorie'),
    path(_('shop/category/<slug:category_slug>/'), views.liste_categorie, name='listing_categorie'),
    path(_('shop/category/<slug:category_slug>/'), views.all_produit, name='all_produit'),

    # ex: shop/review/
    path(_('shop/review/'), views.review_list, name='review_list'),
    path(_('shop/review/<slug:review_id>/'), views.review_detail, name='review_detail'),
    path(_('shop/add_review/<int:produit_id>/'), views.add_review, name='add_review'),

    # ex: shop/profile/
    path('shop/profile/<slug:username>/', views.user_review_list, name='user_review_list'),
    path('shop/profile/', views.user_review_list, name='user_review_list'),

    # ex: shop/recommendation/ - get wine recommendations for the logged user
    path('shop/recommendation/', views.user_recommendation_list, name='user_recommendation_list'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
)
