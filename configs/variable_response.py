from rest_framework.response import Response
from rest_framework import status

def data_response(errors, data):
    return {
        'errors': errors,
        'data': data
    }
    
def response_data(status=status.HTTP_200_OK, errors=None, data=None):
    if errors is None:
        errors = {}
    
    return Response(status=status, data=data_response(errors=errors, data=data))