from builtins import print


class Nematode:

    def __init__(self,cuerpo:float,genero:str,edad:int):
        self.cupero=cuerpo
        self.genero=genero
        self.edad=edad

    def __str__(self) -> str:
        return "Nermatode= {} mm long, gender is {} , {} days old".format(self.cupero,self.genero,self.edad)


    def __repr__(self) -> str:
        return "Nermatode= {}, {} ,{} ".format(self.cupero, self.genero, self.edad)


if __name__=="__main__":
    print()
    nematode1=Nematode(2.5,"hemafrodita", 256)
    print("Cuerpo: ",nematode1.cupero)
    print("Genero: ",nematode1.genero)
    print("Edad",nematode1.edad)
    print()

    print("String: ",nematode1)
    print("Repr: ",nematode1.__repr__())