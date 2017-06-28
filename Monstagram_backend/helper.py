from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# 测试用，直接返回json数据
# @param obj 对象
# @return json
# @author WuXiaokun
def apiTest(obj):
    return HttpResponse(JSONRenderer().render(obj))

# 用于md5加密
# @param str 字符串
# @return str 字符串
# @author WuXiaokun
def md5(src):
    import hashlib
    hash = hashlib.md5()
    hash.update(src.encode('utf-8'))
    return hash.hexdigest()