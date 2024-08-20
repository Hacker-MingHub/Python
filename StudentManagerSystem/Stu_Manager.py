import json

import Student


class StudentManager(object):

    def __init__(self):
        self.students = []
        self.stu_num = 0

    def __str__(self):
        return f'There are {self.stu_num} students. They are {", ".join(self.students)}'

    def load_student(self, file_name):
        """加载学员信息"""
        # 读取 JSON 文件
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                stu_data = json.load(f)
        except FileNotFoundError:
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)
        else:
            for stu in stu_data:
                tmp_stu = Student.Student(stu['name'], stu['gender'], stu['tel'])
                self.students.append(tmp_stu)
                self.stu_num += 1

    def save_student(self, file_name):

        # 1. 打开文件
        with open(file_name, 'w', encoding='utf-8') as f:
            # 2. 写入学员数据
            tmp_list = [stu.__dict__ for stu in self.students]
            json.dump(tmp_list, f, ensure_ascii=False, indent=2)

    def add_student(self):
        """添加新学生"""
        # 1.获取添加学生信息
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')

        # 2.创建学员对象
        tmp_stu = Student.Student(name, gender, tel)

        # 3.判断是否已有该学员
        for stu in self.students:
            if tmp_stu.name == stu.name:
                print('该学员已存在')
                break
        else:
            # 4.该学员不存在，添加学员
            self.students.append(tmp_stu)
            self.stu_num += 1
            print('成功添加该学员信息')

    def remove_student(self):
        """删除指定学员"""
        # 1. 用户输入目标学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 2. 如果用户输入的目标学员存在则删除，否则提示学员不存在
        for stu in self.students:
            if stu.name == del_name:
                self.students.remove(stu)
                self.stu_num -= 1
                print('成功删除该学员信息')
                break
        else:
            print('查无此人')

    def modify_student(self):
        """修改学员信息"""
        # 1. 用户输入目标学员姓名
        modify_name = input('请输入要修改的学员的姓名：')

        # 2. 如果用户输入的目标学员存在则修改，否则提示学员不存在
        for stu in self.students:
            if stu.name == modify_name:
                if input('是否修改姓名?[Y/N]') in ['Y', 'y']:
                    stu.name = input('请输入新的姓名：')
                if input('是否修改性别?[Y/N]') in ['Y', 'y']:
                    stu.gender = input('请输入新的性别：')
                if input('是否修改手机号?[Y/N]') in ['Y', 'y']:
                    stu.tel = input('请输入新的手机号：')
                print('成功修改该学员信息')
                break
        else:
            print('查无此人')

    def search_student(self):
        """查询学员信息"""
        if input('是否查询所有学员信息：[Y/N]') in ['Y', 'y']:
            # 1. 查询所有学员信息
            # 1.1 设置列宽
            name_width = 10
            gender_width = 5
            tel_width = 15

            # 1.2 打印表头
            print(f"{'姓名':<{name_width}} {'性别':<{gender_width}} {'手机号':<{tel_width}}")
            print("-" * (name_width + gender_width + tel_width))

            # 1.3 打印学员信息
            for stu in self.students:
                print(f"{stu.name:<{name_width}} {stu.gender:<{gender_width}} {stu.tel:<{tel_width}}")
        else:
            # 2. 查询指定学员信息
            # 2.1 用户输入目标学员姓名
            search_name = input('请输入要查询学员的姓名：')

            # 2.2 如果用户输入的目标学员存在，则打印学员信息，否则提示学员不存在
            for stu in self.students:
                if stu.name == search_name:
                    print(f'姓名:{stu.name},性别:{stu.gender}, 手机号:{stu.tel}')
                    break
            else:
                print('查无此人')

    @staticmethod
    def show_menu():
        print()
        print('有如下功能：-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('0:退出系统')

    def run(self):
        """程序入口，执行程序提供的函数"""
        # 保存文件路径
        file_path = 'Student_data.json'

        #  加载学员信息
        self.load_student(file_path)

        while True:
            # 1. 显示功能菜单
            self.show_menu()

            # 2. 用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号：'))

            # 3 根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.remove_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 0:
                # 退出系统
                self.save_student(file_path)
                break
            else:
                print('输入功能不存在，请重新输入')
