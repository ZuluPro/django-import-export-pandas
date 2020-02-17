import io
from import_export.formats import base_formats


class PandasFormat(base_formats.Format):
    PANDAS_METHOD = None
    CONTENT_TYPE = 'application/octet-stream'
    EXTENSION = ''

    def get_extension(self):
        return self.EXTENSION

    def export_data(self, dataset, **kwargs):
        return self.export_stream_data(dataset, **kwargs).read()

    def export_stream_data(self, dataset, **kwargs):
        stream = io.BytesIO()
        try:
            func = getattr(dataset, 'to_%s' % self.PANDAS_METHOD)
        except AttributeError:
            raise NotImplementedError("Export in %s not implemented" % self.PANDAS_METHOD)
        func(stream, index=False)
        stream.seek(0)
        return stream

    @classmethod
    def is_available(cls):
        return True

    def can_export(self):
        return True

    def can_export_stream(self):
        return True


class CSV(PandasFormat):
    PANDAS_METHOD = 'csv'
    CONTENT_TYPE = 'text/csv'
    EXTENSION = 'csv'


class JSON(PandasFormat):
    PANDAS_METHOD = 'json'
    CONTENT_TYPE = 'application/json'
    EXTENSION = 'json'


class HTML(PandasFormat):
    PANDAS_METHOD = 'html'
    CONTENT_TYPE = 'text/html'
    EXTENSION = 'html'


class XLSX(PandasFormat):
    PANDAS_METHOD = 'excel'
    CONTENT_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    EXTENSION = 'xlsx'


DEFAULT_FORMATS = [fmt for fmt in (
    CSV,
    XLSX,
    JSON,
    HTML,
) if fmt.is_available()]
