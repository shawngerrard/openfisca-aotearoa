# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person, Company



class growth_years_in_business_for_company(Variable):
        value_type = int
        entity = Company
        default_value = 0
        definition_period = YEAR
        label = u'The amount of years a company has been in business'
        reference = "Needs updating"

class growth_eligible_years_in_business_for_company(Variable):
        value_type = bool
        entity = Company
        default_value = 0
        definition_period = YEAR
        label = u'Determines if the amount of years company has been in business is eligible'
        reference = "Needs updating"
	
	def formula(companies, period):
		return companies("growth_years_in_business_for_company", period) > 2


# *******************************

class growth_rnd_expenditure_nongovernment_funds(Variable):
	value_type = float
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines R&D expenditure sourced from non-government funds in each of the last two financial years.'
	reference = "Needs updating"

class growth_eligible_rnd_expenditure_nongovernment_funds(Variable):
	value_type = bool
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines whether the amount R&D expenditure sourced from non-government funds in each of the last two financial years is eligible or not.'
	reference = "Needs updating"

	def formula(companies, period):
		return companies("growth_rnd_expenditure_nongovernment_funds") >= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_minimum_eligible_rnd_expediture_nongovernment_funds
		

# *******************************


class growth_percentage_rnd_expenditure_of_revenue(Variable):
	value_type = float
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines percentage of eligible R&D expenditure of their revenue in the last two financial years.'
	reference = "Needs updating"

class growth_eligible_percentage_rnd_expenditure_of_revenue(Variable):
	value_type = bool
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines whether the amount of R&D expediture percentage is eligible or not.'
	reference = "Needs updating"

	def formula(companies, period):
		return companies("growth_percentage_rnd_expenditure_of_revenue") >= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_rnd_percentage_of_revenue


class growth_eligible_for_grant_for_company(Variable):
	value_type = bool
	entity = Company
	definition_period = YEAR
	label = u'Determines if the company is eligible for a growth grant'
	reference = "Needs updating"

	def formula(companies, period):
		return companies("growth_eligible_years_in_business_for_company", period) * companies("growth_eligible_rnd_expenditure_nongovernment_funds", period) * companies("growth_eligible_percentage_rnd_expenditure_of_revenue", period) == 1

	
class growth_entitlement_for_company(Variable):
	value_type = float
	entity = Company
	default_value = 0
	definition_period = YEAR
	label = u'Determines the entitlement of the growth grant'
	reference = "Needs updating"

	def formula(company, period, parameters):
		rate = parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_entitlement_rate
		apportioned_amount = company('growth_research_expenditure_for_company',period) * rate
		return select([company('growth_research_expenditure_for_company',period) <= parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_maximum_threshold,company('growth_research_expenditure_for_company',period) > parameters(period).entitlements.callaghan_innovation.growth_grant.growth_grant_maximum_threshold],[apportioned_amount, 5000000])