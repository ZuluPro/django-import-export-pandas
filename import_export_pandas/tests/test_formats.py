import io
import json

from django.test import TestCase

from import_export_pandas import formats
from import_export_pandas.tests import factories
from import_export_pandas.tests.testapp import models


class FormatTestMixin:
    """
    Mixin to easily create Format TestCases.
    """
    def setUp(self):
        self.number = 10
        factories.EntryFactory.create_batch(self.number)
        self.qs = models.Entry.objects.all()
        self.df = self.qs.to_dataframe()
        self.format = self.format_class()

    def _test_output(self, output):
        pass

    def test_export_data(self):
        output = self.format.export_data(self.df)
        self._test_output(output)

    def _test_stream_output(self, output):
        pass

    def test_export_stream_data(self):
        output = self.format.export_stream_data(self.df)
        self._test_stream_output(output)


class CSVFormatTest(FormatTestMixin, TestCase):
    format_class = formats.CSV

    def _test_output(self, output):
        self.assertIsInstance(output, str)
        lines = output.splitlines()
        line_count = len(lines)
        self.assertEqual(line_count, self.number+1)

    def _test_stream_output(self, output):
        self.assertIsInstance(output, io.StringIO)
        self._test_output(output.read())


class JSONFormatTest(FormatTestMixin, TestCase):
    format_class = formats.JSON

    def _test_output(self, output):
        self.assertIsInstance(output, str)
        json.loads(output)

    def _test_stream_output(self, output):
        self.assertIsInstance(output, io.StringIO)
        self._test_output(output.read())


class HTMLFormatTest(FormatTestMixin, TestCase):
    format_class = formats.HTML

    def _test_output(self, output):
        self.assertIsInstance(output, str)

    def _test_stream_output(self, output):
        self.assertIsInstance(output, io.StringIO)
        self._test_output(output.read())


class XLSXFormatTest(FormatTestMixin, TestCase):
    format_class = formats.XLSX

    def _test_output(self, output):
        self.assertIsInstance(output, bytes)

    def _test_stream_output(self, output):
        self.assertIsInstance(output, io.BytesIO)
        self._test_output(output.read())
