#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student-info-app 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：wang.gongpeng
@Date    ：2025/9/3 17:28 
'''
# from student_info.student import Student
# from student_info.system import StudentSystem


from .student import Student
from .system import StudentSystem


def main():
    sys = StudentSystem()
    while True:
        print("\n=== 学生信息录入系统 ===")
        print("1. 添加学生\n2. 查询学生\n3. 列出所有学生\n4. 退出")
        choice = input("请输入选项: ").strip()

        if choice == "1":
            try:
                sid = int(input("学号: ").strip())
                name = input("姓名: ").strip()
                age = int(input("年龄: ").strip())
                courses = [c.strip() for c in input("课程(逗号分隔): ").split(",") if c.strip()]
                sys.add_student(Student(id=sid, name=name, age=age, courses=courses))
                print("✅ 添加成功")
            except ValueError as e:
                print("❌", e)

        elif choice == "2":
            sid = int(input("学号: ").strip())
            s = sys.get_student(sid)
            print(f"学号:{s.id} 姓名:{s.name} 年龄:{s.age} 课程:{s.courses}" if s else "❌ 未找到")

        elif choice == "3":
            for s in sys.list_students():
                print(f"学号:{s.id} 姓名:{s.name} 年龄:{s.age} 课程:{s.courses}")

        elif choice == "4":
            print("👋 已保存到 students.json，退出。")
            break
        else:
            print("❌ 无效选项")


if __name__ == "__main__":
    main()
