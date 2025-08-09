#Crie dois conjuntos, um para cada loja. Identifique quais modelos de
#smartphones cada uma delas vendem. Em seguida, mostre quais
#modelos no total você terá opção de comprar se visita-las e quais
#modelos se encontram disponíveis em ambas as lojas;

loja1 = {'iPhone 14', 'Samsung Galaxy S22', 'Google Pixel 6'}
loja2 = {'Samsung Galaxy S22', 'OnePlus 9', 'Motorola Edge 20'}

ambasLojas = loja1.intersection(loja2) #ambas as lojas
print("Modelos disponíveis em ambas as lojas:", ambasLojas)
totalDisp = loja1.union(loja2)  #total de modelos
print("Modelos disponíveis no total:", totalDisp)
