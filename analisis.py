import json
from collections import defaultdict
from collections import Counter
from pprint import pprint

product_set = []

#Objeto que se crea con la data de un .json en la carpeta /json
class Dataset():
    def __init__(self):
        with open('json/fashion_nova.json') as f:
            self.json = json.load(f)
            self.json = self.json['products']

    #Instancia que cuenta cantidad de vendors y los agrupa en un Counter
    def getVendorsCount(self):
        return Counter(product['vendor']
                       for product in self.json)

    #Instancia que tira un listado único de Vendors
    def getVendorsUnique(self):
        return self.getVendorsCount().keys()

    #Instancia que tira la data de X Vendor, default todos los vendors
    def getVendorData(self, vendor = '*'):
        if vendor == "*":
            return [product
                for product in self.json
            ]
        else:
            return [product
                for product in self.json
                if product['vendor'] == vendor
            ]

#Función que cuenta cantidad de variantes para determiando producto
def countVariants(obj2 = False):
    #product es un dict de un producto entero
    x = 0
    if obj2 == False:
        obj2 = data.json
        return

    for product in obj2:
        for variant in product['variants']:
            x = x + 1
    return int(x)

#Función que suma el precio total para todas las variantes de un producto
def sumPrice(obj1 = False):
    #product es un dict de un producto entero
    p = 0
    if obj1 == False:
        obj1 = data.json
        return

    for product in obj1:
        for variant in product['variants']:
            p = p + float(variant['price'])
    return p

#Función que saca el promedio de la suma de precio sobre la cuenta de variantes
def averagePrice(obj = False):
    if obj == False:
        obj = data.json

    return [ sumPrice(obj) / countVariants(obj) ]

#Inicialización
if __name__ == "__main__":
    data = Dataset()
    print(data.getVendorsUnique())
    #print(data.getVendorData())
    #print(data.json)
    print(averagePrice(data.getVendorData('ColourPop')))
