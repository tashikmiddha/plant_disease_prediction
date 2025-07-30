import os
from django.core.files import File
from project.models import LeafDisease
from django.conf import settings

# Path to the folder containing subfolders like Apple___Apple_scab
DATA_FOLDER = os.path.join(settings.MEDIA_ROOT, 'data')

def import_leaf_images():
    for folder_name in os.listdir(DATA_FOLDER):
        if "___" not in folder_name:
            continue  # Skip malformed folders

        plant_name, disease_name = folder_name.split("___")
        folder_path = os.path.join(DATA_FOLDER, folder_name)

        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)

            if not image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue  # Skip non-image files

            with open(image_path, 'rb') as img_file:
                django_file = File(img_file)
                # Create entry in the DB
                disease = LeafDisease(
                    plant_name=plant_name,
                    disease_name=disease_name,
                    description=f"{disease_name} affecting {plant_name}"
                )
                disease.image.save(image_name, django_file, save=True)

    print("✅ Import complete!")
