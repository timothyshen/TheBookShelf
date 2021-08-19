# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '15/08/2021 23:47'


def filter_product(name):
    product_list = (
        ('100 coins', 'price_1JGWRMBaL13HgkoyNDpWFY15'),
        ('10 coins', 'price_1JF4FxBaL13HgkoymjNPtsCs')
    )

    for item in product_list:
        if name in item:
            return item[1]
