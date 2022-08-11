# Fish-detection-Cascade-Classifier


在本專案中，我們利用[2] 蒐集水中生物的positive image，由於魚種類眾多，我們擷取部分的data 擷取魚的haar 特徵當作我們的positive image，之後我們必須決定 negative image，我們預設場景為深海中，因此我們利用google 的extension Fatkun extension，來下載大量的沒有魚群的深海背景，因此我們就有 negative image，之後同樣透過 opencv 的文件[3]來訓練我們 cascade classifier，之後我們以一段深海實際影片[1] 來測試我們的 cascade classifier，我們可以發現 classifier 可以準確地偵測魚的位置，然而，值得一提的是，並不是所有海洋紀錄影片都可以發揮我們cascade classifier的功用，在部分的影片中，我們發現無法有效辨識，推測與海洋水質混濁，陽光強度與海床環境造成不同場景的色溫擾動而使我們的 cascade classifier無法正確偵測。





![image](https://user-images.githubusercontent.com/108604868/183370854-14a2f97e-77d5-4182-ae53-26dcb7a396b7.png)












https://user-images.githubusercontent.com/108604868/183384243-a9b7d9fe-10f4-40a4-8711-5595bbec3ab0.mp4












跟魚種, 水的顏色, 還有混濁程度都有影響
在部分的影片中即便有魚也完全偵測不到魚。




# Reference
[1] https://www.pexels.com/video/a-fish-swimming-underwater-5548177/  
[2] https://www.kaggle.com/datasets/crowww/a-large-scale-fish-dataset  
[3] https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html 
