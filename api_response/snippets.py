

def validate_response_length(RESPONSE_LENGTH, GET_FULL_RESPONSE):
    try:
        RESPONSE_LENGTH = int(RESPONSE_LENGTH)
        return RESPONSE_LENGTH
    except:
        if RESPONSE_LENGTH == GET_FULL_RESPONSE:
            RESPONSE_LENGTH = None
            return RESPONSE_LENGTH
        else:
            raise TypeError('ENDPOINT_RESPONSE_LENGTH --> Must be either "all" or an integer')