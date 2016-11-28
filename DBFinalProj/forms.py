from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from bandsapp.models import Bands, Hosts
from django.utils.translation import ugettext_lazy as _
import geocoder

class MyRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

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
        fields = ('b_name', 'b_email', 'b_phone','b_availability', 'b_price', 'b_bio', 'b_address')
        labels = {
            'b_name': _('Name'),
            'b_email': _('Email'),
            'b_phone': _('Phone'),
            'b_availability': _('Contact Hours'),
            'b_price': _('Price'),
            'b_bio': _('Biography'),
            'b_address': _('Address')
        }
        # widgets = {
        #     'b_name': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        #     'b_email': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        #     'b_phone': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        #     'b_availability': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        #     'b_price': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        #     'b_bio': forms.Textarea(attrs={'class': 'formsTableStyle'}),
        #     'b_lat': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        #     'b_lon': forms.TextInput(attrs={'class': 'formsTableStyle'}),
        # }

    def save(self, commit=True):


        band = super(Band_MyRegistrationForm, self).save(commit=False)

        #import geocoder
        #g = geocoder.google('Mountain View, CA')
        #g.latlng

        g = geocoder.google(band.b_address)

        band.b_lat, band.b_lon = g.latlng
        

        if commit:
            band.save()

        return band


class Host_MyRegistrationForm(ModelForm):

    class Meta:
        model = Hosts
        fields = ('h_name', 'h_email', 'h_phone','h_availability')
        labels = {
            'h_name': _('Name'),
            'h_email': _('Email'),
            'h_phone': _('Phone'),
            'h_availability': _('Contact Hours'),
        }

    def save(self, commit=True):
        host = super(Host_MyRegistrationForm, self).save(commit=False)


        if commit:
            host.save()

        return host


    
    
