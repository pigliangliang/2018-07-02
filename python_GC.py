#author_by zhuxiaoliang
#2018-07-02 下午6:47
"""
py 垃圾回收机制

"""
#引用技术为主，标记——清除和分代收集为辅

import  gc
import sys
#gc.set_debug(gc.DEBUG_STATS|gc.DEBUG_LEAK)
a = ["hi pig"]
b = []
a.append(b)
print('a refcount:{}'.format(sys.getrefcount(a)))
print('b：',sys.getrefcount(b))

"""
a refcount:2
b： 3
"""

a = "hi pig"
b = []
#a.append(b)
print('a refcount:{}'.format(sys.getrefcount(a)))
print(gc.collect())
print(gc.garbage)
print('b----',sys.getrefcount(b))





a = 1
b = 1
print(a is b)
#输出 True
a = 'zhu'
b = 'zhu'
print(a is b)
#输入 True