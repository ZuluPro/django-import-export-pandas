import factory
from factory import fuzzy


class InstanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'testapp.Instance'

    name = factory.Faker('name')


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'testapp.Entry'

    timestamp = factory.Faker('date_time')
    amount = fuzzy.FuzzyInteger(0, 1024)
    rate = fuzzy.FuzzyFloat(0, 1024)
    tag = factory.Faker('name')
    instance = factory.SubFactory(InstanceFactory)
