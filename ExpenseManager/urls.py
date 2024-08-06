"""
URL configuration for ExpenseManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/add/',views.CategoryCreateView.as_view(),name="category-add"),
    path('category/<int:pk>/change/',views.CategoryUpdateView.as_view(),name="category-edit"),
    path('transactions/add/',views.TransactionCreateView.as_view(),name="transaction-add"),
    path('category/<int:pk>/remove/',views.CategoryDeleteView.as_view(),name="category-delete"),
    path('transactions/<int:pk>/change',views.TransactionsUpdateView.as_view(),name="transaction-edit"),
    path('transactions/<int:pk>/remove',views.TransactionDeleteView.as_view(),name="transaction-delete"),
    path('expense/summary/',views.ExpenseSummaryView.as_view(),name="summary"),
    path('transactions/summary/',views.TransationSummeryView.as_view(),name="transaction-summary"),
    path("chart/",views.ChartView.as_view(),name="chart"),
    path("register/",views.SignUpView.as_view(), name="signup"),
    path("signin/",views.SigninView.as_view(), name="signin"),
]
