from django.test import TestCase
from django.db import models as dj_models
from import_export_pandas.tests import factories
from import_export_pandas.tests.testapp import resources
from import_export_pandas.tests.testapp import models


class DataframeResourceExportTest(TestCase):
    def setUp(self):
        self.number = 10
        factories.EntryFactory.create_batch(self.number)
        self.qs = models.Entry.objects.all()
        self.resource = resources.EntryResource()

    def test_export_from_queryset(self):
        output = self.resource.export(self.qs)
        self.assertEqual(output.shape, (self.number, len(self.resource.fields)))

    def test_export_from_df(self):
        df = self.qs.to_dataframe()
        output = self.resource.export(df=df)
        self.assertEqual(output.shape, (self.number, len(self.resource.fields)))

    def test_foreign_key_attribute(self):
        output = self.resource.export(self.qs)
        self.assertTrue(output['instance_name'].all())

    def test_attribute(self):
        output = self.resource.export(self.qs)
        self.assertTrue(output['amount_x2'].all())

    def test_method(self):
        output = self.resource.export(self.qs)
        self.assertTrue(output['amount_x3'].all())

    def test_foreign_key_attribute_without_field(self):
        output = self.resource.export(self.qs)
        self.assertTrue(output['instance__id'].all())

    def test_dehydrate(self):
        output = self.resource.export(self.qs)
        self.assertTrue(output['amount_x4'].all())

    def test_custom_annotate(self):
        qs = self.qs.annotate(foo=dj_models.Value(42, output_field=dj_models.IntegerField()))
        output = self.resource.export(qs)
        self.assertTrue(output['foo'].all())

    def test_custom_annotate_absent(self):
        output = self.resource.export(self.qs)
        self.assertFalse(output['foo'].any())
