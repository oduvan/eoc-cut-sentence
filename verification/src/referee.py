from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "cut_sentence"
    FUNCTION_NAMES = {
        "python_3": "cut_sentence",
        "js_node": "cutSentence"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''

def cover(func, in_data):
    return func(*in_data)

    ''',
            ENV_NAME.JS_NODE: '''

function cover(func, in_data) {
    return func.apply(this, in_data)
}

    '''
    }