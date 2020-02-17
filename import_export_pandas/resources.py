import pandas as pd
from import_export import resources


class DataframeResource(resources.ModelResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # XXX: Pandas does not do multi-depth lookup
        for field in self.fields:
            self.fields[field].attribute = field

    def export_resource(self, obj):
        data = super().export_resource(obj)
        return pd.Series(data=data)

    def export(self, queryset=None, df=None, *args, **kwargs):
        headers = self.get_export_headers()

        if df is None:
            if queryset is None:
                queryset = self.get_queryset()
            df = queryset.to_dataframe()

        self.before_export(queryset, df, *args, **kwargs)
        df = pd.DataFrame(df.apply(self.export_resource, axis=1))
        df.columns = headers
        self.after_export(queryset, df, *args, **kwargs)
        return df
