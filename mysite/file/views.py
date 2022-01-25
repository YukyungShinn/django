from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse

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