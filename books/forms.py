from django import forms
from .models import User,Login,Inventory

class SignupForm(forms.ModelForm):
    collegename = forms.CharField(label = "College Name")
    password = forms.CharField(widget=forms.PasswordInput)
    retypepassword = forms.CharField(widget=forms.PasswordInput,label='Re-enter Password')

    class Meta:
        model = User
        fields = ["username","collegename","email","phonenumber","address","password","retypepassword"]

    def clean(self):
        cleaned_data = super().clean()

        data = self.cleaned_data

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('retypepassword')
        emailid = self.cleaned_data.get('email')
        phonenumber = self.cleaned_data.get('phonenumber')

        result = User.objects.filter(email = emailid)
        if result:
            raise forms.ValidationError("Already Registered!!Try another Email")

        if len(password1)<8 or len(password2)<8:
            raise forms.ValidationError("Length of password must be more than 8")

        if len(phonenumber)<10 or phonenumber.isdigit() == False:
            raise forms.ValidationError("Invalid Phonenumber")

        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return data

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ["email","password"]

    def clean(self):
        cleaned_data = super().clean()

        data = self.cleaned_data

        password = self.cleaned_data.get('password')
        emailid = self.cleaned_data.get('email')

        result = User.objects.filter(email = emailid,password = password)
        if not result:
            raise forms.ValidationError("User not Registered or Invalid Credentials")

        return data

class InventoryForm(forms.ModelForm):
    productname = forms.CharField(label = "Product Name")
    productquantity = forms.CharField(label = "Number of Products")

    class Meta:
        model = Inventory
        fields = ["productname","productquantity"]

    def clean(self):
        cleaned_data = super().clean()

        data = self.cleaned_data

        productname = self.cleaned_data.get('productname')
        productquantity = self.cleaned_data.get('productquantity')

        return data
