# from flask import session
# from flask_restful import Resource
# from App.common.ErrorCode import ErrorCode
# from App.common.RequestUtils import RequestUtils
# from App.common.UserConstant import UserConstant
# from App.exception.BusinessException import BusinessException
# from App.exts import db
# from App.common.ResultUtils import *
# from App.models.Account import Account
# from App.models.Userold import User
# from flask import  request, make_response
# from App.common.RoleRequired import role_required
#
# def is_not_valid(args):
#     if args.__len__() == 0 or not args.__contains__('id') or int(args.get('id')) <= 0: return True
#     return False
#
# class AddAccount(Resource):
#     def post(self):
#         json = request.json
#         if json is None or len(json) == 0 or RequestUtils.is_blank(json,'password') or RequestUtils.is_blank(json,'username') or RequestUtils.is_blank(json,'name')  or RequestUtils.is_blank(json,'role') or RequestUtils.is_blank(json,'identification'):
#             raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
#         username = request.json.get('username')
#         if Account.query.filter_by(username=username).count() > 0: raise BusinessException(ErrorCode.PARAMS_ERROR,'该账号已存在!')
#         password = request.json.get('password')
#         name = request.json.get('name')
#         role = request.json.get('role')
#         identification = request.json.get('identification')
#         department = None
#         avatar = None
#         score = None
#         captainId = None
#         if request.json.__contains__('department'): department = request.json.get('department')
#         if request.json.__contains__('avatar'): avatar = request.json.get('avatar')
#         if request.json.__contains__('captainId'): captainId = request.json.get('captainId')
#         if request.json.__contains__('score'): score = request.json.get('score')
#         user = User(name=name,role=role,identification=identification,department=department,captainId=captainId,score=score,avatar=avatar)
#         try:
#             db.session.add(user)
#             db.session.flush()
#         except Exception as e:
#             db.session.rollback()
#             db.session.flush()
#         user_id = user.id
#         account = Account(username=username,password=password,userId=user_id)
#         try:
#             print(account)
#             db.session.add(account)
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             db.session.flush()
#         return ResultUtils.success(account, 'ok')
#
#
# class UpdateAccount(Resource):
#     def post(self):
#         json = request.json
#         if len(json) == 0 or not json.__contains__('id') or int(json.get('id')) <= 0 or not json.__contains__(
#                 'password') or len(json.get('password').strip()) == 0 or not json.__contains__('newPassword') or len(json.get('newPassword').strip()) == 0:
#             raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
#         id = request.json.get('id')
#         account = Account.query.get(id)
#         if account is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
#         password = request.json.get('password')
#         if account.password != password: raise BusinessException(ErrorCode.PARAMS_ERROR, '密码错误错误')
#         newPassword = request.json.get('newPassword')
#         account.password = newPassword
#         db.session.commit()
#         return ResultUtils.success(account)
#
# class GetAccount(Resource):
#     def get(self):
#         args = request.args
#         if is_not_valid(args): raise BusinessException(ErrorCode.PARAMS_ERROR)
#         id = args.get('id')
#         account = Account.query.get(id)
#         if account is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
#
#
#         return ResultUtils.success(account)
#
# class GetAccountList(Resource):
#     @role_required(UserConstant.ADMIN_ROLE.value,UserConstant.CAPTAIN_ROLE.value)
#     def get(self):
#         account_list = Account.query.all()
#         return ResultUtils.success(account_list)
#
# class DeleteAccount(Resource):
#     @role_required(UserConstant.ADMIN_ROLE.value)
#     def get(self):
#         args = request.args
#         if is_not_valid(args): raise BusinessException(ErrorCode.PARAMS_ERROR)
#         id = args.get('id')
#         account = Account.query.get(id)
#         if account is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR)
#
#         try:
#             db.session.delete(account)
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             db.session.flush()
#         return ResultUtils.success(None,'删除成功')
#
#
# # def login():
# #     username = request.json['username']
# #      # 用户登录成功，生成 Token
# #     token = generate_token(username)
# #     # 创建响应对象，添加 token 到响应头中
# #     response = make_response(jsonify({'message': 'Login successful'}))
# #     response.headers['Authorization'] = f'Bearer {token}'
# #     # 也可以选择将 token 返回在 JSON 响应中
# #     # return jsonify({'message': 'Login successful', 'token': token})
# #     return response
#
# class Login(Resource):
#     #todo 设置token
#     def post(self):
#         json = request.json
#         print(request.json)
#         if json is None or len(json) == 0 or RequestUtils.is_blank(json,'password') or RequestUtils.is_blank(json,'username') :
#             raise BusinessException(ErrorCode.PARAMS_ERROR, '参数错误')
#         username = json.get('username')
#         password = json.get('password')
#         account = Account.query.filter_by(username=username).first()
#         if account is None: raise BusinessException(ErrorCode.NOT_FOUND_ERROR,'无该账号')
#         if account.password != password: raise BusinessException(ErrorCode.PARAMS_ERROR,'密码错误')
#         user_id = account.userId
#         user = User.query.get(user_id)
#         role = user.role
#         token = RequestUtils.generate_token(username,role)
#         account.password = ''
#         response = make_response(ResultUtils.success(account,'登陆成功'))
#         response.headers['Authorization'] = f'Bearer {token}'
#         session[UserConstant.USER_LOGIN_STATE.value] = user
#         return response