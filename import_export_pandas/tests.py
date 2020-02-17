from django.test import TestCase
from import_export_pandas import formats


class FormatTestMixin:
    def test_export_data(self):
        format_ = self.format_class()
        format_.export_data(df)


class CSVFormatTest(FormatTestMixin, TestCase):
    format_class = formats.CSV


class JSONFormatTest(FormatTestMixin, TestCase):
    format_class = formats.JSON


class HTMLFormatTest(FormatTestMixin, TestCase):
    format_class = formats.HTML


class XLSXFormatTest(FormatTestMixin, TestCase):
    format_class = formats.XLSX
