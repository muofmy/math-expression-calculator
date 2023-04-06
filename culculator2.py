#Данная программа вычисляет математические выражение, которые могут содержать следующие операции:сложение,вычитание,деление,умножение и т.д.; с учетом приоритетов этих операций.



def isdigit(a):                                             #Проверка символа на цифру.
    if a >= '0' and a <= '9':
        return True
    else:
        return False


expression = input('введите математическое выражение - ')   #Ввод выражения пользователя
numb = []
operations = []
i = 0
tmp = ''
if expression[0] == '-':                                    #Случай,когда выражение начинается с минуса
    tmp = '-'
    i += 1


while i < len(expression):                                  #Парсинг выражения на массивы Numb и Operatoins
    if isdigit(expression[i]) or expression[i] == '.':
        tmp = tmp + expression[i]
    else:
        numb.append(float(tmp))
        operations.append(expression[i])
        tmp = ''
    i += 1
numb.append(float(tmp)) 
#print(numb,operations)
i = len(operations)-1

                                                            #Операции с числами
while i > -1:                                               #Возведение в степень
    if operations[i] == '^':
        tmp2 = numb[i] ** numb[i+1]
        operations.pop(i)
        numb.pop(i)
        numb[i] = tmp2
    i -= 1



i = 0
while i < len(operations):                                     #Умножение и деление
    if operations[i] == '*':
        tmp2 = numb[i] * numb[i+1]
        operations.pop(i)
        numb.pop(i)
        numb[i] = tmp2
    elif operations[i] == '/' or operations[i] == ':':
        tmp2 = numb[i] / numb[i+1]
        operations.pop(i)
        numb.pop(i)
        numb[i] = tmp2
    else:
        i += 1



while len(operations) != 0:                                     #Сложение и вычитание
    if operations[0] == '+':
        tmp2 = numb[0] + numb[1]
        operations.pop(0)
        numb.pop(0)
        numb[0] = tmp2
    elif operations[0] == '-':
        tmp2 = numb[0] - numb[1]
        operations.pop(0)
        numb.pop(0)
        numb[0] = tmp2
print('Ответ :',numb[0])                                                   #Вывод ответа

