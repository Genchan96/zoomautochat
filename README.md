# Zoomautochat-beta
これはZoomオンライン授業で入室時に自動で出席チャットをやってくれるツールです。

ツールを改善してくれる方いたらPullrequestかDiscord Genchan_96#0025まで

# 使用方法
-[releases](https://github.com/Genchan96/zoomautochat/releases/tag/beta)に移動

-Source code(zip)をダウンロード

-Zipファイルを展開する

-name.txtに出席番号と自分の名前を入力

-main.exeを実行

-Zoomの入室時に自動でチャットが開かれたあとname.txtの中身がチャットに送信されます

1時間目が始まる前にmain.exeを実行しっぱなしにしておけば、1時間目、2時間目、3時間目…と一日の授業が終わるまで自動で出席チャットを入力してくれるはずです。

# コメント

最初はzoomのapi使おうとしたけどapiがzoomの有料会員しか使えないということで断念。

みんなに使ってもらいたかったのでs-tab等の環境でも動作する設計にしました。

そこでzoomの入室時に起動するcpthost.exeというプロセスを監視しそれが検出されたらpyautoguiでALT+Hでチャットを開いたあとname.txtの内容を入力するというクソみたいな仕組みになっています。

問題点：cpthost.exeはミーティング待機時にも起動するのでミーティング待機時にチャット入力コードが暴発する
あまり大きな影響はないと思う

