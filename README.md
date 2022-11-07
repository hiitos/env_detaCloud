# Deta Cloud

## ログイン
deta login

## deploy
```
deta new
```
か
```
deta new --python
```

## コードを再度デプロイする場合
```
deta deploy
```

## deta への変更を常に監視する場合
※ローカルで編集した内容が即時、Deta側へ反映されます

```
deta watch
```



Databaseを利用する場合は、Deta BaseにてNoSQLでテーブル作成とCRUD操作はできる

Driveには10GBまでファイルをアップロードできる

[参考](https://masa-engineer-blog.com/python-fast-api-deploy-with-deta-cloud/)  
[参考2](https://rest-term.com/archives/3683/)

*注意
appインスタンスの名前にすること  
main.pyを用意すること