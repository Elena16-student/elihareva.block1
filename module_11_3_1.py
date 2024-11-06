import inspect
from pprint import pprint

obj = 65.2
def introspection_info(obj):
    result = {}
    result['type'] = type(obj).__name__
    result['attributes'] = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    result['methods'] = [method for method in dir(type(obj)) if callable(getattr(obj, method))]
    result['module'] = inspect.getmodule(introspection_info)
    return result

attributes = introspection_info(obj)
pprint(attributes)
pprint(inspect.ismethod(introspection_info))
pprint(inspect.isfunction(introspection_info))
pprint(inspect.isclass(obj))

class AnyClass:
    def __init__(self, value):
        self.value = value


any_instance = AnyClass(21)
class_info = introspection_info(any_instance)
print(class_info)
