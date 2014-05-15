
class Model:
    _meta = None
    objects = None

    id = None
    pk = None

    MultipleObjectsReturned = None
    DoesNotExist = None


class Manager:
    def iterator(self):
        pass

    def aggregate(self, *args, **kwargs):
        pass

    def count(self):
        pass

    def get(self, *args, **kwargs):
        pass

    def create(self, **kwargs):
        pass

    def bulk_create(self, objs, batch_size=None):
        pass

    def get_or_create(self, defaults=None, **kwargs):
        pass

    def update_or_create(self, defaults=None, **kwargs):
        pass

    def earliest(self, field_name=None):
        pass

    def latest(self, field_name=None):
        pass

    def first(self):
        pass

    def last(self):
        pass

    def in_bulk(self, id_list):
        pass

    def delete(self):
        pass

    def update(self, **kwargs):
        pass

    def exists(self):
        pass

    def raw(self, raw_query, params=None, translations=None, using=None):
        pass

    def values(self, *fields):
        pass

    def values_list(self, *fields, **kwargs):
        pass

    def dates(self, field_name, kind, order='ASC'):
        pass

    def datetimes(self, field_name, kind, order='ASC', tzinfo=None):
        pass

    def none(self):
        pass

    def all(self):
        pass

    def filter(self, *args, **kwargs):
        pass

    def exclude(self, *args, **kwargs):
        pass

    def complex_filter(self, filter_obj):
        pass

    def select_for_update(self, nowait=False):
        pass

    def select_related(self, *fields):
        pass

    def prefetch_related(self, *lookups):
        pass

    def annotate(self, *args, **kwargs):
        pass

    def order_by(self, *field_names):
        pass

    def distinct(self, *field_names):
        pass

    def extra(self, select=None, where=None, params=None, tables=None, order_by=None, select_params=None):
        pass

    def reverse(self):
        pass

    def defer(self, *fields):
        pass

    def only(self, *fields):
        pass
