from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Advertisement, HomePageDescription, Package, Photo, Gallery
from .forms import HomePageDescriptionForm, AdvertisementForm, PackageForm
from django.shortcuts import get_object_or_404


def home(request):
    """The view for the landing page."""
    advertisements = Advertisement.objects.all().order_by('-created_date')
    home_page_posts = HomePageDescription.objects.all()
    return render(request, 'general/home.html', {'advertisements': advertisements, 'posts': home_page_posts})


def home_body_edit(request, pk):
    """Edit the home page body."""
    home_page_desc = get_object_or_404(HomePageDescription, pk=pk)
    if request.method == "POST":
        form = HomePageDescriptionForm(request.POST, instance=home_page_desc)
        if form.is_valid():
            home_page_desc = form.save(commit=False)
            home_page_desc.author = request.user
            home_page_desc.published_date = timezone.now()
            home_page_desc.save()
            return redirect('home')
    else:
        form = HomePageDescriptionForm(instance=home_page_desc)

    return render(request, 'forms/home_body_edit.html', {'form': form})


def galleries(request):
    """The view that lists the various image galleries."""
    image_galleries = [gallery for gallery in Gallery.objects.all() if gallery.is_published()]
    messages.debug(request, "Pulled {} galleries".format(len(image_galleries)))
    print("Pulled {} galleries".format(len(image_galleries)))
    return render(request, 'general/galleries.html', {'image_galleries': image_galleries})


def gift_certificates(request):
    """Page displaying all of the available gift certificates."""
    return render(request, 'general/gift_certificates.html')


def packages(request):
    """Page displaying all of the available packages."""
    packages = Package.objects.all().order_by('-price')
    return render(request, 'general/packages.html', {'packages': packages})


def facilities(request):
    """Page displaying all of the available facilities."""
    return render(request, 'general/facilities.html')


def faq(request):
    """Page displaying some of the more common questions."""
    return render(request, 'general/faq.html')


def contact_us(request):
    """Page displaying the provided contact information."""
    return render(request, 'general/contact_us.html')


def ad_new(request):
    """Add a new advertisement."""
    if request.method == "POST":
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            desc = form.save(commit=False)
            desc.author = request.user
            desc.published_date = timezone.now()
            desc.save()
            return redirect('home')
    else:
        form = AdvertisementForm()
    return render(request, 'forms/ad_edit.html', {'form': form})


def ad_remove(request, pk):
    """Remove an advertisement."""
    ad = get_object_or_404(Advertisement, pk=pk)
    ad.delete()
    return redirect('home')


def ad_edit(request, pk):
    """Edit an advertisement."""
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.published_date = timezone.now()
            ad.save()
            return redirect('home')
    else:
        form = AdvertisementForm(instance=ad)

    return render(request, 'forms/ad_edit.html', {'form': form})


def package_new(request):
    """Add a new package."""
    if request.method == "POST":
        form = PackageForm(request.POST)
        if form.is_valid():
            desc = form.save(commit=False)
            desc.author = request.user
            desc.published_date = timezone.now()
            desc.save()
            return redirect('packages')
    else:
        form = PackageForm()
    return render(request, 'forms/package_edit.html', {'form': form})


def package_remove(request, pk):
    """Remove an advertisement."""
    package = get_object_or_404(Package, pk=pk)
    package.delete()
    return redirect('packages')


def package_edit(request, pk):
    """Edit an advertisement."""
    package = get_object_or_404(Package, pk=pk)
    if request.method == "POST":
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            package = form.save(commit=False)
            package.author = request.user
            package.published_date = timezone.now()
            package.save()
            return redirect('packages')
    else:
        form = PackageForm(instance=package)

    return render(request, 'forms/package_edit.html', {'form': form})
