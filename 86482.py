#Miguel Antonio Oliveira Rocha, 86482

#Tipo Posicao
#Construtor
def faz_pos(l,c):
    if isinstance(l, int) and isinstance(c,int) and l>=0 and c>=0:
        return (l,c)
    else:
        raise ValueError ('faz_pos: argumentos errados')
#Constroi, a partir de dois inteiros positivos, a posicao da letra.
#Seletores
def linha_pos(p):
    return p[0]
#Devolve a linha correspondente a posicao da letra.
def coluna_pos(p):
    return p[1]
#Devolve a coluna correspondente a posicao da coluna.
#Reconhecedores
def e_pos(arg):
    return isinstance(arg,tuple) and len(arg)==2 and verifica_numero(arg[0]) and verifica_numero(arg[1])
#Verifica se o argumento fornecido e mesmo uma posicao.

def verifica_numero(n):
    return n>=0 and isinstance(n,int)
#Verifica se o numero e positivo e inteiro.

#Testes
def pos_iguais(p1,p2):
    if linha_pos(p1)==linha_pos(p2) and coluna_pos(p1)==coluna_pos(p2):
        return True
    else:
        return False
#Verifica se as posicoes sao iguais.
#---------------------------------------------Fim do Tipo Posicao----------------------------------------
#Tipo Chave
#Construtor
def verifica_letras(l):
    letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for e in l:
        if e not in letras:
            return False
    return True
#A verifica_letras verifica se todos os elementos do l dado estao em letras.
def verifica_string(l, mgc):
    letras = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for e in mgc:
        if e!=' ' and e not in letras:
            return False
    return True
#A verifica_String verifica se todos os elementos da string dada estao em letras.
def gera_chave_linhas(l,mgc):
    if len(l)!=25 or  not verifica_letras(l) or not verifica_string(l,mgc) or not isinstance(mgc,str):
        raise ValueError ('gera_chave_linhas: argumentos errados')
    else:
        chave_mensagem=[]
        if len(l)==25 and isinstance(mgc,str):
            for e in mgc:
                if e!=' ' and  e not in chave_mensagem: #Verifica se existem espacos na string e se os elementos da string ja estao na chave_mensagem.
                    chave_mensagem=chave_mensagem+[e]
            for e in l:
                if e not in mgc: #Se o elemento de l nao esta na string mgc, e adiciona-o.
                    chave_mensagem=chave_mensagem+[e]
            if e_chave([chave_mensagem[0:5],chave_mensagem[5:10],chave_mensagem[10:15],chave_mensagem[15:20],chave_mensagem[20:25]])!=True:
                raise ValueError ('gera_chave_linhas: argumentos errados') #Verifica se a chave_final e mesmo uma chave.
            else:
                return [chave_mensagem[0:5],chave_mensagem[5:10],chave_mensagem[10:15],chave_mensagem[15:20],chave_mensagem[20:25]]   
#A funcao gera_chave_linhas ira gerar uma lista de listas, correspondente as 5 linhas da cifra.
def gera_chave_espiral(l, mgc, s, pos):
    if len(l)!=25 or not isinstance(mgc,str) or (s not in ['r', 'c']) or not verifica_letras(l) or not verifica_string(l,mgc) or not e_pos(pos):
        raise ValueError ('gera_chave_espiral: argumentos errados')
    else:
        cria_espiral={'RIGHT': (0,1), 'DOWN': (1,0), 'LEFT': (0,-1), 'UP': (-1,0)} #Corresponde aos movimentos que o cursor faz dentro da espiral.
        chave_mensagem={}
        linha=linha_pos(pos)
        coluna=coluna_pos(pos)
        chave_final=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']] #Corresponde a lista vazia onde no final, vai ser colocado as letras correspondentes a cada caracter.
        if s=='c' and pos==(0,0): #Corresponde aos movimentos necessarios para criar a espiral no sentido inverso aos ponteiros do relogio, dependendo da posicao inicial.
            cursor=('DOWN', 'RIGHT', 'UP', 'LEFT')
            sentido=0
        elif s=='c' and pos==(0,4):
            cursor=('DOWN', 'LEFT', 'UP', 'RIGHT')
            sentido=1
        elif s=='c' and pos==(4,0):
            cursor=('RIGHT', 'UP', 'LEFT', 'DOWN')
            sentido=2
        elif s=='c' and pos==(4,4):
            cursor=('UP', 'LEFT', 'DOWN', 'RIGHT')
            sentido=3
        elif s=='r' and pos==(0,0): #Corresponde aos movimentos necessarios para criar a espiral no sentido dos ponteiros do relogio, dependendo da posicao inicial.
            cursor=('RIGHT', 'DOWN', 'LEFT', 'UP')
            sentido=0
        elif s=='r' and pos==(0,4):
            cursor=('LEFT', 'DOWN', 'RIGHT', 'UP')
            sentido=1
        elif s=='r' and pos==(4,0):
            cursor=('UP', 'RIGHT', 'DOWN', 'LEFT')
            sentido=2
        elif s=='r' and pos==(4,4):
            cursor=('LEFT', 'UP', 'RIGHT', 'DOWN')
            sentido=3
        else:
            raise ValueError ('gera_chave_espiral: argumentos errados')
#Cria, a partir da posicao inicial, qual dos sentidos vai seguir o cursor.
        def cria_coordenadas(sentido):
            linha_espiral=linha+cria_espiral[cursor[sentido]][0]
            coluna_espiral=coluna+cria_espiral[cursor[sentido]][1]
            while len(chave_mensagem)!=25 and (linha_espiral>4 or coluna_espiral>4 or linha_espiral<0 or coluna_espiral<0 or (linha_espiral, coluna_espiral) in chave_mensagem):
                sentido=(sentido+1)%4 #Divide a espiral em "quadrados" e vai fazendo o sentido de cada quadrado ate chegar ao meio da espiral.
                linha_espiral=linha+cria_espiral[cursor[sentido]][0]
                coluna_espiral=coluna+cria_espiral[cursor[sentido]][1]
            return linha_espiral, coluna_espiral, sentido       
#A funcao cria_coordenadas vai criar a chave que vai ser atribuida a cada caracter da string mgc, que vai constituir
#um dicionario.
        for char in mgc: #Vai criar a parte do dicionario que possui os caracteres que fazem parte da string mgc.
            if char!=' ' and char not in chave_mensagem.values():
                chave_mensagem[(linha, coluna)]=char
                linha, coluna, sentido=cria_coordenadas(sentido)
        for char in l: #Vai criar a parte do dicionario que possui os caracteres que nao fazem parte da string mgc.
            if char not in chave_mensagem.values():
                chave_mensagem[(linha,coluna)]=char
                linha, coluna, sentido=cria_coordenadas(sentido)
        for c in chave_mensagem:
            chave_final[c[0]][c[1]]=chave_mensagem[c] #Transforma o dicionario numa lista de listas, em que cada item da lista e constituido pela
        #letra a que corresponde uma chave - tuplo de dois elementos, com a linha e coluna correspondentes.
        if e_chave(chave_final)!=True:
            raise ValueError ('gera_chave_espiral: argumentos errados') #Verifica se a chave_final e mesmo uma chave.
        else:
            return chave_final
#Seletor
def ref_chave(c,p):
    return c[linha_pos(p)][coluna_pos(p)]
#Dentro da chave, seleciona a letra correspondente a posicao p.
#Modificador
def muda_chave(c,p,l):
    c[linha_pos(p)][coluna_pos(p)]=l
    return c
#Substitui, dentro da chave, a letra que se encontra na posicao p pela letra l.
#Reconhecedor
def e_chave(arg):
    letras_que_faltam=[]
    if isinstance(arg,list) and len(arg)==5:
        for l in arg:
            if isinstance(l,list) and len(l)==5:
                for c in l:
                    if isinstance(c,str) and c in letras and c not in letras_que_faltam:
                        letras_que_faltam=letras_que_faltam+[c]
                    else:
                        return False
            else:
                    return False
        else:
                return True
    else:
        return False
#Verifica se o argumento dado e mesmo uma chave.
#Transformadores
def string_chave(c):
    string_chave=''
    for i in range(len(c)):
        for j in range(len(c)):
            if j!=4: #Enquanto nao chegar ao fim da sub-lista, adiciona o caracter e um espaco.
                string_chave=string_chave+c[i][j]+' '
            else: #Quando chegar ao fim da sub-lista, adiciona o caracter e a mudanca de linha.
                string_chave=string_chave+ c[i][j]+' '+'\n'
    return string_chave
#A funcao string_chave transforma a chave numa string, que corresponde as 5 linhas da matriz 5x5.
#---------------------------------------------------Fim do tipo chave---------------------------------------------
def digramas(mens):
    mensagem_sem_espacos = ''
    for e in mens:
        if e != ' ' :
            mensagem_sem_espacos = mensagem_sem_espacos + e
    mensagem_final=''
    def digramas_aux(mensagem_sem_espacos):
        mensagem_final=''
        if len(mensagem_sem_espacos) <= 1: #Verifica se o tamanho da mensagem e 1, sem espacos.
            return mensagem_sem_espacos
        if mensagem_sem_espacos[0] == mensagem_sem_espacos[1]: #Se os dois elementos seguidos sao iguais, adiciona um X no seu meio.
            mensagem_final = mensagem_sem_espacos[0] + "X" + digramas_aux(mensagem_sem_espacos[1:])
            return mensagem_final
        else:
            mensagem_final = mensagem_sem_espacos[0] + mensagem_sem_espacos[1] + digramas_aux(mensagem_sem_espacos[2:]) #Se forem diferentes, adiciona o proximo e faz recursivamente o resto da string sem espacos.
            return mensagem_final
        
    mensagem_final = digramas_aux(mensagem_sem_espacos)
    if len(mensagem_final)%2!=0: #Se o tamanho da mensagem final for impar, adiciona um 'X' no fim.
        mensagem_final = mensagem_final + "X"
    return mensagem_final
#A funcao digramas devolve a cadeia de caracteres correspondente a string mens, sem espacos e com um X entre duas letras iguais seguidas.

def figura(digrm,chave):
    pos_final=()
    pos1=()
    pos2=()    
    for i in range(len(chave)):
        for j in range(len(chave)):
            if digrm[0]==chave[i][j]:
                pos1=faz_pos(i,j) #Escreve as coordenadas do primeiro caracter da string.
            elif digrm[1]==chave[i][j]:
                pos2=faz_pos(i,j) #Escreve as coordenadas do segundo caracter da string.
        pos_final=(pos1,pos2) #Escreve o tuplo correspondente a ambas as coordenadas.
    if linha_pos(pos_final[0])==linha_pos(pos_final[1]): #Verifica se os caracteres estao na mesma linha.
        fig='l'
    elif coluna_pos(pos_final[0])==coluna_pos(pos_final[1]): #Verifica se os caracteres estao na mesma coluna.
        fig='c'
    else: #Ocorre quando os caracteres nao estao na mesma coluna nem na mesma linha.
        fig='r'
    return (fig, pos1, pos2)
#A funcao figura determina a figura feita pelos dois caracteres que se encontram em digrm:
#se tiverem a mesma linha, fazem uma linha; se tiverem a mesma coluna, fazem uma coluna; se nao tiverem nenhuma em comum, fazem um retangulo.

def codifica_l(pos1,pos2,inc):
    nova_pos1=()
    nova_pos2=()
    if inc==1:
        if coluna_pos(pos1)!=4 and coluna_pos(pos2)!=4: #Se ambas as posicoes nao sao pontas, soma-se 1 a coluna.
            nova_pos1=(linha_pos(pos1),coluna_pos(pos1)+1)
            nova_pos2=(linha_pos(pos2),coluna_pos(pos2)+1)
        elif coluna_pos(pos2)==4:#Se a posicao2 e uma ponta da linha, entao subtrai-se 4 a sua posicao para ela voltar para a outra ponta (coluna 0).
            nova_pos1=(linha_pos(pos1),coluna_pos(pos1)+1)
            nova_pos2=(linha_pos(pos2),coluna_pos(pos2)-4)
        elif coluna_pos(pos1)==4: #Se a posicao1 e uma ponta da linha, entao subtrai-se 4 a sua posicao para ela voltar para a outra ponta (coluna 0).
            nova_pos1=(linha_pos(pos1),coluna_pos(pos1)-4)
            nova_pos2=(linha_pos(pos2),coluna_pos(pos2)+1)
    if inc==-1:
        if coluna_pos(pos1)!=0 and coluna_pos(pos2)!=0: #Se ambas as posicoes nao sao pontas, subtrai-se 1 a coluna.
            nova_pos1=(linha_pos(pos1),coluna_pos(pos1)-1)
            nova_pos2=(linha_pos(pos2),coluna_pos(pos2)-1)
        elif coluna_pos(pos1)==0: #Se a posicao1 e uma ponta da linha, entao soma-se 4 a sua posicao para ela voltar para a outra ponta (coluna 4).
            nova_pos1=(linha_pos(pos1),coluna_pos(pos1)+4)
            nova_pos2=(linha_pos(pos2),coluna_pos(pos2)-1)
        elif coluna_pos(pos2)==0: #Se a posicao2 e uma ponta da linha, entao soma-se 4 a sua posicao para ela voltar para a outra ponta (coluna 4).
            nova_pos1=(linha_pos(pos1),coluna_pos(pos1)-1)
            nova_pos2=(linha_pos(pos2),coluna_pos(pos2)+4)
    return (nova_pos1,nova_pos2)
#A funcao codifica_l ira dar a posicao a seguir - caso incremento seja igual a 1 - ou dar a posicao anterior da mesma linha, caso o incremento seja igual a -1.

def codifica_c(pos1,pos2,inc):
    nova_pos1=()
    nova_pos2=()
    if inc==1:
        if linha_pos(pos1)!=4 and linha_pos(pos2)!=4: #Se ambas as posicoes nao sao pontas, soma-se 1 a linha.
            nova_pos1=(linha_pos(pos1)+1,coluna_pos(pos1))
            nova_pos2=(linha_pos(pos2)+1,coluna_pos(pos2))
        elif linha_pos(pos2)==4: #Se a posicao2 e uma ponta da coluna, subtrai-se 4 para ela voltar para a outra ponta (coluna 0).
            nova_pos1=(linha_pos(pos1)+1,coluna_pos(pos1))
            nova_pos2=(linha_pos(pos2)-4,coluna_pos(pos2))
        elif linha_pos(pos1)==4: #Se a posicao1 e uma ponta da coluna, subtrai-se 4 para ela voltar para a outra ponta (coluna 0).
            nova_pos1=(linha_pos(pos1)-4,coluna_pos(pos1))
            nova_pos2=(linha_pos(pos2)+1,coluna_pos(pos2))
    if inc==-1:
        if linha_pos(pos1)!=0 and linha_pos(pos2)!=0: #Se ambas as posicoes nao sao pontas, subtrai-se 1 a linha.
            nova_pos1=(linha_pos(pos1)-1,coluna_pos(pos1))
            nova_pos2=(linha_pos(pos2)-1,coluna_pos(pos2))
        elif linha_pos(pos2)==0: #Se a posicao2 e uma ponta da coluna, soma-se 4 para ela voltar para a outra ponta (coluna 4).
            nova_pos1=(linha_pos(pos1)-1,coluna_pos(pos1))
            nova_pos2=(linha_pos(pos2)+4,coluna_pos(pos2))
        elif linha_pos(pos1)==0: #Se a posicao1 e uma ponta da coluna, soma-se 4 para ela voltar para a outra ponta (coluna 4).
            nova_pos1=(linha_pos(pos1)+4,coluna_pos(pos1))
            nova_pos2=(linha_pos(pos2)-1,coluna_pos(pos2))
    return (nova_pos1,nova_pos2)
#A funcao codifica_c ira dar a posicao a seguir na coluna - caso incremento seja igual a 1 - ou dar a posicao anterior da mesma coluna, caso o incremento seja igual a -1.
def codifica_r(pos1,pos2):
    nova_pos1=(linha_pos(pos1),coluna_pos(pos2))
    nova_pos2=(linha_pos(pos2),coluna_pos(pos1))
    return (nova_pos1,nova_pos2)
#A funcao codifica_r troca as colunas da posicao 1 e 2, que corresponde ao retangulo formado.

def codifica_digrama(digrm,chave,inc):
    figure=figura(digrm,chave)
    string_cod=''
    if figure[0]=='l': #Verifica se a figura feita pelo digrm e uma linha. Se for, vai chamar a codifica_l e devolver o caracter correspondente as novas posicoes.
        pos_cod=codifica_l(figure[1],figure[2],inc)
        for i in range(len(figure)-1):
            string_cod=string_cod+ref_chave(chave,pos_cod[i])
    elif figure[0]=='c': #Verifica se a figura feita pelo digrm e uma coluna. Se for, vai chamar a codifica_c e devolver o caracter correspondente as novas posicoes.
        pos_cod=codifica_c(figure[1],figure[2],inc)
        for i in range(len(figure)-1):
            string_cod=string_cod+ref_chave(chave,pos_cod[i])
    else: #Verifica se a figura feita pelo digrm e um retangulo. Se for, vai chamar a codifica_r e devolver o caracter correspondente as novas posicoes.
        pos_cod=codifica_r(figure[1],figure[2])
        for i in range(len(figure)-1):
            string_cod=string_cod+ref_chave(chave,pos_cod[i])
    return string_cod
#A funcao codifica_digrama vai verificar qual a figura feita pela string, e devolve a string corresponde as letras nas novas posicoes.

def codifica(mens,chave,inc):
    mensagem_final=''
    tuplo_mens=tuple(digramas(mens))
    for i in range(len(mens)//2):
        digrm=tuplo_mens[i*2:(i+1)*2]
        mensagem_final=mensagem_final+str(codifica_digrama(digrm,chave,inc))
    return mensagem_final
#A funcao codifica devolve, dependendo do incremento (1 ou -1) a string correspondente a codificao ou descodificao da string, atraves da posicao
#da letra na chave, utilizando a digramas como auxiliar e a codifica_digrams para codificar os digrams, dois a dois.