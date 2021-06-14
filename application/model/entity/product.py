class Product:
    def __init__(self, id: int, title: str, images: str, value: int, installments: int, installment_value: int):
        self._id = id
        self._title = title
        self._images = images
        self._value = value
        self._installments = installments
        self._installment_value = installment_value

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value
    
    @property
    def images(self):
        return self._images
    
    @images.setter
    def images(self, value):
        self._images = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def installments(self):
        return self._installments

    @installments.setter
    def installments(self, value):
        self._installments = value

    @property
    def installmentsValue(self):
        return self._installment_value
    
    @installmentsValue.setter
    def installmentsValue(self, value):
        self._installment_value = value
    