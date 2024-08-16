from database import db, Usuario, Anuncio

db.connect()

db.create_tables([Usuario, Anuncio])

# Criando Usuarios

# usuario = Usuario.create(nome="Maria", email="maria@email.com", senha="123456")
# print("Novo usuario:", usuario.id, usuario.nome, usuario.email)

# LISTANDO USUARIOS
# lista_usuarios = Usuario.select()
# print("Listando Usuarios")
# for u in lista_usuarios:
#     print("-",u.id, u.nome, u.email)

#OBTENDO USUARIO PELO ID
# usuario = Usuario.get(Usuario.id == 1)
# print("usuario pelo id", usuario.id, usuario.nome)

#OBTENDO USUARIO PELO EMAIL
# joao = Usuario.get(Usuario.email == "joao@email.com")
# print("Usuario:", joao.id, joao.nome, joao.email)

#ATUALIZANDO UM DADO
# maria = Usuario.get(Usuario.email == "maria@email.com")
# maria.nome = "Maria Python"
# maria.save()
# print("maria atualizada para:", maria.nome)

# TENTANTO CRIAR UM USUARIO COM EMAIL DUPLICADO, POREM TRATANDO O ERRO
# print("tentando criar um usuario com e-amil duplicado")
# try:
#     usuario_duplicado = Usuario.create(nome="duplicado", email="maria@email.com", senha="123456")
# except:
#     print("endereço de email já cadastrado")

# DELETANDO UM USUARIO
# usuario_deletado = Usuario.get(Usuario.email == "teste@teste.com")
# usuario_deletado.delete_instance()

# try:
#     Usuario.get(Usuario.email == "teste@teste.com")
# except:
#     ("Usuario deletado")

# maria = Usuario.get( Usuario.email == "maria@email.com")

# anuncio = Anuncio.create(
#     usuario = maria,
#     titulo = "Briffering de Terça",
#     descricao = "Projeto para entrega de dados de campanhas para clientes",
#     valor = 6500
# )   

# print("Novo anuncio:", anuncio.id, anuncio.titulo)

# Anuncio.create(usuario = maria, titulo = "Anuncio 1", descricao = "Primeiro anuncio", valor = 1000)
# Anuncio.create(usuario = maria, titulo = "Anuncio 2", descricao = "Segundo anuncio", valor = 4000)
# Anuncio.create(usuario = maria, titulo = "Anuncio 3", descricao = "Terceiro anuncio", valor = 1000)

# print("Anuncios maria:")
# anuncios_maria = Anuncio.select().join(Usuario).where(Usuario.email == "maria@email.com")
# for a in anuncios_maria:
#     print("-", a.id, a.titulo, a.descricao)

try:
    Anuncio.delete().execute()
    print("Quantidade de anuncios: ", Anuncio.select().count())
except:
    print("erro ou anuncio")