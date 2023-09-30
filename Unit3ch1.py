def LinearSearchProduct(productList,targetProduct):

    indices = []

    for index, product in enumerate(productList):

        if product ==  targetProduct:

            indices.append(index)            

            return indices

        



products = ["shoes","boot","loafer","shoes","sandals","shoes"]         

target = "loafer"

target2 = "apple"

result = LinearSearchProduct(products,target)

result2 = LinearSearchProduct(products,target2)

print(result) 

print(result2)  