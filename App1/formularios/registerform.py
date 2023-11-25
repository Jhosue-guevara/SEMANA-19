from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True,label="Grupo")

    class Meta:
        model = User
        fields = ("username","email","password1","password2","group")
    
    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.groups.add(self.cleaned_data['group'])
        return User