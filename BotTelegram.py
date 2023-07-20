import telebot

CHAVE_API = "6136884195:AAHQhkSQyYOmsdmpzXry6iLx7Fbuf-Qb1Lc"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["1"])
def pizza(mensagem):
    bot.send_message(
        mensagem.chat.id, "Saindo a pizza pra sua casa: Tempo de espera em 20min"
    )


@bot.message_handler(commands=["2"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o Brabo: em 10min chega ai")


@bot.message_handler(commands=["3"])
def salada(mensagem):
    bot.send_message(
        mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar"
    )


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /1 Pizza
    /2 Hamburguer
    /3 Salada"""
    bot.send_message(mensagem.chat.id, texto)  # Enviar mensagem pelo ID


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(
        mensagem.chat.id,
        "Para enviar uma reclamação, mande um e-mail para reclamação rafarz76dev@gmail.com",
    )  # Enviar mensagem pelo ID


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(
        mensagem.chat.id, "Valeu! RafaRaizer mandou um abraço de volta"
    )  # Enviar mensagem pelo ID


@bot.message_handler(commands=["opcao4"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(
        mensagem.chat.id, "Obrigado, até a próxima!"
    )  # Enviar mensagem pelo ID


# Comandos Final de responder a mensagem
def verificar(mensagem):
    return True


@bot.message_handler(
    func=verificar
)  # todas as funções tem de ter um decorator para quando for executar a função
def responder(mensagem):
    texto = """
    Olá, escolha uma opção para continuar (Clique no item):
     /opcao1 Fazer um pedido
     /opcao2 Reclamar de um pedido
     /opcao3 Mandar um abraço pro RafaRaizer
     /opcao4 Encerrar
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)  # Responder mensagem e texto


bot.polling()  # loop para rodar o bot
