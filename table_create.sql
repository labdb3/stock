
create table if not exists stock_info(ts_code varchar(12) PRIMARY KEY, company_name varchar(12), category varchar(12) )CHARACTER SET utf8;
create table if not exists stock_trade(ts_code varchar(12), trade_date date, open float, high float,low float, close float,pre_close float, pct_change float,vol float, amount float);