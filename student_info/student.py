#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
用于保存学生信息的学生类
@Project ：student-info-app 
@File    ：student.py
@IDE     ：PyCharm 
@Author  ：wang.gongpeng
@Date    ：2025/9/3 17:27 
'''
from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    id: int
    name: str
    age: int
    courses: List[str] = field(default_factory=list)

