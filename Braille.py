


# defining values based on Grade 1 Braille
alphaBraille = ['⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅', '⠇',
 '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', ' ']
numBraille = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
puntuation = [',',';',':','.','?','!', ';','(',')', '/', '-']
puntuationBraille = ['⠂','⠆','⠒','⠲','⠦','⠖','⠐⠣','⠐⠜','⠸⠌','⠤']
character = ['&','*','@','©','®','™','°',]
characterBraille = ['⠈⠯','⠐⠔','⠈⠁','⠘⠉','⠘⠗','⠘⠞','⠘⠚',]

#To test our cases 
translateToBraille = 'This is good day & Tony what are you planning to do @ the mall ?'

translateToEnglish = None 

def main():
    inputString = ' '
    if len(translateToBraille) > 0 : 
        for n in translateToBraille.lower():
            if n in alphabet:
                inputString += alphaBraille[alphabet.index(n)]
            elif n in nums:
                inputString += numBraille[nums.index(n)]
            elif n in puntuation:
                inputString += puntuationBraille[puntuation.index(n)]
            elif n in character:
                inputString += characterBraille[character.index(n)]
        print(inputString)
        return

    if translateToEnglish:
        for n in translateToEnglish:
            if n in alphaBraille:
                inputString += alphabet[alphaBraille.index(n)]
            elif n in numBraille:
                inputString += nums[numBraille.index(n)]
            elif n in puntuationBraille :
                inputString += puntuation[puntuationBraille.index(n)]
            elif n in characterBraille:
                inputString += character[characterBraille.index(n)]

        print(inputString)
        return

## calling main method
main()


