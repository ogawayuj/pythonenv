--DROP TABLE mst_stock

CREATE TABLE mst_stock (
    stock_code INTEGER,
    company_name varchar(40),
    market_name varchar(10),
    industry_name varchar(10),
    share_unit INTEGER,
    nikkei_flg bit,
    PRIMARY KEY (stock_code)
)