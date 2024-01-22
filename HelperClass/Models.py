class ResponseModel:
    def __init__(self, message = None, result_data = [], status = True):
        self.Message = message
        self.ResultData = result_data
        self.Status = status