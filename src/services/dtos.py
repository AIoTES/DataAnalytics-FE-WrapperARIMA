from src.utils.null_object import Null


class MIDto:
    NULL = Null()

    def __init__(self, mid1):
        self.mid1 = mid1

    def to_dict(self):
        return {"mutual_information": list(self.mid1)}
