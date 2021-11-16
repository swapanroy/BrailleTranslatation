# Braille Translatation

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


![output in braille shown in Visual Studio](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/feb32ggm6keogym91wn1.jpg)


For collaboration or suggestion, reach me on my  [Twitter](www.twitter.com/royswapan)
