# -*- coding: utf-8 -*-
"""Created by Paul Hahn 2018-09-26."""
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from django.conf import settings
import os


class Address(models.Model):
    """Start address model."""

    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()


class Contact(models.Model):
    """Model object to store generic contact information for various use cases.
    
    Example use cases would include contact information for facilities and Physicians.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone_number = models.IntegerField()
    description = HTMLField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Persist the contact model and apply the created date."""
        self.updated_date = timezone.now()
        if not self.created_date:
            self.created_date = timezone.now()

        super(Contact, self).save(*args, **kwargs)
        return 'Contact.save'


class Facility(models.Model):
    """Generic model to store facility information."""

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    bio = HTMLField()  # Describe the facility, its duties, etc.
    image = models.ImageField(upload_to='img/facilites/')


class AddOn(models.Model):
    """Non-procedure related options.
    
    An AddOn can be offered indepently, or as part of a Package.
    
    Examples:
        name='Stuffed Teddy Bear, Individual', price='6.00'
        name='Stuffed Teddy Bear, Package A', price='4.00'

    """

    name = models.CharField(max_length=100)
    description = HTMLField()
    image = models.ImageField(upload_to='img/addons/', default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)


class Procedure(models.Model):
    """Procude model object.
    
    An Procedure can be offered indepently, or as part of a Package.
    
    Examples:
        name='Ultrasound Procuedure', price='100.00'
        name='Ultrasound Package Procedure', price='80.00'

    """

    name = models.CharField(max_length=100)
    description = HTMLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)


class Package(models.Model):
    """A package is a collection of procesdures and add-ons.
    
    A package can have it's own price, which does not need to be related to the associated AddOn/Procedure prices.
    """

    name = models.CharField(max_length=100)
    description = HTMLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Persist the package model and apply the created date and default price."""
        self.updated_date = timezone.now()
        if not self.created_date:
            self.created_date = timezone.now()

        if not self.price:
            add_ons = AddOn.objects.filter(package=self.id)
            procedures = Procedure.objects.filter(package=self.id)
            offerings = add_ons | procedures

            p = 0.00
            for o in offerings:
                p += o.price

            self.price = p

        super(Package, self).save(*args, **kwargs)
        return 'Package.save'


class Gallery(models.Model):
    """A collection of Photos."""

    title = models.CharField(max_length=100)
    description = HTMLField()

    def get_photos(self):
        """Return Photo model objects related to this gallery."""
        photos = Photo.objects.filter(gallery=self.id)
        return photos

    def __str__(self):
        """Return the string repr."""
        return self.title


class Photo(models.Model):
    """An image object that can be tied to a model if needed."""

    title = models.CharField(max_length=100, help_text="The image title. This is used as metadeta to imporve SEO.",
                             null=True, blank=True)
    description = HTMLField(help_text="The image description. Displayed as subtext associated with the linked photo.",
                            null=True, blank=True)
    image = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='My Photo', help_text='Upload a photo')
    gallery = models.ManyToManyField(Gallery,
                                     help_text="You can create galleries that contain groups of photos ~ facilities, staff, etc")  # A photo can be published in a gallery, a gallery can have multiple Photo objects.

    def __str__(self):
        """Return the string repr."""
        return self.title


class GiftCertificate(models.Model):
    """This is essentially a post that will advertise a package/addon/procedure and provide some details, etc."""
    name = models.CharField(max_length=100)
    details = HTMLField(verbose_name='Gift Certificate Details')
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Persist the gift ceritifcate model and apply the created/updated dates."""
        self.updated_date = timezone.now()
        if not self.created_date:
            self.created_date = timezone.now()

        super(GiftCertificate, self).save(*args, **kwargs)
        return 'GiftCertificate.save'


class Advertisement(models.Model):
    """This is essentially a post that will advertise a package/addon/procedure and provide some details, etc.
    You can assign a type to these to ensure the front end links can add a shortcut to the associated pages.
    """
    title = models.CharField(max_length=100, verbose_name='Advertisement Title')
    details = HTMLField(verbose_name='Advertisement Details')
    redirect_url = models.URLField(verbose_name='Where do you want the "Learn More" button to go?', default=None,
                                   null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Persist the ad model and apply the created/updated dates."""
        self.updated_date = timezone.now()
        if not self.created_date:
            self.created_date = timezone.now()

        super(Advertisement, self).save(*args, **kwargs)
        return 'Advertisement.save'


class HomePageDescription(models.Model):
    """Generic Post object for various posts across the webpage."""
    title = models.CharField(max_length=100)
    description = HTMLField()
