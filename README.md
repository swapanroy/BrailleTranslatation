# BrailleTranslatation

Python Program to translate to and from Braille (Grade 1 Braille). It includes alphabets, numbers, puntuations and symbols. 

Source for translation : https://www.pharmabraille.com/braille-codes/unified-english-braille-ueb-code/ 

## Defining translation 
        
        
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

## Loop over the index and pick values 


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


![Output of translated Braille](https://github.com/swapanroy/BrailleTranslatation/blob/6dac8fb7437262aa5d96ecd8315594b7bb2ee8db/Braille.jpg )


For collaboration or suggestion, reach me on my  [LinkedIn](www.linkedin.com/in/swapanroy/) [Twitter](www.twitter.com/royswapan)
