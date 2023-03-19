from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('food:main'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Вы успешно зарегестрировались')
                return HttpResponseRedirect(reverse('users:login'))
            except:
                messages.error(request, 'Пользователь с такими данными уже существует')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('food:main'))


@login_required(login_url='users:login')
def profile(request):
    user = request.user

    subscription = user.subscription
    allergy_to = user.allergy_to.all().values_list('title', flat=True)
    context = {
        'user': user,
        'allergy': allergy_to
    }

    if subscription:
        context['subscription'] = subscription.title
        context['subscription_detail'] = subscription.description

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            if request.POST.get('password1') != request.POST.get('password2'):
                messages.error(request, 'Пароли не совпадают!')
            else:
                try:
                    form.save()
                    return HttpResponseRedirect(reverse('users:profile'))
                except:
                    messages.error(request, 'Пользователь с такими данными уже существует')

    else:
        form = UserProfileForm(instance=user)

    context['form'] = form

    return render(request, 'users/lk.html', context=context)
