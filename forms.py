from django import forms

from contact_module.models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='Full Name',
        max_length=50,
        error_messages={
            'required': 'بنویس'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'name'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'email'
        })
    )
    title = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'عنوان'
        })
    )
    massage = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                # 'rows':'5',
                'id': 'message'

        })
    )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'massage']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class':'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'massage': forms.TextInput(attrs={
                'class': 'form-control',
                'id':'message'
            })
        }

        error_messages = {
            'full_name': {
                'required':'haroomi bezan'
            }
        }
