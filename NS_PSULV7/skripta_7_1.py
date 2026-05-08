import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools


# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa
fig, axes = plt.subplots(3, 3, figsize=(6, 6))
fig.suptitle("Primjer slika iz skupa MNIST.", fontsize=14)
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i], cmap="gray")
    ax.set_title(f"Oznaka: {y_train[i]}")
    ax.axis("off")
plt.tight_layout()
plt.show()


# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
model = keras.Sequential()
model.add(Dense(units=100, activation='relu'))
model.add(Dense(units=50, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])


# TODO: provedi treniranje mreze pomocu .fit()
model.fit(x_train_s, y_train_s, epochs=25, batch_size=32)


# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
train_loss, train_acc = model.evaluate(x_train_s, y_train_s)
test_loss, test_acc = model.evaluate(x_test_s, y_test_s)

print(f"\nTocnost mreze na skupu podataka za ucenje: {train_acc*100:.2f} %")
print(f"\nTocnost mreze na skupu podataka za testiranje: {test_acc*100:.2f} %")


# TODO: Prikazite matricu zabune na skupu podataka za testiranje
def confusion_matrix_plot(cm, classes, title="Matrica zabune"):
    fig, ax = plt.subplots(figsize=(9, 8))

    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.colorbar(im, ax=ax)

    ax.set_title(title, fontsize=14)

    tick_marks = np.arange(len(classes))
    ax.set_xticks(tick_marks)
    ax.set_xticklabels(classes)

    ax.set_yticks(tick_marks)
    ax.set_yticklabels(classes)

    thresh = cm.max() / 2.0

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        ax.text(
            j, i,
            format(cm[i, j], "d"),
            ha="center",
            va="center",
            color="white" if cm[i, j] > thresh else "black"
        )

    ax.set_xlabel("Predviđena oznaka")
    ax.set_ylabel("Stvarna oznaka")

    plt.tight_layout()
    plt.show()

y_pred_prob = model.predict(x_test_s)
y_pred = np.argmax(y_pred_prob, axis=1)

cm_test = confusion_matrix(y_test, y_pred)
confusion_matrix_plot(cm_test, classes=list(range(10)), title="Matrica zabune - skup za ucenje")


# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala
wrong_idx = np.where(y_pred != y_test)[0]

rng = np.random.default_rng(seed=42)
sample_idx = rng.choice(wrong_idx, size=9, replace=False)

fig, axes = plt.subplots(3, 3, figsize=(7, 7))

fig.suptitle(
    "Pogrešno klasificirani primjeri iz testnog skupa podataka",
    fontsize=13
)

for ax, idx in zip(axes.flat, sample_idx):
    ax.imshow(x_test[idx], cmap="gray")

    ax.set_title(
        f"Stvarno: {y_test[idx]} | Pogrešno: {y_pred[idx]}",
        fontsize=9,
        color="red"
    )

    ax.axis("off")

plt.tight_layout()
plt.show()
