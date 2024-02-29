# 環境構築の手順

## # 仮想環境作成
VSコードからターミナルタブ → 新しいターミナル → 下に出てくるターミナルより以下を入力
```
conda create -n python310_test_project python=3.10 -y
```

## # 仮想環境のアクティベート
下に出ているターミナルより以下を入力
```
conda activate python310_test_project
```

## # ライブラリのインストール
入れたいライブラリはrequirements.txtに入れる。  
(ライブラリのバージョンまで指定できるとよい　例：streamlit==1.31.1)  
必要なライブラリを入れたら、仮想環境に入った状態で 、 
((python310_test_project) PS ~~~になっている状態で)
以下を入力  
```
pip install -r requirements.txt
```
必ず仮想環境に入った状態で行うこと。(base)のままだと大元のPCにライブラリが入って重くなるため。

# 初期設定
現段階ではなし
# 実行方法
仮想環境に入った状態で((python310_test_project) PS ~~~になっている状態で)
```
print(Hello!)
```
再び(python310_test_project) PS ~~~になるまでは待ち