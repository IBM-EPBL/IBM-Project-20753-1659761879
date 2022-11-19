from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


from .models import Profile
from django.forms import ModelForm, CharField, IntegerField, ChoiceField, NumberInput

CustomUser = get_user_model()
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class ProfileForm(ModelForm):
        # specialization =  CharField(widgets = CharField(attrs={'placeholder': 'Enter your Field of specialization','maxlength':50})),
        # interested_domain =  CharField(widgets = CharField( attrs={'placeholder': 'enter your interested domain. ex: Web development','maxlength':300})),
        # skills =  CharField(widgets = CharField(attrs={'placeholder': 'Enter your skills example, Ex: python','maxlength':200})),
        # address1 =  CharField(widgets = CharField(attrs={'placeholder': 'address1', 'maxlength':400})),
        # address2 = CharField(widgets = CharField(attrs={'placeholder': 'address2', 'maxlength':400})),
        # country = CharField(widgets = CharField(attrs={'placeholder': 'Country', 'maxlength':100})),
        # pincode =  NumberInput(widgets = NumberInput( attrs={'placeholder': 'Enter the pincode','maxlength': 6 })),
        # gender = ChoiceField()
        class Meta:
            model = Profile
            fields =  ['specialization', 'interested_domains', 'skills', 'address1', 'address2','country', 'pincode', 'gender']

        

        
         
        

        