# **COVID-CXR**
In this part of my graduate project I've made a research and managed to make my model to classify COVID-19, pneumonia affected and healthy lungs using only chest X-RAY images.

It was possible to achieve amazing results that are ahead of all similar researches that I have found. You can find specific numbers and comparisons further below.
_____

# **Data Availability and preprocesing**
I've merged several publicly available datasets.
Data I used is available [here](https://mega.nz/file/ksdhiApA#14L2kG7aI6ep06fJEXVqN7OAQ5DzzOZjSsz_HwlluSc)

Data was resized to 224x224 pixels and normalized. 

Data augmentations techniques were applied.

# **Model overview**

I've implemented and tried both State-Of-Art models and models from scratch. Experiments showed that DenseNet201 achieved better results amidst all models so I chose it for further developing.

# **Results and comparisons**

| metrics             | our model | [RA20](https://doi.org/https://doi.org/10.1016/j.imu.2020.100360)   | [Sad+21](https://www.nature.com/articles/s41598-021-95561-y) | [MSH22](https://doi.org/https://doi.org/10.1016/j.eij.2022.01.002)  | [Luj+20](https://doi.org/10.3390/math8091423) | [Bac+21](https://doi.org/10.1101/2021.07.15.21260605) |
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

