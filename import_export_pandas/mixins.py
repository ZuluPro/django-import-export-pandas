from import_export import mixins
from import_export_pandas import formats


class ExportViewMixin(mixins.ExportViewMixin):
    formats = formats.DEFAULT_FORMATS
