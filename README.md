# 環境設定

## asdfのインストール

https://asdf-vm.com/guide/getting-started.html#_1-install-dependencies

```
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.1

# edit ~/.bashrc
. "$HOME/.asdf/asdf.sh"

```


## pythonのインストール

```
sudo yum install libffi-devel
asdf plugin list all | grep python
asdf plugin add python https://github.com/danhper/asdf-python.git
asdf install python 3.10.12
asdf global python 3.10.12
python --version
```

## poetryのインストール

```
asdf plugin-add poetry
asdf install poetry 1.8.2
asdf global poetry 1.8.2
poetry --version
```

## 依存ライブラリの導入

```
poetry config virtualenvs.in-project true --local
poetry install
```


## LangChain学習環境の動作確認

### 実行方法

コンソールアプリの例：

```
poetry run python app/1_langchain.py
```

Streamlitアプリの例：

```
poetry run streamlit run app/4_streamlit.py --server.port 8080
```

# !!! この先は通常は不要な手順です !!!

## poetryプロジェクトの初期化(新規プロジェクトの場合)

```
# poetry初期化（基本的に全部デフォルトで良い）
poetry init

# 仮想環境の使用
poetry config virtualenvs.in-project true --local

# pythonのバージョン確認
poetry run python --version
```

## requirements.txtから依存パッケージをインストールする(新規プロジェクトの場合)

```
cat requirements.txt | xargs poetry add
```
