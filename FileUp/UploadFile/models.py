from django.db import models

# Create your models here.

class DataModel(models.Model):
    """(DataModel description): this is a test model to test file upload and the content """
    name = models.CharField(blank=True, max_length=100, null=True)
    email_id = models.CharField(blank=True, null=True, max_length=100)
    contact_no = models.CharField(blank=True, max_length=100, null=True)
    data = models.TextField(blank=True, null=True)
    updated_time = models.CharField(blank=True,null=True, max_length=100)

    def __unicode__(self):
        return u"DataModel"

    def __str__(self):
        return '{}'.format(self.name)

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
    file_path = models.FileField()
    uploaded_at = models.DateTimeField(blank=True, auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"FileStore"
