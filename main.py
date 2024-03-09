#Apresentar nome do usuário
nome = input("Informe o nome do usuário: ")
print("Seja bem-vindo", nome)

#Apresentar nome do usuário e altura
nome = input("Informe o nome do usuário: ")
print("Seja bem-vindo", nome)
altura = float(input("Informe a altura do usuário: "))
print("A altura do usuário", nome, "é", altura)
print("Obrigado pelas informações")

#Apresentar dados do endereço do usuário
print("Por favor, preencha os dados de endereço")
rua = input("Informe o nome da rua: ")
numero = int(input("Informe o número da residência: "))
bairro = input("Informe o nome do bairro: ")
cidade = input("Informe o nome da cidade: ")
estado = input("Informe o nome do estado: ")
cep = int(input("Informe o CEP: "))
print("O endereço do usuário é:")
print("Rua", rua)
print("Número", numero)
print("Bairro", bairro)
print("Cidade", cidade)
print("Estado", estado)
print("O CEP é:", cep)

#Informar valores para somar e multiplicar
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))
valor4 = int(input("Informe o quarto valor: "))
valor5 = int(input("Informe o quinto valor: "))
soma = valor1 + valor2 + valor3 + valor4 + valor5
print("A soma dos valores é", soma)
multiplicacao = valor1 * valor2 * valor3 * valor4 * valor5
print("A multiplicação dos valores é", multiplicacao)

#Calcular valores para área
#Valores "b","c" são respectivamente base e altura para o triângulo
#Valores "a","b","c","d" formam o retângulo
#Valor "e" o raio para área do círculo
a = int(input("Informe o primeiro valor:"))
b = int(input("Informe o segundo valor:"))
c = int(input("Informe o terceiro valor:"))
d = int(input("Informe o quarto valor:"))
e = int(input("Informe o quinto valor:"))
areaTriangulo = (b * c) / 2
print("A área do triângulo é", areaTriangulo)
perimetroRetangulo = a + b + c + d
print("O perímetro do retângulo é", perimetroRetangulo)
areaCirculo = 3.14 * e * e
print("A área do círculo é", areaCirculo)

#Apresentar notas e resultado final
trabalho = float(input("Informe a nota do trabalho: "))
prova = float(input("Informe a nota da prova: "))
teste = float(input("Informe a nota do teste: "))
notaFinal = (trabalho * 0.1) + (prova * 0.6) + (teste * 0.3)
print("A nota final do aluno é", notaFinal)

#Apresentar notas de todas as avaliações (Grau A e Grau B) e imprima a nota final
atividadePratica = float(input("Informe a nota da atividade prática: "))
atividadeTeorica = float(input("Informe a nota da atividade teórica: "))
provaLaboratorio = float(input("Informe a nota da prova em laboratório: "))
testeTeorico = float(input("Informe a nota do teste teórico: "))
trabalhoExtraclasse = float(input("Informe a nota do trabalho extraclasse: "))
notaGrauA = (atividadePratica * 0.45) + (atividadeTeorica * 0.55)
notaGrauB = (provaLaboratorio * 0.6) + (testeTeorico * 0.2) + (trabalhoExtraclasse * 0.2)
notaFinal = (notaGrauA * 0.33) + (notaGrauB * 0.67)
print("A nota do Grau A é", notaGrauA)
print("A nota do Grau B é", notaGrauB)
print("A nota final do aluno é", notaFinal)