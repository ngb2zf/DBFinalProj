from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from bandsapp.models import Bands, Hosts

class MyRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']
        # user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user


class Band_MyRegistrationForm(ModelForm):

    class Meta:
        model = Bands
        fields = ('b_name', 'b_email', 'b_phone','b_availability', 'b_price', 'b_bio', 'b_lat', 'b_lon')

    def save(self, commit=True):
        band = super(Band_MyRegistrationForm, self).save(commit=False)


        if commit:
            band.save()

        return band


    
    
