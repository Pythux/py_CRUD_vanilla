
from abc import ABCMeta, abstractmethod
from CRUD_vanilla import CRUD


class InterfaceCRUD(CRUD, metaclass=ABCMeta):
    @property
    @abstractmethod
    def table():
        raise NotImplementedError

    @property
    @abstractmethod
    def key_name():
        raise NotImplementedError

    @abstractmethod
    def get_params_and_values(obj):
        raise NotImplementedError
