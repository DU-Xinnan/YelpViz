from server.models.NBA import NBA


def get_class_instance(dataname):
    last_module_name = dataname
    class_name = dataname
    module = __import__('server', fromlist=['models', str(dataname)]).models
    last_module = getattr(module, last_module_name)
    _class = getattr(last_module, class_name)
    return _class()
