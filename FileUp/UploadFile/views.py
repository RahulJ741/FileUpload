from django.shortcuts import render
import os, sys, datetime
import time
import django.apps
from .models import *
try:
    import pandas as pd
except ImportError:
    print('Pandas library is not installed in your system. Installing it now')
    time.sleep(4)
    os.system('pip install --user pandas')
finally:
    pass
# Create your views here.
models_dict = {i.__name__: i for i in django.apps.apps.get_models()}

def upload_file(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['excel_file']
            model_name = request.POST['model_selection']
            print(upload_file, ":::::::::::::::::")
            file_upload = FileStore(file_path = uploaded_file, is_active=True, uploaded_at=datetime.datetime.now())
            print(file_upload, "||||||||||||")
            file_upload.save()
            print("--------------------------")
            # return handle_upload(file_upload.file_path.path, model_name)
        except Exception as e:
            print(e, "Error is herr")
            print('line of error is {}'.format(sys.exc_info()[-1].tb_lineno))

    models_name = [i.__name__ for i in django.apps.apps.get_models()]
    return render(request,'upload_file.html',{'models_list': models_name})


def handle_upload(request,file_path,model_name):
    if request.method=='GET':
        print(file_path, "PPPPPPPPPPPPPP")
        global models_dict
        models_class_name = models_dict[model_name]
        return render(request, 'base.html',{})
    elif request.method=='POST':
        pass
