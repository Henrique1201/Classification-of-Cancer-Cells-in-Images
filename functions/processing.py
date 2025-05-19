import os
import pandas as pd

def create_dataframe(DATA_PATH):
    image_paths = []
    labels = []

    for patient_id in os.listdir(DATA_PATH):
        patient_folder = os.path.join(DATA_PATH)
        for label in ['0', '1']:
            label_folder = os.path.join(patient_folder, label)
            if os.path.isdir(label_folder):
                for img_name in os.listdir(label_folder):
                    image_paths.append(os.path.join(label_folder, img_name))
                    labels.append(str(label))

    df = pd.DataFrame({'image_path': image_paths, 'label': labels})
    return df