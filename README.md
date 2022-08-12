# Fish-detection-Cascade-Classifier


In this project, we aim to introduce a cascade classifier to identify the marine creatures in the deep ocean. We first collect the images of different fish species from the kaggle image database [1]. Owing to plenty of fish species, we randomly choose parts of images to be the positive frames for training. It is noted that we also apply the cropping process to extract the primary Haar features of the fishes. To establish the pools of negative images, we employ one of google's extensions ---Fatkun [2], to batch-download the deep ocean background. Then, we set up the training software from Opencv [3] to derive the fish cascade classifier. We verify the validity of our classifier with actual footage taken in the deep ocean [4]. The result shows that the classifier can detect the fish precisely in the footage. However, one should note that the classifier fails to detect the fishes in other reels. So what is the problem? Regardless of the fish species, the authors in [5] stated that the key obstacles for fish detection are 1) uneven light distribution and 2) fish overlapping. Besides, we found out that the following issues can be investigated further:
1. What kinds of negative images would be better?
2. How many fish photos will be enough for training?  





![image](https://user-images.githubusercontent.com/108604868/183370854-14a2f97e-77d5-4182-ae53-26dcb7a396b7.png)














https://user-images.githubusercontent.com/108604868/184276607-3e51f243-de73-44ba-a62f-70a1696af00a.mp4
























# Reference
[1] A Large Scale Fish Dataset:  
https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset .  
[2] Fatkun:  
https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=zh-TW .  
[3] Cascade Classifier Training:  
https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html .     
[4] Fish footage from Taryn Elliott:  
https://www.pexels.com/video/a-fish-swimming-underwater-5548177/ .  
[5] Guanglei, et al., Detection of Bluefin Tuna by Cascade Classifier and Deep Learning for Monitoring Fish Resources, 2020.

