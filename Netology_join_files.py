line_count_dict = {}
with open('1.txt', 'r', encoding='utf-8') as f1:
    count_f1 = 0
    while True:
        if '\n' in f1.readline():
            count_f1 += 1
        else:
            count_f1 += 1
            break

with open('2.txt', 'r', encoding='utf-8') as f2:
    count_f2 = 0
    while True:
        if '\n' in f2.readline():
            count_f2 += 1
        else:
            count_f2 += 1
            break

with open('3.txt', 'r', encoding='utf-8') as f3:
    count_f3 = 0
    while True:
        if '\n' in f3.readline():
            count_f3 += 1
        else:
            count_f3 += 1
            break

line_count_dict.update([('1.txt', count_f1), ('2.txt', count_f2), ('3.txt', count_f3)])
line_count_list = sorted(list(line_count_dict.items()), key=lambda x: x[1])

with open('4.txt', 'w+', encoding='utf-8') as f4:
    for i in line_count_list:
        f4.write(f'{i[0]}\n')
        f4.write(f'{i[1]}\n')
        with open(i[0], 'r+', encoding='utf-8') as f4_1:
            f4.write(f4_1.read() + '\n')
    f4.flush()
    # Ниже вызываем еще один контекстный менеджер с целью удалить пустую строку, появляющуюся после чтения последнего
    # файла
    with open('4.txt', 'r+', encoding='utf-8') as f4_2:
        lines = f4_2.readlines()
        if '\n' in lines[-1]:
            replace_symbol = lines[-1].replace('\n', '')
        lines.pop(-1)
        lines.append(replace_symbol)
        f4_2.seek(0)
        f4_2.truncate()
        f4_2.write("".join(lines))
