from flask import Flask


app = Flask(__name__)

@app.route("/")
def numeros_primos():
    qtdTotal = 100
    primos = "1,2,"
    candPrimo = 3
    qtdEncontrados = 2
    ehPrimo = 1

    while qtdEncontrados < qtdTotal:
        for i in range(2, candPrimo):
            if candPrimo % i == 0:
                ehPrimo = 0
                break
        if ehPrimo == 1:
            primos = primos + str(candPrimo) + ','
            qtdEncontrados +=1
        ehPrimo = 1    
        candPrimo += 1
    return primos
            

    

if __name__ == "__main__": 
    app.run(debug=True, port=5000)