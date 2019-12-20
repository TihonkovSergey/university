class Supplicant:
    def __init__(self, supplicant):
        self.supplicant_id = str(supplicant[0])
        self.name = str(supplicant[1])
        self.telephone_number = str(supplicant[2])

    def __str__(self):
        return (self.supplicant_id + " " +
                self.name + " " +
                self.telephone_number)

    def __print__(self):
        print(str(self))

