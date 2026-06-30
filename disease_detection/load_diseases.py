from disease_detection.models import DiseaseInfo

diseases = [

    {
        "disease_name": "Tomato - Bacterial Spot",
        "description": "Bacterial Spot is caused by Xanthomonas bacteria and affects leaves, stems, and fruits.",
        "signs_of_damage": "Dark leaf spots\nYellow halos\nFruit lesions\nDefoliation",
        "prevention": "Use certified seeds\nCrop rotation\nCopper sprays\nAvoid overhead irrigation",
        "crop_health": 70,
        "yield_loss": 25
    },

    {
        "disease_name": "Tomato - Early Blight",
        "description": "Early Blight is a fungal disease caused by Alternaria solani that affects tomato foliage and fruits.",
        "signs_of_damage": "Concentric ring lesions\nYellowing leaves\nLeaf drop\nReduced fruit production",
        "prevention": "Crop rotation\nRemove infected debris\nApply fungicides",
        "crop_health": 65,
        "yield_loss": 30
    },

    {
        "disease_name": "Tomato - Late Blight",
        "description": "Late Blight is a destructive disease caused by Phytophthora infestans and can rapidly destroy tomato crops.",
        "signs_of_damage": "Water-soaked lesions\nBrown leaf spots\nWhite fungal growth\nFruit rot",
        "prevention": "Use resistant varieties\nAvoid excess moisture\nApply fungicides",
        "crop_health": 40,
        "yield_loss": 55
    },

    {
        "disease_name": "Tomato - Leaf Mold",
        "description": "Leaf Mold is a fungal disease common in humid greenhouse conditions.",
        "signs_of_damage": "Yellow leaf patches\nOlive-green mold\nLeaf curling\nReduced photosynthesis",
        "prevention": "Improve ventilation\nReduce humidity\nUse resistant varieties",
        "crop_health": 70,
        "yield_loss": 20
    },

    {
        "disease_name": "Tomato - Septoria Leaf Spot",
        "description": "Septoria Leaf Spot is a fungal disease causing numerous small spots on tomato leaves.",
        "signs_of_damage": "Small circular spots\nLeaf yellowing\nPremature leaf drop",
        "prevention": "Crop rotation\nRemove infected leaves\nApply fungicides",
        "crop_health": 65,
        "yield_loss": 25
    },

    {
        "disease_name": "Tomato - Spider Mites",
        "description": "Spider Mites are tiny pests that damage tomato plants by feeding on leaf tissues.",
        "signs_of_damage": "Yellow stippling\nLeaf bronzing\nWebbing\nLeaf drop",
        "prevention": "Use biological controls\nMaintain humidity\nApply miticides when required",
        "crop_health": 70,
        "yield_loss": 20
    },

    {
        "disease_name": "Tomato - Target Spot",
        "description": "Target Spot is a fungal disease that causes lesions on leaves, stems, and fruits.",
        "signs_of_damage": "Brown circular lesions\nLeaf blight\nFruit spotting",
        "prevention": "Improve airflow\nCrop rotation\nApply fungicides",
        "crop_health": 65,
        "yield_loss": 25
    },

    {
        "disease_name": "Tomato - Yellow Leaf Curl Virus",
        "description": "A viral disease transmitted by whiteflies that severely affects tomato growth and yield.",
        "signs_of_damage": "Leaf curling\nYellowing leaves\nStunted growth\nPoor fruit set",
        "prevention": "Control whiteflies\nUse resistant varieties\nRemove infected plants",
        "crop_health": 45,
        "yield_loss": 50
    },

    {
        "disease_name": "Tomato - Mosaic Virus",
        "description": "Tomato Mosaic Virus is a viral disease causing mottled leaves and reduced crop productivity.",
        "signs_of_damage": "Mosaic leaf patterns\nLeaf distortion\nReduced vigor\nPoor fruit quality",
        "prevention": "Use disease-free seeds\nDisinfect tools\nRemove infected plants",
        "crop_health": 55,
        "yield_loss": 35
    },

    {
        "disease_name": "Tomato - Healthy",
        "description": "The tomato plant appears healthy with no visible disease symptoms.",
        "signs_of_damage": "No disease symptoms detected",
        "prevention": "Continue proper irrigation, fertilization, and monitoring",
        "crop_health": 98,
        "yield_loss": 0
    }

]

for disease in diseases:

    DiseaseInfo.objects.update_or_create(
        disease_name=disease["disease_name"],
        defaults=disease
    )

print("Batch 4 inserted successfully.")