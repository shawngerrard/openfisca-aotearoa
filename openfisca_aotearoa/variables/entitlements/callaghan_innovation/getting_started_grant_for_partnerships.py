# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Partnership


class getting_started_years_in_business_for_partnership(Variable):
        value_type = int
        entity = Partnership
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a partnership has been in business'
        reference = "Needs updating"
	

class getting_started_research_expenditure_for_partnership(Variable):
        value_type = float
        entity = Partnership
        default_value = 0
        definition_period = YEAR
        label = u'The amount of Research and Development expenditure for the partnership'
        reference = "Needs updating"


class getting_started_eligible_for_grant_for_partnership(Variable):
	value_type = bool
	entity = Partnership
	definition_period = YEAR
	label = u'Determines if the partnership is eligible for a getting started grant'
	reference = "Needs updating"

	def formula(partnerships, period):
		return partnerships("getting_started_years_in_business_for_partnership", period) == 1


class getting_started_entitlement_for_partnership(Variable):
	value_type = float
	entity = Partnership
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the getting started grant'
	reference = "Needs updating"

	def formula(partnership, period, parameters):
		rate = parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_entitlement_rate
		apportioned_amount = partnership('getting_started_research_expenditure_for_partnership',period) * rate
		return select([partnership('getting_started_research_expenditure_for_partnership',period) <= parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_maximum_threshold,partnership('getting_started_research_expenditure_for_partnership',period) > parameters(period).entitlements.callaghan_innovation.getting_started_grant.getting_started_grant_maximum_threshold],[apportioned_amount, 5000])