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
        self.__move = 'X'
        self.__result = '-'
        self.moves = []

    def __del__(self):
        pass

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
            self.__move = '0' if self.__move == 'X' else 'X'
            self.moves.append(sector)
            self.__checkWin(self)
        else:
            raise


    @property
    def getResult(self):
        return self.__result 


    @property
    def getPosition(self):
        position = []
        for i in self.__position:
            for j in i:
                position.append(j)
        return position
        


    @staticmethod   
    def __checkWin(self):
        for i in COMBINATIONS.keys():
            a1 = COMBINATIONS.get(i)[0]
            a2 = COMBINATIONS.get(i)[1]
            a3 = COMBINATIONS.get(i)[2]
            if a1 in self.moves and a2 in self.moves and a3 in self.moves:
                if self.moves.index(a1) % 2 == self.moves.index(a2) % 2 == self.moves.index(a3) % 2:
                    if self.moves.index(a1) % 2 == 1:
                        self.__result = "0"
                    else:
                        self.__result = "X"
            if self.__result == '-' and len(self.moves) == 9:
                self.__result = '#'



#Код выше является игрой в крестики нолики. 
#Сделать ход функцией getMove(сектор по принципу СтрокаСтолбец)
#Получить текущую позицию игры можно функцией getPosition
#Получить результат игры можно функцией getResult
#Все ходы записываются в параметр object.moves
