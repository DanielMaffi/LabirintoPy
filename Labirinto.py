from pyamaze import maze, agent, textLabel

#maze(5,5) tamnanho do labirinto 5X5
labirinto = maze(100, 100)

#Local a 5X5 onde o final do labirinto vai começar
#labirinto.CreateMaze(5, 5)

#Salva um arquivo CSV do labirinto
#labirinto.CreateMaze(SaveMaze=True)

#Carrega o labirinto que foi salvo no codigo anterior
#labirinto.CreateMaze(loadMaze="Labirinto.csv")

#Gera um labirindo com mais espacos para passar livro
#Quanto maior o numero mais caminhos para chegar ao caminho final
#O padrao e 0
#labirinto.CreateMaze(loopPercent=50)

#Cria o labirindo padrao sem configuracao
labirinto.CreateMaze()

#labirinto.grid mede as celulas do labiirinto 
celulas = labirinto.grid
print(celulas)

#Mosta as posicoes e mostra se e possivel ir para norte sul lesta ou oeste
mapa = labirinto.maze_map
print(mapa)

#Mostra o caminho perfeito que alguem teria que fazer para chegar ao objetivo  
caminhoGabarito = labirinto.path
print(caminhoGabarito)

#Gera um "agente" (pontinho) no labirindo que voce pode usar para controla-lo
#Os  proximos parametros mostra onde que ele vai começar
#agente = agent(labirinto, 7, 10)

#O parametro fillded=True vai preencher o quadrado a onde esta o agente 
#agente = agent(labirinto, 7, 10, filled=True)

#O parametro footprints=True mostra o caminho que o agente percorreu
#agente = agent(labirinto, 7, 10, footprints=True)

agente = agent(labirinto, filled=True, footprints=True)

#agente.position mostra a posicao do agente
#posicao = agente.positon
#print(posicao)

#Tambem e possivel altear a posicao do agente
#agente.position = (10,9)

#Criando um caminho do tipo dicionario passando o caminho que o agente vai percorrer
#A as chaves do dicionario e onde o agente esta antes de fazer o movimento e o resultado e para onde ele vai
#caminho = {(10, 10): (10, 9), (10, 9): (10, 8), (10,8): (9,8)}

#OUTRA FORMA DE FAZER O CAMINHO E POR TEXTO
#No caso estou passaondo que ele vai para o norte(north) uma vez depois para o oeste(West), sul(south) e por ultimo leste(east)
#caminho ="NWSE"

#Executando o medodo que faz o agente seguir o caminho 
#O primeiro parametro e o objeto seguido de (Dois pontos) : logo depois o caminho
#O parametro delay mostra quando tempo que ele vai fazer de caminho a cada caminho padrao e delay = 300
#labirinto.tracePath({agente: caminho}, delay=600)

#E possivel passar o caminhoGabrito para ele ir ate o final
labirinto.tracePath({agente: caminhoGabarito}, delay=100)

#textLabel faz aparece um texto no objeto labirinto que voce passou e com o titulo que voce pasosu em title 
#Em seguida o value com o tamanho do numero que voce quer mostrar no caso estou passando o lenque e um medoto que mostra o tamanho 
texto = textLabel(labirinto,title="N passos", value=len(caminhoGabarito))

labirinto.run()