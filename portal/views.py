from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .forms import AddBuildingForm, UpdateBuildingForm, AddUserForm, AddProfileForm, UpdateUserForm, UpdateProfileForm
from .models import Building, UserProfile, Counter
from cyrtranslit import to_latin


@login_required
# @staff_member_required
def home(request):
    return render(request, 'portal/index.html')


@login_required
# @staff_member_required
def buildings_list(request):
    add_form = AddBuildingForm()
    update_form = UpdateBuildingForm()
    all_buildings = Building.objects.all()
    context = {'add_form' : add_form, 'all_buildings' : all_buildings, 'update_form' : update_form, }
    return render(request, 'portal/buildings.html', context)

@login_required
@require_POST
# @staff_member_required
def add_building(request):
    form = AddBuildingForm(request.POST)
    form.save()
    return redirect('buildings_list')


@login_required
@require_POST
# @staff_member_required
def update_building(request, building_id = 0):
    form = UpdateBuildingForm(request.POST)
    if form.is_valid():
        Building.objects.filter(id=building_id).update(cityName=form.cleaned_data['cityName'], streetName=form.cleaned_data['streetName'], houseNumber=form.cleaned_data['houseNumber'])
    return redirect('buildings_list')


@login_required
# @staff_member_required
def delete_building(request, building_id = 0):
    Building.objects.get(pk=building_id).delete()
    return redirect('buildings_list')


@login_required
# @staff_member_required
def users_list(request):
    add_user_form = AddUserForm()
    add_user_profile_form = AddProfileForm()
    update_user_form = UpdateUserForm()
    update_user_profile_form = UpdateProfileForm()
    all_users = User.objects.all()
    all_buildings = Building.objects.all()
    all_profiles = UserProfile.objects.all().values()
    for profile in all_profiles:
        profile['first_name'] = all_users.filter(id = profile['user_id'])[0].first_name #TODO: enhance it, not to call [0], it should be always just one item in the list, but anyway
        profile['last_name'] = all_users.filter(id = profile['user_id'])[0].last_name
        profile['building'] = f"{all_buildings.filter(id = profile['building_id'])[0].cityName}, {all_buildings.filter(id = profile['building_id'])[0].streetName}, {all_buildings.filter(id = profile['building_id'])[0].houseNumber}"
    context = {'add_user_form' : add_user_form, 'add_user_profile_form' : add_user_profile_form, 'all_users' : all_users, 'all_profiles' : all_profiles, 'all_buildings' : all_buildings, 'update_user_form': update_user_form, 'update_user_profile_form' : update_user_profile_form }
    return render(request, 'portal/users.html', context)


@require_POST
@login_required
# @staff_member_required
def add_user(request):
    if request.method == "POST":
        user_form = AddUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            translated_first_name = to_latin(user.first_name, 'ru').replace("'",'')
            translated_last_name = to_latin(user.last_name, 'ru').replace("'",'')
            user.username = f"{translated_first_name}_{translated_last_name}"
            user.set_password('Password12')
            user.save()
        profile_form = AddProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('users_list')
    

@login_required
# @staff_member_required
def delete_profile(request, profile_id):
    UserProfile.objects.get(pk=profile_id).delete()
    return redirect('users_list')


@login_required
@require_POST
# @staff_member_required
def update_user(request, profile_id = 0):
    if request.method == "POST":
        profile_form = UpdateProfileForm(request.POST)
        if profile_form.is_valid():
            profile = UserProfile.objects.filter(id=profile_id)
            user_id = profile[0].user_id
            UserProfile.objects.filter(id=profile_id).update(telephone=profile_form.cleaned_data['telephone'], building_id=profile_form.cleaned_data['building'], flatNumber=profile_form.cleaned_data['flatNumber'])
        user_form = UpdateUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            translated_first_name = to_latin(user.first_name, 'ru').replace("'",'')
            translated_last_name = to_latin(user.last_name, 'ru').replace("'",'')
            user.username = f"{translated_first_name}_{translated_last_name}"
            User.objects.filter(id=user_id).update(username=user.username, first_name=user.first_name, last_name=user.last_name)
        return redirect('users_list')
    

@login_required
# @staff_member_required
def profile_counters(request, user_profile_id):
    print(user_profile_id)
    counters = Counter.objects.filter(profile_id=user_profile_id)
    profile_data = UserProfile.objects.get(pk=user_profile_id)
    user_id = profile_data.user_id
    user_data = User.objects.get(pk=user_id)
    context = {'counters' : counters, 'profile_data' : profile_data, 'user_data' : user_data}
    return render(request, 'portal/profile_counters.html', context)