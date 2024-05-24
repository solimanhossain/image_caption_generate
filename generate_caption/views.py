from django.shortcuts import render
from .forms import ImageForm
from . import process


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
            print(form.instance.image)
            img_obj = form.instance
            url = 'http://localhost:8000/media/' + str(img_obj.image)
            text_img, text_bn = process.show_generate(url, img_obj.image, greedy=False)
            return render(request, 'index.html',
                          {'form': form, 'img_obj': img_obj, 'caption': text_img, 'caption_bn': text_bn})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
