import threading
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
#randint minimo e máximo são exatamente os colocados no randint


class Gerenciador(ScreenManager):
    pass


class Main(Screen):

    def update_func(self):
        maximo = int(self.ids.participantes.text)
        for e in range(25):
            sorteado = randint(1,maximo)
            self.ids.resultado.text = str(sorteado)
            sleep(0.2)
        self.ids.resultado.theme_text_color = "Custom"
        self.ids.resultado.text_color = (0,1,0,1)


    def sortear(self, maximo):
        self.ids.resultado.theme_text_color = "Error"
        # self.ids.resultado.text_color = (0, 1, 0, 1)
        # for e in range(50):
        #     numero = randint(1,int(maximo))
        #     self.ids.resultado.text = str(numero)
        #     sleep(0.2)
        threading.Thread(target=self.update_func).start()

class SorteadorApp(MDApp):
    def build(self):
        gerenciador = Gerenciador()
        gerenciador.add_widget(Main(name='Principal'))
        return gerenciador

if __name__ == "__main__":
    sorteador = SorteadorApp()
    sorteador.run()