# 1) MELHORAR O MÉTODO DE DAR REFRESH NAS SENHAS GERADAS
# 2) MELHORAR MEU ALGORITMO DE GERAÇÃO DE SENHAS
# 3) POSICIONAR MELHOR O LABEL "Password Length" DO TKINTER

from tkinter import *
import random
import pyperclip


class MyApp():
    def __init__(self, parent):

        # Parâmetros de bordas/espaços dos widgets
        
        button_width = 7            # comprimento horizontal do botão 
        button_largura = '2m'       # largura do botão
        button_espessura = '1m'     # espessura do botão
        buttons_frame_padx = '3m'   # largura do frame
        buttons_frame_pady = '2m'   # espessura do frame
        buttons_frame_ipadx = '8m'  # espaço vertical de distância ocupado por um widget em relação a outro vizinho
        buttons_frame_ipady = '2m'  # espaço horizontal de distância ocupado por um widget em relação a outro vizinho
        
        # Frame principal
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()

        # Frame dos botões
        self.buttons_frame = Frame(self.frame)
        self.buttons_frame.pack(side=BOTTOM,
                                ipadx=buttons_frame_ipadx,
                                ipady=buttons_frame_ipady,
                                padx=buttons_frame_padx,
                                pady=buttons_frame_pady)

        # Frame da barra de rolagem
        self.slider_frame = Frame(self.frame)
        self.slider_frame.pack(side=TOP,
                               ipadx='3m',
                               ipady='1m',
                               padx='1m',
                               pady='2m')

        # Barrinha de rolagem para definir o tamanho da senha
        self.slider = Scale(self.slider_frame,
                            orient=HORIZONTAL,
                            command=self.select,
                            from_=4, to=74,
                            length=150,
                            font=('Arial', 11, 'bold'))
        self.slider.pack(side=LEFT, ipadx=32)
        
        self.Label = Label(self.slider_frame, text='Password Length')
        self.Label.configure(font=('Helvetica', 11, 'bold'))
        self.Label.pack(side=LEFT, ipadx=10)

        # Botão que executará o gerador de senha
        self.button_generator = Button(self.frame, command=self.copy_button)
        self.button_generator.configure(text='  Copy  ',
                                        bg='blue',
                                        fg='white',
                                        pady=3,
                                        font=('Helvetica', 11, 'bold')
                                        )
        self.button_generator.pack(side=RIGHT, padx=20)

        # Campo onde a senha aparecerá após ser gerada 
        self.entrada = Entry(self.frame,
                             width=34,
                             bd=4)
        self.entrada.pack(side=LEFT, padx=10)

        # Botões parâmetro para a senha
        self.button_maiusculas = Button(self.buttons_frame, command=self.tirar_maiusculas)
        self.button_maiusculas.configure(text='A-Z',
                                         bg='green',
                                         width=button_width,
                                         padx=10,
                                         pady=button_espessura)
        self.button_maiusculas.pack(side=LEFT, padx=10)

        self.button_minusculas = Button(self.buttons_frame, command=self.tirar_minusculas)
        self.button_minusculas.configure(text='a-z',
                                         bg='green',
                                         width=button_width,
                                         padx=10,
                                         pady=button_espessura)
        self.button_minusculas.pack(side=LEFT, padx=10)

        self.button_numeros = Button(self.buttons_frame, command=self.tirar_numeros)
        self.button_numeros.configure(text='0-9',
                                      bg='green',
                                      width=button_width,
                                      padx=10,
                                      pady=button_espessura)
        self.button_numeros.pack(side=RIGHT, padx=10)

        self.button_simbolos = Button(self.buttons_frame, command=self.tirar_simbolos)
        self.button_simbolos.configure(text='!@#$%^&*',
                                       bg='green',
                                       width=button_width,
                                       padx=10,
                                       pady=button_espessura)
        self.button_simbolos.pack(side=RIGHT, padx=10)

        # Variáveis/Métodos contendo as listas de caracteres
        self.lista_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*8
        self.lista_minusculas = 'abcdefghijklmnopqrstuvwxyz'*8
        self.lista_simbolos = '!@#$%^&*()?'*8
        self.lista_numeros = '0123456789'*8
        self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)

        # Variável para contar o número de botões apertados ao mesmo tempo 
        self.contador = 0
        

        
    def tirar_numeros(self):
        if self.contador == 3 and self.button_numeros['bg'] == 'green':
            pass
        
        else:
            if self.button_numeros['bg'] == 'green' and self.lista_numeros == '0123456789'*8:
                self.button_numeros['bg'] = 'red'
                self.contador += 1 
                self.lista_numeros = ''
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)
            else:
                self.button_numeros['bg'] = 'green'
                self.contador -= 1 
                self.lista_numeros = '0123456789'*8
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)

            
    def tirar_maiusculas(self):
        if self.contador == 3 and self.button_maiusculas['bg'] == 'green':
            pass
        
        else:
            if self.button_maiusculas['bg'] == 'green' and self.lista_maiusculas == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*8:
                self.button_maiusculas['bg'] = 'red'
                self.contador += 1 
                self.lista_maiusculas = ''
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)
            else:
                self.button_maiusculas['bg'] = 'green'
                self.contador -= 1 
                self.lista_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*8
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)


    def tirar_minusculas(self):
        if self.contador == 3 and self.button_minusculas['bg'] == 'green':
            pass
        
        else:
            if self.button_minusculas['bg'] == 'green' and self.lista_minusculas == 'abcdefghijklmnopqrstuvwxyz'*8:
                self.button_minusculas['bg'] = 'red'
                self.contador += 1 
                self.lista_minusculas = ''
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)
            else:
                self.button_minusculas['bg'] = 'green'
                self.contador -= 1 
                self.lista_minusculas = 'abcdefghijklmnopqrstuvwxyz'*8
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)
            

    def tirar_simbolos(self):
        if self.contador == 3 and self.button_simbolos['bg'] == 'green':
            pass
        
        else:
            if self.button_simbolos['bg'] == 'green' and self.lista_simbolos == '!@#$%^&*()?'*8:
                self.button_simbolos['bg'] = 'red'
                self.contador += 1 
                self.lista_simbolos = ''
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)
            else:
                self.button_simbolos['bg'] = 'green'
                self.contador -= 1 
                self.lista_simbolos = '!@#$%^&*()?'*8
                self.lista = (self.lista_maiusculas+self.lista_minusculas+self.lista_simbolos+self.lista_numeros)
    
        
    def select(self, val):
        '''This algorithm reads the last two characters generated and checks if
        the next one is not equal to them. This is made to avoid characters
        repetition on the nearby'''
        self.sel = int(val)
        self.characters_counter = self.sel
        self.senha = []
        while self.characters_counter != 0:
            self.gerador = random.choice(self.lista)
            if len(self.senha) > 2:
                if self.senha[self.sel-(self.characters_counter+2)] != self.gerador != self.senha[self.sel-(self.characters_counter+1)]:
                        self.senha.append(self.gerador)
                        self.characters_counter-=1
            else:
                self.senha.append(self.gerador)
                self.characters_counter-=1
        self.senha = "".join(self.senha)
        self.entrada.delete(0, END)
        self.entrada.insert(0, self.senha)

    def copy_button(self):
        self.copiado = self.entrada.get()
        pyperclip.copy(self.copiado)
                  
        
root = Tk()
root.geometry('430x152')
root.resizable(False, False)
root.title('Password Generator')

myapp = MyApp(root)
root.mainloop()


