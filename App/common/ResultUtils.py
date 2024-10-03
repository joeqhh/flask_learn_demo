import dataclasses
from dataclasses import dataclass
from datetime import datetime


# from App.models.User import User
# @dataclasses.dataclass
# class Num:
#     num_list : list = dataclasses.field(default_factory=list)
#     num:int = dataclasses.field(default_factory=int)
#     age :int =  dataclasses.field(default_factory=int)
#     user :User =  dataclasses.field(default_factory=User)
#
#     def __init__(self, num_list, age, num, user):
#         self.num_list = num_list
#         self.age = age
#         self.num = num
#         self.user = user


class ResultUtils:

    @staticmethod
    def success(data, message='success'):
        return {
            'message': message,
            'data': ResultUtils.return_data(data),
            'code': 0
        }

    @staticmethod
    def error(error_code):
        return {
            'message': error_code.message,
            'data': None,
            'code': error_code.code
        }

    @staticmethod
    def return_data(data):
        res = None
        if data is not None:
            if type(data) == list:
                res = []
                for i in data:
                    dict_i = dataclasses.asdict(i)
                    if  dict_i.__contains__('time')and isinstance(dict_i['time'], datetime):
                        dict_i['time'] = dict_i['time'].strftime('%Y-%m-%d %H:%M:%S')
                    res.append(dict_i)
            else:
                dict_data = dataclasses.asdict(data)
                if dict_data.__contains__('time') and isinstance(dict_data['time'], datetime):
                    dict_data['time'] = dict_data['time'].strftime('%Y-%m-%d %H:%M:%S')
                res = dict_data
        return res

    # @staticmethod
    # def serialize_datetime(data):
    #     if isinstance(data, dict):
    #         return {key: ResultUtils.serialize_datetime(value) for key, value in data.items()}
    #     elif isinstance(data, list):
    #         return [ResultUtils.serialize_datetime(item) for item in data]
    #     elif isinstance(data, datetime):
    #         return data.strftime('%Y-%m-%d %H:%M:%S')  # 转换为字符串
    #     return data