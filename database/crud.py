from database import CRUDHelper


class CRUD(CRUDHelper):
    def create(self, obj):
        obj.key = self._create(*self.get_params_and_values(obj))

    def read(self, obj):
        u_names, u_values = self.get_unique(obj)
        selected = self._read(obj.key, u_names, u_values)
        if selected:
            self.set_obj(obj, selected)
            return True
        return False

    def update(self, obj):
        self._update(
            obj.key, *self.get_params_and_values(obj))

    def delete(self, obj):
        self._delete(obj)

    def update_or_create(self, obj):
        if not obj.key:
            self.read(obj)
        if obj.key:
            self.update(obj)
        else:
            self.create(obj)
