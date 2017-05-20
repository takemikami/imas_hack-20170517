このリポジトリは、  
2017/05/17に開催された「アイマスエンジニア MeetUp in Tokyo」で発表した  
「担当アイドルに反応してLチカする予測モデル開発」のソースコード及び補足説明です。

アイマスエンジニア MeetUp in Tokyo  
2017.05.17 @ クラウドワークス  
https://imas.connpass.com/event/54949/

# 概要

このソースコードで実施するシステムの全体像は、以下の図のようになります。

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/62769571@N03/31160691940/in/dateposted-public/" title="iotlt20160812_1"><img src="https://c5.staticflickr.com/1/758/31160691940_7ced556096_z.jpg" width="640" height="360" alt="iotlt20160812_1"></a>

## ファイル構成

- README.md ... このファイル
- prepare-data.py ... 学習用データの準備
- opencv-face.ipynb ... OpenCVによる顔認識
- keras-train.ipynb ... TensorFlow/Kerasによる分類(学習)
- keras-predict.ipynb ... TensorFlow/Kerasによる分類(予測)
- pyserial-led.ipynb ... pyserialによるArduinoへの通信
- sketch_may17a/sketch_may17a.ino ... Arduino側のLチカ用プログラム
- requirements.txt ... 依存ライブラリリスト


# 実行環境のセットアップ

私の実施した環境は、macos上で、  
pyenvから「anaconda3-4.3.0」を、  
homebrewで「OpenCV」をインストールしています。

具体的な手順は、以下のブログエントリを参考にしてください。  
http://takemikami.com/2016/12/10/TensorFlowLEDIoTLT.html

anacondaのセットアップが出来たら、  
TensorFlowをインストールします。

```
$ conda install -c conda-forge tensorflow
```

次に、以下のようにして依存ライブラリをインストールします。

```
$ pip install -r requirements.txt
```


# 学習用データの準備

以下のプログラムを実行して、学習用のデータを準備します。

```
$ python prepare-data.py
```

学習用のデータは「data」ディレクトリ配下にファイルが出力されます。

具体的に行っている処理は以下の通りです。

- アニメ顔検出器のダウンロード ( http://ultraist.hatenablog.com/entry/20110718/1310965532 )
- プラチナスターズのアイドルPVをダウンロード
- コマ送りにしてアイドルの顔画像を切り出す
- 適当な雪歩・美希、やよいの画像データをダウンロード


# OpenCVによる顔認識

この手順以降は、jupyternotebookを用いて行うので、以下コマンドで起動します。

```
$ jupyter notebook
```

「opencv-face.ipynb」ファイルが、対象の処理です。

jupternotebookで実行しながら確認してください。


# TensorFlow/Kerasによる分類

「keras-train.ipynb」が学習の処理、  
「keras-predict.ipynb」が予測の処理です。

こちらもjupternotebookで実行しながら確認してください。


# pyserialによるArduinoへの通信

「pyserial-led.ipynb」ファイルが、対象の処理です。

arduino側のプログラムは「sketchf_may11a」以下のファイルになります。
