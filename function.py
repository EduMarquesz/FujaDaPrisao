def linha(tam=60):
    linha = print('-' * tam)
    return linha


class AdventureGame:
    def __init__(self):
        self.situation1 = 'Acorda! Você tem que fugir da prisão hoje. (Levantar/Deitar) '
        self.situation2 = 'Vai lá distraia o guarda, você pode chamar ele e tentar pegar a chave ou desmaiar ele. (Chave/Desmaiar) '
        self.situation3 = 'Droga tem um guarda aqui, podemos distrair ele ou atacar, oq sugere? (Distrair/Atacar) '
        self.final = 'Conseguimos fugir! vamos correr o mais longe daqui, vamos pegar um carro? (Sim/Não) '
        self.resp1A = 'Pelo visto você quer mesmo fugir em, então vamos.'
        self.resp1b = 'já é 14:00 horas, não podemos fugir mais, já vamos ser transferidos para segurança máxima.'
        self.resp2A = 'Boa! você conseguiu, vamos pelos fundos.'
        self.resp2B = 'O alarme foi disparado, acho que acharam o guarda desmaiado, droga! nos pegaram.'
        self.resp3A = 'Ok vamos distrair, vou jogar essa pedra do outro lado e você vai abrir a porta.'
        self.resp3B = 'Você e seu colega atacaram o guarda, mas seu companheiro acabou sendo baleado e você foi preso.'
        self.respfinal1 = 'Vocês roubaram um carro e a Polícia rastreou e os cercaram, vocês foram presos.'
        self.respfinal2 = 'Vocês foram correndo e a polícia não conseguiu localiza-los, fuga bem sucedida.'


    def iniciar(self):
        linha()
        answer1 = input(self.situation1).upper()[0]
        if answer1 == 'L':
            print(self.resp1A)
            answer2 = input(self.situation2).upper()[0]
            if answer2 == 'C':
                print(self.resp2A)
                answer3 = input(self.situation3).upper()[0]
                if answer3 == 'D':
                    print(self.resp3A)
                    answer4 = input(self.final).upper()[0]
                    if answer4 == 'N':
                        print(self.respfinal2)
                    else:
                        print(self.respfinal1)
                else:
                    print(self.resp3B)
            else:
                print(self.resp2B)
        else:
            print(self.resp1b) 
        print('Fim do Jogo')
        linha()