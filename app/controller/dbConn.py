from mysql import connector


class DbEscola:
    def __init__(self):
        self.conn = connector.connect(host='localhost', database='escola', user='root', password='', autocommit=True)
        self.cursor = self.conn.cursor()
        self.close()

    def close(self):
        self.conn.close()

    def open(self):
        self.conn = connector.connect(host='localhost', database='escola', user='root', password='', autocommit=True)
        self.cursor = self.conn.cursor()

    def create(self, aluno):
        self.open()
        query = f"""  INSERT INTO colaboradores values ("{aluno['matricula']}", "{aluno['nome']}",
                "{aluno['email']}", "{aluno['curso']}");"""
        self.cursor.execute(query)
        self.close()

    def update(self, aluno):
        self.open()
        query = f"""  UPDATE colaboradores
                        SET nome = "{aluno['nome']}", email = "{aluno['email']}", curso = "{aluno['curso']}"
                        WHERE matricula = {aluno['matricula']} limit 1;"""
        self.cursor.execute(query)
        self.close()

    def read(self, matricula=None):
        self.open()
        colab = {'matricula': str, 'nome': str, 'email': str, "curso": str}
        colabs = []
        if not matricula:
            query = """  SELECT * FROM colaboradores;   """
            self.cursor.execute(query)
            for value in self.cursor.fetchall():
                colab['matricula'] = value[0]
                colab['nome'] = value[1]
                colab['email'] = value[2]
                colab['curso'] = value[3]
                colabs.append(colab.copy())
                colab.clear()
            self.close()
            return colabs
        else:
            query = f"""  SELECT * FROM colaboradores WHERE matricula ={matricula};   """
            self.cursor.execute(query)
            res = self.cursor.fetchone()
            colab['matricula'] = res[0]
            colab['nome'] = res[1]
            colab['email'] = res[2]
            colab['curso'] = res[3]
            self.close()
            return colab

    def excluir(self, matricula):
        query = f"""  DELETE FROM colaboradores WHERE matricula = "{matricula}"   """
        self.open()
        self.cursor.execute(query)
        self.close()
