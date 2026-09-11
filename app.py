import streamlit as st 
import database as db
import pandas as pd

db.criar_tabela()

st.title("FORMULARIO LIVROS",text_alignment="center")

st.markdown("#### ---Cadastro livro---",text_alignment="center")

with st.form("Cadastro_livro"):
    titulo = st.text_input("titulo",placeholder= "Coloque aqui o título do seu livro")
    autor = st.text_input("autor",placeholder= "Coloque aqui o nome do autor desse livro")
    ano_publicacao = st.number_input("ano",placeholder= "Coloque aqui o ano de publicação do seu livro",step = 1,min_value = 2000)
    
    btn_cadastro_livro = st.form_submit_button("Cadastrar")
    
    if btn_cadastro_livro :
        msg = db.cadastro_livro(titulo,autor,ano_publicacao)
        st.warning(msg)

st.markdown("#### ---Delete Livro---",text_alignment="center")

with st.form("Delete_Livro"):
    id = st.number_input("id do seu livro",placeholder="coloque aqui o id do seu livro",step = 1)

    btn_delete_livro = st.form_submit_button("Deletar")
    
    if btn_delete_livro:
        msg_delete = db.delete_livro(id)
        if msg_delete == True:
            st.success("Livro Deletado")
        else:
            st.warning("Livro não encontrado")
             
    
        
st.markdown("#### ---Modificar Livro---",text_alignment="center")

with st.form("modificar_livro"):

    id = st.number_input("id do seu livro",placeholder="coloque aqui o id do seu livro",step = 1)
    status = st.selectbox("status",("lendo","lerei","lido"),placeholder= "Status atual do seu livro")
    

    btn_modificar_livro = st.form_submit_button("Modificar")
    
    if btn_modificar_livro:
        msg_modificar = db.update_livro(id,status)
        if msg_modificar == True:
            st.success("Livro Modificado")
        else:
            st.warning(msg_modificar)

#todos_livros = {
  #"calories": [420, 380, 390],
  #"duration": [50, 40, 45]
#}

#df = pd.DataFrame(db.get_livro(id,), index = ["livro1 ", "day2", "day3"])

#print(df)

#todos_livros = {
  #"Livros": [id


#df = pd.DataFrame([db.get_livro],columns = [id,titulo,autor,ano_publicacao]) 

st.markdown("#### ---Lista dos livros---",text_alignment="center")

st.dataframe(todos_alunos,column_config=[1,"id",2,"titulo",3,"autor",4,"ano_publicacao"])