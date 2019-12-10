--DROP TABLE trn_stock_price_by_date

CREATE TABLE trn_stock_price_by_date (
    stock_code INTEGER,
    recorded_date DATE,
    price_open INTEGER,
    price_close INTEGER,
    price_highest INTEGER,
    price_ceapest INTEGER,
    price_the_day_before INTEGER,
    volume_stock_trading INTEGER,
    memo1 VARCHAR(30),
    memo2 VARCHAR(30),
    PRIMARY KEY (stock_code, recorded_date)
)