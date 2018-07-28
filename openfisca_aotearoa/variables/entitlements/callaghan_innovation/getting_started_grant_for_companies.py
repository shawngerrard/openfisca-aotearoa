# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Company


class getting_started_first_time_in_business(Variable):
        value_type = bool
        entity = Company
        definition_period = YEAR
        label = u'Is a company classified as eligible to the getting started grant'
        reference = "Needs updating"


class getting_started_years_in_business(Variable):
        value_type = int
        entity = Company
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a company has been in business'
        reference = "Needs updating"
	

class getting_started_eligible_for_grant(Variable):
	value_type = bool
	entity = Company
	definition_period = YEAR
	label = u'Determines if the company is eligible for a getting started grant'
	reference = "Needs updating"

	def formula(companies, period):
		return companies("getting_started_first_time_in_business", period)       


class getting_started_entitlement_for_company(Variable):
	value_type = float
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the getting started grant'
	reference = "Needs updating"

	def formula(company, period, parameters):
		eligible_company = persons.company("getting_started_eligible_for_grant", period)
		return eligible_company