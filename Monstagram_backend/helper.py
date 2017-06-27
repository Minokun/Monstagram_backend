from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# 测试用，直接返回json数据
# @param obj 对象
# @return json
# @author WuXiaokun
def apiTest(obj):
    return HttpResponse(JSONRenderer().render(obj))