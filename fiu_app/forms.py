from django import forms
from .models import HomePageDescription, Advertisement, Package
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class HomePageDescriptionForm(forms.ModelForm):
    """The home page post form."""
    description = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 30, 'rows': 10}))

    class Meta:
        model = HomePageDescription
        fields = ('title', 'description',)


class AdvertisementForm(forms.ModelForm):
    """The home page post form."""
    details = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 30, 'rows': 10}))

    class Meta:
        model = Advertisement
        fields = ('title', 'details', 'redirect_url')


class PackageForm(forms.ModelForm):
    """The package edit form."""
    description = forms.CharField(widget=TinyMCEWidget(attrs={'cols': 30, 'rows': 10}))

    class Meta:
        model = Package
        fields = ('name', 'description', 'price')
