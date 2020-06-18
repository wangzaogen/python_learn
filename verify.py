from io import BytesIO
from bottle import get, response
val = [2,4,8,9]
# print("列表的的三倍，{0}".format(222))
print([3*x for x in val])
print([x for x in val if x % 2==0])
# print([x if x % 2==0 for x in val])