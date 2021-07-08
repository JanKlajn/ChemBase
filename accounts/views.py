from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import LoginForm, CreateUserForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', 'index'))
            return render(request, 'form.html', {'form': form, 'message': 'wrong login data'})
        return render(request, 'form.html', {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class CreateUserView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateUserView(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        else:
            return render(request, 'form.html', {'form': form})



