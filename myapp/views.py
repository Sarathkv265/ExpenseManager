from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from myapp.forms import CategoryForm,TransactionsForm,TransactionFilterForm,RegisterForm,LoginForm

from django.utils import timezone

from myapp.models import Category,Transactions

from django.db.models import Sum



class CategoryCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance = CategoryForm()

        qs=Category.objects.all()

        return render(request,"category_add.html",{"form":form_instance,"categories":qs})
    
    def post(self,request,*args,**kwargs):

        form_instance=CategoryForm(request.POST)

        if form_instance.is_valid():

            # data=form_instance.cleaned_data

            # Category.objects.create(**data)

            form_instance.save()

            return redirect("category-add")
        
        else:

            return render(request,"category_add.html",{"form":form_instance}) 
        

class CategoryUpdateView(View):


    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        category_object=Category.objects.get(id=id)

        form_instance=CategoryForm(instance=category_object)

        return render(request,"category_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        cat_obj=Category.objects.get(id=id)

        form_instance=CategoryForm(request.POST,instance=cat_obj)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("category-add")
        else:
            
            return render(request,"category_edit.html",{"form":form_instance})
        

class CategoryDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Category.objects.get(id=id).delete()

        return redirect("category-add")
        

class TransactionCreateView(View):

    def get(self,request,*args,**kwargs):
        
        form_instance=TransactionsForm()

        cur_month=timezone.now().month

        cur_year=timezone.now().year

        qs=Transactions.objects.filter(created_date__month=cur_month,created_date__year=cur_year)

        return render(request,"transaction_add.html",{"form":form_instance,"transactions":qs})
    
    def post(self,request,*args,**kwargs):

        form_instance=TransactionsForm(request.POST)

        if form_instance.is_valid():
            
            form_instance.save()

            return redirect("transaction-add")
        
        else:

            return render(request,"transaction_add.html",{"form":form_instance})
        

class TransactionsUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        trans_obj=Transactions.objects.get(id=id)

        form_instance=TransactionsForm(instance=trans_obj)

        return render(request,"transaction_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        trans_obj=Transactions.objects.get(id=id)

        form_instance=TransactionsForm(request.POST,instance=trans_obj)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("transaction-add")
        else:
            
            return render(request,"transaction_edit.html",{"form":form_instance})



class TransactionDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Transactions.objects.get(id=id).delete()

        return redirect("transaction-add")
    
class ExpenseSummaryView(View):

    def get(Self,request,*args,**kwargs):

        cur_month=timezone.now().month

        cur_year=timezone.now().year

        qs=Transactions.objects.filter(created_date__month=cur_month,created_date__year=cur_year)

        total_expense=qs.values("amount").aggregate(total=Sum("amount"))
        
        category_summary=qs.values("category_object__name").annotate(total=Sum("amount"))

        payment_summary=qs.values("payment_method").annotate(total=Sum("amount"))


        
        print(payment_summary)

        data={
            "total_expense":total_expense.get("total"),
            "category_summary":category_summary,
            "payment_summary":payment_summary
            
        }


        return render(request,"expense_summary.html",data)
class TransationSummeryView(View):
    
    def get(self,request,*args,**kwargs):
        
        form_instance=TransactionFilterForm()
        
        cur_month=timezone.now().month
        cur_year=timezone.now().year
        
        if "start_date" in request.GET and "end_date" in request.GET:
            st_date = request.GET.get("start_date")
            ed_date = request.GET.get("end_date")
            
            qs=Transactions.objects.filter(created_date__range=(st_date,ed_date))
            
        else:
            qs=Transactions.objects.filter(created_date__month=cur_month,created_date__year=cur_year)
        
        total_expense=qs.values("amount").aggregate(total=Sum("amount"))
        data={"total_expense":total_expense.get("total"),
               "transactions":qs,"form":form_instance}
        
        return render(request,"transation_summary.html",data)
    
    
class ChartView(View):
    def get(self,request,*args,**kwargs):
        
        return render(request,"chart.html")
    


class SignUpView(View):
    
    def get(self,request,*args,**kwargs):
        
        form_instance = RegisterForm()
        
        return render(request,"register.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance= RegisterForm(request.POST)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            print("account created sucessfully")
            
            return redirect("signup")
        
        else:
            
            print("failed to create account")
            return render(request,"register.html",{"form":form_instance})
        
        
class SigninView(View):
    
    def get(self,request,*args,**kwargs):
        
        form_instance = LoginForm()
        
        return render(request,"signin.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        from_instance = LoginForm(request.POST)
        
        if from_instance.is_valid():
            
            data = from_instance.cleaned_data()
            
            u_name = data.get("username")
            pwd = data.get("password")
    
        


# > __gt (grater than)
# < __lt (less then)
# >=__gte 
# >=__lte









