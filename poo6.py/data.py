class Data:
    def __init__(self, dia: int, mes: int, ano: int ):
        if dia < 0 or mes < 0 or ano < 0:
            raise ValueError("Data invalida")
        if mes > 12 or dia > 31:
            raise ValueError("Data invalida")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, valor):
        if valor < 1 or valor > 31:
            print("Dia inválido")
        else:
            self.__dia = valor
    
    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, valor):
        if valor < 1 or valor > 12:
            print("mes inválido")
        else:
            self.__mes = valor
        
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
            self.__ano = valor

    def __str__(self):
        return f'''{self.__dia if self.__dia > 10 else "0" + str(self.__dia)}/{self.__mes if self.__mes > 10 else "0" + str(self.__mes)}/
        {"0"*(4 - (len(str(self.__ano)))) + str(self.__ano) if len(str(self.__ano)) < 4 else self.__ano }'''
    
    def setData(self, dia: int, mes:int, ano: int):
        if dia < 0 or mes < 0 or ano < 0:
            return print("Data inavalida")
        if mes > 12 or dia > 31:
            return print("Data invalida")
        
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    

calendario = Data(20, 4, 2023)
print(calendario)
calendario.setData(5, 6, 23)
print(calendario)