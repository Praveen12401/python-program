# here __call__ method explain
from typing import Any


class add(object):
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def __call__(self,a,b, *args: Any, **kwds: Any) -> Any:
        return a+b
    
a1=add(10,20)
print(callable(a1))
print(a1(2,2))


