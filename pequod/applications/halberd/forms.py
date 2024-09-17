from django import forms
from .models import User, user_level, user_status, user_type
from django.contrib.auth import authenticate, login, logout

class formUpdateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'names', 'lastname', 'lastname2', 'telephone', 'city' ]

        widgets = {
            'email': forms.TextInput(
                attrs= {
                    'placeholder': 'ingrese correo electronico'
                }
            )
        }


    #todo pone alguna restriccion o requisito conb el que deba cumplir el campo y los agrega directamente a los requisitos del form
    #def clean_telephone(self):
    #    phone = self.cleaned_data['telephone']
    #    if len(phone) != 10:
    #        raise forms.ValidationError('el numero de telefono debe tener 10 digitos')
    #    return phone


class formUserDetail(forms.Form):
    email = forms.EmailField()
    lastname = forms.CharField(max_length=200)
    lastname2 = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    user_status_name = forms.CharField(max_length=200)
    user_type_name = forms.CharField(max_length=200)
    user_level_name = forms.CharField(max_length=200)


class formUpdateUserlevel(forms.ModelForm):

    class Meta:
        model = user_level
        fields = ['user_level_name', 'user_level_description', 'user_level_assigned_number', 'user_level_assigned_letter', 'user_level_short_name', 'user_level_code_name' ]


class formNewUserLevel(forms.ModelForm):

    class Meta:
        model = user_level
        fields = ('__all__')


class formUpdateUserStatus(forms.ModelForm):

    class Meta:
        model = user_status
        fields = ['user_status_name', 'user_status_description', 'user_status_assigned_letter', 'user_status_short_name', 'user_status_code_name' ]


class formNewUserStatus(forms.ModelForm):

    class Meta:
        model = user_status
        fields = ('__all__')



class formUpdateUserType(forms.ModelForm):

    class Meta:
        model = user_type
        fields = ['user_type_name', 'user_type_description', 'user_type_short_name', 'user_type_code_name' ]


class formNewUserType(forms.ModelForm):

    class Meta:
        model = user_type
        fields = ('__all__')



class formNewUser(forms.ModelForm):

    password1 = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'ingresa contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'repetir contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Confirmar contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = ['email', 'names', 'lastname', 'lastname2', 'telephone', 'user_level', 'user_type']


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2',' las contraseñas deben coincidir')


class loginForm(forms.Form):

        
    email = forms.EmailField(
        label = 'Correo',
        required = True,
        widget = forms.EmailInput(
            attrs = {
                'placeholder': 'ingresa Correo'
            }
        )
    )

    password1 = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'ingresa contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(loginForm, self).clean()
        email = self.cleaned_data['email']
        password1 = self.cleaned_data['password1']
        if not authenticate(email = email, password= password1):
            raise forms.ValidationError('los datos son incorrectos')
        
        return self.cleaned_data
        
    