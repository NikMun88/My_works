import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping

# Загрузка данных
data = pd.read_csv('data.csv')

# Предполагаем, что последняя колонка - это целевая переменная
X = data.iloc[:, :-1].values  # Все колонки кроме последней
y = data.iloc[:, -1].values    # Последняя колонка

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

 # Стандартизация данных
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

 # Создание модели
model = keras.Sequential([
    layers.Dense(32, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Для бинарной классификации
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Обучение и условие отсутвия переобучения
early_stopping = EarlyStopping(monitor='val_loss', patience=6)
model.fit(X_train, y_train, epochs=200, batch_size=10, verbose=1)

# Оценка модели на тестовых данных
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Качество предсказания: {accuracy * 100:.2f}%')

# Предсказания
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int)  # Преобразуем вероятности в классы
