# Multi-Otsu-Thresholding-Sample
OpenCVで画像を読み込み、scikit-imageのMulti-Otsu-Thresholdingを実行するサンプルです。

https://user-images.githubusercontent.com/37477845/225489356-891142cf-3e97-4188-8528-d4661769cc7c.mp4

# Requirement 
* OpenCV 3.4.2 or later
* scikit-image 0.19.1 or later

# Demo
デモの実行方法は以下です。
```bash
python sample.py
```
* --device<br>
カメラデバイス番号の指定<br>
デフォルト：0
* --movie<br>
動画ファイルの指定 ※指定時はカメラデバイスより優先<br>
デフォルト：指定なし

# Reference
* [sciki-image：Multi-Otsu Thresholding](https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_multiotsu.html)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
Multi-Otsu-Thresholding-Sample is under [Apache-2.0 License](LICENSE).

# License(Movie)
サンプル動画は[NHKクリエイティブ・ライブラリー](https://www.nhk.or.jp/archives/creative/)の[フランス・パリ セーヌ川とポンデザール（芸術橋）](https://www2.nhk.or.jp/archives/movies/?id=D0002161451_00000)を使用しています。


