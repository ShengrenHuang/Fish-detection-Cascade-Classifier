# Fish-detection-Cascade-Classifier


在本專案中，我們利用[2] 蒐集水中生物的positive image，由於魚種類眾多，我們擷取部分的data 擷取魚的haar 特徵當作我們的positive image，之後我們必須決定 negative image，我們預設場景為深海中，因此我們利用google 的extension Fatkun extension，來下載大量的沒有魚群的深海背景，因此我們就有 negative image，之後同樣透過 opencv 的文件[3]來訓練我們 cascade classifier，之後我們以一段深海實際影片[1] 來測試我們的 cascade classifier，我們可以發現 classifier 可以準確地偵測魚的位置，然而，值得一提的是，並不是所有海洋紀錄影片都可以發揮我們cascade classifier的功用，在部分的影片中，我們發現無法有效辨識，推測與海洋水質混濁，different species, 陽光強度與海床環境造成不同場景的色溫擾動而使我們的 cascade classifier無法正確偵測。

In this project, we aim to introduce a cascade classifier to identify the marine creatures in the deep ocean. We first collect the images of different fish species from the kaggle image database [1]. Owing to plenty of fish species, we randomly choose parts of images to be the positive frames for training. It is noted that we also apply the cropping process to extract the primary Haar features of the fishes. To establish the pools of negative images, we employ one of google's extensions ---Fatkun [2], to batch-download the deep ocean background. Then, we set up the training software from Opencv [3] to derive the fish cascade classifier. We verify the validity of our classifier with actual footage taken in the deep ocean [4]. The result shows that the classifier can detect the fish precisely in the footage. However, one should note that the classifier fails to detect the fishes in other reels. So what is the problem? Regardless of the fish species, the authors in [5] stated that the key obstacles for fish detection are 1) uneven light distribution and 2) fish overlapping. Besides, we found out that the following issues can be investigated further:
1. What kinds of negative images would be better?
2. How many fish photos will be enough for training?  





![image](https://user-images.githubusercontent.com/108604868/183370854-14a2f97e-77d5-4182-ae53-26dcb7a396b7.png)














https://user-images.githubusercontent.com/108604868/184276607-3e51f243-de73-44ba-a62f-70a1696af00a.mp4
























# Reference
[1] https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset  
[2] https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=zh-TW
[3] https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html 
[4] https://www.pexels.com/video/a-fish-swimming-underwater-5548177/  
[5] Detection of Bluefin Tuna by Cascade Classifier and Deep Learning for Monitoring Fish Resources

