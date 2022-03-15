from pickle import TRUE
from flask import Flask, render_template #Importamos flask y 
                                         #render_template 
                                         #para poder usarlo

app = Flask(__name__)

@app.route('/') #Define la ruta raiz
def Principal():
    return render_template('index.html')

@app.route('/tablas') #Define la ruta tablas
def Tabla():
    return render_template('tabla.html')

if __name__ == '__main__': #Levanta el servidor web flask
    app.run(debug=True) #levanta el servidor y el debug lo refresca
