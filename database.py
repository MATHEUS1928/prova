import sqlite3 

def banco_connect(nome_banco = "livraria.db"):
    conn = sqlite3.connect(nome_banco)
    return conn 

def criar_tabela(nome_banco = "livraria.db"):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()
    
    cursor.execute(""" CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER NOT NULL,
        status TEXT DEFAULT 'não lido' NOT NULL
    )                       
                    """)
    
    conn.commit()
    conn.close()

def cadastro_livro(titulo:str,autor:str,ano_publicacao,nome_banco = "livraria.db"): 

    if titulo.strip() == "":
        return "Título não pode ficar em branco"
    
    if autor.strip() == "":
        return "Autor não pode ficar em branco "

    if ano_publicacao  > 2026:
        return "Ano da publicação não pode ser maior que o ano atual"
    else :
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()
                
        cursor.execute("INSERT INTO livros (titulo,autor,ano_publicacao) VALUES (?,?,?)",(titulo,autor,ano_publicacao))
                
        conn.commit()
        conn.close() 
        return "Livro cadastrado com Sucesso"
     
    
def delete_livro(id,nome_banco = "livraria.db"): 
    if id <= 0 :
        return "Identificação Invalida"
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM livros WHERE id =?",(id,))
    livro = cursor.fetchone()
    
    if not livro :
        conn.close()
        return "O livro inserido não consta no sistema"
    else:
        cursor.execute("DELETE FROM livros WHERE id = ?",(id,))
        deletou = cursor.rowcount
        
        if deletou > 0:
            conn.commit()
            conn.close() 
            return True 
        else:
            conn.close()
            return False
        
def update_livro(id,status,nome_banco = "livraria.db"): 
    if id <= 0 :
        return "Identificação Invalida"
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM livros WHERE id =?",(id,))
    status1 = cursor.fetchone()
    
    if not status1 :
        conn.close()
        return "O livro inserido não consta no sistema"
    else:
        cursor.execute("UPDATE livros SET status = ? WHERE id = ?",(status,id))
        modificou = cursor.rowcount
        
        if modificou > 0:
            conn.commit()
            conn.close() 
            return True
        else:
            conn.close()
            return False
def get_livro(id,nome_banco = "livraria.db"):

    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros WHERE id= ?",(id,))
    todos_livros = cursor.fetchall()

    conn.commit()
    conn.close()

    return todos_livros
