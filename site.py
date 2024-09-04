from flask import Flask, render_template

app= Flask(__name__)

#colocar a 1º pag no site
#route---> oque vemn depois do dominio ex: site.com/home ; site.com/usuario .... route= caminho depois do nome do meu dominio 
#funçao --->    oque voce quer exipir na quela pag
#tempalte

@app.route("/")
def homeoag():
    return render_template("homepage.html")
@app.route("/pag1")
def contatos():
    return render_template("teste.html")
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html")
#colocar ele no ar 
if __name__ == "__main__":
    app.run(debug=True)