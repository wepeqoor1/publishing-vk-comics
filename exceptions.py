# {'error': {'error_code': 3, 'error_msg': 'Unknown method passed', 'request_params': [{'key': 'group_id', 'value': '215521916'}, {'key': 'v', 'value': '5.131'}, {'key': 'method', 'value': 'photos.getWallUploadServe'}, {'key': 'oauth', 'value': '1'}]}}
class VKCodeExceptions(Exception):
    def __init__(self, error_code: int):
        self.error_code = error_code


    return self.error_code