"""
Módulo Collections - Counter

Collections -> High-Performance Container Dateatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o
elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elmento.

# Realizando o import
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui utilizamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 2: 5, 3: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou
# valor a quantidade de ocorrências.

# Exemplo 2
print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

# Realizando o import
from collections import Counter

# Exemplo 3
text = """
Em 1942, assumiu a presidência do Vasco da Gama Cyro Aranha. Naquela época, o clube não ganhava qualquer título dentro da cidade do Rio de Janeiro há cinco anos. Tentando reverter essa situação, Cyro adotou uma política de longo prazo, baseada na contratação de jovens jogadores. Foi assim que chegaram o goleiro Barbosa, o atacante Ademir de Menezes, os meias Jair, Lelé, Isaías, Ely e Djalma e o ponta Chico. O técnico era o uruguaio Ondino Viera que adotou o 4-2-4 como esquema da equipe.[2][3]


O atacante Ademir de Menezes, líder do Expresso da Vitória, marcou 301 gols com a camisa cruzmaltina.[4][5]
O primeiro título veio em 1944, com a vitória no Torneio Relâmpago. Ainda na mesma temporada, o elenco conquistaria os Torneios Início e Municipal. No Campeonato Carioca, o Expresso chegou à última rodada empatado em pontos com o Flamengo. No final do jogo decisivo, o jogador rubro-negro Valido marcou de cabeça o único gol da partida, gerando discussões posteriormente. O atacante teria se apoiado no zagueiro vascaíno Argemiro para cabecear. Contudo, o gol foi validado e o time cruzmaltino acabou como vice-campeão.[6][7]

No ano de 1945, o time continuou a ganhar mais títulos. O clube foi bicampeão dos Torneios Início e Municipal e campeão Carioca invicto (com treze vitórias e cinco empates), o primeiro desde a era do profissionalismo. Neste carioca, o elenco vascaíno produziu diversas goleadas, chegando a 58 gols marcados na competição e 15 sofridos ao total de dezoito jogos. O time base era composto por Rodrigues, Augusto e Rafanelli, Berascochea, Ely e Argemiro, Djalma, Ademir de Menezes, Lelé, Isaías e Jair da Rosa Pinto.[8] Esta campanha levou a um cantor, num programa musical da Rádio Nacional, ao se apresentar, a dizer que dedicaria uma música ao Vasco, chamado por ele de "Expresso da Vitória", por atropelar seus adversários em campo, com a alcunha se popularizando então.[9][3]

Em 1946, o Vasco perdeu seu principal atacante: Ademir de Menezes, que foi para Fluminense. Além dele, saía o uruguaio Ondino Viera para o Botafogo e assumia o técnico português Ernesto dos Santos. Mesmo com os desfalques, o Expresso ainda ganhou naquele ano os Torneios Relâmpago e Municipal. Neste, estreava Barbosa, considerado por muitos o maior goleiro vascaíno de todos os tempos.[10][11] No Carioca, contudo, o time não passou do quinto lugar.[12]

Em 1947, assumiu o técnico Flávio Costa, tricampeão em 1942, 1943 e 1944 pelo Flamengo, assumindo no lugar de Ernesto. Naquele ano, o time foi tetracampeão do Torneio Municipal, mais uma vez campeão Carioca invicto e conquistou a Taça Centenários, ao bater por 4-3 o Combinado Sporting, Benfica e Belenenses em amistoso no Estádio Nacional de Lisboa.[13] O grande destaque da temporada foi o ataque vascaíno, composto por Djalma, Maneca, Friaça, Lelé e Chico. No Torneio Municipal foram 40 gols em 10 jogos; no campeonato estadual o time marcou 68 vezes em 20 jogos.[14] Neste, o elenco perpetrou diversas goleadas, se destacando os 14-1 sobre o Canto do Rio, maior placar da era profissional do futebol carioca.[13][15]

Torneio dos Campeões Sul-Americanos
Ver artigo principal: Campeonato Sul-Americano de Campeões de 1948
Em 18 de dezembro de 1947, o Vasco recebeu o convite oficial para a disputa do Campeonato Sul-Americano de Campeões, em Santiago, organizado pelo clube chileno Colo-Colo. Além do Vasco e do organizador, outros cinco clubes estavam presentes na competição: o Nacional, campeão uruguaio de 1947; o Municipal, vice-campeão peruano no mesmo ano; o Litoral, campeão de La Paz em 1947; o Emelec, a convite do anfitrião; e o River Plate, bicampeão argentino em 1941 e 42, campeão em 1945 e novamente em 1947. Este último era tido como o favorito do torneio, tendo amplo domínio sobre o futebol argentino na década de 40, o time do River, apelidado de La Máquina (A Máquina), tinha como grande estrela Di Stéfano, tido como o melhor jogador do mundo em sua época, enquanto o elenco argentino era apontado como o grande esquadrão sul-americano. O Nacional também era apontado como favorito ao título, ao contrário do Vasco que não gozava de tal prestígio no âmbito do jornalismo internacional.[16][17][18]
"""
palavras = text.split()

# Encontrando as 5 palavras com mais ocorrência no texto
print(Counter(palavras).most_common(5))