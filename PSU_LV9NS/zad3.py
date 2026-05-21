import tensorflow as tf
from tensorflow.keras import models
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

CLASS_NAMES = [
    "Ograničenje brzine (20 km/h)",
    "Ograničenje brzine (30 km/h)",
    "Ograničenje brzine (50 km/h)",
    "Ograničenje brzine (60 km/h)",
    "Ograničenje brzine (70 km/h)",
    "Ograničenje brzine (80 km/h)",
    "Kraj ograničenja brzine (80 km/h)",
    "Ograničenje brzine (100 km/h)",
    "Ograničenje brzine (120 km/h)",
    "Zabrana pretjecanja",
    "Zabrana pretjecanja za vozila > 3.5t",
    "Pravo prolaza na raskrizju",
    "Glavna cesta",
    "Stop",
    "Daj prednost",
    "Prednost prolaza",
    "Zabrana prolaza",
    "Zabrana prolaza za vozila > 3.5t",
    "Zabrana prolaza za vozila s visinom > 3.5m",
    "Opasnost",
    "Opasna krivina lijevo",
    "Opasna krivina desno",
    "Dvostruke krivine",
    "Neravna cesta",
    "Skliski kolnik",
    "Suženje ceste desno",
    "Radovi na cesti",
    "Semafori",
    "Pješaci",
    "Djeca na cesti",
    "Biciklisti",
    "Led / snijeg",
    "Divlje životinje",
    "Kraj svih ograničenja",
    "Skretanje desno",
    "Skretanje lijevo",
    "Ravno",
    "Ravno ili desno",
    "Ravno ili lijevo",
    "Držati se desno",
    "Držati se lijevo",
    "Kružni tok",
    "Kraj zabrane pretjecanja",
    "Kraj zabrane pretjecanja za vozila > 3.5t",
]
IMAGE_SIZE = (48, 48)

def load_and_preprocess(image_path: str) -> tf.Tensor:
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3, expand_animations=False)
    img = tf.image.resize(img, IMAGE_SIZE)
    img = tf.cast(img, tf.float32)
    img = tf.expand_dims(img, axis=0)
    return img

def classify(model_path: str, image_path: str) -> None:
    if not os.path.exists(model_path):
        print(f"[GREŠKA] Model nije pronađen: {model_path}")
        return
    if not os.path.exists(image_path):
        print(f"[GREŠKA] Slika nije pronađena: {image_path}")
        return
    print(f"Učitavanje modela iz: {model_path}")
    model = models.load_model(model_path)

    img_tensor = load_and_preprocess(image_path)

    predictions = model.predict(img_tensor)[0]
    pred_class  = int(np.argmax(predictions))
    confidence  = float(predictions[pred_class]) * 100

    print(f"\n{'='*50}")
    print(f"Ulazna slika   : {image_path}")
    print(f"Predviđena klasa: {pred_class} – {CLASS_NAMES[pred_class]}")
    print(f"Pouzdanost      : {confidence:.2f}%")
    print(f"{'='*50}\n")
    print(f"Raw klasa broj: {pred_class}")


    top5_idx = np.argsort(predictions)[::-1][:5]
    print("Top-5 predikcija:")
    for rank, idx in enumerate(top5_idx, 1):
        print(f"  {rank}. [{idx:2d}] {CLASS_NAMES[idx]:<45} {predictions[idx]*100:.2f}%")
    
    img_display = tf.image.decode_image(
        tf.io.read_file(image_path), channels=3, expand_animations=False
    ).numpy()

    plt.figure(figsize=(5, 5))
    plt.imshow(img_display)
    plt.axis("off")
    plt.title(
        f"Predviđeno: {CLASS_NAMES[pred_class]}\n"
        f"Klasa {pred_class}  |  Pouzdanost: {confidence:.1f}%",
        fontsize=11,
    )
    plt.tight_layout()
    plt.savefig("klasifikacija_rezultat.png", dpi=100)
    plt.show()
    print("Rezultat spremljen u klasifikacija_rezultat.png")

if __name__ == "__main__":
    MODEL_PATH = "checkpoints/best_model.keras"

    if len(sys.argv) > 1:
        IMAGE_PATH = sys.argv[1]
    else:
        IMAGE_PATH = "znak.png"

    classify(MODEL_PATH, IMAGE_PATH)