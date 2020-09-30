from share.transform.chain import ChainTransformer, Parser
from typing import Any

LINK_FORMAT: str
FIELDS: Any

class Person(Parser):
    family_name: Any = ...
    given_name: Any = ...

class FullNamePerson(Parser):
    schema: str = ...
    name: Any = ...

class PrincipalInvestigator(Parser):
    agent: Any = ...

class OtherInvestigator(Parser):
    schema: str = ...
    agent: Any = ...

class AdditionalInvestigator(Parser):
    schema: str = ...
    agent: Any = ...

class WorkIdentifier(Parser):
    uri: Any = ...

class Registration(Parser):
    title: Any = ...
    description: Any = ...
    date_published: Any = ...
    date_updated: Any = ...
    related_agents: Any = ...
    identifiers: Any = ...
    class Extra:
        registration_date: Any = ...
        questions_and_objectives: Any = ...
        study_type: Any = ...
        study_type_detail: Any = ...
        contact_details: Any = ...
        participating_institutions: Any = ...
        countries_of_recruitment: Any = ...
        funders: Any = ...
        problems_studied: Any = ...
        patient_population: Any = ...
        interventions: Any = ...
        inclusion_criteria: Any = ...
        exclusion_criteria: Any = ...
        control_or_comparators: Any = ...
        primary_outcomes: Any = ...
        key_secondary_outcomes: Any = ...
        target_sample_size: Any = ...
        recruitment_status: Any = ...
        other_recruitment_status: Any = ...
        first_enrollment_date: Any = ...
        expected_enrollment_completion_date: Any = ...
        expected_research_completion_date: Any = ...
        ethical_approval: Any = ...
        ethical_approval_details: Any = ...
        ethical_committee_judgment: Any = ...
        data: Any = ...
        published_paper: Any = ...
        study_website: Any = ...
        study_results: Any = ...
    def get_link(self, id: Any): ...
    def split_names(self, obj: Any): ...

class RRTransformer(ChainTransformer):
    VERSION: int = ...
    root_parser: Any = ...