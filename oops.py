class MARKSHEET:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {}

    def add_mark(self):
        for i in range(4):
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            self.__marks[subject] = marks

    def show(self):
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:")

        total = 0
        for sub, m in self.__marks.items():
            print(sub, ":", m)
            total += m

        print("Total:", total)
        print("Average:", total / len(self.__marks))


# main
name = input("Enter name: ")
roll_no = int(input("Enter roll: "))

result = MARKSHEET(name, roll_no)

result.add_mark()   # ✅ correct
result.show()