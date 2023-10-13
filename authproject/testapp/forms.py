from django import forms 
class SignUpForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['username','password','email','firstname','lastname']
