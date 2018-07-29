# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Partnership



class growth_years_in_business_for_partnership(Variable):
        value_type = int
        entity = Partnership
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a partnership has been in business'
        reference = "Needs updating"

class growth_eligible_years_in_business_for_partnership(Variable):
        value_type = bool
        entity = Partnership
        definition_period = YEAR
        label = u'Determines if the amount of years partnership has been in business is eligible'
        reference = "Needs updating"
	
	def formula(companies, period):
		return partnerships("growth_years_in_business_for_partnership", period) > 2


# *******************************

class growth_rnd_expenditure_nongovernment_funds_for_partnership(Variable):
	value_type = float
	entity = Partnership
	default_value = 0
	definition_period = YEAR
	label = u'Determines R&D expenditure sourced from non-government funds in each of the last two financial years.'
	reference = "Needs updating"

class growth_eligible_rnd_expenditure_nongovernment_funds_for_partnership(Variable):
	value_type = bool
	entity = Partnership
	definition_period = YEAR
	label = u'Determines whether the amount R&D expenditure sourced from non-government funds in each of the last two financial years is eligible or not.'
	reference = "Needs updating"

	def formula(companies, period):
		return partnerships("growth_rnd_expenditure_nongovernment_funds_for_partnership") >= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_minimum_eligible_rnd_expediture_nongovernment_funds
		

# *******************************


class growth_percentage_rnd_expenditure_of_revenue_for_partnership(Variable):
	value_type = float
	entity = Partnership
	default_value = 0
	definition_period = YEAR
	label = u'Determines percentage of eligible R&D expenditure of their revenue in the last two financial years.'
	reference = "Needs updating"

class growth_eligible_percentage_rnd_expenditure_of_revenue_for_partnership(Variable):
	value_type = bool
	entity = Partnership
	definition_period = YEAR
	label = u'Determines whether the amount of R&D expediture percentage is eligible or not.'
	reference = "Needs updating"

	def formula(companies, period):
		return partnerships("growth_percentage_rnd_expenditure_of_revenue_for_partnership") >= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_rnd_percentage_of_revenue


class growth_eligible_for_grant_for_partnership(Variable):
	value_type = bool
	entity = Partnership
	definition_period = YEAR
	label = u'Determines if the partnership is eligible for a growth grant'
	reference = "Needs updating"

	def formula(companies, period):
		return partnerships("growth_eligible_years_in_business_for_partnership", period) * partnerships("growth_eligible_rnd_expenditure_nongovernment_funds_for_partnership", period) * partnerships("growth_eligible_percentage_rnd_expenditure_of_revenue_for_partnership", period) == 1

	
class growth_entitlement_for_partnership(Variable):
	value_type = float
	entity = Partnership
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the growth grant'
	reference = "Needs updating"

	def formula(partnership, period, parameters):
		rate = parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_entitlement_rate
		apportioned_amount = partnership('growth_rnd_expenditure_nongovernment_funds_for_partnership',period) * rate
		return select([partnership('growth_rnd_expenditure_nongovernment_funds_for_partnership',period) <= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_maximum_threshold,partnership('growth_rnd_expenditure_nongovernment_funds_for_partnership',period) > parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_maximum_threshold],[apportioned_amount, 5000000])