# _*_ coding: utf-8 _*_

__author__ = 'Rick'
__date__ = '08/09/2021 17:03'

from django.urls import path, re_path, include
from django.views.generic import TemplateView
from .views import Transaction_HistoryView,Income_HistoryView,Author_PoolView,Transaction_History_DetailsView

urlpatterns = [
    path("transation_history", Transaction_HistoryView.as_view(), name='transation_history'),
    path('transation_history/<int:transaction_id>', Transaction_History_DetailsView.as_view(), name='transation_history-details'),
    path("income_history", Income_HistoryView.as_view(), name='income_history'),
    path("author_pool", Author_PoolView.as_view(), name='author_pool'),
]

