COMBINATIONS = {
    0: [11, 12, 13],
    1: [21, 22, 23],
    2: [31, 32, 33],
    3: [11, 21, 31],
    4: [12, 22, 32],
    5: [13, 23, 33],
    6: [11, 22, 33],
    7: [13, 22, 31]

}
class game():
    def __init__(self, name) -> None:  #создание игры 
        self.name = name
        self.__position = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.__combinatios = {}
        self.__move = 'X'
        self.__result = '-'
        self.moves = []


    def __str__(self) -> str: #функция отображения текущего состояния игры в строковом типе
        position = str()
        for i in range(0, 3):
            for j in range(0, 3):
                position += ' \'' + self.__position[i][j] + '\' '
            position += '\n'
            
        answer = self.name + '\n' + position + '\nХодят '+ self.__move + '\nРезультат: ' + self.__result + '\n'
        return answer


    def getMove(self, sector: int): #функция хода в формате xy, где x - первая цифра, обозначающая строку, а y - вторая цифра, обозначающая столбец 
        if self.__position[sector // 10 - 1][sector % 10 - 1] == ' ':
            self.__position[sector // 10 - 1][sector % 10 - 1] = self.__move 
            self.__addCombination(self, sector) 
            self.__checkCombination(self)
            self.__move = '0' if self.__move == 'X' else 'X'
            self.moves.append(sector)
        else:
            raise


    @property
    def getResult(self):
        return self.__result 


    @property
    def getPosition(self):
        return self.__position


    @staticmethod   
    def __addCombination(self, sector: int):  #функция, добавляющая наш ход в возможные выигрывающие комбинации 
        for i in COMBINATIONS.keys():
            if sector in COMBINATIONS[i] and i not in self.__combinatios.keys():
                self.__combinatios[i] = self.__move


    @staticmethod
    def __checkCombination(self): #функция, проверяющая комбинации на потенциальную или действительную победу
        for i in self.__combinatios.keys():
            if len(self.__combinatios.get(i)) == 3 and self.__combinatios.get(i)[0] == self.__combinatios.get(i)[1] == self.__combinatios.get(i)[2]:
                self.__result = self.__move
                break
        draw = True 
        for i in self.__position:
            for j in i:
                if j == ' ':
                    draw = False
                    break 
        if draw:
            self.__result = '#'
            
        dels = []
        for i in self.__combinatios.keys():
            if len(self.__combinatios.get(i)) > 1 and (self.__combinatios.get(i)[0] != self.__combinatios.get(i)[1] or self.__combinatios.get(i)[1] != self.__combinatios.get(i)[2]):
                dels.append(i)
        for i in dels:
            self.__combinatios.pop(i)

#Код выше является игрой в крестики нолики. 
#Сделать ход функцией getMove(сектор по принципу СтрокаСтолбец)
#Получить текущую позицию игры можно функцией getResult
#Получить результат игры можно функцией getResult
#Все ходы записываются в параметр object.moves


        

#Алгоритм...




