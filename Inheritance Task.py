class Electronic_device():
    mob = "SamsungJ7"
class Pocket_gadget(Electronic_device):
    mob_cvr = "Cat cover"
    handsfree = "Beats"
    def gadget(self):
        return f"I have handsfree of {self.handsfree} and a mob cover of {self.mob_cvr}"

class Phone(Pocket_gadget):
    camera = "6.5 Mega pixel"
    sensor = "Touc screen"
    unlock = "On screen"
    def mob(self):
        return f"I have {self.mob} with backcover {self.mob_cvr}.And I have handsfree of {self.handsfree}.It's specifications are {self.camera}and {self.sensor} and it have fingerprint {self.unlock}"

Mobile = Electronic_device()
Gadget = Pocket_gadget ()
Phone = Phone()
print(Mobile.mob)
print(Gadget.gadget())
print(Phone.mob())