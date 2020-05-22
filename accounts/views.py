from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import (TemplateView, FormView)
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import json
from django.shortcuts import get_object_or_404
from .forms import RegisterForm, LoginForm, PhoneVerificationForm
from .authy_api import send_verfication_code, verify_sent_code
from .models import User
<<<<<<< HEAD
from django.contrib.auth.models import Group
from .decorators import allowed_users
=======

>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866

class IndexView(TemplateView):

    template_name = 'accounts/index.html'


class RegisterView(SuccessMessageMixin, FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_message = "One-Time password sent to your registered mobile number.\
                        The verification code is valid for 10 minutes."

    def form_valid(self, form):
<<<<<<< HEAD

        user=self.request.POST

=======
        # user = form.save()
        user=self.request.POST
        # print(user)
        # username = self.request.POST['username']
        # password = self.request.POST['password1']
        # user = authenticate(username=username, password=password)
        # print(user.message)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        try:
            response = send_verfication_code(user)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR,
                                'verification code not sent. \n'
                                'Please re-register.')
            return redirect('/register')
        data = json.loads(response.text)

<<<<<<< HEAD
        # print(response.status_code, response.reason)
        # print(response.text)
        # print(data['success'])
=======
        print(response.status_code, response.reason)
        print(response.text)
        print(data['success'])
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        if data['success'] == False:
            messages.add_message(self.request, messages.ERROR,
                            data['message'])
            return redirect('/register')

        else:
            kwargs = {'user': user}
<<<<<<< HEAD
            # print("this is kwargs under register view")
            # print(kwargs)
=======
            print("this is kwargs under register view")
            print(kwargs)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
            self.request.method = 'GET'
            return PhoneVerificationView(self.request,**kwargs)







def view1(request):
<<<<<<< HEAD
    if request.user.is_authenticated:
        return redirect('/')
    # print("under view1 login get request")
=======
    print("under view1 login get request")
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
    return render(request,'accounts/login.html')

def resend_url(request,phone_number,country_code):

    user={"phone_number":phone_number,"country_code":country_code}
    try:
        response = send_verfication_code(user)
        pass
    except Exception as e:

<<<<<<< HEAD
        # print("Exception while sending verification code")
=======
        print("Exception while sending verification code")
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        messages.add_message(request, messages.ERROR,
                'verification code not sent. \n'
                )
        return redirect('/login')
    data = json.loads(response.text)

    if data['success'] == False:
<<<<<<< HEAD
=======




>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        messages.add_message(request, messages.ERROR,
        data['message'])
        return redirect('/login')

<<<<<<< HEAD
    # print(response.status_code, response.reason)
    # print(response.text)
    if data['success'] == True:

        request.method = "GET"
        # print(request.method)
=======
    print(response.status_code, response.reason)
    print(response.text)
    if data['success'] == True:

        request.method = "GET"
        print(request.method)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        kwargs = {'user':user}
        dict={'user':user}
        return PhoneVerificationView(request,**kwargs)


def LoginView(request):
<<<<<<< HEAD


    # print("under view1 login get request")
    template_name='accounts/login.html'
    # print("Inside login 1")
    if request.method == "POST":
        # print("Inside login post method")
=======
    print("under view1 login get request")
    template_name='accounts/login.html'
    print("Inside login 1")
    if request.method == "POST":
        print("Inside login post method")
        # username = request.POST['username']
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        user=request.POST
        userob = User.objects.filter(phone_number=user['phone_number'])
        if userob:
            try:
                response = send_verfication_code(user)
                pass
            except Exception as e:
<<<<<<< HEAD
                # print("Exception while sending verification code")
=======
                print("Exception while sending verification code")
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
                messages.add_message(request, messages.ERROR,
                        'verification code not sent. \n'
                        'Please retry logging in.')
                return redirect('/login')
            data = json.loads(response.text)

            if data['success'] == False:
<<<<<<< HEAD
                    # print("If verifiacation code is not sent by twilio")
=======
                    print("If verifiacation code is not sent by twilio")
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
                    messages.add_message(request, messages.ERROR,
                    data['message'])
                    return redirect('/login')

<<<<<<< HEAD
            # print(response.status_code, response.reason)
            # print(response.text)
            if data['success'] == True:
                # print("if verification code is sent by twilio")
                request.method = "GET"
                # print(request.method)
=======
            print(response.status_code, response.reason)
            print(response.text)
            if data['success'] == True:
                print("if verification code is sent by twilio")
                request.method = "GET"
                print(request.method)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
                kwargs = {'user':user}
                dict={'user':user}
                return PhoneVerificationView(request,**kwargs)
            else:
                messages.add_message(request, messages.ERROR,
                data['message'])
                return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR,
                    'User does not exist. \n'
                    'Please register.')
            return redirect('/register')

    else:
        return HttpResponse("Not Allowed")




<<<<<<< HEAD
=======
# class LoginView(View):
#     template_name = 'accounts/login.html'
#
#     form_class =LoginForm
#     print("under login view")
#     # success_message = "One-Time password sent to your registered mobile number.\
#     #                     The verification code is valid for 10 minutes."
#
#     def post(self,request):
#         print("under post method")
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user=self.request.POST
#             print(user)
#
#             try:
#                 response = send_verfication_code(user)
#             except Exception as e:
#                 messages.add_message(self.request, messages.ERROR,
#                                 'verification code not sent. \n'
#                                 'Please re-login.')
#                 return redirect('/login')
#             data = json.loads(response.text)
#
#             print(response.status_code, response.reason)
#             print(response.text)
#             print(data['success'])
#             if data['success'] == False:
#                 messages.add_message(self.request, messages.ERROR,
#                                 data['message'])
#                 return redirect('/login')
#
#             else:
#                 kwargs = {'user': user}
#                 print("this is kwargs under register view")
#                 print(kwargs)
#                 self.request.method = 'GET'
#                 return PhoneVerificationView(self.request,**kwargs)
#



    #
    #
    # def get(self,request):
    #     print("under get method")
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866








flag=False
user_for_phone_confirmation={}
def PhoneVerificationView(request, **kwargs):
    template_name = 'accounts/phone_confirm.html'
    global flag,user_for_phone_confirmation
    if flag==False and user_for_phone_confirmation=={} and kwargs!={}:
<<<<<<< HEAD
        # print(kwargs['user'])
=======
        print(kwargs['user'])
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
        user_for_phone_confirmation=kwargs['user']
        flag=True




    if request.method == "POST":
        flag=False
        phone_number = request.POST['phone_number']
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            user=user_for_phone_confirmation
            verification_code = request.POST['one_time_password']
            response = verify_sent_code(verification_code, user)
<<<<<<< HEAD
            # print(response.text)
=======
            print(response.text)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
            data = json.loads(response.text)

            if data['success'] == True:
                # flag=False
                try:
                    already=User.objects.get(phone_number=phone_number)
                except:
                    already=None
                if already:
                    login(request, already)
<<<<<<< HEAD
                    if already.groups.filter(name='restaurant').exists():
                        return redirect('/restaurant')

=======
                    # if user.phone_number_verified is False:
                    #     user.phone_number_verified = True
                        # user.save()
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
                    return redirect('/index')


                else:
                    userob=User.objects.create(full_name=user['full_name'],
                                            phone_number=user['phone_number'],
                                            country_code=user['country_code'])
<<<<<<< HEAD
                    group = Group.objects.get(name='customer')
                    userob.groups.add(group)
                    # print(userob)
=======
                    print(userob)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
                    login(request, userob)
                    return redirect('/index')
            else:
                messages.add_message(request, messages.ERROR,
                                data['message'])
                user_for_phone_confirmation=user
                return render(request, template_name, {'user':user})
        else:
            context = {
                'user': user,
                'form': form,
            }
            return render(request, template_name, context)

    elif request.method == "GET":
        try:
            user = kwargs['user']
            return render(request, template_name, {'user': user})
        except Exception as e:
<<<<<<< HEAD
            # print("This is Exception")
            # print(e)
=======
            print("This is Exception")
            print(e)
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
            return HttpResponse("Not Allowed")



<<<<<<< HEAD
=======
# class LoginView(FormView):
#
#     template_name = 'login.html'
#     form_class = LoginForm
#     success_url = '/dashboard'
#     print('before dispatch')
#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             messages.add_message(self.request, messages.INFO,
#                                 "User already logged in")
#             return redirect('/dashboard')
#         else:
#             return super().dispatch(request, *args, **kwargs)
#
#
#     print('after dispatch')
#     def form_valid(self, form):
#         user = form.save()
#         # user=User.object.get(phone_number)
#         # print(user.two_factor_auth)
#         # if user.two_factor_auth is False:
#         #     login(self.request, user)
#         #     return redirect('/dashboard')
#         # else:
#
#
#         try:
#             response = send_verfication_code(user)
#             pass
#         except Exception as e:
#             messages.add_message(self.request, messages.ERROR,
#                                 'verification code not sent. \n'
#                                 'Please retry logging in.')
#             return redirect('/login')
#         data = json.loads(response.text)
#
#         if data['success'] == False:
#             messages.add_message(self.request, messages.ERROR,
#                             data['message'])
#             return redirect('/login')
#
#         print(response.status_code, response.reason)
#         print(response.text)
#         if data['success'] == True:
#             self.request.method = "GET"
#             print(self.request.method)
#             kwargs = {'user':user}
#             return PhoneVerificationView(self.request, **kwargs)
#         else:
#             messages.add_message(self.request, messages.ERROR,
#                     data['message'])
#             return redirect('/login')

#
# def view1(request):
#     return render(request,'accounts/login.html')
#
# def LoginView(request):
#     template_name='accounts/login.html'
#
#     if request.method == "POST":
#         # username = request.POST['username']
#         phone_number = request.POST['phone_number']
#         user = User.objects.get(phone_number=phone_number)
#         if user:
#             try:
#                 response = send_verfication_code(user)
#                 pass
#             except Exception as e:
#                 messages.add_message(request, messages.ERROR,
#                         'verification code not sent. \n'
#                         'Please retry logging in.')
#                 return redirect('/login')
#             data = json.loads(response.text)
#
#             if data['success'] == False:
#                     messages.add_message(request, messages.ERROR,
#                     data['message'])
#                     return redirect('/login')
#
#             print(response.status_code, response.reason)
#             print(response.text)
#             if data['success'] == True:
#                 request.method = "GET"
#                 print(request.method)
#                 kwargs = {'user':user}
#                 dict={'user':user}
#                 return PhoneVerificationView(request,**kwargs)
#             else:
#                 messages.add_message(request, messages.ERROR,
#                 data['message'])
#                 return redirect('/login')
#         else:
#             return redirect('/login')
#
#
#     else:
#         return HttpResponse("Not Allowed")

>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866




@method_decorator(login_required(login_url="/login/"), name='dispatch')
class DashboardView(SuccessMessageMixin, View):
    template_name = 'accounts/dashboard.html'

    def get(self, request):
        context = {
            'user':self.request.user,
            }
<<<<<<< HEAD
        return render(self.request, self.template_name, {})


@login_required
@allowed_users(allowed_roles=['restaurant'])
def RestaurantView(request):
    template_name="accounts/restaurant.html"
    return render(request,template_name)





# @method_decorator(login_required(login_url="/login/"),name='dispatch')
# @method_decorator(allowed_users(allowed_roles=['restaurant']),name='dispatch')
# class RestaurantView(LoginRequiredMixin,View):
#     template_name="accounts/restaurant.html"
#
#     def get(self,request):
#
#         # restaurant_owner=User.objects.filter(request.user)
#         return render(self.request,self.template_name)   #{'user':restaurant_owner}
=======
        # if not request.user.phone_number_verified:
        #     messages.add_message(self.request, messages.INFO,
        #                         "User Not verified.")
        # return render(self.request, self.template_name, context)

    # def post(self, request):
    #     if 'two_factor_auth' in request.POST:
    #         if request.user.two_factor_auth:
    #             request.user.two_factor_auth = False
    #         else:
    #             request.user.two_factor_auth = True
    #         request.user.save()

        return render(self.request, self.template_name, {})
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
