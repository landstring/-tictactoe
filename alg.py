from main import game
import time
from progress.bar import IncrementalBar

#Сделать ход функцией getMove(сектор по принципу СтрокаСтолбец)
#Получить текущую позицию игры можно функцией getPosition
#Получить результат игры можно функцией getResult
#Все ходы записываются в параметр object.moves

positions = {}

sectors = {
    0: 11,
    1: 12,
    2: 13,
    3: 21,
    4: 22,
    5: 23,
    6: 31,
    7: 32, 
    8: 33
}


def learning(depth):
    for i in range(0, depth): 
        bar.next()
        element = game("Игра " + str(i))
        recording = {}
        while element.getResult == '-':
            position = element.getPosition
            var = []
            for i in range(0, len(position)):
                if position[i] == ' ':
                    var.append(sectors.get(i))
            textNotation = str()
            for i in position:
                textNotation += i
            if not textNotation in positions.keys():
                positions[textNotation] = []
                for i in var:
                    positions.get(textNotation).append([0, i])
            element.getMove(positions.get(textNotation)[0][1])
            recording[textNotation] = positions.get(textNotation)[0][1]
        if element.getResult == '#':
            for i in recording.keys():
                positions[i][0][0] -= 1
                positions.get(i).sort(key = lambda x: x[0], reverse = True)
        else:
            stack = 1 if element.getResult == 'X' else 0
            for i in recording.keys():
                if stack % 2 == 1:
                    positions[i][0][0] += 3
                    positions.get(i).sort(key = lambda x: x[0], reverse = True)
                    stack += 1
                else:
                    positions[i][0][0] -= 2
                    positions.get(i).sort(key = lambda x: x[0], reverse = True)
                    stack += 1
        del element
          
def play():
    mygame = game(input('Введите называние игры: '))
    stack = 1 if input('Вы за крестики или за нолики? ') == 'крестики'  else 2
    nowStack = 1
    while mygame.getResult == '-':
        print(mygame)
        if nowStack == stack:
            mygame.getMove(int(input('Ваш ход: ')))
        else:
            position = mygame.getPosition
            textNotation = str()
            for i in position:
                textNotation += i
            mygame.getMove(positions.get(textNotation)[0][1])
        nowStack = 1 if nowStack == 2 else 2
    print("Победили: " + mygame.getResult + ' Ещё партейку?')
    
bar = IncrementalBar('Анализ', max = 1000000, fill='@', suffix='%(percent)d%%')
learning(1000000)
bar.finish()
play()
