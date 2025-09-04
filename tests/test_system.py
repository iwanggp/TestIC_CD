#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student-info-app 
@File    ：test_system.py
@IDE     ：PyCharm 
@Author  ：wang.gongpeng
@Date    ：2025/9/3 17:29 
'''
import pytest
from student_info.student import Student
from student_info.system import StudentSystem

def test_add_and_get(tmp_path):
    sys = StudentSystem(storage_file=tmp_path / "students.json")
    sys.add_student(Student(id=1, name="Alice", age=18, courses=["Math"]))
    s = sys.get_student(1)
    assert s and s.name == "Alice" and "Math" in s.courses

def test_duplicate_id(tmp_path):
    sys = StudentSystem(storage_file=tmp_path / "students.json")
    sys.add_student(Student(id=1, name="Bob", age=20))
    with pytest.raises(ValueError):
        sys.add_student(Student(id=1, name="Bob2", age=21))
