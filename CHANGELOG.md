# Changelog

# 4.0.2 - [#42](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/22)
Legislation improvement.
* Added Accommodation Supplement from the Social Security Act 1964

# 4.0.1 - [#42](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/42)
Technical improvement.
* Details:
  - Moving the version bump check to its own segment of the circle ci config, This means it appears as a separate check within a github PR, and so we can see quickly that the input/output tests pass - and it's only the version bump that's missing.

# 4.0.0 - [#22](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/22)

* Tax and benefit system evolution. Major change.
* Impacted periods: all
* Impacted areas: `entities.families, tests/best_start, tests/family_scheme, tests/working_for_families, variables/demographics, variables/rates_rebates, variables/entitlements/income_tax/best_start.py, variables/entitlements/income_tax/family_scheme.py, variables/entitlements/income_tax/working_for_families.py`
* Details:
  - removed extraneous rates_rebates variable file,
  - added `variables/demographics` section with variables (`date_of_birth, due_date_of_birth, age, age_of_youngest`)
  - added `variables/entitlements/income_tax/best_start.py` with variables (`income_tax__caregiver_eligible_for_best_start_tax_credit, income_tax__family_has_children_eligible_for_best_start, income_tax__best_start_tax_credit_per_child,  income_tax__entitlement_for_best_start_tax_credit, income_tax__person_is_best_start_child_as_year`)
  - added `variables/entitlements/income_tax/family_scheme.py` with variables (`income_tax__qualifies_for_entitlements_under_family_scheme, income_tax__caregiver_age_qualifies_under_family_scheme, income_tax__person_principal_carer_qualifies_under_family_scheme, income_tax__family_scheme_income, income_tax__proportion_as_principal_carer`)
  - added `variables/entitlements/income_tax/working_for_families.py` with variables (`social_security__received_income_tested_benefit, veterans_support__received_parents_allowance, veterans_support__received_childrens_pension, income_tax__resident, income_tax__family_has_dependent_children, income_tax__dependent_child`)

# 3.0.0 - [#20](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/20)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - Variables `income_tax__tax_payer_filing_status, income_tax__annual_gross_income, income_tax__annual_total_deduction, income_tax__net_income, income_tax__net_loss, income_tax__available_tax_loss, income_tax__taxable_income, rates_rebates__dependants, rates_rebates__rates_total, rates_rebates__combined_income, rates_rebates__rebate, rates_rebates__maximum_income_for_full_rebate, rates_rebates__minimum_income_for_no_rebate`
* Details:
  - Variable renaming, impacts the OpenFisca-Aotearoa public API (for instance renaming or removing a variable)

## 2.2.0 - [#19](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/19)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas: Entities
* Details:
  - Add a `Family` entity.
<!-- -->
* Tax and benefit system evolution.
* Impacted periods: after 2017-04.
* Impacted areas: “Working for families” parameters
* Details:
  - Add the `principal_caregiver_minimum_exclusive_care_percentage`, `principal_caregiver_age_threshold`, `full_year_abatement_threshold`, `full_year_abatement_rate` and `dependent_children_minimum_threshold` parameters.

## 2.1.0 - [#18](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/18)

* Tax and benefit system evolution
* Impacted periods: from 2000-04-01
* Impacted areas:
  - Variables `tax_payer_filing_status__income_tax, annual_gross_income__income_tax, annual_total_deduction__income_tax, net_income__income_tax, net_loss__income_tax, available_tax_loss__income_tax, taxable_income__income_tax`
  - Parameters `individual_income_tax_rate`
* Details:
  - Introducing some initial income_tax variables, laid out as per current best practice

# 2.0.0 - [#12](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/12)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas:
  - Variables `rates_rebates`
  - Entities `Propertee`
* Details:
  - Renaming Titled_Property entity (from Propertee)
  - Renaming of combined_income_as_per_rates_rebates (from salary)
  - Renaming of dependants_as_per_rates_rebates (from dependants)
  - Renaming of rates_total_as_per_rates_rebates (from rates)


### 1.0.1 - [#10](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/10)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas:
  - Variables `rates_rebates`
* Details:
  - Addition of Math floor function to conform rates_rebates variable with existing infrastructure.


# 1.0.0 - [#6](https://github.com/ServiceInnovationLab/openfisca-aotearoa/pull/6)

* Tax and benefit system evolution
* Impacted periods: from 1973-07
* Impacted areas:
  - Parameters `benefits/rates_rebates`
  - Variables `rates_rebates`
  - Entities
* Details:
  - Create calculations for rates rebates system, based on year
    - Introduce `Propertee` entity
    - Introduce `benefits/rates_rebates/additional_per_dependant` parameter
    - Introduce `benefits/rates_rebates/income_threshold` parameter
    - Introduce `benefits/rates_rebates/initial_contribution` parameter
    - Introduce `benefits/rates_rebates/maximum_allowable` parameter
    - Introduce `dependants` variable
    - Introduce `rates` variable
    - Introduce `rates_rebate` variable
    - Introduce `maximum_income_for_full_rebate` variable
    - Introduce `minimum_income_for_no_rebate` variable
<!-- -->
* Tax and benefit system evolution
* Impacted periods: from 1898-01-01
* Impacted areas:
  - Parameters `general`
* Details:
  - Introduce new general legislation parameters
    - Introduce `general/age_of_majority` parameter
    - Introduce `general/age_of_superannuation` parameter
<!-- -->
* Tax and benefit system evolution
* Impacted periods: from 2000-04-01
* Impacted areas:
  - Parameters `taxes`
* Details:
  - Introduce income tax parameters
    - Introduce `taxes/income_tax_rate` parameter
