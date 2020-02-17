from import_export.fields import Field
from import_export_pandas import resources
from import_export_pandas.tests.testapp import models


class EntryResource(resources.DataframeResource):
    amount_x2 = resources.DataframeField(
        attribute="amount_x2",
    )
    amount_x4 = resources.DataframeField(
        attribute="amount_x2",
    )
    instance_name = resources.DataframeField(
        attribute="instance__name",
    )
    foo = resources.DataframeField(
        attribute="foo",
    )

    class Meta:
        model = models.Entry
        fields = export_order = (
            'amount_x2',
            'timestamp',
            'amount',
            'rate',
            'tag',
            'instance_name',
            'instance__id',
        )

    def dehydrate_amount_x4(self, obj):
        if 'object' in obj:
            return obj['object'].amount_x2 * 2
