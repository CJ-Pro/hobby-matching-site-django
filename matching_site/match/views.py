from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date
from django.utils.timezone import now


@login_required
def home(request):
    # Get logged in user Object
    logged_in = Profile.objects.filter(username=request.user)

    # Get logged in user item from QuerySet
    logged_in_user = logged_in.first()

    # Get all users excluding the logged in user ,filter common hobbies , then sort by count of common hobbies
    users = Profile.objects\
        .exclude(username=request.user)\
        .filter(hobbies__in=logged_in_user.hobbies.all()) \
        .annotate(common_hobbies_count=Count('hobbies')).order_by('-common_hobbies_count')

    # Check for AJAX request and return html data based on checked values
    if request.is_ajax():
        gender = None
        age1 = None
        age2 = None
        age_range_error = None
        filtered_users = None

        if request.GET.get('male') and request.GET.get('female'):
            filtered_users = users

        elif request.GET.get('male'):
            gender = request.GET.get('male')
            filtered_users = users.filter(gender=gender)

        elif request.GET.get('female'):
            gender = request.GET.get('female')
            filtered_users = users.filter(gender=gender)

        elif request.GET.get('age1') and request.GET.get('age2'):
            age1 = int(request.GET.get('age1'))
            age2 = int(request.GET.get('age2'))
            if age2 > age1 > 0:
                current = now().date()
                max_date = date(current.year - age1, current.month, current.day)
                min_date = date(current.year - age2, current.month, current.day)
                filtered_users = users.filter(date_of_birth__gte=min_date, date_of_birth__lte=max_date)
            else:
                age1 = None
                age2 = None
                age_range_error = "Error in given Age Range :("

        else:
            filtered_users = users

        context = {
            'users': filtered_users,
            'gender': gender,
            'age1': age1,
            'age2': age2,
            'age_range_error': age_range_error,
            'logged_in_user': logged_in_user,
        }
        return render(request, 'match/filter.html', context)

    # If request is not from AJAX
    context = {
        'users': users,
        'logged_in_user':  logged_in_user,
    }
    return render(request, 'match/home.html', context)

