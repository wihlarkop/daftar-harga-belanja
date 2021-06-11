# Daftar Harga Belanja

## Description

Inspired by (https://github.com/k1m0ch1/BiBiT)

## TODO

- [x] Klikindomart
- [ ] Alfacart

## Installation

create virtual environment,

1. pip install -r requirements.txt

### Environment Variable

create .env file and write this on .env

```
KLIKINDOMART_BASE_URL=https://www.klikindomaret.com
KLIKINDOMART_PARAMS=?categories=&productbrandid=&sortcol=&pagesize=50&startprice=&endprice=&attributes=
KLIKINDOMART_PARAM_PAGE=&page=
```

## Running

if you want display all promo you need to run

```python
python main.py
```

if you want to search product you need to run

```python
python main.py "product_name"
```