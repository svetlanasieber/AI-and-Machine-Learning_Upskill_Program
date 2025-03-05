class NumberProcessor:
    def __init__(self, first_num, second_num, third_num):
        self.first_num = first_num
        self.second_num = second_num
        self.third_num = third_num
        self.EMPTY = ""
        self.NEW_LINE = "\r\n"
        self.SPACE = " "
        self.output = self.EMPTY

    def compute_output(self):
        for i in range(1, self.first_num + 1):
            if i % 2 == 0:
                for j in range(1, self.second_num + 1):
                    if j in (2, 3, 5, 7):
                        for k in range(1, self.third_num + 1):
                            if k % 2 == 0:
                                self.output += f"{i}{self.SPACE}{j}{self.SPACE}{k}{self.NEW_LINE}"
        return self.output


first_num = int(input())
second_num = int(input())
third_num = int(input())


processor = NumberProcessor(first_num, second_num, third_num)
output = processor.compute_output()
print(output)
