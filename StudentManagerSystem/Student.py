class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"Student: {self.name}, {self.gender}, {self.tel}"


if __name__ == '__main__':
    s1=Student('zhangshan','male','10086')
    print(s1)