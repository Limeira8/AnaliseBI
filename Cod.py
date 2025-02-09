import pandas as pd

sales_data = pd.read_csv('C:/Users/raian/Desktop/Dados/report.csv', encoding='ISO-8859-1', delimiter=';')

sales_data['Data'] = pd.to_datetime(sales_data['Data'], format='%d/%m/%Y')

sales_data['Valor'] = sales_data['Valor'].replace('[R$]', '', regex=True).replace(',', '.', regex=True).astype(float)

sales_data = sales_data.drop(columns=['Unnamed: 5'])

sales_data.to_csv('C:/Users/raian/Desktop/Dados/tratado.csv', index=False)
