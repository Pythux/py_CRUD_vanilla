
class DataBase:
    def __init__(self, dict_entity):
        self.dict_entity = dict_entity

    def __getattr__(self, name):
        def chose_service(obj, *args):
            entity_name = obj.__class__.__name__
            f = getattr(self.dict_entity[entity_name], name)
            return f(obj, *args)

        return chose_service
