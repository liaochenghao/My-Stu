# coding: utf-8
from enum import Enum, unique


@unique
class StudentOperationType(Enum):
    """学生操作类型 ，全部以1开头，如100、101、110"""
    # 创建订单
    ADD_ORDER = 100


@unique
class OrderOperationType(Enum):
    """订单操作类型 ，全部以2开头，如200、201、210"""
    # 创建订单
    ADD_ORDER = 200


@unique
class UserOperationType(Enum):
    """后台管理人员操作类型 ，全部以3开头，如300、301、310"""
    # 登录系统
    LOGIN = 300
    UPDATE_INFO = 301


# print(StudentOperationType.ADD_ORDER.value)
