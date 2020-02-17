from django.db import models
import pandas as pd
from import_export import resources


class DataframeField(resources.Field):
    def get_value(self, obj):
        try:
            value = obj[self.attribute]
        except KeyError:
            try:
                value = super().get_value(obj['object'])
            except KeyError:
                value = None
        return value


class DataframeResource(resources.ModelResource):
    DEFAULT_RESOURCE_FIELD = DataframeField

    def export_resource(self, obj):
        data = super().export_resource(obj)
        return pd.Series(data=data)

    def export(self, queryset=None, df=None, *args, **kwargs):
        headers = self.get_export_headers()

        if df is None:
            if queryset is None:
                queryset = self.get_queryset()

            for fieldname, field in self.fields.items():
                field.attribute = field.attribute or fieldname
                if '__' in field.attribute and not field.attribute.startswith('__'):
                    # XXX: Pandas does not do multi-depth lookup
                    # So we annotate
                    queryset = queryset.annotate(**{field.attribute: models.F(field.attribute)})
                    # self.fields[fieldname].attribute = fieldname

            df = queryset.to_dataframe()
            df['object'] = queryset

        self.before_export(queryset, df, *args, **kwargs)
        df = pd.DataFrame(df.apply(self.export_resource, axis=1))
        df.columns = headers
        self.after_export(queryset, df, *args, **kwargs)
        return df
