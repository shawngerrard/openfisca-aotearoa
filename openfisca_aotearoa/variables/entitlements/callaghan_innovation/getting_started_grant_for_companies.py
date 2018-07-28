# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Company


class getting_started_years_in_business_for_company(Variable):
        value_type = int
        entity = Company
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a company has been in business'
        reference = "Needs updating"
	

class getting_started_research_expenditure_for_company(Variable):
        value_type = float
        entity = Company
        default_value = 0
        definition_period = YEAR
        label = u'The amount of Research and Development expenditure for the company'
        reference = "Needs updating"


class getting_started_eligible_for_grant_for_company(Variable):
	value_type = bool
	entity = Company
	definition_period = YEAR
	label = u'Determines if the company is eligible for a getting started grant'
	reference = "Needs updating"

	def formula(companies, period):
		return companies("getting_started_years_in_business_for_company", period) == 1


class getting_started_entitlement_for_company(Variable):
	value_type = float
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the getting started grant'
	reference = "Needs updating"

	def formula(company, period, parameters):
		return select(
			[getting_started_research_expenditure_for_company <= parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_maximum_threshold, getting_started_research_expenditure_for_company > parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_maximum_threshold],
			[getting_started_research_expenditure_for_company * parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_entitlement_rate, 5000]
		)