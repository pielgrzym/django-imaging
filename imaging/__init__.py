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

    def register(self, model):
        self.registry[model.__name__.lower()] = model

    def has_model(self, model):
        if model in self.registry.keys():
            return True
        else:
            return False

galleries = GalleryRegistry()
