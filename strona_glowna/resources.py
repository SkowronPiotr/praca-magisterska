from import_export import resources
from .models import Gatunek


class GatunekResource(resources.ModelResource):
    class Meta:
        model = Gatunek
