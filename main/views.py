<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from .models import Product,Restaurant
from .forms import ProductForm,RestaurantForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.decorators import allowed_users

def homepage(request):
    return render(request,'main/index.html')


#
# def ProductFormView(request):
#     if request.method=="POST":
#         product_form = ProductForm(data=request.POST)
#         if product_form.is_valid():
#             product=product_form.save()
#             if 'photo' in request.FILES:
#                 product.photo=request.FILES['photo']
#             product.save()
#         else:    #in case if there is error in validation of input data
#             print(product_form.errors)
#         return redirect("/restaurant")
#     else:      #in case if the method is not post
#         product_form=ProductForm()
#
#     context_dic={"product_form":product_form}
#     return render(request,"main/add_product.html",context_dic)
#
#
# def RestaurantFormView(request):
#     if request.method=="POST":
#         restaurant_form = RestaurantForm(data=request.POST)
#         if restaurant_form.is_valid():
#
#             restaurant=restaurant_form.save(commit=False)
#             restaurant.user = request.user
#             if 'photo' in request.FILES:
#                 restaurant.photo=request.FILES['photo']
#             restaurant.save()
#         else:    #in case if there is error in validation of input data
#             print(restaurant_form.errors)
#         return redirect("/restaurant")
#     else:      #in case if the method is not post
#         restaurant_form=RestaurantForm()
#
#     context_dic={"restaurant_form":restaurant_form}
#     return render(request,"main/add_restaurant.html",context_dic)





@method_decorator(login_required(login_url="/login/"), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['restaurant']),name='dispatch')
class RestaurantListView(ListView):
    context_object_name="restaurants"
    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)

# class RestaurantDetailView(DetailView):
#     context_object_name="restaurant_details"
#     model=Restaurant
@method_decorator(login_required(login_url="/login/"), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['restaurant']),name='dispatch')
class RestaurantCreateView(CreateView):
    fields=('name','description','photo','address','city','email','contact_number')
    model=Restaurant
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)


# class RestaurantUpdateView(UpdateView):
#     fields=("name","principal")
#     model=models.School


# class RestaurantDeleteView(DeleteView):
#     model=models.School
#     success_url=reverse_lazy("basic_app:school_list")
=======
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'main/index.html')
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
