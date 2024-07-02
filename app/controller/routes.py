from app import app
from flask import render_template, request, redirect, url_for, flash
from app.controller.dbConn import DbEscola


@app.route('/', methods=['GET', 'POST'])
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        matricula = request.form['matricula']
        nome = request.form['nome']
        email = request.form['email']
        curso = request.form['curso']
        aluno = {'matricula': matricula, 'nome': nome, 'email': email, 'curso': curso}
        try:
            db = DbEscola()
            db.create(aluno)
        except Exception as erro:
            flash(erro.__str__())
        else:
            flash(f'{nome.capitalize()} foi cadastrado com sucesso!')
        return redirect(url_for('create'))


@app.route('/read')
def read():
    db = DbEscola()
    alunos = db.read()
    return render_template('read.html', alunos=alunos)


@app.route('/update/', methods=['POST', 'GET'])
@app.route('/update/<matricula>')
def update(matricula=None):
    db = DbEscola()
    if request.method == "GET":
        if matricula or request.args.get('matricula'):
            if request.args.get('matricula'):
                matricula = request.args.get('matricula')
            aluno = db.read(matricula)
            return render_template('update.html', aluno=aluno)
        else:
            alunos = db.read()
            return render_template('update.html', alunos=alunos)
    else:
        matricula = request.form['matricula']
        nome = request.form['nome']
        email = request.form['email']
        curso = request.form['curso']
        aluno = {'matricula': matricula, 'nome': nome, 'email': email, 'curso': curso}
        db.update(aluno)
        flash(f'Dados do colaborador "{nome}" foram atualizado com sucesso!')
        return redirect(url_for('update'))


@app.route('/delete/', methods=['GET', 'POST'])
@app.route('/delete/<matricula>')
def delete(matricula=None):
    db = DbEscola()
    if request.method == 'GET':
        if matricula:
            aluno = db.read(matricula)
            db.excluir(matricula)
            flash(f'Colaborador "{aluno['nome']}" de matricula "{aluno['matricula']}" foi excluido com sucessor!')
            return redirect(url_for('delete'))
        else:
            alunos = db.read()
            return render_template('delete.html', alunos=alunos)
    else:
        matricula = request.form.get('matricula')
        aluno = db.read(matricula)
        db.excluir(matricula)
        flash(f'Colaborador "{aluno['nome']}" de matricula "{aluno['matricula']}" foi excluido com sucessor!')
        return redirect(url_for('delete'))
