programa
{
	funcao inicio()
	{
		inteiro Idade, Idade_Acomp
		escreva(" Bem vindo ao open DBA")
		escreva("\nQuantos anos você tem? ")
		leia(Idade)

		escreva("Você tem ",Idade," anos")

		se	(Idade < 15)
			{escreva("\nVocê não tem permissão para entrar nesse local.")}
			senao{
				se(Idade >= 16 e Idade < 18)
					{escreva("\nVocê precisa de um acompanhante para entrar nesse local")}
			senao
				{escreva(" e não precisa de um acompanhante para entrar, seja bem vindo.")}		
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 490; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */