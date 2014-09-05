from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.utils.timezone import utc
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit
from uuid import uuid4


class User(AbstractUser):

    """
    Custom User model for kawaldpr
    """

    # Personal data for each User
    picture = models.ImageField(upload_to='user/profile', null=True, blank=True)
    picture_thumbnail = ImageSpecField(source='picture',
                                       processors=[ResizeToFit(200, 200)],
                                       format='JPEG',
                                       options={'quality': 70})


class Static(TimeStampedModel):

    """
    Static represent static page on kawaldpr. Web pages like About, Team, Vision, and Contact. It need to use
    slug field to make the URL SEO-friendly.
    """

    title = models.CharField(max_length=100)
    content = RichTextField(blank=True)
    published = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title', max_length=100, unique=True)

    def __unicode__(self):
        return self.title


class Contact(TimeStampedModel):

    """
    Keep user issue and complain from the contact page
    """

    # Data
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=50)
    message = models.TextField()


class ForgotPassword(TimeStampedModel):
    """
    Model to let User reset their password
    """
    user = models.ForeignKey(User)
    guid = models.CharField(max_length=60)

    def save(self, *args, **kwargs):
        uuid_token = uuid4()
        self.guid = uuid_token.get_hex()

        super(ForgotPassword, self).save(*args, **kwargs)

    def is_valid(self):
        if self.created < datetime.utcnow().replace(tzinfo=utc) - timedelta(days=1):
            return True
        else:
            return False

    def __unicode__(self):
        return self.user.get_full_name() + " " + self.guid
