#1. Crie duas Series com os seguintes valores:
#• seriesAno1: {‘Java’: 16.25, ‘C’: 16.04, ‘Python’: 9.85}
#• seriesAno2: {‘C’: 16.21, ‘Python’: 12.12, ‘Java’: 11.68}
#2. Os valores das Series criadas na Questão 1 representam as fatias de
#mercado (porcentagem) de 3 linguagens de programação populares em
#dois anos consecutivos. Para cada ano, apresente a porcentagem total que
#elas juntas representam no mercado;
#3. Apresente o crescimento/declínio no mercado de cada linguagem do
#primeiro ano para o segundo ano;
#4. Baseado nos resultados da Questão 3, mostre apenas os dados das
#linguagens que tiveram crescimento;
#5. Se estas porcentagens de crescimento/declínio se mantivessem iguais
#para os próximos 2 anos, qual seria a linguagem mais popular?

import pandas as pd
#1.
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

#2.
totAno1 = seriesAno1.sum()
totAno2 = seriesAno2.sum()
print(f'Total Ano 1: {totAno1}%')
print(f'Total Ano 2: {totAno2}%')

#3.
crescDecl = seriesAno2 - seriesAno1
print('\nCrescimento/Declínio de cada linguagem do primeiro ano para o segundo ano:')
print(crescDecl)

#4.
cresc = crescDecl[crescDecl > 0]
print('\nLinguagens que tiveram crescimento:')
print(cresc)

#5.
crescFut = crescDecl * 2
futAno2 = seriesAno2 + crescFut
maisPop = futAno2.nlargest(1)
print('\nLinguagem mais popular em 2 anos:')
print(maisPop)
