import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
import numpy as np
import matplotlib.pyplot as plt
import os

DATASET_DIR = "gtsrb"
IMAGE_SIZE = (48, 48)
BATCH_SIZE = 32
NUM_CLASSES = 43
EPOCHS = 15

train_ds = image_dataset_from_directory(directory=os.path.join(DATASET_DIR, "Train"), labels="inferred", label_mode="categorical", batch_size=BATCH_SIZE, subset="training", seed=123, validation_split=0.2, image_size=IMAGE_SIZE)

validation_ds = image_dataset_from_directory(directory=os.path.join(DATASET_DIR, "Train"), labels="inferred", label_mode="categorical", batch_size=BATCH_SIZE, subset="validation", seed=123, validation_split=0.2, image_size=IMAGE_SIZE)

test_ds = image_dataset_from_directory(directory=os.path.join(DATASET_DIR, "Test"), labels="inferred", label_mode="categorical", batch_size=BATCH_SIZE, image_size=IMAGE_SIZE)

print(train_ds.class_names)


normalization_layer = layers.Rescaling(1.0 / 255)
train_ds      = train_ds.map(lambda x, y: (normalization_layer(x), y))
validation_ds = validation_ds.map(lambda x, y: (normalization_layer(x), y))
test_ds       = test_ds.map(lambda x, y: (normalization_layer(x), y))

AUTOTUNE = tf.data.AUTOTUNE
train_ds      = train_ds.prefetch(AUTOTUNE)
validation_ds = validation_ds.prefetch(AUTOTUNE)
test_ds       = test_ds.prefetch(AUTOTUNE)

def build_model(input_shape=(48, 48, 3), num_classes=43):
    inputs = layers.Input(shape=input_shape)
    x = inputs

    for num_filters in [32, 64, 128]:
        x = layers.Conv2D(num_filters, (3,3), strides=1, padding="same", activation="relu")(x)
        x = layers.Conv2D(num_filters, (3, 3), strides=1, padding="valid", activation="relu")(x)
        x = layers.MaxPooling2D(pool_size=(2, 2), strides=2)(x)
        x = layers.Dropout(0.2)(x)
    
    x = layers.Flatten()(x)

    x = layers.Dense(512, activation="relu")(x)

    x = layers.Dropout(0.5)(x)

    outputs = layers.Dense(num_classes, activation="softmax")(x)

    model = models.Model(inputs, outputs)
    return model

model = build_model()
model.summary()

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)


os.makedirs("checkpoints", exist_ok=True)
os.makedirs("logs",        exist_ok=True)

checkpoint_cb = ModelCheckpoint(
    filepath="checkpoints/best_model.keras",
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1,
)

tensorboard_cb = TensorBoard(
    log_dir="logs",
    histogram_freq=1,
)

history = model.fit(
    train_ds,
    epochs=EPOCHS,
    validation_data=validation_ds,
    callbacks=[checkpoint_cb, tensorboard_cb],
)

best_model = models.load_model("checkpoints/best_model.keras")

test_loss, test_acc = best_model.evaluate(test_ds)
print(f"\nTočnost na testnom skupu: {test_acc * 100:.2f}%")

y_true = np.concatenate([y.numpy() for _, y in test_ds], axis=0)
y_true_labels = np.argmax(y_true, axis=1)

y_pred_probs = best_model.predict(test_ds)
y_pred_labels = np.argmax(y_pred_probs, axis=1)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_true_labels, y_pred_labels)

fig, ax = plt.subplots(figsize=(16, 16))
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(ax=ax, colorbar=False, xticks_rotation=90)
ax.set_title("Matrica zabune – testni skup")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=100)
plt.show()
print("Matrica zabune spremljena u confusion_matrix.png")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(history.history["accuracy"],     label="Train")
axes[0].plot(history.history["val_accuracy"], label="Validation")
axes[0].set_title("Tocnost")
axes[0].set_xlabel("Epoha")
axes[0].legend()

axes[1].plot(history.history["loss"],     label="Train")
axes[1].plot(history.history["val_loss"], label="Validation")
axes[1].set_title("Gubitak")
axes[1].set_xlabel("Epoha")
axes[1].legend()

plt.tight_layout()
plt.savefig("training_history.png", dpi=100)
plt.show()