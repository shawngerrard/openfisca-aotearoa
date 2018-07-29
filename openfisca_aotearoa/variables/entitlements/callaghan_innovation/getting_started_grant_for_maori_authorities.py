# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Maori_Authority


class getting_started_years_in_business_for_maori_authorities(Variable):
        value_type = int
        entity = Maori_Authority
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a maori_authority has been in business'
        reference = "Needs updating"
	

class getting_started_research_expenditure_for_maori_authorities(Variable):
        value_type = float
        entity = Maori_Authority
        default_value = 0
        definition_period = YEAR
        label = u'The amount of Research and Development expenditure for the maori_authorities'
        reference = "Needs updating"


class getting_started_eligible_for_grant_for_maori_authorities(Variable):
	value_type = bool
	entity = Maori_Authority
	definition_period = YEAR
	label = u'Determines if the maori_authorities is eligible for a getting started grant'
	reference = "Needs updating"

	def formula(maori_authorities, period):
		return maori_authorities("getting_started_years_in_business_for_maori_authorities", period) == 1


class getting_started_entitlement_for_maori_authorities(Variable):
	value_type = float
	entity = Maori_Authority
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the getting started grant'
	reference = "Needs updating"

	def formula(maori_authority, period, parameters):
		rate = parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_entitlement_rate
		apportioned_amount = maori_authority('getting_started_research_expenditure_for_maori_authorities',period) * rate
		return select([maori_authority('getting_started_research_expenditure_for_maori_authorities',period) <= parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_maximum_threshold,maori_authority('getting_started_research_expenditure_for_maori_authority',period) > parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_maximum_threshold],[apportioned_amount, 5000])