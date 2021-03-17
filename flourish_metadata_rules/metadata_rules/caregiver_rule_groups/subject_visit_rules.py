from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, P, register
from ...predicates import CaregiverPredicates

app_label = 'flourish_caregiver'
pc = CaregiverPredicates()

@register()
class  MaternalVisitRuleGroup(CrfRuleGroup):

    preg_prior = CrfRule(
        predicate=pc.func_preg_no_prior_participation,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.foodsecurityquestionnaire',
                       f'{app_label}.ultrasound',
                       f'{app_label}.caregiveredinburghdeprscreening',])

    biological_with_hiv = CrfRule(
        predicate=pc.func_bio_mothers_hiv,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.hivviralloadandcd4',])

    hiv_no_prior = CrfRule(
        predicate=pc.func_pregnant_hiv,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.arvsprepregnancy',
                       f'{app_label}.maternalarvduringpreg'])

    non_preg = CrfRule(
        predicate=pc.func_non_pregnant_caregivers,
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.caregiverhamddeprscreening',
                       f'{app_label}.caregiverphqdeprscreening'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.maternalvisit'