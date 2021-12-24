import json
from datetime import datetime,timedelta
import numpy as np

class Product(object):
    def __init__(self,sku,name):
        self.sku= sku
        self.name=name

class Purchase(object):
    def __init__(self,number,date,products):
        self.number=number
        self.date=date
        self.products=products

def jsonToList(customer):
    for buyer in customer["customer"]["purchases"]:
        productsTemp = []
        for product in buyer["products"]:
            productTemp = Product(product["sku"], product["name"])
            productsTemp.append(productTemp)
        purchases.append(Purchase(buyer["number"], datetime.strptime(buyer["date"],'%Y-%m-%d'), productsTemp))

def getFrecuencia(date1,date2):
    return (date1 - date2 )/ timedelta(days=1)

def detectAtypical(data):

    cuartil1, cuartil3 = np.percentile(sorted(data), [25, 75])

    iqr = cuartil3 - cuartil1

    lowerBound = cuartil1 - (1.5 * iqr)
    upperBound = cuartil3 + (1.5 * iqr)

    atypical = [x for x in data if x <= lowerBound or x >= upperBound]

    return atypical

def getMedia(values):
    return sum(values)/len(values)

def nextRebuy(ultimaCompra,media):
    return ultimaCompra + timedelta(days=round(media))

if __name__ == "__main__":

    file = open('purchases-v2.json')
    customer = json.load(file)
    purchases=[]
    products=[]
    keysAux = []
    skuAndDates = {}
    ultimaCompra={}

    jsonToList(customer)

    for p in purchases:
        for d in p.products:
            if d.sku in skuAndDates.keys():
                a = skuAndDates[d.sku]
                a.append(p.date)
                skuAndDates.update({d.sku: a})
            else:
                skuAndDates.update({d.sku: [p.date]})


    for keys in skuAndDates:
        if len(skuAndDates[keys]) == 1:
            keysAux.append(keys)
        else:
            distances = []
            ultimaCompra.update({keys:skuAndDates[keys][len(skuAndDates[keys])-1]})
            for index in range(len(skuAndDates[keys])):
                if index + 1 < len(skuAndDates[keys]):
                    distances.append(getFrecuencia(purchases[index + 1].date,purchases[index].date))
            skuAndDates.update({keys:distances})

    for key in keysAux:
        skuAndDates.pop(key)

    print(len(skuAndDates))

    for sku in skuAndDates:
        for a in detectAtypical(skuAndDates[sku]):
            skuAndDates[sku].remove(a)
        print("Es probable que la próxima fecha de recompra del producto ",sku," sea el",nextRebuy(ultimaCompra[sku],getMedia(skuAndDates[sku])))


