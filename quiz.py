import random
import time
import threading
import os

def restaurar():
    global perguntas
    perguntas = [
    {"tema":"Esportes","pergunta":"Qual a cor da primeira faixa do Jiu Jitsu?","resposta":["branca","branco"]},
    {"tema":"Animes","pergunta":"Cite uma das espadas que Kirito usa na sua primeira vez em modo dual-wield.","resposta":["dark repulser","elucidator"]},
    {"tema":"Música","pergunta":"Qual banda lançou o álbum 'Abbey Road'?","resposta":["the beatles","beatles"]},
    {"tema":"Geografia","pergunta":"Qual é o maior país do mundo em extensão territorial?","resposta":["rússia","russia"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual é o maior oceano do mundo?","resposta":["pacífico","oceano pacífico"]},
    {"tema":"Jogos","pergunta":"Qual é o reino principal de 'Zelda: Ocarina of Time'?","resposta":["hyrule","hirule"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual elemento tem símbolo 'Au' na tabela periodica?","resposta":["ouro","gold"]},
    {"tema":"Esportes","pergunta":"Há quantos jogadores em uma partida de futebol?","resposta":["22","vinte e dois"]},
    {"tema":"Animes","pergunta":"Quem é o protagonista do anime 'Naruto'?","resposta":["naruto uzumaki","naruto"]},
    {"tema":"Música","pergunta":"Quem é conhecido como o 'Rei do Pop'?","resposta":["michael jackson","mj"]},
    {"tema":"Geografia","pergunta":"Qual é a capital da França?","resposta":["paris"]},
    {"tema":"Filmes e Séries","pergunta":"Qual filme apresenta personagens chamados Woody e Buzz?","resposta":["toy story"]},
    {"tema":"Jogos","pergunta":"Quem é o principal mascote da Nintendo?","resposta":["mario","super mario"]},
    {"tema":"Esportes","pergunta":"Quantos sets são necessários para vencer um jogo de tênis masculino grand slam?","resposta":["3","5"]},
    {"tema":"Animes","pergunta":"Qual era o principal meio de locomoção do Goku quando ele era criança em 'Dragon Ball'?","resposta":["nuvem voadora","nuvem"]},
    {"tema":"Música","pergunta":"Qual cantora lançou o álbum '1989'?","resposta":["taylor swift"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual planeta é conhecido como Planeta Vermelho?","resposta":["marte"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do bruxo mais famoso da cultura pop?","resposta":["harry potter"]},
    {"tema":"Jogos","pergunta":"Qual jogo tem o protagonista chamado 'Link'?","resposta":["the legend of zelda","zelda"]},
    {"tema":"Geografia","pergunta":"Qual é o rio mais longo do mundo?","resposta":["amazonas"]},
    {"tema":"Esportes","pergunta":"Qual país sediou a Copa do Mundo de 2018?","resposta":["rússia","russia"]},
    {"tema":"Animes","pergunta":"Qual é o nome da vila onde Naruto cresceu?","resposta":["konoha","aldeia da folha", "vila da folha", "konohagakure"]},
    {"tema":"Música","pergunta":"Qual banda lançou a música 'Bohemian Rhapsody'?","resposta":["queen"]},
    {"tema":"Geografia","pergunta":"Qual é a capital do Japão?","resposta":["tóquio","tokyo"]},
    {"tema":"Filmes e Séries","pergunta":"Qual filme apresenta os personagens Simba, Mufasa e Scar?","resposta":["o rei leão","the lion king"]},
    {"tema":"Jogos","pergunta":"Qual o jogo battle royale mais popular do mundo atualmente?","resposta":["fortnite"]},
    {"tema":"Conhecimento Geral","pergunta":"Quem pintou a Mona Lisa?","resposta":["leonardo da vinci","da vinci"]},
    {"tema":"Esportes","pergunta":"Em qual esporte se pratica slam dunk?","resposta":["basquete","basketball"]},
    {"tema":"Animes","pergunta":"Qual é o nome do chefe da organização criminosa em 'One Piece' chamada 'Baroque Works'?","resposta":["crocodile"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do cientista que cria o DeLorean no filme 'De Volta para o Futuro'?","resposta":["doc brown","dr. brown","dr brown","emmett brown","emmett"]},
    {"tema":"Filmes e Séries","pergunta":"Em qual filme aparece o personagem Jack Sparrow?","resposta":["piratas do caribe","pirates of the caribbean"]},
    {"tema":"Jogos","pergunta":"Qual personagem é famoso por dizer 'It's-a me'?","resposta":["mario", "super mario"]},
    {"tema":"Esportes","pergunta":"Quantos pontos vale uma cesta de longe no basquete?","resposta":["3","três"]},
    {"tema":"Animes","pergunta":"Quem é o capitão dos Espadachins da Soul Society em 'Bleach'?","resposta":["byakuya kuchiki", "byakuya"]},
    {"tema":"Música","pergunta":"Qual cantor lançou o álbum 'Divide' em 2017?","resposta":["ed sheeran","sheeran"]},
    {"tema":"Conhecimento Geral","pergunta":"Quantos estados tem o Brasil?","resposta":["26","vinte e seis"]},
    {"tema":"Filmes e Séries","pergunta":"Qual série se passa na cidade de Hawkins e tem o monstro chamado Demogorgon?","resposta":["stranger things"]},
    {"tema":"Jogos","pergunta":"Qual jogo tem uma ilha chamada Koholint?","resposta":["link's awakening","zelda","the legend of zelda link's awakening","the legend of zelda"]},
    {"tema":"Geografia","pergunta":"Qual é o continente mais populoso do mundo?","resposta":["ásia","asia"]},
    {"tema":"Esportes","pergunta":"Qual país venceu a Copa do Mundo de 2014?","resposta":["alemanha","germany"]},
    {"tema":"Animes","pergunta":"Qual é o nome do protagonista de 'Death Note'?","resposta":["light yagami","light", "kira"]},
    {"tema":"Música","pergunta":"Quem cantou 'Shape of You'?","resposta":["ed sheeran","sheeran"]},
    {"tema":"Geografia","pergunta":"Qual é o menor país do mundo em extensão territorial?","resposta":["vaticano"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do parque temático em 'Jurassic Park'?","resposta":["jurassic park"]},
    {"tema":"Jogos","pergunta":"Qual personagem é o protagonista em 'Pokemon Fire Red'?","resposta":["red"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual é o maior planeta do sistema solar?","resposta":["júpiter","jupiter"]},
    {"tema":"Esportes","pergunta":"Em qual esporte se usa um bastão e uma bola chamada 'puck'?","resposta":["hóquei","hockey"]},
    {"tema":"Animes","pergunta":"Quem é o melhor amigo de Naruto e também é seu rival?","resposta":["sasuke uchiha","sasuke"]},
    {"tema":"Música","pergunta":"Qual banda lançou 'Stairway to Heaven'?","resposta":["led zeppelin","zeppelin"]},
    {"tema":"Geografia","pergunta":"Qual é o deserto mais seco do mundo?","resposta":["atacama"]},
    {"tema":"Filmes e Séries","pergunta":"Quem é o arqueólogo mais famoso da cultura pop?","resposta":["indiana jones","jones"]},
    {"tema":"Jogos","pergunta":"Em Minecraft, qual material é usado para criar uma crafting table/bancada de trabalho?","resposta":["madeira"]},
    {"tema":"Esportes","pergunta":"Quantos gols vale um gol olímpico?","resposta":["1"]},
    {"tema":"Animes","pergunta":"Qual é o nome do tripulante dos Chapéus de Palha que é atirador em 'One Piece'?","resposta":["usopp"]},
    {"tema":"Música","pergunta":"Quem cantou 'Rolling in the Deep'?","resposta":["adele"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual é a capital da Austrália?","resposta":["camberra","canberra"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do vilão de 'Os Vingadores' que usa a Manopla do Infinito?","resposta":["thanos"]},
    {"tema":"Jogos","pergunta":"Qual o primeiro jogo da franquia Super Mario em que Mario viaja entre galáxias?","resposta":["super mario galaxy", "mario galaxy"]},
    {"tema":"Geografia","pergunta":"Qual é o maior lago de água doce do mundo?","resposta":["superior","lago superior"]},
    {"tema":"Esportes","pergunta":"Qual país venceu a Copa do Mundo de 2002?","resposta":["brasil","brazil"]},
    {"tema":"Animes","pergunta":"Em 'Attack on Titan', qual é o nome do Titã Colossal?","resposta":["bertholdt","bertholdt hoover"]},
    {"tema":"Música","pergunta":"Qual cantora lançou o álbum 'Lemonade'?","resposta":["beyoncé","beyonce"]},
    {"tema":"Geografia","pergunta":"Qual é o menor continente em extensão territorial?","resposta":["oceania"]},
    {"tema":"Filmes e Séries","pergunta":"Qual filme de 1999 apresenta os personagens Neo e Morpheus?","resposta":["matrix"]},
    {"tema":"Jogos","pergunta":"Que objeto é o principal item do jogo 'The Legend of Zelda: Majora's Mask'?","resposta":["máscara"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual é o símbolo químico do ferro?","resposta":["fe"]},
    {"tema":"Esportes","pergunta":"Em que superficie se pratica o esporte 'curling'?","resposta":["gelo"]},
    {"tema":"Animes","pergunta":"Qual é o verdadeiro nome do personagem 'All Might' em 'My Hero Academia'?","resposta":["toshinori yagi","yagi"]},
    {"tema":"Música","pergunta":"Qual banda lançou o álbum 'In Utero'?","resposta":["nirvana"]},
    {"tema":"Geografia","pergunta":"Qual é a capital do Egito?","resposta":["cairo","caire"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do robô protagonista do filme 'WALL-E'?","resposta":["wall-e","walle"]},
    {"tema":"Jogos","pergunta":"Qual é o nome do jogo em que se constrói e explora mundos em blocos?","resposta":["minecraft"]},
    {"tema":"Esportes","pergunta":"Quantos pontos vale um touchdown no futebol americano?","resposta":["6","seis"]},
    {"tema":"Animes","pergunta":"Em 'One Piece', quem é o atual usuário da akuma no mi 'Mera Mera no Mi'?","resposta":["sabo"]},
    {"tema":"Música","pergunta":"Quem lançou a música 'Bad Guy'?","resposta":["billie eilish","billie"]},
    {"tema":"Conhecimento Geral","pergunta":"Qual é a unidade básica da vida?","resposta":["célula","celula"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do arqueólogo interpretado por Harrison Ford?","resposta":["indiana jones","jones"]},
    {"tema":"Jogos","pergunta":"Qual é o nome do reino em 'Kingdom Hearts'?","resposta":["destiny islands","destiny island"]},
    {"tema":"Geografia","pergunta":"Qual é o rio mais longo da África?","resposta":["nilo","nile"]},
    {"tema":"Jogos","pergunta":"Qual é o nome da cidade principal em 'GTA V'?","resposta":["los santos","los"]},
    {"tema":"Animes","pergunta":"Em 'One Piece', qual é o nome da akuma no mi que Luffy comeu?","resposta":["gomu gomu","gomu gomu no mi"]},
    {"tema":"Filmes e Séries","pergunta":"Quem é o diretor do filme 'Jurassic Park'?","resposta":["steven spielberg","spielberg"]},
    {"tema":"Jogos","pergunta":"Qual é o nome do protagonista do jogo 'Hades'?","resposta":["Zagreus","zagreus"]},
    {"tema":"Animes","pergunta":"Qual é o verdadeiro nome do Kira em Death Note?","resposta":["light yagami","light"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do personagem principal de 'Back to the Future'?","resposta":["marty mcfly","marty","mcfly"]},
    {"tema":"Jogos","pergunta":"Qual é o nome do protagonista masculino de 'The Last of Us'?","resposta":["joel","joel miller"]},
    {"tema":"Jogos","pergunta":"Qual é o nome da protagonista feminina de 'The Last of Us'?","resposta":["ellie","ellie williams"]},
    {"tema":"Filmes e Séries","pergunta":"Como é conhecido o assassino em série da franquia de filmes 'Pânico'?","resposta":["ghostface"]},
    {"tema":"Jogos","pergunta":"Qual jogo da Nintendo é conhecido como 'Mario de Futebol'?","resposta":["mario strikers"]},
    {"tema":"Animes","pergunta":"Como é chamado alguém com habilidades paranormais em 'Mob Psycho 100'?","resposta":["esper"]},
    {"tema":"Filmes e Séries","pergunta":"Em 'Matrix', qual personagem escolhe a pílula vermelha?","resposta":["neo"]},
    {"tema":"Animes","pergunta":"Qual é o usuário de Nen que cria a habilidade 'Bungee Gum'?","resposta":["hisoka morow","hisoka"]},
    {"tema":"Filmes e Séries","pergunta":"Quem é o capitão do time de quadribol da grifinória no ano em que Harry entra para o time?","resposta":["olivio","olivio wood"]},
    {"tema":"Animes","pergunta":"Qual é o verdadeiro nome do personagem conhecido como Chainsaw Man?","resposta":["denji"]},
    {"tema":"Jogos","pergunta":"Qual é o jogo que apresenta o personagem Geralt de Rivia?","resposta":["the witcher 3","the witcher"]},
    {"tema":"Animes","pergunta":"Qual é a arma principal de Kurapika em 'Hunter x Hunter'?","resposta":["correntes","corrente"]},
    {"tema":"Filmes e Séries","pergunta":"Qual é o nome do jovem hobbit que carrega o anel em 'O Senhor dos Anéis'?","resposta":["frodo bolseiro","frodo"]},
    {"tema":"Animes","pergunta":"Quem é o atacante conhecido como 'Lazy Genius' ou 'Gênio Preguiçoso' em Blue Lock?","resposta":["seishiro nagi","nagi"]},
    {"tema":"Animes","pergunta":"Qual é o nome do protagonista de 'Steins;Gate'?","resposta":["okabe rintarou","rintarou","okabe"]}
]
               
def limpar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
while True:
    restaurar()
    def start():
        global vida
        vida = 3
        global pontos
        pontos = 0
        print(f'''\nBem vindo ao 'Quiz Trívia'!
Você terá uma sequência de 100 perguntas e ganhará o jogo quando responder todas elas corretamente.
Você terá apenas 3 vidas, ou seja, você pode errar até duas vezes!
Agora, digite qualquer coisa para iniciarmos:\n''')
        comec = input()  
        limpar()
    start()

    def responder():
        global resp
        resp = input().lower()

    def quiz():
        limpar()
        print("Escolhendo pergunta...")
        time.sleep(1.5)
        global perguntasort
        global perguntas
        global pontos
        if perguntas==[]:
            limpar()
            print('''Parabéns, você conseguiu acertar todas as perguntas e zerar o jogo!
Saiba que pode jogar de novo sempre que quiser, viu?
Você é FODA!''')
            time.sleep(5)
            start()
        else:
            perguntasort = random.choice(perguntas)
            print(f'''Tema sorteado: {perguntasort["tema"]}
Pergunta sorteada: {perguntasort["pergunta"]}
Digite sua resposta!
Você tem apenas 15 segundos para responder.\n''')
            global resp
            resp = None
            t = threading.Thread(target=responder)
            t.start()
            t.join(timeout=15)

            if resp == None:
                global vida
                vida-=1
                print(f'''Tempo excedido!
-1 Vida... (Vidas atuais: {vida})\n''')
                time.sleep(2)
                if vida==0:
                    print('''GAME OVER!
Você perdeu todas as suas vidas...
Mas lembre-se, você sempre pode tentar de novo!''')
                    time.sleep(5)
                    start()
                else:
                    print("Você tem 5 segundos de descanso... Esperando...")
                    time.sleep(5)
                    limpar()
                    quiz()
            elif resp in perguntasort["resposta"]:
                pontos+=1
                print(f'''Parabéns, você acertou a resposta!
+1 Ponto (Pontos atuais: {pontos})
Vidas atuais: {vida}\n''')
                perguntas.remove(perguntasort)
                time.sleep(2)
                print("Você tem 5 segundos de descanso... Esperando...")
                time.sleep(5)
                limpar()
                quiz()
            else:
                vida-=1
                print(f'''Infelizmente você errou a resposta...
-1 Vida... (Vidas atuais: {vida})\n''')
                time.sleep(2)
                if vida==0:
                    limpar()
                    print('''GAME OVER!
Você perdeu todas as suas vidas...
Mas lembre-se, você sempre pode tentar de novo!''')
                    time.sleep(5)
                    start()
                else:
                    print("Você tem 5 segundos de descanso... Esperando...")
                    time.sleep(5)
                    limpar()
                    quiz()
    quiz()          