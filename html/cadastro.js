document.getElementById('login').value = "oi"

/*
    Variáveis
    var String
    var Number
    var Boolean
*/

//String
var texto = "variável string"

//Number
var numeroInteiro = -8
var numeroFracionado = 1002.55

//Boolean
var teste = true

//Null
var teste2 = null

//Undefined
var teste3
var teste4 = undefined

document.write("Esse código é uma " + texto + " que pode ser concatenada!<br>")

console.log(numeroFracionado)

var nome = prompt("Digite o seu nome: ")
var idade = prompt("Digite a sua idade: ")

document.write("Hi, my name is " + nome + " and i was " + idade + " years <br>")


//If Else
if (2 !== '2') {
    document.write("Verdadeiro<br>")
} else {
    document.write("Farso<br>")
}

/*
    Comparadores lógicos
    ==
    === , mesmo valor e tipo
    != , valores diferentes
    !== , valores e tipos diferentes
*/