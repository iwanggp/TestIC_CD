#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：student-info-app 
@File    ：system.py
@IDE     ：PyCharm 
@Author  ：wang.gongpeng
@Date    ：2025/9/3 17:28
数据业务类
'''

import json
from typing import Dict
from .student import Student


class StudentSystem:
    """
    初始化
    """

    def __init__(self, storage_file: str = "students.json"):
        self.storage_file = storage_file
        self.students: Dict[int, Student] = {}
        self.load()

    def add_student(self, s: Student):
        if s.id in self.students:
            raise ValueError(f"Student ID {s.id} already exists")
        self.students[s.id] = s
        self.save()

    def get_student(self, sid: int):
        return self.students.get(sid)

    def list_students(self):
        return list(self.students.values())

    def save(self):
        data = [s.__dict__ for s in self.students.values()]
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                self.students[item["id"]] = Student(**item)
        except FileNotFoundError:
            pass
