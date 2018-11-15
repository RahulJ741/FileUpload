from django.shortcuts import render
import os, sys, datetime
import time
import django.apps
from .models import *
from FileUp import settings
from django.http import HttpResponse
try:
    import pandas as pd
except ImportError:
    print('Pandas library is not installed in your system. Installing it now')
    time.sleep(4)
    os.system('pip install --user pandas')
finally:
    import pandas as pd
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        try:
            print(request.POST, "request.post is here")
            uploaded_file = request.FILES['excel_file']
            model_name = request.POST['model_selection']
            file_upload = FileStore(file_path = uploaded_file, is_active=True, uploaded_at=datetime.datetime.now())
            file_upload.save()
            print("--------------------------")
            return handle_upload(request,file_upload.file_path.path, model_name)
        except Exception as e:
            print(e, "Error is herr")
            print('line of error is {}'.format(sys.exc_info()[-1].tb_lineno))

    print(settings.BASE_DIR, "lllllllll")
    models_name = [i.__name__ for i in django.apps.apps.get_models()]
    return render(request,'upload_file.html',{'models_list': models_name})


def handle_upload(request,file_path,model_name):
    models_dict = {i.__name__: i for i in django.apps.apps.get_models()}
    if request.method=='POST':
        print('POST method')
        models_class_name = models_dict[model_name]
        model_fields = [f.name for f in models_class_name._meta.get_fields()]
        df = pd.read_excel(file_path)
        column_name = list(df.columns.values)
        return render(request, 'base.html',{'fields': model_fields,'columns': column_name, 'model':model_name})

# TODO: https://docs.djangoproject.com/en/2.1/ref/models/querysets/#bulk-create
def save_data(request):
    models_dict = {i.__name__: i for i in django.apps.apps.get_models()}
    if request.method == 'POST':
        print(request.POST, "123456789123456789123456789123456789")
        model_class = models_dict[request.POST['model']]
        model_fields = [f.name for f in model_class._meta.get_fields()]
        list_data = {}
        file_obj = FileStore.objects.filter(is_active=True).order_by('-uploaded_at')[0]
        df = pd.read_excel(file_obj.file_path.path)
        for field in model_fields:
            # print(request.POST[field+'_sel'], "opopopopopoppopopopopopop")
            list_data[field] = request.POST[field+'_sel']

        for index, row in df.iterrows():
            try:
                # print(row['Email'], "==========")
                upload_data = model_class.objects.create()
                print(upload_data, "object is here")
                for model_field, dataframe_field in list_data.items():
                    print(model_field,"----------",row[dataframe_field],"Data of a field is here")
                    upload_data.model_field = row[dataframe_field]
                    # print(upload_data.model_field, ";-;-;-;-;--;-;-;-;-;")
                upload_data.save()

            except Exception as e:
                print(e, "eoor at inner function")
                print('line of error {}'.format(sys.exc_info()[-1].tb_lineno))

        return HttpResponse("Done hheck the db")
