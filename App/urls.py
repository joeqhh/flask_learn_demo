from App.apis.AccountApi import *
from .apis.AttendanceApi import *
from .apis.UserApi import *
from .exts import api

#账号
api.add_resource(AddAccount,'/api/account/add')
api.add_resource(UpdateAccount,'/api/account/update')
api.add_resource(GetAccount,'/api/account/get')
api.add_resource(GetAccountList,'/api/account/get/list')
api.add_resource(DeleteAccount,'/api/account/delete')
api.add_resource(Login,'/api/login')

#用户
api.add_resource(AddUser,'/api/user/add')
api.add_resource(UpdateUser,'/api/user/update')
api.add_resource(GetUser,'/api/user/get')
api.add_resource(GetUserList,'/api/user/get/list')
api.add_resource(DeleteUser,'/api/user/delete')

#签到
api.add_resource(AddAttendance,'/api/attendance/add')
api.add_resource(GetAttendance,'/api/attendance/get')
api.add_resource(GetAttendanceList,'/api/attendance/get/list')
api.add_resource(DeleteAttendance,'/api/attendance/get/delete')