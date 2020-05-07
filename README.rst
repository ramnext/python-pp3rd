==============
乗りログアプリ
==============


目的
====


Webブラウザーでコメントを投稿するWebアプリケーションの練習。


ツールのバージョン
==================
:Python:    3.7.5
:pip:       20.0.2


インストールと起動方法
======================


リポジトリーからコードを取得し、その下にvenv環境を用意します::


    $ git clone https://github.com/ramnext/python-pp3rd.git
    $ cd norilog
    $ python3.7 -m venv .venv
    $ source .venv/bin/activate.fish
    (venv) $ pip install .
    (venv) $ norilog
     * Running on http://0.0.0.0:8000/


開発手順
========


開発用インストール
==================


1. チェックアウトする
2. 以下の手順でインストールする::

    (venv) $ pip install -e .


依存ライブラリ変更時
====================


1. \`\`setup.py\`\`の\`\`install_requires\`\`を更新する
2. 以下の手順で環境を更新する::

    (venv) $ deactivate
    $ python3.7 -m venv --clear .venv
    $ source .venv/bin/activate.fish
    (venv) $ pip install -e .
    (venv) $ pip freeze > requirements.txt

3. setup.pyとrequirements.txtをリポジトリーにコミットする

