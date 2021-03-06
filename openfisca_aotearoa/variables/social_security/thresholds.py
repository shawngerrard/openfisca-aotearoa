# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class accommodation_supplement__below_income_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Income is below threshold?"
    definition_period = MONTH


class accommodation_supplement__below_cash_threshold(Variable):
    value_type = bool
    default_value = True
    entity = Person
    label = u"Cash is below threshold?"
    definition_period = MONTH
