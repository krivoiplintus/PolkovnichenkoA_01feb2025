import json


my_data = open('test_data.json')
global_data = json.load(my_data)


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, property: str) -> str:
        return self.data.get(property)

    def getint(self, property: str) -> int:
        return int(self.data.get(property))

    def get_clientId(self) -> int:
        return self.data.get("clientId")

    def get_orderId(self) -> int:
        return self.data.get("orderId")

    def get_goodId(self) -> int:
        return self.data.get("goodId")

    def get_quantity(self) -> int:
        return self.data.get("quantity")

    def get_cityId(self) -> str:
        return self.data.get("cityId")
