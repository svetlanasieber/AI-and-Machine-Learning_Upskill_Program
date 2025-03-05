EMPTY = ""
NEW_LINE = "\r\n"
SPACE = " "


first_num = int(input())
second_num = int(input())
third_num = int(input())


output = EMPTY


for i in range(1, first_num + 1):
    if i % 2 == 0:
        for j in range(1, second_num + 1):

            is_simple = j in (2, 3, 5, 7)
            if is_simple:
                for k in range(1, third_num + 1):
                    if k % 2 == 0:

                        output += f"{i}{SPACE}{j}{SPACE}{k}{NEW_LINE}"


print(output)
