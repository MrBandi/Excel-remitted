import pandas as pd

xlsx_file = '112-4.xlsx'
rd_xlsx = pd.read_excel(xlsx_file, header=0)

criteria2 = {'類別名稱': '電機與電子群_資電類', '學校名稱': '私立啟英高中'}

filtered_data2 = rd_xlsx[(rd_xlsx['類別名稱'] == criteria2['類別名稱']) & (rd_xlsx['學校名稱'] == criteria2['學校名稱'])]

columns = list(rd_xlsx.columns)
indices = [columns.index(col) for col in ['國文合計', '英文合計', '數學', '專一', '專二', '總分', '總分排名']]

output1 = filtered_data2.iloc[:, indices]

output1.to_excel('output1.xlsx', index=False)
