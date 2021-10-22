from django.db.models import fields
import django_filters
from django_filters import DateFilter
from django_filters.filters import (
    CharFilter,
    ChoiceFilter,
    NumberFilter,
    NumericRangeFilter,
)
from .models import *


class BloggerFilter(django_filters.FilterSet):
    # platform = ChoiceFilter(choices="PLATFORM")
    # platform = CharFilter(field_name="platform")
    name = CharFilter(field_name="name", lookup_expr="icontains", label="TEST")
    # note = CharFilter(field_name="note", lookup_expr="icontains")

    class Meta:
        model = bloggers
        fields = ["name", "platform"]
        exclude = ["phone", "profile_link"]
