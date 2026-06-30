from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from ai_model.predictor import predict_disease
from .models import DiseaseInfo


@login_required(login_url='/login/')
def upload_image(request):

    if request.method == "POST":

        uploaded_file = request.FILES['image']

        fs = FileSystemStorage(
            location='media/uploads/'
        )

        filename = fs.save(
            uploaded_file.name,
            uploaded_file
        )

        file_path = 'media/uploads/' + filename

        prediction = predict_disease(
            file_path
        )

        disease_info = DiseaseInfo.objects.filter(
            disease_name=prediction
        ).first()

        return render(
            request,
            'result.html',
            {
                'prediction': prediction,
                'image_url': '/media/uploads/' + filename,
                'info': disease_info
            }
        )

    return render(
        request,
        'upload.html'
    )