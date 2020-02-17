import io
from import_export.formats import base_formats


class PandasFormat(base_formats.Format):
    PANDAS_METHOD = None
    CONTENT_TYPE = 'application/octet-stream'
    EXTENSION = ''
    STREAM_TYPE = io.BytesIO

    def get_extension(self):
        return self.EXTENSION

    def get_export_kwargs(self):
        return {'index': False}

    def export_data(self, dataset, **kwargs):
        return self.export_stream_data(dataset, **kwargs).read()

    def export_stream_data(self, dataset, **kwargs):
        stream = self.STREAM_TYPE()
        try:
            func = getattr(dataset, 'to_%s' % self.PANDAS_METHOD)
        except AttributeError:
            raise NotImplementedError("Export in %s not implemented" % self.PANDAS_METHOD)
        export_kwargs = self.get_export_kwargs()
        func(stream, **export_kwargs)
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
    STREAM_TYPE = io.StringIO


class JSON(PandasFormat):
    PANDAS_METHOD = 'json'
    CONTENT_TYPE = 'application/json'
    EXTENSION = 'json'
    STREAM_TYPE = io.StringIO

    def get_export_kwargs(self):
        return {}


class HTML(PandasFormat):
    PANDAS_METHOD = 'html'
    CONTENT_TYPE = 'text/html'
    EXTENSION = 'html'
    STREAM_TYPE = io.StringIO


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
