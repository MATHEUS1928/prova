import database as db
import sqlite3
import os
import unittest

class TestCadastroLivro(unittest.TestCase):
    def setUp(self):
        
        self.banco_teste = "banco_teste.db"
        db.criar_tabela(nome_banco= self.banco_teste)
    
    def tearDown(self):
        if os.path.exists(self.banco_teste):
            os.remove(self.banco_teste)
            
    def test_cadastro_livro_com_sucesso(self):
    
        abobora = db.cadastro_livro("matheus","isabelly",2024,self.banco_teste)
        
        self.assertEqual("Livro cadastrado com Sucesso",abobora)
        
class TesteDeleteLivro(unittest.TestCase):
    def setUp(self):
        
        self.test_banco = "banco_teste.db"
        db.criar_tabela(nome_banco= self.test_banco)
    
    def tearDown(self):
        if os.path.exists(self.test_banco):
            os.remove(self.test_banco)

    def test_delete_livro_com_sucesso(self):
        
        db.cadastro_livro("viellas","vh",2025,self.test_banco)
        abobora1 = db.delete_livro(1,self.test_banco)
        
        self.assertTrue(abobora1)
        
if __name__ == "__main__":
    unittest.main()
    