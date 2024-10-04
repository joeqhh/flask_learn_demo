from flask import request
from flask_cors import CORS

from App import create_app
from App.common.ErrorCode import ErrorCode
from App.common.RequestUtils import RequestUtils
from App.common.ResultUtils import ResultUtils
from App.exception.BusinessException import BusinessException


app = create_app()

# CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})
CORS(app,expose_headers=["Authorization"])



# 全局异常处理器
@app.errorhandler(BusinessException)
def handle_business_exception(error):
    return ResultUtils.error(error)

#
# @app.before_request
# def before_request():
#     token = request.headers.get('Authorization')
#     path = request.path
#     if path != '/api/login':
#         if not token:
#             raise BusinessException(ErrorCode.PARAMS_ERROR,'Token is missing!')
#         else: RequestUtils.decode_token(token,app.config['SECRET_KEY'])


if __name__ == '__main__':
    app.run(debug=True)