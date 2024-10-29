from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

class SetPasswordForm(forms.Form):
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput, max_length=128)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, max_length=128)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
