class Product:
    def __init__(self, id: int, title: str, images: str, value: int, installments: int, installment_value: int):
        self._id = id
        self._title = title
        self._images = images
        self._value = value
        self._installments = installments
        self._installmentValue = installment_value