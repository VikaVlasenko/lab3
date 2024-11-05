Лабораторная работа 3
# Image Processing Desktop Application

Это десктопное приложение на Python, которое позволяет загружать изображения и применять к ним низкочастотные фильтры (сглаживающие) и морфологические операции с возможностью выбора структурирующего элемента.

## Особенности

- Загрузка изображений в формате JPG, PNG, BMP.
- Применение низкочастотных фильтров:
  - Blur (Размытие)
  - Gaussian Blur (Гауссово размытие)
  - Median Blur (Медианное размытие)
- Применение морфологических операций:
  - Erode (Эрозия)
  - Dilate (Дилатация)
  - Open (Открытие)
  - Close (Закрытие)
- Возможность выбора размера структурирующего элемента.

## Запуск

Скачайте и запустите main.exe

![изображение](https://github.com/user-attachments/assets/113f7ca1-1cbd-46c6-b76a-13a571d37d58)


## Установка в Python

1. Установите зависимости:

   ```bash
   pip install pyinstaller opencv-python-headless numpy
Создайте исполняемый файл:

bash
Copy
pyinstaller --onefile --windowed main.py
Исполняемый файл будет находиться в директории dist.

Использование
Загрузите изображение с помощью кнопки "Load Image".

Выберите тип фильтра (Blur, Gaussian Blur, Median Blur).

Выберите тип морфологической операции (Erode, Dilate, Open, Close).

Укажите размер ядра (Kernel Size).

Нажмите "Process Image" для обработки изображения.

Структура проекта
Copy
image_processing_app/
│
├── main.py
└── README.md
└── main.exe

Зависимости
opencv-python-headless==4.5.3.56

numpy==1.21.2

pyinstaller==4.5.1

Автор
Власенко Виктория Владимировна 10 группа

