# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Maori_Authority



class growth_years_in_business_for_maori_authorities(Variable):
        value_type = int
        entity = Maori_Authority
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a Maori_Authority has been in business'
        reference = "Needs updating"

class growth_eligible_years_in_business_for_maori_authorities(Variable):
        value_type = bool
        entity = Maori_Authority
        definition_period = YEAR
        label = u'Determines if the amount of years Maori_Authority has been in business is eligible'
        reference = "Needs updating"
	
	def formula(companies, period):
		return maori_authorities("growth_years_in_business_for_maori_authorities", period) > 2


# *******************************

class growth_rnd_expenditure_nongovernment_funds_for_maori_authorities(Variable):
	value_type = float
	entity = Maori_Authority
	default_value = 0
	definition_period = YEAR
	label = u'Determines R&D expenditure sourced from non-government funds in each of the last two financial years.'
	reference = "Needs updating"

class growth_eligible_rnd_expenditure_nongovernment_funds_for_maori_authorities(Variable):
	value_type = bool
	entity = Maori_Authority
	definition_period = YEAR
	label = u'Determines whether the amount R&D expenditure sourced from non-government funds in each of the last two financial years is eligible or not.'
	reference = "Needs updating"

	def formula(companies, period):
		return maori_authorities("growth_rnd_expenditure_nongovernment_funds_for_maori_authorities") >= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_minimum_eligible_rnd_expediture_nongovernment_funds
		

# *******************************


class growth_percentage_rnd_expenditure_of_revenue_for_maori_authorities(Variable):
	value_type = float
	entity = Maori_Authority
	default_value = 0
	definition_period = YEAR
	label = u'Determines percentage of eligible R&D expenditure of their revenue in the last two financial years.'
	reference = "Needs updating"

class growth_eligible_percentage_rnd_expenditure_of_revenue_for_maori_authorities(Variable):
	value_type = bool
	entity = Maori_Authority
	definition_period = YEAR
	label = u'Determines whether the amount of R&D expediture percentage is eligible or not.'
	reference = "Needs updating"

	def formula(companies, period):
		return maori_authorities("growth_percentage_rnd_expenditure_of_revenue_for_maori_authorities") >= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_rnd_percentage_of_revenue


class growth_eligible_for_grant_for_maori_authorities(Variable):
	value_type = bool
	entity = Maori_Authority
	definition_period = YEAR
	label = u'Determines if the Maori_Authority is eligible for a growth grant'
	reference = "Needs updating"

	def formula(companies, period):
		return maori_authorities("growth_eligible_years_in_business_for_maori_authorities", period) * maori_authorities("growth_eligible_rnd_expenditure_nongovernment_funds_for_maori_authorities", period) * maori_authorities("growth_eligible_percentage_rnd_expenditure_of_revenue_for_maori_authorities", period) == 1

	
class growth_entitlement_for_maori_authorities(Variable):
	value_type = float
	entity = Maori_Authority
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the growth grant'
	reference = "Needs updating"

	def formula(Maori_Authority, period, parameters):
		rate = parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_entitlement_rate
		apportioned_amount = Maori_Authority('growth_rnd_expenditure_nongovernment_funds_for_maori_authorities',period) * rate
		return select([Maori_Authority('growth_rnd_expenditure_nongovernment_funds_for_maori_authorities',period) <= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_maximum_threshold,Maori_Authority('growth_rnd_expenditure_nongovernment_funds_for_maori_authorities',period) > parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_maximum_threshold],[apportioned_amount, 5000000])