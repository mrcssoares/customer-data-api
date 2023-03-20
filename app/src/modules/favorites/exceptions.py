from fastapi import HTTPException, status


class CustomerException(Exception):
    def __init__(self, message):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=message)


class CustomerNotFound(CustomerException):
    def __init__(self, customer_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Customer with id {customer_id} not found')
