from enum import Enum
class ErrorCode(Enum):

    SUCCESS = 1
    PARAMS_ERROR = 2
    NOT_LOGIN_ERROR = 3
    NO_AUTH_ERROR = 4
    NOT_FOUND_ERROR = 5
    FORBIDDEN_ERROR = 6
    SYSTEM_ERROR = 7
    OPERATION_ERROR = 8


ErrorCode.SUCCESS.code = 0
ErrorCode.SUCCESS.message = "ok"
ErrorCode.PARAMS_ERROR.code = 40000
ErrorCode.PARAMS_ERROR.message = "请求参数错误"
ErrorCode.NOT_LOGIN_ERROR.code = 40100
ErrorCode.NOT_LOGIN_ERROR.message = "未登录"
ErrorCode.NO_AUTH_ERROR.code = 40101
ErrorCode.NO_AUTH_ERROR.message = "无权限"
ErrorCode.NOT_FOUND_ERROR.code = 40400
ErrorCode.NOT_FOUND_ERROR.message = "请求数据不存在"
ErrorCode.FORBIDDEN_ERROR.code = 40300
ErrorCode.FORBIDDEN_ERROR.message = "禁止访问"
ErrorCode.SYSTEM_ERROR.code = 50000
ErrorCode.SYSTEM_ERROR.message = "系统内部异常"
ErrorCode.OPERATION_ERROR.code = 50001
ErrorCode.OPERATION_ERROR.message = "操作失败"