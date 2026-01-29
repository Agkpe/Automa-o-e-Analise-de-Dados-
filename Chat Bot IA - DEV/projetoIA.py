# Chat Bot C/ IA
   # Titulo
   # Input do chat(campo mensagem)
   # A cada mensagem enviada pelo usuário:
       # mostrar a mensagem que o usuário enviou no chat
       # pegar a pergunta e enviar para IA responder
       # exibir a resposta da IA na tela
       
# Frameworks -> Bibliotecas/ pacotes de códigos criado para resolver um problema em especifico - regras exclusivas
    # StreamLit  -> apenas com Python criar o front e o back end     -- Hashtag tem um video de front do streamlit
    # Flask  / Django  / FastAPI
    
# A IA utilizada sera a OPenAI  - pip install openai streamlit
# Para rodar o código  utilizaremos: streamlit run projetoIA.py(nome do projeto)
import streamlit as st
from openai import OpenAI  #  da biblioteca da openai importa a função ada api da openai, a OpenAI

modelo_ia = OpenAI(api_key="# travei aqui- precisa pegar API e aplicar nessa programação")




st.write("# Chatbot com Ágatha")  # No streamlit os texto seguem formato markdown (# -> para criar titulo)

if not "lista_mensagens" in st.session_state:   # se eu não encontrar historico de mensagem nos cookies do usuário
    st.session_state["lista_mensagens"] = []    # Os colchetes em branco representam o espaço a ser preenchido pelo novo usuario. o session_state verifica os cookies navegador utilizados pelo usuário para ver se ele ja tem uma lista de mensagens, ou seja, utilixou o site, caso contrário não rodará


texto_usuario = st.chat_input("Escreva sua mensagem aqui")  # Bota chat para o usurio escrever, e cria variavel para biblioteca de respostas
  # É possível carregar imagens com o st.file_uploader()

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem ["role"]
    content= mensagem["content"]
    st.chat_message(role).write(content)
    
    
if texto_usuario:
    print(texto_usuario)
    st.chat_message("user").write(texto_usuario)     # entre parenteses determinar quem escreve a mensagem (user/ assistant/ nome)
    mensagem_usuario = {"role": "user", "content": texto_usuario}   # informação para lista
    st.session_state["lista_mensagens"].append(mensagem_usuario)  # Adiciona informação retirada da lista e a coloca no dicionario session state
    #IA responde
    
    resposta_ia = "Você perguntou: " + texto_usuario
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
       
       # Hugging Face - modelo de IA
       # API - maneira de se comunicar com o sistema
       #Langchain - padronização de ferramentas de IA
       