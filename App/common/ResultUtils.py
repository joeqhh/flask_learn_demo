import dataclasses
from dataclasses import dataclass
from datetime import datetime, date


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
                    if 'is_delete' in dict_i.keys(): del dict_i['is_delete']
                    for key in dict_i.keys():
                        if isinstance(dict_i[key], datetime):
                            dict_i[key] = dict_i[key].strftime('%Y-%m-%d %H:%M:%S')
                        if isinstance(dict_i[key], date):
                            dict_i[key] = dict_i[key].strftime('%Y-%m-%d')
                        if isinstance(dict_i[key], bytes):
                            dict_i[key] =  int.from_bytes(dict_i[key], byteorder='big')
                    res.append(dict_i)
            else:
                dict_data = dataclasses.asdict(data)
                if 'is_delete' in dict_data.keys(): del dict_data['is_delete']
                for key in dict_data.keys():
                    if isinstance(dict_data[key], datetime):
                        dict_data[key] = dict_data[key].strftime('%Y-%m-%d %H:%M:%S')
                    if isinstance(dict_data[key], date):
                        dict_data[key] = dict_data[key].strftime('%Y-%m-%d')
                    if isinstance(dict_data[key], bytes):
                        dict_data[key] = int.from_bytes(dict_data[key], byteorder='big')
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