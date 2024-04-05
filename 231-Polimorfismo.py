# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem


    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando -', self.mensagem)
        return True


class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando -', self.mensagem)
        return True
    

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada!')
    else:
        print('Notificação não enviada!')


# Tem dois métodos diferentes para chamar esse método: 
# Posso instânciar a classe dentro da função:
notificar(NotificacaoSms('POST de uma mensagem do tipo SMS...'))

# Ou podemos instânciar a classe e passa-la para dentro do método:
msg_email = NotificacaoEmail('POST de uma mensagem do tipo E-mail...')
notificar(msg_email)