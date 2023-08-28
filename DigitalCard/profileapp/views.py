from django.shortcuts import render, redirect
from . import models 
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")    
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        # Kullanıcı oluşturulduğunda profil de oluşturulacak
        create_user_profile(self.request, self.object)
        return response
    
def homepage(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request,"profileapp/home.html", context={"users": users})


def create_user_profile(request, username):
    # Bu fonksiyon kullanıcının profili oluşturur
    models.Profile.objects.create(user=username)

def viewProfile(request,username):
    profile = get_object_or_404(models.Profile, user__username=username)  
    context = {'profile': profile}
    return render(request,"profileapp/profile.html", context=context)

@login_required
def update_profile(request):
    user = request.user
    profile = get_object_or_404(models.Profile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('viewProfile', args=[user.username]))  # Profil sayfasına yönlendirme yapabilirsiniz
    else:
        return render(request, 'profileapp/updateprofile.html')

    context = {'profile': profile}
    return render(request, 'profileapp/updateprofile.html', context)
