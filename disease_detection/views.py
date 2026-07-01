from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from ai_model.predictor import predict_disease
from .models import DiseaseInfo
from .pdf_generator import generate_pdf

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

        prediction = predict_disease(file_path)

        disease_info = DiseaseInfo.objects.filter(
            disease_name=prediction
        ).first()

        request.session["prediction"] = prediction
        request.session["filename"] = filename

        return render(
            request,
            "result.html",
            {
                "prediction": prediction,
                "image_url": "/media/uploads/" + filename,

                "description": disease_info.description if disease_info else "",

                "signs": disease_info.signs_of_damage if disease_info else "",

                "prevention": disease_info.prevention if disease_info else "",

                "recommendation": disease_info.recommendation if disease_info else "",

                "crop_health": disease_info.crop_health if disease_info else 0,

                "yield_loss": disease_info.yield_loss if disease_info else 0,
            }
        )

    return render(
        request,
        "upload.html"
    )
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse


@login_required(login_url="/login/")
def download_report(request):

    prediction = request.session.get("prediction")
    filename = request.session.get("filename")

    if not prediction or not filename:
        return HttpResponse(
            "No prediction found. Please analyze a plant first."
        )

    disease_info = DiseaseInfo.objects.filter(
        disease_name=prediction
    ).first()

    if disease_info is None:
        return HttpResponse(
            "Disease information not found."
        )

    return generate_pdf(
        request,
        prediction,
        disease_info,
        filename
    )