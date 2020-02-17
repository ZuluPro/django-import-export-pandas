from import_export_pandas import resources
from import_export_pandas.tests.testapp import models


class EntryResource(resources.DataframeResource):
    class Meta:
        model = models.Entry
        fields = export_order = (
            'timestamp',
            'amount',
            'rate',
            'tag',
            'instance'
        )
