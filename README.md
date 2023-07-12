# stock

## 数据初始化教程
a_share.csv文件过大，超出了github单个文件的大小限制，我是手动传到服务器上的。可以'scp fcg@10.129.166.41:/home/fcg/stock/a_share.csv /your_diectory' 传输到本地
1. 运行table_create.sql中的sql语句。
2. 运行import_stock_info.py，注意修改其中的mysql账号密码信息。
3. 运行import_stock_info.py,注意修改其中的mysql账号密码信息。
4. 删除stock_trade中东方财富无法获取行情信息和已经退市的股票
'''
delete from stock where ts_code like '%.BJ';
delete from stock where ts_code='002417.SZ';
delete from stock where ts_code='688555.SH';
delete from stock where ts_code='688086.SH';
'''