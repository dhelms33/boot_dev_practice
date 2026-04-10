MAX_RETRY_COUNT = 6
#additive count is not in global scope
def get_additive_count(adjust):
    """ enter in adjustment to the MAX_RETRY_COUNT"""
    additive_count = MAX_RETRY_COUNT + adjust
    return additive_count