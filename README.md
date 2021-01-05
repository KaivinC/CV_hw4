# HW4

## Abstract

In this work, I use SRFBN to train my model

SRFBN [Paper](https://arxiv.org/pdf/1903.09814.pdf)|[Github](https://github.com/Paper99/SRFBN_CVPR19)

## Reproducing Submission

To reproduct my submission without retrainig, do the following steps

1. [Installation](#installation)
2. [Download Official Image](#download-official-image)
3. [Download Pretrained models](#pretrained-models)
4. [Inference](#inference)
5. [Make Submission](#make-submission)

## Installation

```bash
python3 -m pip3 install -r requirements.txt
```

## Dataset Prepare

### Prepare Images

The default data path as

```
data
    +-dataset
        +- training_hr_images
        +- testing_lr_images
        +- training
        +- val
        +- val_hr_image
```

### Download Official Image

Download and extract training_hr_images.zip and testing_lr_images.zip to dataraw directory.

#### Split Dataset

Please split image from training dataset by youslef.

And you need run following when first run.

```bash
TRAIN data augmentation:
python3 ./scripts/Prepare_TrainData_HR_LR.py -data_path [the path of dataset] -save_path [the path of augmentaion image save]

VAL data augmentation:
python3 ./scripts/Prepare_ValData_HR_LR.py -data_path [the path of dataset] -save_path [the path of augmentaion image save]
```

## Training

Please change the training and val image path in the ./options/train_SRFBN.json first.

My final submission is use SRFBN 

Run `train.py` to train.

```bash
python3 train.py -opt options/train_SRFBN.json
```

The expected training times are

Model | GPUs | Image size | Training Epochs | Training Time
------------ | ------------- | ------------- | ------------- | -------------
SRFBN | 2x 2080Ti | 40 | 140 | 6 hours

## Pretrained models

Because the size of the pretrained model is small, so I put it in the ./models

## Inference

Please remember change testing image path in ./options/test_SRFBN.json first.

If trained weights are prepared, you can create the result images which in the ./result by run below command

```bash
$python3 test.py -opt options/test_SRFBN.json
```


## Make Submission

Click [here](https://drive.google.com/drive/folders/1sbb527to9S8Ej-25QOb0IrQ-d2TDBcYK) to submission the json file!!

## Citation

```

@inproceedings{li2019srfbn,
    author = {Li, Zhen and Yang, Jinglei and Liu, Zheng and Yang, Xiaomin and Jeon, Gwanggil and Wu, Wei},
    title = {Feedback Network for Image Super-Resolution},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    year= {2019}
}

@inproceedings{wang2018esrgan,
    author = {Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},
    title = {ESRGAN: Enhanced super-resolution generative adversarial networks},
    booktitle = {The European Conference on Computer Vision Workshops (ECCVW)},
    year = {2018}
}
```