from .apis.UserApi import *
from .apis.DepartmentApi import *
from .exts import api

#用户
api.add_resource(AddUser,'/api/user/add')
api.add_resource(UpdateUser,'/api/user/update')
api.add_resource(GetUser,'/api/user/get')
api.add_resource(GetUserList,'/api/user/get/list')
api.add_resource(DeleteUser,'/api/user/delete')

#部门
api.add_resource(AddDepartment,'/api/department/add')
api.add_resource(UpdateDepartment,'/api/department/update')
api.add_resource(GetDepartment,'/api/department/get')
api.add_resource(GetDepartmentList,'/api/department/get/list')
api.add_resource(DeleteDepartment,'/api/department/delete')
