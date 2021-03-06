# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity


Titled_Property = build_entity(
    key="titled_property",
    plural="titled_properties",
    label=u'Titled Property',
    doc='''
    A Titled property represents a property that is owned by a Person or group of Persons.

    Example usage:
    Check the number of individuals of a specific role: check how many persons co-own the property: `titled_properties.nb_persons(Titled_Property.OWNER)`.
    Calculate a variable applied to each tenant of the group entity: calculate the income of each member of the Property: `tenants_incomes = titled_properties.members('income', period = MONTH); tenants_total_income = titled_properties.sum(tenants_incomes)`.

    For more information on group entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles=[
        {
            'key': 'owner',
            'plural': 'owners',
            'label': u'Owners',
            'doc': u'The one or more persons who hold title for the property.'
            }
        ]
    )

Person = build_entity(
    key="person",
    plural="persons",
    label=u'Person',
    doc='''
    A Person represents an individual, the minimal legal entity on which a legislation might be applied.

    Example:
    The 'salary' and 'income_tax' variables are usually defined for the entity 'Person'.

    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'owner' in a 'Titled_Property' entity with person.has_role(Titled_Property.owner)).

    For more information on entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person=True,
    )

Family = build_entity(
    key="family",
    plural="families",
    label=u'Family',
    doc='''
    A Family represents a collection of related persons.

    Family entities are required for calculations across a number of entitlements including for example "Working for families" and "Paid Parental Leave"

    A family can contain a number of roles, such as 'principal_caregiver', 'partner' & 'child'.

    For more information on entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html

    Families can have multiple principle_caregivers but as each entitlement is calculated in relation to the Principle Caregiver we recommend for modelling you create multiple family sets per caregiver to describe each scenario
    ''',
    roles=[
        {
            'key': 'principal_caregiver',
            'label': u'Principal caregiver',
            'doc': u'The one person who is the principal caregiver of a family.',
            'max': 1
            },
        {
            'key': 'partner',
            'plural': 'partners',
            'label': u'Partners',
            'doc': u'The one or more persons who are partners of a family principal caregiver.'
            },
        {
            'key': 'child',
            'plural': 'children',
            'label': u'Children',
            'doc': u'The children of a family.'
            }
        ]
    )

Company = build_entity (
	key="company",
	plural="companies",
	label=u'Company',
	doc='''
	A company represents a collection of individuals.

	Company entities are required to calculate the entitlements to various Callaghan grants.

	A company can contain roles such as 'Shareholder' & 'Director'.

	For more information on entities, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
	
	Companies can have multiple shareholders and directors.
    ''',
	roles=[
		{
		'key': 'director',
		'plural':'directors',
		'label': u'Director',
		'doc': u'People who hold directorship for a company'
		},
		{
		'key':'shareholder',
		'plural': 'shareholders',
		'label': u'Shareholder',
		'doc': u'People who own shares in a company'
		}
	]
)

Partnership = build_entity (
	key="partnership",
	plural="partnerships",
	label=u'Partnership',
	doc='''
	A partnership represents two persons who are treated as a single partnership entity.

	Partnership entities are required to calculate the entitlements to various Callaghan grants.	

	A partnership will contain the role 'Partner'.

	Only two partners can form a partnership
	''',
	roles=[
		{
		'key':'partner',
		'plural':'partners',
		'label':u'partner',
		'max':2,
		'doc':u'People who are partners of the partnership'		
		}
	]
)


Maori_Authority = build_entity (
	key="maori_authority",
	plural="maori_authorities",
	label=u'maori_authorities',
	doc='''
	A Maori Authority represents an incorporation or trust established under the Te Ture Whenua Maori Act or to manage Treaty of Waitangi settlements, or a Maori statutory body or business controlled by any of these entities.

	Maori authority entities are required to calculate the entitlements to various Callaghan grants.	

	A Maori Authority will contain the roles 'Trustee', 'Beneficiary', 'Director', or 'Shareholder'.
	''',
	roles=[
		{
		'key':'trustee',
		'plural':'trustees',
		'label':u'trustee',
		'doc':u'People who are trustees of the Authority'		
		},
		{
		'key':'beneficiary',
		'plural':'beneficiaries',
		'label':u'beneficiary',
		'doc':u'People who are beneficiaries of the Authority'		
		},
		{
		'key':'director',
		'plural':'directors',
		'label':u'director',
		'doc':u'People who are directors of the Authority'		
		},
		{
		'key':'shareholder',
		'plural':'shareholders',
		'label':u'shareholder',
		'doc':u'People who are shareholders of the Authority'		
		}
	]
)

entities = [Titled_Property, Person, Family, Company, Partnership, Maori_Authority]
