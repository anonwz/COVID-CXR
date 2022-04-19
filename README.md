# **COVID-CXR**
In this part of my graduate project I've made a research and managed to make my model to classify COVID-19, pneumonia affected and healthy lungs using only chest X-RAY images.

It was possible to achieve amazing results that are ahead of all similar researches that I have found. You can find specific numbers and comparisons further below.
_____

# **Data Availability and preprocesing**
I've merged several publicly available datasets.
Data I used is available [here](https://mega.nz/file/ksdhiApA#14L2kG7aI6ep06fJEXVqN7OAQ5DzzOZjSsz_HwlluSc) or in Model folder

Data was resized to 224x224 pixels and normalized. 

Data augmentations techniques were applied.

# **Model overview**

I've implemented and tried both State-Of-Art models and models from scratch. Experiments showed that DenseNet201 achieved better results amidst all models so I chose it for further developing.

# **Results and comparisons**

| amount             | our model | [RA20](https://doi.org/https://doi.org/10.1016/j.imu.2020.100360)   | [Sad+21](https://www.nature.com/articles/s41598-021-95561-y) | [MSH22](https://doi.org/https://doi.org/10.1016/j.eij.2022.01.002)  | [Luj+20](https://doi.org/10.3390/math8091423) | [Bac+21](https://doi.org/10.1101/2021.07.15.21260605) |
|---------------------|-----------|--------|--------|--------|--------|--------|
| precision healthy   | 99.3%     | 97.2%  | 90.5%  | 96.26% | 62%    | 94%    |
| recall healthy      | 99.7%     | 97.2%  | 95%    | 98.57% | 99%    | 94%    |
| F1 healthy          | 99.5%     | 97.2%  |        | 97.4%  | 76%    | 94%    |
| precision COVID-19  | 99.4%     | 99.8%  | 97.9%  | 99.65% | 100%   | 95%    |
| recall COVID-19     | 97.9%     | 89.1%  | 92%    | 93.98% | 94%    | 98%    |
| F1 COVID-19         | 98.7%     | 89.3%  |        | 96.74% | 97%    | 96%    |
| precision pneumonia | 99.2%     | 97.7%  | 92.1%  | 99.45% | 100%   | 98%    |
| recall pneumonia    | 100%      | 98.9%  | 93%    | 97.98% | 82%    | 98%    |
| F1 pneumonia        | 99.6%     | 97.6%  |        | 98.71% | 76%    | 98%    |
| accuracy  healthy   | 99.6%     | 91.8%  |        | 88.03% | 86.13% | 97.05% |
| accuracy COVID-19   | 99.6%     | 96.7%  |        | 99.4%  | 99.7%  | 99.38% |
| accuracy pneumonia  | 99.6%     | 93.8%  |        | 99.23% | 86.43% | 97.05% |
| total accuracy      | 99.32%    | 94.79% | 93.3%  | 96.56% | 91%    | 96.74  |
___________________
| metrics             | our model | [RA20](https://doi.org/https://doi.org/10.1016/j.imu.2020.100360)   | [Sad+21](https://www.nature.com/articles/s41598-021-95561-y) | [MSH22](https://doi.org/https://doi.org/10.1016/j.eij.2022.01.002)  | [Luj+20](https://doi.org/10.3390/math8091423) | [Bac+21](https://doi.org/10.1101/2021.07.15.21260605) |
|-----------|-------|-------|-------|-----------|------|------|
| COVID-19  | 5205  | 180   | 617   | 70(min)   | 287  | 576  |
| pneumonia | 4270  | 6054  | 6069  | 4273(min) | 4273 | 4273 |
| healthy   | 10092 | 8851  | 8851  | 1611(min) | 1583 | 1583 |
| total     | 19567 | 15085 | 15537 | 7512      | 6143 | 6432 |
_______________

"min" in [MSH22](https://doi.org/https://doi.org/10.1016/j.eij.2022.01.002) section indicates that given amount was used undoubtly. Information about the rest of the images was not given in the paper.

# Usage of our model
If you'd like to try out and test my model on some X-Rays from archive or your own images you can do it following these steps.
## Dependencies
+ python 
+ keras
+ tensorflow
+ matplotlib
+ cv2
+ sklearn
+ seaborn
## How to load
Download and unarchive the [zip file](https://mega.nz/file/ksdhiApA#14L2kG7aI6ep06fJEXVqN7OAQ5DzzOZjSsz_HwlluSc) and place it where you want.

Import necessary dependencies
```python
import seaborn as sns
import os
import keras
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
```

Then use
```python
model = keras.models.load_model('YourPath/Diplom96nevBN224')
```
where 'YourPath' is path to unarchived folder.

```python
input_path = 'path_to_unarchived_folder'
img_dims=224
```

Then we need to preprocess our images

```python
def process_data2(img_dims):
    test_data = []
    test_labels = []
    for cond in ['/COVID/', '/NORMAL/', '/PNEUMONIA/']:
        for img in (os.listdir(input_path + '/' + 'test' + cond)):
            img = cv2.imread(input_path+ '/' + 'test'+cond+img)
            img = cv2.resize(img, (img_dims, img_dims))
            if cond=='/NORMAL/':
                label = 1
            elif cond=='/PNEUMONIA/':
                label = 2
            elif cond=='/COVID/':
                label = 0
            test_data.append(img)
            test_labels.append(label)
        
    test_data = np.array(test_data) / 255.0
    test_labels = np.array(test_labels)
    
    return test_data, test_labels
test_data, test_labels = process_data2(img_dims)
```
Evaluate it and print confusion matrix
```python
preds = model.predict(test_data)
predIdxs = np.argmax(preds,axis=1)
cm=confusion_matrix(test_labels, predIdxs, labels =[0, 1, 2])
ax = sns.heatmap(cm, annot=True, fmt=".0f", cmap="Blues", xticklabels=["NORMAL", "PNEUMONIA", "COVID"], yticklabels=["NORMAL", "PNEUMONIA", "COVID"])
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual');
```



_Full paper will be translated and available soon._
_Stay tuned for updates._
