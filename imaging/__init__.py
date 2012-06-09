"""

Django Imaging

Author: Jakub Nawalaniec <pielgrzym@prymityw.pl>
Version: 1.0.0

"""
VERSION = "1.0.0"

class SingletonError(Exception):
    pass

class GalleryRegistry(object):
    __obj_count = 0

    def __init__(self):
        self.__obj_count += 1
        if self.__obj_count > 1:
            raise SingletonError("Well, there can be only ONE. One singleton-highlander!")
        self.registry = {}
        self.relations_registry = {}
        self.from_model_registry = {}

    def register(self, model):
        self.registry[model.__name__.lower()] = model

    def register_relation(self, model):
        from django.db import models
        fks = filter(lambda x: isinstance(x, models.ForeignKey), model._meta.fields)
        from_field = None
        intermediate = model
        to_field = None
        for f in fks:
            import ipdb
            ipdb.set_trace()
            m = f.rel.to
            if isinstance(m, str):
                m = self.get_from_model(m)
            if len(m._meta.many_to_many):
                from_field = m
            else:
                to_field = m
        self.relations_registry[from_field] = [intermediate, to_field]

    def has_model(self, model):
        if model in self.registry.keys():
            return True
        else:
            return False

galleries = GalleryRegistry()
