from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


from .models import LeafDisease

from django.db.models import Count

def library_home(request):
    # Get unique plant names with image count
    plants = LeafDisease.objects.values('plant_name').annotate(image_count=Count('id')).order_by('plant_name')
    return render(request, 'library_home.html', {'plants': plants})


from django.http import JsonResponse

def plant_gallery(request, plant_name):
    return render(request, 'plant_gallery.html', {'plant_name': plant_name})

def load_images(request, plant_name):
    offset = int(request.GET.get('offset', 0))
    limit = 60
    images = LeafDisease.objects.filter(plant_name=plant_name)[offset:offset+limit]

    data = []
    for img in images:
        data.append({
            'id': img.id,
            'disease_name': img.disease_name,
            'description': img.description,
            'image_url': img.image.url,
        })
    return JsonResponse({'images': data})



from django.shortcuts import render, redirect
from .form import ReviewForm
from .models import Review

def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../review/')
    else:
        form = ReviewForm()
    
    reviews = Review.objects.order_by('-created_at')
    return render(request, 'review.html', {'form': form, 'reviews': reviews})



import os
from django.shortcuts import render
from .form import ImageUploadForm
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model


model = load_model('/Users/tashikmiddha/Desktop/practice/disease/myenv/disease_prediction/project/my_model.h5')
class_names = {
    0: "Apple___Apple_scab",
    1: "Apple___Black_rot",
    2: "Apple___Cedar_apple_rust",
    3: "Apple___healthy",
    4: "Blueberry___healthy",
    5: "Cherry_(including_sour)___Powdery_mildew",
    6: "Cherry_(including_sour)___healthy",
    7: "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    8: "Corn_(maize)___Common_rust_",
    9: "Corn_(maize)___Northern_Leaf_Blight",
    10: "Corn_(maize)___healthy",
    11: "Grape___Black_rot",
    12: "Grape___Esca_(Black_Measles)",
    13: "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    14: "Grape___healthy",
    15: "Orange___Haunglongbing_(Citrus_greening)",
    16: "Peach___Bacterial_spot",
    17: "Peach___healthy",
    18: "Pepper,_bell___Bacterial_spot",
    19: "Pepper,_bell___healthy",
    20: "Potato___Early_blight",
    21: "Potato___Late_blight",
    22: "Potato___healthy",
    23: "Raspberry___healthy",
    24: "Soybean___healthy",
    25: "Squash___Powdery_mildew",
    26: "Strawberry___Leaf_scorch",
    27: "Strawberry___healthy",
    28: "Tomato___Bacterial_spot",
    29: "Tomato___Early_blight",
    30: "Tomato___Late_blight",
    31: "Tomato___Leaf_Mold",
    32: "Tomato___Septoria_leaf_spot",
    33: "Tomato___Spider_mites Two-spotted_spider_mite",
    34: "Tomato___Target_Spot",
    35: "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    36: "Tomato___Tomato_mosaic_virus",
    37: "Tomato___healthy"
}


def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0 

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class = class_names[predicted_class_index]
    return predicted_class


def upload_view(request):
    prediction = None
    image_url = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            path = f'media/{img.name}'
            with open(path, 'wb+') as dest:
                for chunk in img.chunks():
                    dest.write(chunk)
            prediction = predict_image(path)
            image_url = '/' + path
    else:
        form = ImageUploadForm()

    return render(request, 'disease_prediction.html', {'form': form, 'prediction': prediction, 'image_url': image_url})


def privacy(request):
    return render(request,'privacy.html')

def term(request):
    return render(request,'term.html')
