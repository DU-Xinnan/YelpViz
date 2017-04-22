from server.models.Cleveland import Cleveland
from server.models.LasVegas import LasVegas
from server.models.Madison import Madison

def get_class_instance(dataname):
    last_module_name = dataname
    class_name = dataname
    module = __import__('server', fromlist=['models', str(dataname)]).models
    last_module = getattr(module, last_module_name)
    _class = getattr(last_module, class_name)
    return _class()