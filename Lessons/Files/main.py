#try:
    #txt_file = open("hello.txt", "wt", encoding="UTF-8")
#except Exception as e:
    #print(e)


# 2 способ
try:
    with open("hello.txt", "wt", encoding="UTF-8") as txt_file:
        for i in range(10):
            res_line = f"Строка номер: {i}\n"
            txt_file.write(res_line)

except Exception as e:
    print(e)

try:
    with open("hello.txt", "rt", encoding="UTF-8") as txt_file:
        for line in txt_file:
            print(line)

except Exception as e:
    print(e)