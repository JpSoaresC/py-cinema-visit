class CinemaBar:
    @staticmethod
    def __init__(self, product: str, customer:str):
        self.product = product
        self.customer = customer
        def sell_product ():
            print(f"Cinema bar sold {self.product} to {self.customer}.")
    pass