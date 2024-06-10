import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

#Charge les données de training
X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle", "rb"))

#normalise les données en mettant les valeurs des pixels entre 0 et 1
X = X/255.0

#Initialise modèle de réseau de neurones séquentiel = pile linéaire de couches
model = Sequential()
#ajout d'une couche de convolution avec 64 filtres de taille 3x3
model.add(Conv2D(64, (3,3), input_shape = X.shape[1:]))
#ajout d'une fonction d'activation ReLu, intrdouit la non-linéarité dans le modèle. Transforme val negatives en 0
model.add(Activation("relu"))
#ajout couche de pooling max qui réduit la dimension spatiale de l'entrée de moitié => Reduit le nb de paramètres
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#aplati la sortie des couches en un vect 1D. Passe de la partie convolutionnelle à la connectée
model.add(Flatten())
#ajout d'une couche dense avec 64 neurones
model.add(Dense(64))

#ajout d'une couche dense finale avec 1 seule neurone qui sera la sortie du modèle
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

model.fit(X, y, batch_size=32, epochs = 10, validation_split=0.1)
