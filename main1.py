import pandas as pd

X_files = ['112-1.xlsx', '112-2.xlsx', '112-3.xlsx', '112-4.xlsx']

for v in X_files:
    rd_xlsx = pd.read_excel(v, header=0)
    filtered_data = rd_xlsx[rd_xlsx['類別名稱'] == '電機與電子群_資電類']
    subjects = ['國文合計', '英文合計', '數學', '專一', '專二', '總分']
    subject_scores = filtered_data[subjects]

    sum_scores = subject_scores.sum()

    num_schools = filtered_data['學校名稱'].nunique()

    average_scores = sum_scores / num_schools

    average_scores_formatted = average_scores.apply(lambda x: f'{x:.2f}')

    with open(f'{v}.txt', 'w') as file:
        for subject, score in average_scores_formatted.items():
            file.write(f'{subject}: {score}\n')
