from deta import Deta

# "project key" is necessary in local, but it's not on Deta base
deta = Deta()
# userテーブル(名前:fastapi-crud)を作成
users = deta.Base("fastapi-crud")