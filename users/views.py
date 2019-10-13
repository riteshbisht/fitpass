from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .forms import LoginForm, RegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from users.models import UserRoles, UserProfile, User

class CustomLoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context=context)


    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        login_form = LoginForm(request.POST)
        custom_errors = {}
        if login_form.is_valid():
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                context = {
                    'login_form': login_form,
                    'custom_errors': custom_errors
                }
                custom_errors = {'errors': 'Invalid Credentials'}
                context.update(custom_errors)
                return render(request, 'login.html', context=context)
        else:
            context = {
                'login_form': login_form,
                'custom_errors': custom_errors
            }
            return render(request, 'login.html', context=context)



class RegisterView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request, *args, **kwargs):
        register_form = RegisterForm(request.POST)
        context = {
            'register_form': register_form
        }
        if register_form.is_valid():
            register_form.save()
            email = register_form.cleaned_data.get('email')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            role = register_form.cleaned_data['role']
            gender = register_form.cleaned_data.get('gender')
            marital_status = register_form.cleaned_data.get('marital_status')
            UserRoles.objects.create(user=user, role=role)
            UserProfile.objects.create(
                user=user, gender=gender, marital_status=marital_status
            )
            login(request, user)
            return redirect('/')
        else:
            context = {
                'register_form': register_form,
            }
            return render(request, 'register.html', context=context)  
        return render(request, 'register.html', context=context)


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        user_profile = user.user_profile
        user_profile_form = UserProfileForm(instance=user_profile)
        context = {
            'user_profile_form': user_profile_form,
            'user': user
        }
        return render(request, 'user_profile.html', context=context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        user_profile = user.user_profile
        user_profile_form = UserProfileForm(instance=user_profile, data=request.POST)
        if user_profile_form.is_valid():
            user_profile_form.save()

        context = {
            'user_profile_form': user_profile_form
        }

        return render(request, 'user_profile.html', context=context)


