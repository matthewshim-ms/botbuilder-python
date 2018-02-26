# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LuisResult(Model):
    """Prediction, based on the input query, containing intent(s) and entities.

    :param query: The input utterance that was analized.
    :type query: str
    :param altered_query: The corrected utterance (when spell checking was
     enabled).
    :type altered_query: str
    :param top_scoring_intent:
    :type top_scoring_intent: ~luisruntime.models.IntentModel
    :param intents: All the intents (and their score) that were detected from
     utterance.
    :type intents: list[~luisruntime.models.IntentModel]
    :param entities: The entities extracted from the utterance.
    :type entities: list[~luisruntime.models.EntityModel]
    :param composite_entities: The composite entities extracted from the
     utterance.
    :type composite_entities: list[~luisruntime.models.CompositeEntityModel]
    """

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'altered_query': {'key': 'alteredQuery', 'type': 'str'},
        'top_scoring_intent': {'key': 'topScoringIntent', 'type': 'IntentModel'},
        'intents': {'key': 'intents', 'type': '[IntentModel]'},
        'entities': {'key': 'entities', 'type': '[EntityModel]'},
        'composite_entities': {'key': 'compositeEntities', 'type': '[CompositeEntityModel]'},
    }

    def __init__(self, query=None, altered_query=None, top_scoring_intent=None, intents=None, entities=None, composite_entities=None):
        super(LuisResult, self).__init__()
        self.query = query
        self.altered_query = altered_query
        self.top_scoring_intent = top_scoring_intent
        self.intents = intents
        self.entities = entities
        self.composite_entities = composite_entities