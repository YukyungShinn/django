from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from config import settings
import os

def upload1(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'file/upload1.html')

def upload2(request):
    if request.method == 'POST':
        upload_files = request.FILES.getlist('file')
        result = ''
        for upload_file in upload_files:
            name = upload_file.name
            size = upload_file.size
            
            with open(name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)
            result += '%s<br>%s<hr>' % (name, size)
        return HttpResponse(result)
    return render(request, 'file/upload2.html')

def upload3(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFile = form.save()
            # uploadFile = form.save(commit=False)
            name = uploadFile.file.name
            size = uploadFile.file.size
            return HttpResponse('%s<br>%s' % (name, size))
    else:
        form = UploadFileForm()
    return render(
        request, 'file/upload3.html', {'form': form})

from .models import UploadFile
def img_show(request):
    id = request.GET.get('id')
    uploadFile = UploadFile.objects.get(id=id)
    return render(
        request, 'file/img_show.html',
        {'uploadFile': uploadFile})

def download(request):
    id = request.GET.get('id')
    uploadFile = UploadFile.objects.get(id=id)
    
    filepath = str(settings.BASE_DIR) + ('/media/%s' % uploadFile.file.name)
    filename = os.path.basename(filepath)
    
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response