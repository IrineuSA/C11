#3. Por meio do dataset space.csv, trace um gráfico em torta
#ilustrando a porcentagem de missões da empresa Roscosmos que
#deram certo e que deram errado;

import pandas as pd
import matplotlib.pyplot as plt

dSpace = pd.read_csv('C:\\Users\\Irineu\\Documents\\Projetos\\C11\\Cap-6\\Data\\space.csv',delimiter=';')
dRoscosmos = dSpace[dSpace["Company Name"] == "Roscosmos"]
statusMis = dRoscosmos["Status Mission"].value_counts()

plt.pie(statusMis, labels=list(statusMis.index), autopct='%1.1f%%', startangle=90, colors=["green","red","orange"])
plt.title("Missões da Roscosmos")
plt.show()