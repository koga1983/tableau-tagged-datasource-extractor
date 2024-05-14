# 🏷️ tableau-tagged-datasource-extractor

このプロジェクトは、**Tableau Server Client (TSC)** を使用して、特定のタグが設定されたデータソースを **Tableau Server** または **Tableau Online** から抽出するためのツールです。

## 📋 必要条件

- Tableau Server または Tableau Online のアカウント
- API トークン
- Python 3.6以上
- Tableau Server Client ライブラリ

## 🚀 インストール

1. リポジトリをクローンします:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. 必要な Python パッケージをインストールします:

    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ 使用方法

1. `extract_datasource.py` ファイルを編集し、以下の情報を入力します:

    ```python
    server_url = 'https://your-tableau-server'
    api_token_name = 'your-token-name'
    api_token_value = 'your-token-value'
    site_id = 'your-site-id'
    desired_tag = 'your-tag'
    ```

2. スクリプトを実行します:

    ```bash
    python extract_datasource.py
    ```

スクリプトは指定されたタグを持つデータソースを抽出し、指定されたディレクトリに保存します。

## ⚙️ 機能

- **データソースの抽出**: 特定のタグが設定されたデータソースを抽出します。
- **エラーハンドリングとリトライ**: エラーが発生した場合に自動的にリトライします。
- **ページネーション**: 大量のデータソースを効率的に処理します。


## 🛡️ エラーハンドリングとリトライ

このスクリプトには、エラーハンドリングとリトライ機能が組み込まれています。データソースの取得やダウンロードに失敗した場合、最大3回までリトライを行います。

## 📜 ページネーション

大量のデータソースを取得する際にAPI制限に引っかからないよう、ページネーションを利用しています。一度に100件のデータソースを取得し、全データソースを取得するまで繰り返します。

## 📄 ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。[LICENSE](./LICENSE)

---

## 📚 詳細情報

- **Tableau Server Client ドキュメント**: [Tableau Server Client Library](https://tableau.github.io/server-client-python/docs/)
- **Tableau REST API ドキュメント**: [Tableau REST API](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm)

## 💡 注意事項

このスクリプトを実行する際には、適切なAPIトークンとアクセス権限が必要です。APIトークンの管理には十分注意してください。

---


### 🌟 **スターを付けてください！** 🌟

このリポジトリが役に立った場合は、スターを付けてください。あなたのサポートが私たちの励みになります！

[![GitHub Stars](https://img.shields.io/github/stars/koga1983/ansible?style=social)](https://github.com/koga1983/ansible/stargazers)
