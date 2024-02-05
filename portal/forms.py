from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Building, UserProfile

class ExtendedAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'id' : 'loginusername', 'name' : 'username', 'placeholder' : 'Username', 'type' : 'username', 'value' : '', 'tabindex' : '1',})
        self.fields['password'].widget.attrs.update({'class' : 'form-control', 'id' : 'loginPassword', 'name' : 'password', 'placeholder' : 'Password', 'type' : 'password', 'value' : '', 'tabindex' : '2',})



class AddBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ('cityName', 'streetName', 'houseNumber')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cityName'].widget.attrs.update({'class' :'form-control', 'id' : 'city', 'name' : 'city', 'placeholder' : 'City', 'type' : 'text', 'value' : '',})
        self.fields['streetName'].widget.attrs.update({'class' :'form-control', 'id' : 'street', 'name' : 'street', 'placeholder' : 'Street', 'type' : 'text', 'value' : '',})
        self.fields['houseNumber'].widget.attrs.update({'class' :'form-control', 'id' : 'house', 'name' : 'house', 'placeholder' : 'House', 'type' : 'text', 'value' : '',})


class UpdateBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ('cityName', 'streetName', 'houseNumber')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cityName'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateCity', 'name' : 'city_update', 'placeholder' : 'City', 'type' : 'text', 'value' : '',})
        self.fields['streetName'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateStreet', 'name' : 'street_update', 'placeholder' : 'Street', 'type' : 'text', 'value' : '',})
        self.fields['houseNumber'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateHouse', 'name' : 'house_update', 'placeholder' : 'House', 'type' : 'text', 'value' : '',})


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' :'form-control', 'id' : 'name', 'name' : 'name', 'placeholder' : 'Username', 'type' : 'hidden', 'value' : '0', 'required' : False})
        self.fields['first_name'].widget.attrs.update({'class' :'form-control', 'id' : 'name', 'name' : 'name', 'placeholder' : 'Name', 'type' : 'text', 'value' : '',})
        self.fields['last_name'].widget.attrs.update({'class' :'form-control', 'id' : 'surname', 'name' : 'surname', 'placeholder' : 'Surname', 'type' : 'text', 'value' : '',})


class AddProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('telephone', 'flatNumber', 'building')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telephone'].widget.attrs.update({'class' :'form-control', 'id' : 'telephone', 'name' : 'telephone', 'placeholder' : 'Telephone', 'type' : 'text', 'value' : '',})
        self.fields['building'].widget.attrs.update({'class' :'form-control', 'id' : 'building', 'name' : 'building', 'placeholder' : 'Building', 'type' : 'text', 'value' : '',})
        self.fields['flatNumber'].widget.attrs.update({'class' :'form-control', 'id' : 'flatNumber', 'name' : 'flatNumber', 'placeholder' : 'Flat', 'type' : 'text', 'value' : '',})


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateId', 'name' : 'name', 'placeholder' : 'Username', 'type' : 'hidden', 'value' : '0', 'required' : False})
        self.fields['first_name'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateName', 'name' : 'name', 'placeholder' : 'Name', 'type' : 'text', 'value' : '',})
        self.fields['last_name'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateSurname', 'name' : 'surname', 'placeholder' : 'Surname', 'type' : 'text', 'value' : '',})


class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('telephone', 'building', 'flatNumber')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telephone'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateTelephone', 'name' : 'telephone', 'placeholder' : 'Telephone', 'type' : 'text', 'value' : '',})
        self.fields['building'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateBuilding', 'name' : 'building', 'placeholder' : 'Building', 'type' : 'text', 'value' : '',})
        self.fields['flatNumber'].widget.attrs.update({'class' :'form-control', 'id' : 'formUpdateFlat', 'name' : 'flat', 'placeholder' : 'Flat', 'type' : 'text', 'value' : '',})