class SortDiscountElems:
    def get(self, discountElems):
        x = []
        for elem in discountElems:
            b = [elem, elem.text]
            x.append(b)
        x.sort(key=lambda x: x[1])
        return (x)
