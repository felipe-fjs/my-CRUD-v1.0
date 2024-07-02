# my-CRUD-v1.0
 Aqui vai estar meu primeiro sistema CRUD (Create, Read, Update e Delete)
para cadastro de colaboradores (alunos) de evento!

 O sistema não possuo complexidade nem no front nem no Back-end, pois não adicionei criptografia
nem qualquer segurança ao projeto, coisas que irei adicionar/aperfeiçoar para a v2.0 do my-CRUD.

(Pretendo hospedá-lo em algum servidor para interação com o projeto)

    Tecnologias utilizadas:
        * Python
        * Flask
            * render_template()
            * request
            * redirect()
            * url_for()
            * flash()
        * Mysql
            * mysql-connector
        * Bootstrap5
    
    Para a conexão com o banco de dados criei/utilizado uma Classe "DbEscola" que contém os métodos:
        * close()
        * open()
        * create()
        * update()
        * read()
        * delete()