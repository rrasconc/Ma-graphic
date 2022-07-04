from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'name':'name', 'class':'form-control gt', 'id':'name', 'placeholder':'Tu nombre', 'data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label = "Email", widget=forms.EmailInput(
        attrs={'class':'form-control gt', 'name':'email', 'id':'email', 'placeholder':'Correo electrónico', 'data-rule':'email', 'data-msg':'Please enter a valid email'}
    ), min_length=3, max_length=100)
    message = forms.CharField(label = "Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control gt', 'name':'message', 'id':'message', 'rows':2, 'data-rule':'required', 'data-msg':'Please write something for us', 'placeholder':'Mensaje...'}
    ), min_length=10, max_length=1000)