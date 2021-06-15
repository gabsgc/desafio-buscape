from application.model.entity.product import Product
import json
from typing import List

class ProductDAO:
    def __init__(self):
        product1 = Product(2321312, "Smartphone Apple iPhone 7 128GB", "http://thumbs.buscape.com.br/celular-e-smartphone/smartphone-apple-iphone-7-128gb_600x600-PU98460_1.jpg", 3509.10, 10, 389.90)
        product2 = Product(9971, "Smart TV Samsung Série 4 UN32J4300AG 32 polegadas LED Plana", "http://mthumbs.buscape.com.br/tv/smart-tv-samsung-serie-4-un32j4300ag-32-polegadas-led-plana_600x600-PU95547_1.jpg", 1139.90, 10, 134.11)
        product3 = Product(6717131, "Câmera Digital Canon EOS Rebel T5i 18.0 Megapixels", "http://mthumbs.buscape.com.br/camera-digital/canon-eos-rebel-t5i-18-0-megapixels_600x600-PU7bf7b_1.jpg", 1999.20, 10, 235.20)
        product4 = Product(6717132, "Lenovo IdeaPad 310 80UH0004BR Intel Core i7-6500U 2.5 GHz 8192 MB 1024 GB", "http://mthumbs.buscape.com.br/notebook/lenovo-ideapad-310-80uh0004br-intel-core-i7-6500u-2-5-ghz-8192-mb-1024-gb_600x600-PU98e6e_1.jpg", 2599.00, 10, 259.90)

        self._products = [product1, product2, product3, product4]

        self._cart_list = []

    def findAll(self):
        return self._products

    def addCart(self):
        return self._cart_list

    """
    def findAll(self):
        product_list = []
        with open('data.json', 'r') as file:
            product_list_json = json.load(file)
            product_list = self.dictToList(product_list_json)
        return product_list

    def dictToList(self, product_list):
        product_list = []
        for product_dict in product_list:
            product = Product()
            product._id(product_dict['id'])
            product._name(product_dict['name'])
            product._images(product_dict['images'])
            product._value(product_dict['value'])
            product._installments(product_dict['installments'])
            product._installment_value(product_dict['installment_value'])
            product_list.append(product)
        return product_list
    """