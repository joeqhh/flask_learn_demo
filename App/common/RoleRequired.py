from App.common.ErrorCode import ErrorCode
from App.common.RequestUtils import RequestUtils
from App.exception.BusinessException import BusinessException



def role_required(*allowed_roles):
    def decorator(f):
        def wrapped(*args, **kwargs):
            current_user = RequestUtils.get_login_user()
            if current_user.role in allowed_roles:
                return f(*args, **kwargs)
            raise BusinessException(ErrorCode.NO_AUTH_ERROR)
        return wrapped
    return decorator