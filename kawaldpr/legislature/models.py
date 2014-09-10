from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from model_utils.models import TimeStampedModel


class Area(TimeStampedModel):
    """
    Legislature area
    """
    name = models.CharField(max_length=200)


class Fraction(TimeStampedModel):
    """
    Fraction of Indonesia party
    """
    name = models.CharField(max_length=200)


class Legislature(TimeStampedModel):
    """
    Main model for Indonesia's legislatures.
    """

    SEX = (
        (1, 'Man'),
        (2, 'Woman')
    )

    # Bio data
    name = models.CharField(max_length=200)
    birth_place = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.IntegerField(choices=SEX, null=True, blank=True)

    # Work record
    last_education = RichTextField(null=True, blank=True)
    last_Education_alert = RichTextField(null=True, blank=True)
    track_record = RichTextField(null=True, blank=True)
    track_record_alert = RichTextField(null=True, blank=True)
    organization_work = RichTextField(null=True, blank=True)
    organization_work_alert = RichTextField(null=True, blank=True)
    incumbent = models.BooleanField(default=False)

    # Social media
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    linkedin = models.CharField(max_length=200, null=True, blank=True)

    # Affiliation
    area = models.ForeignKey(Area, null=True, blank=True)
    fraction = models.ForeignKey(Fraction, null=True, blank=True)

    slug = AutoSlugField(populate_from='name', null=True, blank=True)

    # Active
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Medium(TimeStampedModel):
    """
    This model is to store all media publication about the legislature
    """
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True)

    reference = models.TextField(null=True, blank=True)

    legislatures = models.ManyToManyField(Legislature, null=True, blank=True, related_name='media')

    slug = AutoSlugField(populate_from='title', null=True, blank=True)

    # Active
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Statement(TimeStampedModel):
    """
    Every public statement made by the legislature
    """
    title = models.CharField(max_length=200, blank=True)
    content = RichTextField(blank=True)

    reference = models.TextField(null=True, blank=True)
    legislature = models.ForeignKey(Legislature)

    # Active
    published = models.BooleanField(default=False)

