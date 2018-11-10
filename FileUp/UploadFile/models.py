from django.db import models

# Create your models here.

class DataModel(models.Model):
    """(DataModel description): this is a test model to test file upload and the content """
    name = models.CharField(blank=True, max_length=100)
    email_id = models.EmailField(blank=True)
    contact_no = models.CharField(blank=True, max_length=100)
    data = models.TextField(blank=True)
    updated_time = models.DateTimeField(blank=True, auto_now = False, auto_now_add=False)

    def __unicode__(self):
        return u"DataModel"

    def __str__(self):
        return '{}'.format()

import os
# import datetime
def upload_file(instance, filename):
    _, extension = os.path.splitext(filename)
    # NOTE: Uncomment this line if you want the file to have name as datetime
    # new_filename = "{}".format(datetime.datetime.strftime(instance.uploaded_at,'%d_%m_%Y_%H:%M'))
    new_filename = '{}{}'.format(os.urandom(8).hex(),extension)
    print(filename, "filename -----------------", new_filename, "new_filename ___")

class FileStore(models.Model):
    """(FileStore description)"""
    file_path = models.FileField(upload_to=upload_file)
    uploaded_at = models.DateTimeField(blank=True, auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"FileStore"