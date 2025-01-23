import sys
import os
import pytest
import json

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app


def test_buy_products_1():
    response = app.test_client().get('/products/buy?product_codes=GR1,GR1')
    res = json.loads(response.data)
    assert res["total_price"] == 3.11
    
def test_buy_products_2():
    response = app.test_client().get('/products/buy?product_codes=SR1,SR1,GR1,SR1')
    res = json.loads(response.data)
    assert res["total_price"] == 16.61
    
def test_buy_products_3():
    response = app.test_client().get('/products/buy?product_codes=GR1,CF1,SR1,CF1,CF1')
    res = json.loads(response.data)
    assert res["total_price"] == 30.57