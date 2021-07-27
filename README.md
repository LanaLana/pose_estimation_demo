# Pose estimation demo

![Alt Text](https://github.com/LanaLana/pose_estimation_demo/blob/main/pose_estimation.gif)

This repo includes the following steps:

* downloading [video from youtube](https://www.youtube.com/watch?v=1ovAjgh2ezM&ab_channel=%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D0%B5%D0%BC%D0%B5%D0%B4%D0%B8%D0%B0.%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8)
* runing inference for pose estimation. Pre-trained on COCO model weights for Lightweight OpenPose model are downloaded from: https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth
* detecting and counting scenes with hands up
* streaming video with pose estimation and results   

To launch server with results vizualization:

```bash
python app.py
```

To launch full code with data preprocessing and pose estimation model see [pose_estimation.ipynb](https://github.com/LanaLana/pose_estimation_demo/blob/main/pose_estimation.ipynb)

Code for pose estimation is from https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch.git

![Alt Text](https://github.com/LanaLana/pose_estimation_demo/blob/main/processed/frame_66_0.jpg)

Example of detected scene with hands up
