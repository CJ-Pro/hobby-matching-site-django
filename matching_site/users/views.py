from django.shortcuts import render,redirect
from django.contrib import messages
from match.models import Profile
from .forms import UserRegisterForm,ImageUpdateForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            # Save form for user , use get_user variable to create profile based on One-to-One relationship
            get_user = form.save()

            get_gender = form.cleaned_data.get('gender')
            get_date_of_birth = form.cleaned_data.get('date_of_birth')
            username = form.cleaned_data.get('username')
            get_hobbies = form.cleaned_data.get('hobbies')

            messages.success(request, f'Account created for {username} , You can now Log In! ')

            # Create new Profile from form data
            user = Profile.objects.create(
                username=get_user,
                gender=get_gender,
                date_of_birth=get_date_of_birth,
            )

            # Set hobbies from form data after profile was created
            user.hobbies.set(get_hobbies)

            return redirect('match-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'register_form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        image_form = ImageUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if image_form.is_valid():
            image_form.save()
            messages.success(request, f'Image successfully updated :)')
            return redirect('match-profile')
    else:
        image_form = ImageUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'image_form': image_form})
