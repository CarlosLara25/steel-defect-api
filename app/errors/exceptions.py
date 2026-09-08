
class PredictionError(Exception):
    """Raised when inference cannot be completed"""

    def __init__(self, message: str="Prediction failed"):

        self.message = message
        super().__init__(self.message)


