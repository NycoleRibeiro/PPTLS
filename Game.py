import pygame
import animjokenpo
import animregras
import animperdedor
import animvencedor
import os.path
import random

# Nycole Ribeiro
# Juan Pablo


class Jogo:
    def __init__(self, t_partidas=True, t_nome=False, t_escolha=False,
                 t_placar=False):
        self.t_partidas = t_partidas
        self.t_nome = t_nome
        self.t_escolha = t_escolha
        self.t_placar = t_placar

    def cont(self, lista, jog, pc):
        if len(lista) == 0:
            return jog, pc
        else:
            if lista[0] == "jogador":
                jog += 1
            elif lista[0] == "pc":
                pc += 1
            return self.cont(lista[1:], jog, pc)

    def efeitoSound(self, efeito):
        # Efeito sonoro do botão do Play da segunda tela
        posMusica = pygame.mixer.music.get_pos()
        posMusica = posMusica / 1000
        pygame.mixer.music.load(efeito)
        pygame.mixer.music.play()
        pygame.time.wait(200)
        pygame.mixer.music.load("sounds/rockytheme.mp3")
        pygame.mixer.music.play(-1, posMusica)

    def sortear(self, opc):
        # foi chamada dentro da função escolha(), dentro do if jogador != ''
        if os.path.exists("data/"+player+".txt"):
            arc = open("data/"+player+".txt", "r+")
            content = arc.readline()
            arc.close()

            content = content.split(" => ")
            esc = content[4]
            esc = esc.split(": ")

            if len(esc) > 1:
                c_pedra = 0
                c_tesoura = 0
                c_lagarto = 0
                c_spock = 0
                c_papel = 0

                l = []
                esco = esc[1]
                l2 = esco.split(", ")
                if len(l2) > 10:

                    for j in range(0, len(l2)):
                        if l2[j] == "pedra":
                            c_pedra += 1
                        elif l2[j] == "papel":
                            c_papel += 1
                        elif l2[j] == "spock":
                            c_spock += 1
                        elif l2[j] == "lagarto":
                            c_lagarto += 1
                        else:
                            c_tesoura += 1
                    # regra de tres para determinar a porcentagem aproximada
                    # de cada item na lista
                    tesoura = int(c_tesoura)*100 / len(l2)
                    tesoura = int(tesoura)
                    papel = int(c_papel)*100 / len(l2)
                    papel = int(papel)
                    spock = int(c_spock)*100 / len(l2)
                    spock = int(spock)
                    lagarto = int(c_lagarto)*100 / len(l2)
                    lagarto = int(lagarto)
                    pedra = int(c_pedra)*100 / len(l2)
                    pedra = int(pedra)

                    # resultado da regra divido por 2, pois cada item contem
                    # 2 fraquezas que precisam ser escritas em mesma
                    # quantidade na lista
                    p_tesoura = int(tesoura / 2)
                    p_pedra = int(pedra / 2)
                    p_spock = int(spock / 2)
                    p_lagarto = int(lagarto / 2)
                    p_papel = int(papel / 2)

                    # escreve na lista conforme necessidade
                    for i in range(0, p_tesoura):
                        l.append("spock")
                        l.append("pedra")

                    for i in range(0, p_pedra):
                        l.append("papel")
                        l.append("spock")

                    for i in range(0, p_spock):
                        l.append("lagarto")
                        l.append("papel")

                    for i in range(0, p_lagarto):
                        l.append("pedra")
                        l.append("tesoura")

                    for i in range(0, p_papel):
                        l.append("tesoura")
                        l.append("lagarto")

                    num = random.randint(0, len(l))
                    pc = l[num]
                else:
                    num = random.randint(0, 4)
                    pc = opc[num]
            else:
                num = random.randint(0, 4)
                pc = opc[num]
        else:
            num = random.randint(0, 4)
            pc = opc[num]
        return pc

    def texto(self, msg, cor, tam, left, top):
        # Função pra exibir string na tela
        font = pygame.font.SysFont("SegoeUI", tam)
        texto1 = font.render(msg, True, cor)
        screen.blit(texto1, [left, top])

    def partidas(self):
        # Tela onde o usuário escolhe o número de partidas
        done = False
        global num_part

        while not done:
            bg = pygame.image.load("imagens/Tela_Partidas.jpg")
            screen.blit(bg, (0, 0))
            mouse = pygame.mouse.get_pos()

            # Botões mudando de cor quando passa o cursor do mouse por cima

            # Botão 1 partida
            if 125+110 > mouse[0] > 125 and 250+105 > mouse[1] > 250:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and
                # (CoorTop+Altura > PosMouseY > CoorTop)
                self.texto("1", cores["azul"], 50, 125+45, 250+15)
            else:
                self.texto("1", cores["branco"], 50, 125+45, 250+15)

            # Botão 2 partidas
            if 295+110 > mouse[0] > 295 and 250+105 > mouse[1] > 250:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and
                # (CoorTop+Altura > PosMouseY > CoorTop)
                self.texto("2", cores["azul"], 50, 295+45, 250+15)
            else:
                self.texto("2", cores["branco"], 50, 295+45, 250+15)

            # Botão 3 partidas
            if 465+110 > mouse[0] > 465 and 250+105 > mouse[1] > 250:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and
                # (CoorTop+Altura > PosMouseY > CoorTop)
                self.texto("3", cores["azul"], 50, 465+45, 250+15)
            else:
                self.texto("3", cores["branco"], 50, 465+45, 250+15)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    jogando = False
                    return jogando
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vai atribuir a variavel "num_part" o número que o
                    # jogador clicar
                    mouse = pygame.mouse.get_pos()
                    if 125+110 > mouse[0] > 125 and 250+105 > mouse[1] > 250:
                        num_part = 1

                    elif 295+110 > mouse[0] > 295 and 250+105 > mouse[1] > 250:
                        num_part = 2

                    elif 465+110 > mouse[0] > 465 and 250+105 > mouse[1] > 250:
                        num_part = 3

                    if num_part > 0:
                        print(f"Nº de partidas escolhido: {num_part}")
                        done = True
                        jogando = True
                        return jogando
            pygame.display.flip()

    def inputbox(self):
        # Tela onde o usuário irá digitar seu nome
        bg = pygame.image.load("imagens/Tela_Nome.jpg")
        font = pygame.font.SysFont(None, 48)
        input_box = pygame.Rect(245, 225, 465-245, 270-225)  # left, top, largura, altura
        text = ''
        global player
        global nome  # Variavel que receberá o nome digitado
        # active = True
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    jogando = False
                    return jogando
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()

                    # Para quando o usuário clicar no botão Play
                    if 615+75 > mouse[0] > 615 and 415+75 > mouse[1] > 415:
                        # (CoorLeft+largura > PosMouseX > CoorLeft) and (CoorTop+Altura > PosMouseY > CoorTop)
                        print(f"Nome do jogador: {text}")
                        nome.append(text)
                        player = nome[0].upper()
                        self.efeitoSound("sounds/Blup2.mp3")
                        done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if done:
                    jogando = True
                    return jogando

            txt_surface = font.render(text, True, cores["preto"])

            screen.blit(bg, (0, 0))
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

            pygame.display.flip()

    def escolha(self):
        # Tela de escolha do usuário
        opcoes = {"nada": pygame.image.load("imagens/Opcoes.png"),
                  "Pedra": pygame.image.load("imagens/OpcoesPedra.png"),
                  "Papel": pygame.image.load("imagens/OpcoesPapel.png"),
                  "Tesoura": pygame.image.load("imagens/OpcoesTesoura.png"),
                  "Lagarto": pygame.image.load("imagens/OpcoesLagarto.png"),
                  "Spock": pygame.image.load("imagens/OpcoesSpock.png")}
        jogador = ''
        global num_part
        global vencedor
        opc = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
        Pedra = pygame.Rect(140, 154, 87, 89)  # left, top, largura, altura
        Papel = pygame.Rect(225, 220, 87, 89)
        Tesoura = pygame.Rect(195, 322, 87, 89)
        Lagarto = pygame.Rect(88, 322, 87, 89)
        Spock = pygame.Rect(55, 220, 87, 89)
        ajuda = pygame.Rect(660, 5, 35, 35)
        bg = pygame.image.load("imagens/Tela_Escolha2.jpg")
        screen.blit(bg, (0, 0))
        done = False

        while not done:
            mouse = pygame.mouse.get_pos()
            # Passando o mouse por cima troca a cor dos icones

            # Pedra
            if 140+87 > mouse[0] > 140 and 154+89 > mouse[1] > 154:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and (CoorTop+Altura > PosMouseY > CoorTop)
                screen.blit(opcoes["Pedra"], (40, 140))

            # Papel
            elif 225+87 > mouse[0] > 225 and 220+89 > mouse[1] > 220:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and (CoorTop+Altura > PosMouseY > CoorTop)
                screen.blit(opcoes["Papel"], (40, 140))

            # Tesoura
            elif 195+87 > mouse[0] > 195 and 322+89 > mouse[1] > 322:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and (CoorTop+Altura > PosMouseY > CoorTop)
                screen.blit(opcoes["Tesoura"], (40, 140))

            # Lagarto
            elif 88+87 > mouse[0] > 88 and 322+89 > mouse[1] > 322:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and (CoorTop+Altura > PosMouseY > CoorTop)
                screen.blit(opcoes["Lagarto"], (40, 140))

            # Spock
            elif 55+87 > mouse[0] > 55 and 220+89 > mouse[1] > 220:
                # (CoorLeft+largura > PosMouseX > CoorLeft) and (CoorTop+Altura > PosMouseY > CoorTop)
                screen.blit(opcoes["Spock"], (40, 140))

            else:
                screen.blit(opcoes["nada"], (40, 140))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogando = False
                    return jogando

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vai atribuir a variavel "jogador" a opção escolhida pelo usuário
                    if ajuda.collidepoint(event.pos):
                        animregras.main2(imagens)
                        bg = pygame.image.load("imagens/Tela_Escolha2.jpg")
                        screen.blit(bg, (0, 0))
                    if Pedra.collidepoint(event.pos):
                        jogador = "pedra"
                        escolhas_jogador.append("pedra")
                    if Papel.collidepoint(event.pos):
                        jogador = "papel"
                        escolhas_jogador.append("papel")
                    if Tesoura.collidepoint(event.pos):
                        jogador = "tesoura"
                        escolhas_jogador.append("tesoura")
                    if Lagarto.collidepoint(event.pos):
                        jogador = "lagarto"
                        escolhas_jogador.append("lagarto")
                    if Spock.collidepoint(event.pos):
                        jogador = "spock"
                        escolhas_jogador.append("spock")
                    if jogador != '':
                        pc = self.sortear(opc)
                        print(f"PC escolheu: {pc}")
                        print(f"Jogador escolheu: {jogador}")
                        print(f"Faltam {num_part - 1} partidas")
                        animjokenpo.main2()
                        self.resultado(jogador, pc, vencedor)

                        if num_part == 1:
                            # finaliza a tela de escolha, fim das partidas
                            done = True
                            playing = True
                            return playing
                        else:
                            # vai repetir a tela de escolha caso o número de partidas não tenha acabado
                            num_part -= 1
                            jogador = ''
                            bg = pygame.image.load("imagens/Tela_Escolha2.jpg")
                            screen.blit(bg, (0, 0))

            pygame.display.flip()

    def resultado(self, jogador, pc, vencedor):
        # Tela de resultado de cada partida
        escolha = {"Pedra": pygame.image.load("imagens/Pedra.png"),
                   "Papel": pygame.image.load("imagens/Papel.png"),
                   "Tesoura": pygame.image.load("imagens/Tesoura.png"),
                   "Lagarto": pygame.image.load("imagens/Lagarto.png"),
                   "Spock": pygame.image.load("imagens/Spock.png")}
        bg = pygame.image.load("imagens/Tela_Resultado.jpg")
        screen.blit(bg, (0, 0))
        pygame.display.flip()

        # condições de vitória, qm ganha é acrescentado a lista "vencedor" para a contagem no placar final
        if (jogador == "pedra"):
            screen.blit(escolha["Pedra"], (115, 140))

            if (pc == "pedra"):
                print("Empate")
                vencedor.append("Empate")
                screen.blit(escolha["Pedra"], (440, 140))
                self.texto("Empate!", cores["branco"], 50, 250, 380)

            elif (pc == "papel"):
                print("Papel cobre Pedra")
                vencedor.append("pc")
                screen.blit(escolha["Papel"], (440, 140))
                self.texto("Papel cobre pedra", cores["branco"], 50, 155, 380)

            elif (pc == "tesoura"):
                print("Pedra quebra Tesoura")
                vencedor.append("jogador")
                screen.blit(escolha["Tesoura"], (440, 140))
                self.texto("Pedra quebra tesoura", cores["branco"], 50, 120, 380)

            elif (pc == "lagarto"):
                print("Pedra derruba Lagarto")
                vencedor.append("jogador")
                screen.blit(escolha["Lagarto"], (440, 140))
                self.texto("Pedra derruba lagarto", cores["branco"], 50, 120, 380)

            elif (pc == "spock"):
                print("Spock vaporiza Pedra")
                vencedor.append("pc")
                screen.blit(escolha["Spock"], (440, 140))
                self.texto("Spock vaporiza pedra", cores["branco"], 50, 120, 380)

            pygame.display.flip()

        elif (jogador == "papel"):
            screen.blit(escolha["Papel"], (115, 140))

            if (pc == "pedra"):
                print("Papel cobre Pedra")
                vencedor.append("jogador")
                screen.blit(escolha["Pedra"], (440, 140))
                self.texto("Papel cobre pedra", cores["branco"], 50, 155, 380)

            elif (pc == "papel"):
                print("Empate")
                vencedor.append("Empate")
                screen.blit(escolha["Papel"], (440, 140))
                self.texto("Empate!", cores["branco"], 50, 250, 380)

            elif (pc == "tesoura"):
                print("Tesoura corta Papel")
                vencedor.append("pc")
                screen.blit(escolha["Tesoura"], (440, 140))
                self.texto("Tesoura corta papel", cores["branco"], 50, 125, 380)

            elif (pc == "lagarto"):
                print("Lagarto come Papel")
                vencedor.append("pc")
                screen.blit(escolha["Lagarto"], (440, 140))
                self.texto("Lagarto come papel", cores["branco"], 50, 150, 380)

            elif (pc == "spock"):
                print("Papel refuta Spock")
                vencedor.append("jogador")
                screen.blit(escolha["Spock"], (440, 140))
                self.texto("Papel refuta Spock", cores["branco"], 50, 120, 380)

        elif (jogador == "tesoura"):
            screen.blit(escolha["Tesoura"], (115, 140))

            if (pc == "pedra"):
                print("Pedra quebra Tesoura")
                vencedor.append("pc")
                screen.blit(escolha["Pedra"], (440, 140))
                self.texto("Pedra quebra tesoura", cores["branco"], 50, 120, 380)

            elif (pc == "papel"):
                print("Tesoura corta Papel")
                vencedor.append("jogador")
                screen.blit(escolha["Papel"], (440, 140))
                self.texto("Tesoura corta papel", cores["branco"], 50, 125, 380)

            elif (pc == "tesoura"):
                print("Empate")
                vencedor.append("Empate")
                screen.blit(escolha["Tesoura"], (440, 140))
                self.texto("Empate!", cores["branco"], 50, 250, 380)

            elif (pc == "lagarto"):
                print("Tesoura prende Lagarto")
                vencedor.append("jogador")
                screen.blit(escolha["Lagarto"], (440, 140))
                self.texto("Tesoura prende lagarto", cores["branco"], 50, 125, 380)

            elif (pc == "spock"):
                print("Spock derrete Tesoura")
                vencedor.append("pc")
                screen.blit(escolha["Spock"], (440, 140))
                self.texto("Spock derrete tesoura", cores["branco"], 50, 120, 380)

        elif (jogador == "lagarto"):
            screen.blit(escolha["Lagarto"], (115, 140))

            if (pc == "pedra"):
                print("Pedra derruba Lagarto")
                vencedor.append("pc")
                screen.blit(escolha["Pedra"], (440, 140))
                self.texto("Pedra derruba lagarto", cores["branco"], 50, 120, 380)

            elif (pc == "papel"):
                print("Lagarto come Papel")
                vencedor.append("jogador")
                screen.blit(escolha["Papel"], (440, 140))
                self.texto("Lagarto come papel", cores["branco"], 50, 150, 380)

            elif (pc == "tesoura"):
                print("Tesoura prende Lagarto")
                vencedor.append("pc")
                screen.blit(escolha["Tesoura"], (440, 140))
                self.texto("Tesoura prende lagarto", cores["branco"], 50, 125, 380)

            elif (pc == "lagarto"):
                print("Empate")
                vencedor.append("Empate")
                screen.blit(escolha["Lagarto"], (440, 140))
                self.texto("Empate!", cores["branco"], 50, 250, 380)

            elif (pc == "spock"):
                print("Lagarto adormece Spock")
                vencedor.append("jogador")
                screen.blit(escolha["Spock"], (440, 140))
                self.texto("Lagarto adormece Spock", cores["branco"], 50, 115, 380)

        elif (jogador == "spock"):
            screen.blit(escolha["Spock"], (115, 140))

            if (pc == "pedra"):
                print("Spock vaporiza Pedra")
                vencedor.append("jogador")
                screen.blit(escolha["Pedra"], (440, 140))
                self.texto("Spock vaporiza pedra", cores["branco"], 50, 120, 380)

            elif (pc == "papel"):
                print("Papel refuta Spock")
                vencedor.append("pc")
                screen.blit(escolha["Papel"], (440, 140))
                self.texto("Papel refuta Spock", cores["branco"], 50, 125, 380)

            elif (pc == "tesoura"):
                print("Spock derrete Tesoura")
                vencedor.append("jogador")
                screen.blit(escolha["Tesoura"], (440, 140))
                self.texto("Spock derrete tesoura", cores["branco"], 50, 120, 380)

            elif (pc == "lagarto"):
                print("Lagarto adormece Spock")
                vencedor.append("pc")
                screen.blit(escolha["Lagarto"], (440, 140))
                self.texto("Lagarto adormece Spock", cores["branco"], 50, 115, 380)

            elif (pc == "spock"):
                print("Empate")
                vencedor.append("Empate")
                screen.blit(escolha["Spock"], (440, 140))
                self.texto("Empate!", cores["branco"], 50, 250, 380)

        pygame.display.flip()
        pygame.time.wait(3500)  # tempo que fica aparecendo as opções
        # escolhidas na tela até passar para proxima partida ou
        # tela final: 3.5 segundos

    def placar(self):
        # Tela de Placar Final, pontuação total Jogador / pontuação total Pc
        # Fica na tela até o usuário fechar o jogo
        global vencedor
        global nome
        nome = nome[0].upper()
        jog = 0
        pc = 0
        plac = self.cont(vencedor, jog, pc)
        placar_jog = plac[0]
        placar_pc = plac[1]
        c_vit = 0
        c_der = 0
        c_emp = 0

        # Prints no terminal de qm venceu
        if (placar_jog) > (placar_pc):
            print(f"{nome} VENCEU O JOGO!")
            print(f"{nome} {vencedor.count('jogador')} X {vencedor.count('pc')} PC")
            animvencedor.main2()
            c_vit += 1
        elif (placar_pc) > (placar_jog):
            print(f"O COMPUTADOR VENCEU O JOGO!")
            print(f"{nome} {vencedor.count('jogador')} X {vencedor.count('pc')} PC")
            animperdedor.main2()
            c_der += 1
        else:
            print("EMPATOU!")
            c_emp += 1

        if os.path.exists("data/"+nome+".txt"):
            arc = open("data/"+nome+".txt", "r+")
            content = arc.readline()
            arc.close()
        else:
            arc = open("data/"+nome+".txt", "w+")
            content = "Player: "+nome+" => Vitorias: 0 => Derrotas: 0 => Empates: 0 => Escolhas: "
            arc.close()

        content = content.split(" => ")
        vit = content[1]
        der = content[2]
        emp = content[3]
        esc = content[4]
        vit = vit.split(": ")
        der = der.split(": ")
        emp = emp.split(": ")
        esc = esc.split(": ")
        vic = int(vit[1])
        derr = int(der[1])
        empt = int(emp[1])
        esco = esc[1]
        lista_escolhas = esco.split(", ")
        r_vit = str(vic + c_vit)
        r_der = str(derr + c_der)
        r_emp = str(empt + c_emp)
        for k in range(0, len(escolhas_jogador)):
            lista_escolhas.append(escolhas_jogador[k])
        n_esc = ", ".join(lista_escolhas)
        arc = open("data/"+nome+".txt", "w")
        arc.write("Player: "+nome+" => Vitorias: "+r_vit+" => Derrotas: "+r_der+" => Empates: "+r_emp+" => Escolhas: "+n_esc)
        arc.close()
        print("::::Pontuacao Partida::::\n"+nome+":\nVitorias: "+str(c_vit)+"\nDerrotas: "+str(c_der)+"\nEmpates: "+str(c_emp))
        print("::::Pontuacao Geral::::\n"+nome+":\nVitorias: "+r_vit+"\nDerrotas: "+r_der+"\nEmpates: "+r_emp)

        PlayAgain_btn = pygame.Rect(255, 395, 185, 75)  # left, top, largura, altura
        bg = pygame.image.load("imagens/Tela_Placar1.jpg")
        screen.blit(bg, (0, 0))
        pygame.display.flip()
        done = False

        # Redimensionando nome do usuário
        if len(nome) <= 2:
            tam_nome = 40
            left = 195
        elif 2 < len(nome) <= 4:
            tam_nome = 40
            left = 170
        else:
            tam_nome = 40 - (len(nome) - 4)*3
            left = 170 - (len(nome) - 4)*3

        # Escrevendo na tela Nomes e Placar
        self.texto(nome, cores["branco"], tam_nome, left, 160)
        self.texto(str(placar_jog), cores["branco"], 50, 205, 240)
        self.texto("PC", cores["branco"], 40, 455, 160)
        self.texto(str(placar_pc), cores["branco"], 50, 465, 240)
        pygame.display.flip()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogando = False
                    return jogando
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PlayAgain_btn.collidepoint(event.pos):
                        return "jogar dnv"


def main(start):
    jogando = True
    clock = pygame.time.Clock()

    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando = False

            # Tela 1: Qtd de Partidas
            if start.t_partidas:
                jogando = start.partidas()
                start = Jogo(False, True)

            # Tela 2: Nome do Usuário
            if jogando:
                if start.t_nome:
                    jogando = start.inputbox()
                    start = Jogo(False, False, True)

            # Tela 3: Escolhas
            if jogando:
                if start.t_escolha:
                    jogando = start.escolha()
                    start = Jogo(False, False, False, True)
                # Tela 4: Placar Final
                if jogando:
                    if start.t_placar:
                        jogando = start.placar()
                        if jogando == "jogar dnv":
                            game = jogando
                            return game
                        else:
                            game = "bye"
                            return game

        clock.tick(30)


pygame.init()

# Dicionário dos RGB das cores
cores = {"branco": (255, 255, 255),
         "azul": (108, 194, 236),
         "verde": (152, 231, 114),
         "preto": (0, 0, 0),
         "cinzadark": (78, 78, 78)}

# Carregamento dos frames de ajuda
imagens = [pygame.image.load("animacoes/regras/regras (1).jpg"),
           pygame.image.load("animacoes/regras/regras (2).jpg"),
           pygame.image.load("animacoes/regras/regras (3).jpg"),
           pygame.image.load("animacoes/regras/regras (4).jpg"),
           pygame.image.load("animacoes/regras/regras (5).jpg"),
           pygame.image.load("animacoes/regras/regras (6).jpg"),
           pygame.image.load("animacoes/regras/regras (7).jpg"),
           pygame.image.load("animacoes/regras/regras (8).jpg"),
           pygame.image.load("animacoes/regras/regras (9).jpg"),
           pygame.image.load("animacoes/regras/regras (10).jpg"),
           pygame.image.load("animacoes/regras/regras (11).jpg"),
           pygame.image.load("animacoes/regras/regras (12).jpg"),
           pygame.image.load("animacoes/regras/regras (13).jpg"),
           pygame.image.load("animacoes/regras/regras (14).jpg"),
           pygame.image.load("animacoes/regras/regras (15).jpg"),
           pygame.image.load("animacoes/regras/regras (16).jpg"),
           pygame.image.load("animacoes/regras/regras (17).jpg"),
           pygame.image.load("animacoes/regras/regras (18).jpg"),
           pygame.image.load("animacoes/regras/regras (19).jpg"),
           pygame.image.load("animacoes/regras/regras (20).jpg"),
           pygame.image.load("animacoes/regras/regras (21).jpg"),
           pygame.image.load("animacoes/regras/regras (22).jpg"),
           pygame.image.load("animacoes/regras/regras (23).jpg"),
           pygame.image.load("animacoes/regras/regras (24).jpg"),
           pygame.image.load("animacoes/regras/regras (25).jpg"),
           pygame.image.load("animacoes/regras/regras (26).jpg"),
           pygame.image.load("animacoes/regras/regras (27).jpg"),
           pygame.image.load("animacoes/regras/regras (28).jpg"),
           pygame.image.load("animacoes/regras/regras (29).jpg"),
           pygame.image.load("animacoes/regras/regras (30).jpg"),
           pygame.image.load("animacoes/regras/regras (31).jpg"),
           pygame.image.load("animacoes/regras/regras (32).jpg"),
           pygame.image.load("animacoes/regras/regras (33).jpg"),
           pygame.image.load("animacoes/regras/regras (34).jpg"),
           pygame.image.load("animacoes/regras/regras (35).jpg"),
           pygame.image.load("animacoes/regras/regras (36).jpg"),
           pygame.image.load("animacoes/regras/regras (37).jpg"),
           pygame.image.load("animacoes/regras/regras (38).jpg"),
           pygame.image.load("animacoes/regras/regras (39).jpg"),
           pygame.image.load("animacoes/regras/regras (40).jpg"),
           pygame.image.load("animacoes/regras/regras (41).jpg"),
           pygame.image.load("animacoes/regras/regras (42).jpg"),
           pygame.image.load("animacoes/regras/regras (43).jpg"),
           pygame.image.load("animacoes/regras/regras (44).jpg"),
           pygame.image.load("animacoes/regras/regras (45).jpg"),
           pygame.image.load("animacoes/regras/regras (46).jpg"),
           pygame.image.load("animacoes/regras/regras (47).jpg"),
           pygame.image.load("animacoes/regras/regras (48).jpg"),
           pygame.image.load("animacoes/regras/regras (49).jpg"),
           pygame.image.load("animacoes/regras/regras (50).jpg"),
           pygame.image.load("animacoes/regras/regras (51).jpg"),
           pygame.image.load("animacoes/regras/regras (52).jpg"),
           pygame.image.load("animacoes/regras/regras (53).jpg"),
           pygame.image.load("animacoes/regras/regras (54).jpg"),
           pygame.image.load("animacoes/regras/regras (55).jpg"),
           pygame.image.load("animacoes/regras/regras (56).jpg"),
           pygame.image.load("animacoes/regras/regras (57).jpg"),
           pygame.image.load("animacoes/regras/regras (58).jpg"),
           pygame.image.load("animacoes/regras/regras (59).jpg"),
           pygame.image.load("animacoes/regras/regras (60).jpg"),
           pygame.image.load("animacoes/regras/regras (61).jpg"),
           pygame.image.load("animacoes/regras/regras (62).jpg"),
           pygame.image.load("animacoes/regras/regras (63).jpg"),
           pygame.image.load("animacoes/regras/regras (64).jpg"),
           pygame.image.load("animacoes/regras/regras (65).jpg"),
           pygame.image.load("animacoes/regras/regras (66).jpg"),
           pygame.image.load("animacoes/regras/regras (67).jpg"),
           pygame.image.load("animacoes/regras/regras (68).jpg"),
           pygame.image.load("animacoes/regras/regras (69).jpg"),
           pygame.image.load("animacoes/regras/regras (70).jpg"),
           pygame.image.load("animacoes/regras/regras (71).jpg"),
           pygame.image.load("animacoes/regras/regras (72).jpg"),
           pygame.image.load("animacoes/regras/regras (73).jpg"),
           pygame.image.load("animacoes/regras/regras (74).jpg"),
           pygame.image.load("animacoes/regras/regras (75).jpg"),
           pygame.image.load("animacoes/regras/regras (76).jpg"),
           pygame.image.load("animacoes/regras/regras (77).jpg"),
           pygame.image.load("animacoes/regras/regras (78).jpg"),
           pygame.image.load("animacoes/regras/regras (79).jpg"),
           pygame.image.load("animacoes/regras/regras (80).jpg"),
           pygame.image.load("animacoes/regras/regras (81).jpg"),
           pygame.image.load("animacoes/regras/regras (82).jpg"),
           pygame.image.load("animacoes/regras/regras (83).jpg"),
           pygame.image.load("animacoes/regras/regras (84).jpg"),
           pygame.image.load("animacoes/regras/regras (85).jpg"),
           pygame.image.load("animacoes/regras/regras (86).jpg"),
           pygame.image.load("animacoes/regras/regras (87).jpg"),
           pygame.image.load("animacoes/regras/regras (88).jpg"),
           pygame.image.load("animacoes/regras/regras (89).jpg"),
           pygame.image.load("animacoes/regras/regras (90).jpg"),
           pygame.image.load("animacoes/regras/regras (91).jpg"),
           pygame.image.load("animacoes/regras/regras (92).jpg"),
           pygame.image.load("animacoes/regras/regras (93).jpg"),
           pygame.image.load("animacoes/regras/regras (94).jpg"),
           pygame.image.load("animacoes/regras/regras (95).jpg"),
           pygame.image.load("animacoes/regras/regras (96).jpg"),
           pygame.image.load("animacoes/regras/regras (97).jpg"),
           pygame.image.load("animacoes/regras/regras (98).jpg"),
           pygame.image.load("animacoes/regras/regras (99).jpg"),
           pygame.image.load("animacoes/regras/regras (100).jpg"),
           pygame.image.load("animacoes/regras/regras (101).jpg"),
           pygame.image.load("animacoes/regras/regras (102).jpg"),
           pygame.image.load("animacoes/regras/regras (103).jpg"),
           pygame.image.load("animacoes/regras/regras (104).jpg"),
           pygame.image.load("animacoes/regras/regras (105).jpg"),
           pygame.image.load("animacoes/regras/regras (106).jpg"),
           pygame.image.load("animacoes/regras/regras (107).jpg"),
           pygame.image.load("animacoes/regras/regras (108).jpg"),
           pygame.image.load("animacoes/regras/regras (109).jpg"),
           pygame.image.load("animacoes/regras/regras (110).jpg"),
           pygame.image.load("animacoes/regras/regras (111).jpg"),
           pygame.image.load("animacoes/regras/regras (112).jpg"),
           pygame.image.load("animacoes/regras/regras (113).jpg"),
           pygame.image.load("animacoes/regras/regras (114).jpg"),
           pygame.image.load("animacoes/regras/regras (115).jpg"),
           pygame.image.load("animacoes/regras/regras (116).jpg"),
           pygame.image.load("animacoes/regras/regras (117).jpg"),
           pygame.image.load("animacoes/regras/regras (118).jpg"),
           pygame.image.load("animacoes/regras/regras (119).jpg"),
           pygame.image.load("animacoes/regras/regras (120).jpg"),
           pygame.image.load("animacoes/regras/regras (121).jpg"),
           pygame.image.load("animacoes/regras/regras (122).jpg"),
           pygame.image.load("animacoes/regras/regras (123).jpg"),
           pygame.image.load("animacoes/regras/regras (124).jpg"),
           pygame.image.load("animacoes/regras/regras (125).jpg"),
           pygame.image.load("animacoes/regras/regras (126).jpg"),
           pygame.image.load("animacoes/regras/regras (127).jpg"),
           pygame.image.load("animacoes/regras/regras (128).jpg"),
           pygame.image.load("animacoes/regras/regras (129).jpg"),
           pygame.image.load("animacoes/regras/regras (130).jpg"),
           pygame.image.load("animacoes/regras/regras (131).jpg"),
           pygame.image.load("animacoes/regras/regras (132).jpg"),
           pygame.image.load("animacoes/regras/regras (133).jpg"),
           pygame.image.load("animacoes/regras/regras (134).jpg"),
           pygame.image.load("animacoes/regras/regras (135).jpg"),
           pygame.image.load("animacoes/regras/regras (136).jpg"),
           pygame.image.load("animacoes/regras/regras (137).jpg"),
           pygame.image.load("animacoes/regras/regras (138).jpg"),
           pygame.image.load("animacoes/regras/regras (139).jpg"),
           pygame.image.load("animacoes/regras/regras (140).jpg"),
           pygame.image.load("animacoes/regras/regras (141).jpg"),
           pygame.image.load("animacoes/regras/regras (142).jpg"),
           pygame.image.load("animacoes/regras/regras (143).jpg"),
           pygame.image.load("animacoes/regras/regras (144).jpg"),
           pygame.image.load("animacoes/regras/regras (145).jpg"),
           pygame.image.load("animacoes/regras/regras (146).jpg"),
           pygame.image.load("animacoes/regras/regras (147).jpg"),
           pygame.image.load("animacoes/regras/regras (148).jpg"),
           pygame.image.load("animacoes/regras/regras (149).jpg"),
           pygame.image.load("animacoes/regras/regras (150).jpg"),
           pygame.image.load("animacoes/regras/regras (151).jpg"),
           pygame.image.load("animacoes/regras/regras (152).jpg"),
           pygame.image.load("animacoes/regras/regras (153).jpg"),
           pygame.image.load("animacoes/regras/regras (154).jpg"),
           pygame.image.load("animacoes/regras/regras (155).jpg"),
           pygame.image.load("animacoes/regras/regras (156).jpg"),
           pygame.image.load("animacoes/regras/regras (157).jpg"),
           pygame.image.load("animacoes/regras/regras (158).jpg"),
           pygame.image.load("animacoes/regras/regras (159).jpg"),
           pygame.image.load("animacoes/regras/regras (160).jpg"),
           pygame.image.load("animacoes/regras/regras (161).jpg"),
           pygame.image.load("animacoes/regras/regras (162).jpg"),
           pygame.image.load("animacoes/regras/regras (163).jpg"),
           pygame.image.load("animacoes/regras/regras (164).jpg"),
           pygame.image.load("animacoes/regras/regras (165).jpg"),
           pygame.image.load("animacoes/regras/regras (166).jpg"),
           pygame.image.load("animacoes/regras/regras (167).jpg"),
           pygame.image.load("animacoes/regras/regras (168).jpg"),
           pygame.image.load("animacoes/regras/regras (169).jpg"),
           pygame.image.load("animacoes/regras/regras (170).jpg"),
           pygame.image.load("animacoes/regras/regras (171).jpg"),
           pygame.image.load("animacoes/regras/regras (172).jpg"),
           pygame.image.load("animacoes/regras/regras (173).jpg"),
           pygame.image.load("animacoes/regras/regras (174).jpg"),
           pygame.image.load("animacoes/regras/regras (175).jpg"),
           pygame.image.load("animacoes/regras/regras (176).jpg"),
           pygame.image.load("animacoes/regras/regras (177).jpg"),
           pygame.image.load("animacoes/regras/regras (178).jpg"),
           pygame.image.load("animacoes/regras/regras (179).jpg"),
           pygame.image.load("animacoes/regras/regras (180).jpg"),
           pygame.image.load("animacoes/regras/regras (181).jpg"),
           pygame.image.load("animacoes/regras/regras (182).jpg"),
           pygame.image.load("animacoes/regras/regras (183).jpg"),
           pygame.image.load("animacoes/regras/regras (184).jpg"),
           pygame.image.load("animacoes/regras/regras (185).jpg"),
           pygame.image.load("animacoes/regras/regras (186).jpg"),
           pygame.image.load("animacoes/regras/regras (187).jpg"),
           pygame.image.load("animacoes/regras/regras (188).jpg"),
           pygame.image.load("animacoes/regras/regras (189).jpg"),
           pygame.image.load("animacoes/regras/regras (190).jpg"),
           pygame.image.load("animacoes/regras/regras (191).jpg"),
           pygame.image.load("animacoes/regras/regras (192).jpg"),
           pygame.image.load("animacoes/regras/regras (193).jpg"),
           pygame.image.load("animacoes/regras/regras (194).jpg"),
           pygame.image.load("animacoes/regras/regras (195).jpg"),
           pygame.image.load("animacoes/regras/regras (196).jpg"),
           pygame.image.load("animacoes/regras/regras (197).jpg"),
           pygame.image.load("animacoes/regras/regras (198).jpg"),
           pygame.image.load("animacoes/regras/regras (199).jpg"),
           pygame.image.load("animacoes/regras/regras (200).jpg"),
           pygame.image.load("animacoes/regras/regras (201).jpg"),
           pygame.image.load("animacoes/regras/regras (202).jpg"),
           pygame.image.load("animacoes/regras/regras (203).jpg"),
           pygame.image.load("animacoes/regras/regras (204).jpg"),
           pygame.image.load("animacoes/regras/regras (205).jpg"),
           pygame.image.load("animacoes/regras/regras (206).jpg"),
           pygame.image.load("animacoes/regras/regras (207).jpg"),
           pygame.image.load("animacoes/regras/regras (208).jpg"),
           pygame.image.load("animacoes/regras/regras (209).jpg"),
           pygame.image.load("animacoes/regras/regras (210).jpg"),
           pygame.image.load("animacoes/regras/regras (211).jpg"),
           pygame.image.load("animacoes/regras/regras (212).jpg"),
           pygame.image.load("animacoes/regras/regras (213).jpg"),
           pygame.image.load("animacoes/regras/regras (214).jpg"),
           pygame.image.load("animacoes/regras/regras (215).jpg"),
           pygame.image.load("animacoes/regras/regras (216).jpg"),
           pygame.image.load("animacoes/regras/regras (217).jpg"),
           pygame.image.load("animacoes/regras/regras (218).jpg"),
           pygame.image.load("animacoes/regras/regras (219).jpg"),
           pygame.image.load("animacoes/regras/regras (220).jpg"),
           pygame.image.load("animacoes/regras/regras (221).jpg"),
           pygame.image.load("animacoes/regras/regras (222).jpg"),
           pygame.image.load("animacoes/regras/regras (223).jpg"),
           pygame.image.load("animacoes/regras/regras (224).jpg"),
           pygame.image.load("animacoes/regras/regras (225).jpg"),
           pygame.image.load("animacoes/regras/regras (226).jpg"),
           pygame.image.load("animacoes/regras/regras (227).jpg"),
           pygame.image.load("animacoes/regras/regras (228).jpg"),
           pygame.image.load("animacoes/regras/regras (229).jpg"),
           pygame.image.load("animacoes/regras/regras (230).jpg"),
           pygame.image.load("animacoes/regras/regras (231).jpg"),
           pygame.image.load("animacoes/regras/regras (232).jpg"),
           pygame.image.load("animacoes/regras/regras (233).jpg"),
           pygame.image.load("animacoes/regras/regras (234).jpg"),
           pygame.image.load("animacoes/regras/regras (235).jpg"),
           pygame.image.load("animacoes/regras/regras (236).jpg"),
           pygame.image.load("animacoes/regras/regras (237).jpg"),
           pygame.image.load("animacoes/regras/regras (238).jpg"),
           pygame.image.load("animacoes/regras/regras (239).jpg"),
           pygame.image.load("animacoes/regras/regras (240).jpg"),
           pygame.image.load("animacoes/regras/regras (241).jpg"),
           pygame.image.load("animacoes/regras/regras (242).jpg"),
           pygame.image.load("animacoes/regras/regras (243).jpg"),
           pygame.image.load("animacoes/regras/regras (244).jpg"),
           pygame.image.load("animacoes/regras/regras (245).jpg"),
           pygame.image.load("animacoes/regras/regras (246).jpg"),
           pygame.image.load("animacoes/regras/regras (247).jpg"),
           pygame.image.load("animacoes/regras/regras (248).jpg"),
           pygame.image.load("animacoes/regras/regras (249).jpg"),
           pygame.image.load("animacoes/regras/regras (250).jpg"),
           pygame.image.load("animacoes/regras/regras (251).jpg"),
           pygame.image.load("animacoes/regras/regras (252).jpg"),
           pygame.image.load("animacoes/regras/regras (253).jpg"),
           pygame.image.load("animacoes/regras/regras (254).jpg"),
           pygame.image.load("animacoes/regras/regras (255).jpg"),
           pygame.image.load("animacoes/regras/regras (256).jpg"),
           pygame.image.load("animacoes/regras/regras (257).jpg"),
           pygame.image.load("animacoes/regras/regras (258).jpg"),
           pygame.image.load("animacoes/regras/regras (259).jpg"),
           pygame.image.load("animacoes/regras/regras (260).jpg"),
           pygame.image.load("animacoes/regras/regras (261).jpg"),
           pygame.image.load("animacoes/regras/regras (262).jpg"),
           pygame.image.load("animacoes/regras/regras (263).jpg"),
           pygame.image.load("animacoes/regras/regras (264).jpg"),
           pygame.image.load("animacoes/regras/regras (265).jpg"),
           pygame.image.load("animacoes/regras/regras (266).jpg"),
           pygame.image.load("animacoes/regras/regras (267).jpg"),
           pygame.image.load("animacoes/regras/regras (268).jpg"),
           pygame.image.load("animacoes/regras/regras (269).jpg"),
           pygame.image.load("animacoes/regras/regras (270).jpg"),
           pygame.image.load("animacoes/regras/regras (271).jpg"),
           pygame.image.load("animacoes/regras/regras (272).jpg"),
           pygame.image.load("animacoes/regras/regras (273).jpg"),
           pygame.image.load("animacoes/regras/regras (274).jpg"),
           pygame.image.load("animacoes/regras/regras (275).jpg"),
           pygame.image.load("animacoes/regras/regras (276).jpg"),
           pygame.image.load("animacoes/regras/regras (277).jpg"),
           pygame.image.load("animacoes/regras/regras (278).jpg"),
           pygame.image.load("animacoes/regras/regras (279).jpg"),
           pygame.image.load("animacoes/regras/regras (280).jpg"),
           pygame.image.load("animacoes/regras/regras (281).jpg"),
           pygame.image.load("animacoes/regras/regras (282).jpg"),
           pygame.image.load("animacoes/regras/regras (283).jpg"),
           pygame.image.load("animacoes/regras/regras (284).jpg"),
           pygame.image.load("animacoes/regras/regras (285).jpg"),
           pygame.image.load("animacoes/regras/regras (286).jpg"),
           pygame.image.load("animacoes/regras/regras (287).jpg"),
           pygame.image.load("animacoes/regras/regras (288).jpg"),
           pygame.image.load("animacoes/regras/regras (289).jpg"),
           pygame.image.load("animacoes/regras/regras (290).jpg"),
           pygame.image.load("animacoes/regras/regras (291).jpg"),
           pygame.image.load("animacoes/regras/regras (292).jpg"),
           pygame.image.load("animacoes/regras/regras (293).jpg"),
           pygame.image.load("animacoes/regras/regras (294).jpg"),
           pygame.image.load("animacoes/regras/regras (295).jpg"),
           pygame.image.load("animacoes/regras/regras (296).jpg"),
           pygame.image.load("animacoes/regras/regras (297).jpg"),
           pygame.image.load("animacoes/regras/regras (298).jpg"),
           pygame.image.load("animacoes/regras/regras (299).jpg"),
           pygame.image.load("animacoes/regras/regras (300).jpg"),
           pygame.image.load("animacoes/regras/regras (301).jpg"),
           pygame.image.load("animacoes/regras/regras (302).jpg"),
           pygame.image.load("animacoes/regras/regras (303).jpg"),
           pygame.image.load("animacoes/regras/regras (304).jpg"),
           pygame.image.load("animacoes/regras/regras (305).jpg"),
           pygame.image.load("animacoes/regras/regras (306).jpg"),
           pygame.image.load("animacoes/regras/regras (307).jpg"),
           pygame.image.load("animacoes/regras/regras (308).jpg"),
           pygame.image.load("animacoes/regras/regras (309).jpg"),
           pygame.image.load("animacoes/regras/regras (310).jpg"),
           pygame.image.load("animacoes/regras/regras (311).jpg"),
           pygame.image.load("animacoes/regras/regras (312).jpg"),
           pygame.image.load("animacoes/regras/regras (313).jpg"),
           pygame.image.load("animacoes/regras/regras (314).jpg"),
           pygame.image.load("animacoes/regras/regras (315).jpg"),
           pygame.image.load("animacoes/regras/regras (316).jpg"),
           pygame.image.load("animacoes/regras/regras (317).jpg"),
           pygame.image.load("animacoes/regras/regras (318).jpg"),
           pygame.image.load("animacoes/regras/regras (319).jpg"),
           pygame.image.load("animacoes/regras/regras (320).jpg"),
           pygame.image.load("animacoes/regras/regras (321).jpg"),
           pygame.image.load("animacoes/regras/regras (322).jpg"),
           pygame.image.load("animacoes/regras/regras (323).jpg"),
           pygame.image.load("animacoes/regras/regras (324).jpg"),
           pygame.image.load("animacoes/regras/regras (325).jpg"),
           pygame.image.load("animacoes/regras/regras (326).jpg"),
           pygame.image.load("animacoes/regras/regras (327).jpg"),
           pygame.image.load("animacoes/regras/regras (328).jpg"),
           pygame.image.load("animacoes/regras/regras (329).jpg"),
           pygame.image.load("animacoes/regras/regras (330).jpg"),
           pygame.image.load("animacoes/regras/regras (331).jpg"),
           pygame.image.load("animacoes/regras/regras (332).jpg"),
           pygame.image.load("animacoes/regras/regras (333).jpg"),
           pygame.image.load("animacoes/regras/regras (334).jpg"),
           pygame.image.load("animacoes/regras/regras (335).jpg"),
           pygame.image.load("animacoes/regras/regras (336).jpg"),
           pygame.image.load("animacoes/regras/regras (337).jpg"),
           pygame.image.load("animacoes/regras/regras (338).jpg"),
           pygame.image.load("animacoes/regras/regras (339).jpg"),
           pygame.image.load("animacoes/regras/regras (340).jpg"),
           pygame.image.load("animacoes/regras/regras (341).jpg"),
           pygame.image.load("animacoes/regras/regras (342).jpg"),
           pygame.image.load("animacoes/regras/regras (343).jpg"),
           pygame.image.load("animacoes/regras/regras (344).jpg"),
           pygame.image.load("animacoes/regras/regras (345).jpg"),
           pygame.image.load("animacoes/regras/regras (346).jpg"),
           pygame.image.load("animacoes/regras/regras (347).jpg"),
           pygame.image.load("animacoes/regras/regras (348).jpg"),
           pygame.image.load("animacoes/regras/regras (349).jpg"),
           pygame.image.load("animacoes/regras/regras (350).jpg"),
           pygame.image.load("animacoes/regras/regras (351).jpg"),
           pygame.image.load("animacoes/regras/regras (352).jpg"),
           pygame.image.load("animacoes/regras/regras (353).jpg"),
           pygame.image.load("animacoes/regras/regras (354).jpg"),
           pygame.image.load("animacoes/regras/regras (355).jpg"),
           pygame.image.load("animacoes/regras/regras (356).jpg"),
           pygame.image.load("animacoes/regras/regras (357).jpg"),
           pygame.image.load("animacoes/regras/regras (358).jpg"),
           pygame.image.load("animacoes/regras/regras (359).jpg"),
           pygame.image.load("animacoes/regras/regras (360).jpg"),
           pygame.image.load("animacoes/regras/regras (361).jpg"),
           pygame.image.load("animacoes/regras/regras (362).jpg"),
           pygame.image.load("animacoes/regras/regras (363).jpg"),
           pygame.image.load("animacoes/regras/regras (364).jpg"),
           pygame.image.load("animacoes/regras/regras (365).jpg"),
           pygame.image.load("animacoes/regras/regras (366).jpg"),
           pygame.image.load("animacoes/regras/regras (367).jpg"),
           pygame.image.load("animacoes/regras/regras (368).jpg"),
           pygame.image.load("animacoes/regras/regras (369).jpg"),
           pygame.image.load("animacoes/regras/regras (370).jpg"),
           pygame.image.load("animacoes/regras/regras (371).jpg"),
           pygame.image.load("animacoes/regras/regras (372).jpg"),
           pygame.image.load("animacoes/regras/regras (373).jpg"),
           pygame.image.load("animacoes/regras/regras (374).jpg"),
           pygame.image.load("animacoes/regras/regras (375).jpg"),
           pygame.image.load("animacoes/regras/regras (376).jpg"),
           pygame.image.load("animacoes/regras/regras (377).jpg"),
           pygame.image.load("animacoes/regras/regras (378).jpg"),
           pygame.image.load("animacoes/regras/regras (379).jpg"),
           pygame.image.load("animacoes/regras/regras (380).jpg"),
           pygame.image.load("animacoes/regras/regras (381).jpg"),
           pygame.image.load("animacoes/regras/regras (382).jpg"),
           pygame.image.load("animacoes/regras/regras (383).jpg"),
           pygame.image.load("animacoes/regras/regras (384).jpg"),
           pygame.image.load("animacoes/regras/regras (385).jpg"),
           pygame.image.load("animacoes/regras/regras (386).jpg"),
           pygame.image.load("animacoes/regras/regras (387).jpg"),
           pygame.image.load("animacoes/regras/regras (388).jpg"),
           pygame.image.load("animacoes/regras/regras (389).jpg"),
           pygame.image.load("animacoes/regras/regras (390).jpg"),
           pygame.image.load("animacoes/regras/regras (391).jpg"),
           pygame.image.load("animacoes/regras/regras (392).jpg"),
           pygame.image.load("animacoes/regras/regras (393).jpg"),
           pygame.image.load("animacoes/regras/regras (394).jpg"),
           pygame.image.load("animacoes/regras/regras (395).jpg"),
           pygame.image.load("animacoes/regras/regras (396).jpg"),
           pygame.image.load("animacoes/regras/regras (397).jpg"),
           pygame.image.load("animacoes/regras/regras (398).jpg"),
           pygame.image.load("animacoes/regras/regras (399).jpg"),
           pygame.image.load("animacoes/regras/regras (400).jpg"),
           pygame.image.load("animacoes/regras/regras (401).jpg"),
           pygame.image.load("animacoes/regras/regras (402).jpg"),
           pygame.image.load("animacoes/regras/regras (403).jpg"),
           pygame.image.load("animacoes/regras/regras (404).jpg"),
           pygame.image.load("animacoes/regras/regras (405).jpg"),
           pygame.image.load("animacoes/regras/regras (406).jpg"),
           pygame.image.load("animacoes/regras/regras (407).jpg"),
           pygame.image.load("animacoes/regras/regras (408).jpg"),
           pygame.image.load("animacoes/regras/regras (409).jpg"),
           pygame.image.load("animacoes/regras/regras (410).jpg"),
           pygame.image.load("animacoes/regras/regras (411).jpg"),
           pygame.image.load("animacoes/regras/regras (412).jpg"),
           pygame.image.load("animacoes/regras/regras (413).jpg"),
           pygame.image.load("animacoes/regras/regras (414).jpg"),
           pygame.image.load("animacoes/regras/regras (415).jpg"),
           pygame.image.load("animacoes/regras/regras (416).jpg"),
           pygame.image.load("animacoes/regras/regras (417).jpg"),
           pygame.image.load("animacoes/regras/regras (418).jpg"),
           pygame.image.load("animacoes/regras/regras (419).jpg"),
           pygame.image.load("animacoes/regras/regras (420).jpg"),
           pygame.image.load("animacoes/regras/regras (421).jpg"),
           pygame.image.load("animacoes/regras/regras (422).jpg"),
           pygame.image.load("animacoes/regras/regras (423).jpg"),
           pygame.image.load("animacoes/regras/regras (424).jpg"),
           pygame.image.load("animacoes/regras/regras (425).jpg"),
           pygame.image.load("animacoes/regras/regras (426).jpg"),
           pygame.image.load("animacoes/regras/regras (427).jpg"),
           pygame.image.load("animacoes/regras/regras (428).jpg"),
           pygame.image.load("animacoes/regras/regras (429).jpg"),
           pygame.image.load("animacoes/regras/regras (430).jpg"),
           pygame.image.load("animacoes/regras/regras (431).jpg"),
           pygame.image.load("animacoes/regras/regras (432).jpg"),
           pygame.image.load("animacoes/regras/regras (433).jpg"),
           pygame.image.load("animacoes/regras/regras (434).jpg"),
           pygame.image.load("animacoes/regras/regras (435).jpg"),
           pygame.image.load("animacoes/regras/regras (436).jpg"),
           pygame.image.load("animacoes/regras/regras (437).jpg"),
           pygame.image.load("animacoes/regras/regras (438).jpg"),
           pygame.image.load("animacoes/regras/regras (439).jpg"),
           pygame.image.load("animacoes/regras/regras (440).jpg"),
           pygame.image.load("animacoes/regras/regras (441).jpg"),
           pygame.image.load("animacoes/regras/regras (442).jpg"),
           pygame.image.load("animacoes/regras/regras (443).jpg"),
           pygame.image.load("animacoes/regras/regras (444).jpg"),
           pygame.image.load("animacoes/regras/regras (445).jpg"),
           pygame.image.load("animacoes/regras/regras (446).jpg"),
           pygame.image.load("animacoes/regras/regras (447).jpg"),
           pygame.image.load("animacoes/regras/regras (448).jpg"),
           pygame.image.load("animacoes/regras/regras (449).jpg"),
           pygame.image.load("animacoes/regras/regras (450).jpg"),
           pygame.image.load("animacoes/regras/regras (451).jpg"),
           pygame.image.load("animacoes/regras/regras (452).jpg"),
           pygame.image.load("animacoes/regras/regras (453).jpg"),
           pygame.image.load("animacoes/regras/regras (454).jpg"),
           pygame.image.load("animacoes/regras/regras (455).jpg"),
           pygame.image.load("animacoes/regras/regras (456).jpg"),
           pygame.image.load("animacoes/regras/regras (457).jpg"),
           pygame.image.load("animacoes/regras/regras (458).jpg"),
           pygame.image.load("animacoes/regras/regras (459).jpg"),
           pygame.image.load("animacoes/regras/regras (460).jpg"),
           pygame.image.load("animacoes/regras/regras (461).jpg"),
           pygame.image.load("animacoes/regras/regras (462).jpg"),
           pygame.image.load("animacoes/regras/regras (463).jpg"),
           pygame.image.load("animacoes/regras/regras (464).jpg"),
           pygame.image.load("animacoes/regras/regras (465).jpg"),
           pygame.image.load("animacoes/regras/regras (466).jpg"),
           pygame.image.load("animacoes/regras/regras (467).jpg"),
           pygame.image.load("animacoes/regras/regras (468).jpg"),
           pygame.image.load("animacoes/regras/regras (469).jpg"),
           pygame.image.load("animacoes/regras/regras (470).jpg"),
           pygame.image.load("animacoes/regras/regras (471).jpg"),
           pygame.image.load("animacoes/regras/regras (472).jpg"),
           pygame.image.load("animacoes/regras/regras (473).jpg"),
           pygame.image.load("animacoes/regras/regras (474).jpg"),
           pygame.image.load("animacoes/regras/regras (475).jpg"),
           pygame.image.load("animacoes/regras/regras (476).jpg"),
           pygame.image.load("animacoes/regras/regras (477).jpg"),
           pygame.image.load("animacoes/regras/regras (478).jpg"),
           pygame.image.load("animacoes/regras/regras (479).jpg"),
           pygame.image.load("animacoes/regras/regras (480).jpg"),
           pygame.image.load("animacoes/regras/regras (481).jpg"),
           pygame.image.load("animacoes/regras/regras (482).jpg"),
           pygame.image.load("animacoes/regras/regras (483).jpg"),
           pygame.image.load("animacoes/regras/regras (484).jpg"),
           pygame.image.load("animacoes/regras/regras (485).jpg"),
           pygame.image.load("animacoes/regras/regras (486).jpg"),
           pygame.image.load("animacoes/regras/regras (487).jpg"),
           pygame.image.load("animacoes/regras/regras (488).jpg"),
           pygame.image.load("animacoes/regras/regras (489).jpg"),
           pygame.image.load("animacoes/regras/regras (490).jpg"),
           pygame.image.load("animacoes/regras/regras (491).jpg"),
           pygame.image.load("animacoes/regras/regras (492).jpg"),
           pygame.image.load("animacoes/regras/regras (493).jpg"),
           pygame.image.load("animacoes/regras/regras (494).jpg"),
           pygame.image.load("animacoes/regras/regras (495).jpg"),
           pygame.image.load("animacoes/regras/regras (496).jpg"),
           pygame.image.load("animacoes/regras/regras (497).jpg"),
           pygame.image.load("animacoes/regras/regras (498).jpg"),
           pygame.image.load("animacoes/regras/regras (499).jpg"),
           pygame.image.load("animacoes/regras/regras (500).jpg"),
           pygame.image.load("animacoes/regras/regras (501).jpg"),
           pygame.image.load("animacoes/regras/regras (502).jpg"),
           pygame.image.load("animacoes/regras/regras (503).jpg"),
           pygame.image.load("animacoes/regras/regras (504).jpg"),
           pygame.image.load("animacoes/regras/regras (505).jpg"),
           pygame.image.load("animacoes/regras/regras (506).jpg"),
           pygame.image.load("animacoes/regras/regras (507).jpg"),
           pygame.image.load("animacoes/regras/regras (508).jpg"),
           pygame.image.load("animacoes/regras/regras (509).jpg")]

screen = pygame.display.set_mode((700, 500))
screen.fill(cores['preto'])
pygame.display.set_caption("PPTLS")
musica = pygame.mixer.music.load("sounds/rockytheme.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
game = "jogar dnv"

start = Jogo()
while game == "jogar dnv":
    num_part = 0
    vencedor = []
    escolhas_jogador = []
    nome = []
    game = main(start)
pygame.quit()
