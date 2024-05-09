package main

import (
  "fmt"
  "unicode"
  "strings"
)

func ReverseWords(inputString string)(string){
  var outputString string

  // For storing individual words in reverse order
  var reversedWord []string

  // Iterate over the inputString
  for _, char := range inputString{

    // If the char is alphabet or number then prepred it to the reversedWord
    // Otherwise append reversedWord and char to the outputString
    // and reset the value of reversedWord
    if (unicode.IsLetter(char) || unicode.IsDigit(char)){
        reversedWord = append([]string{string(char)}, reversedWord...)
    } else {
        if len(reversedWord)>0{
          outputString+=strings.Join(reversedWord,"")
        }
        outputString+=string(char)
        reversedWord = []string{}
    } 
  }

  // If any word is left to append then add it to the outputString
  if len(reversedWord)>0{
    outputString+=strings.Join(reversedWord,"")
  }

  return outputString
}

func main(){
  testcases := [][]string{
    []string{"String; 2be reversed...", "gnirtS; eb2 desrever..."},
    []string{"i j k x y", "i j k x y"},
    []string{"Hello, how are you?", "olleH, woh era uoy?"},
    []string{"abcd 1234; !@#$%^&*()", "dcba 4321; !@#$%^&*()"},
  }

  for _, test := range testcases{
    result := ReverseWords(test[0])
    if result!=test[1]{
      errorMsg := fmt.Sprintf("Expected reversed word \"%s\" but received \"%s\"", test[1], result)
      panic(errorMsg)
    } else {
      fmt.Println("Assertion successful for input:", test[0], "output:", test[1])
    }
  }
}
