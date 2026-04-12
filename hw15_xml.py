"""
The program reads data from an XML file and displays the total cost of all goods.
"""

import xml.etree.ElementTree as ET


def parse_xml(xml_str):
    root = ET.fromstring(xml_str)
    price_list = []

    for product in root.findall('product'):
        price = float(product.find('price').text)
        price_list.append(price)
    total_price = sum(price_list)
    return print(f'Total cost of all products: {total_price}')


with open('products.xml', 'r', encoding='utf-8') as file:
    content = file.read()
    parse_xml(content)
