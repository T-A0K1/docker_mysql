docker上でmysqlを起動するためのファイルです。

【概要】
・本ディレクトリは以下を参考にしています。
https://mmtomitomimm.blogspot.com/2018/04/docker-mysqldb.html
・上記からの一番の変更点として、mysqlのデータが永続化(dockerを再起動しても保存されている)するようにしています。
　コンテナ上の/var/lib/mysqlが保存されます。

【備考】
・"./mysql/db/init.sql"はテスト用の初期実行ファイルです。
 不要な場合は、当該ファイルを削除した上で、docker-compose.ymlから"- ./mysql/db:/docker-entrypoint-initdb.d #初期データ"の記載を削除してください。
・mysqlのベースイメージは、2020/12/13時点のlatestを使用しています。

【操作方法】
・docker-composeでmysqlを起動する
・本ディレクトリ上で、以下を実行することで起動できます。
docker-compose build #dockerfileをもとにビルド
docker-compose up -d #dockerコンテナの起動
docker exec -it mysql_1 bash #dockerコンテナへ接続
・接続後は、以下のコマンドでmysqlへ接続できます。
(デフォルトのrootパスワードはpasswordです。docker-compose.ymlを参照)
mysql -u root -p
・停止する場合
docker-compose down
・クライアントから直接mysqlへ接続
mysql -u root -p -h localhost -P 3306 --protocol=tcp