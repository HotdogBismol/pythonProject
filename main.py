import tkinter as tk
import requests

SERVIDOR = "localhost"
PUERTO = "8080"
CLIENTE = "Python"

class CalculadoraGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x200")  # Establece el tamaño de la ventana

        self.resultado_label = tk.Label(self, text="")
        self.resultado_label.pack()

        # Crear los campos de entrada
        self.num1_label = tk.Label(self, text="Número 1:")
        self.num1_label.pack()  # Empaqueta el widget en la ventana

        self.num1_entry = tk.Entry(self)  # Campo de entrada para el primer número
        self.num1_entry.pack()

        self.num2_label = tk.Label(self, text="Número 2:")
        self.num2_label.pack()

        self.num2_entry = tk.Entry(self)  # Campo de entrada para el segundo número
        self.num2_entry.pack()



        button_container1 = tk.Frame(self)
        button_container1.pack()  # Empaqueta el contenedor en la ventana

        self.suma_button = tk.Button(button_container1, text="Suma", command=self.restSuma) #Suma
        self.suma_button.pack(side="left")  # Coloca el botón a la izquierda

        self.resta_button = tk.Button(button_container1, text="Resta", command=self.restResta) #Resta
        self.resta_button.pack(side="left")

        self.multiplicacion_button = tk.Button(button_container1, text="Multiplicacion",command=self.restMulti) #Multiplicacion
        self.multiplicacion_button.pack(side="left")

        self.division_button = tk.Button(button_container1, text="Division",command=self.restDivi) #Division
        self.division_button.pack(side="left")



        button_container2 = tk.Frame(self)
        button_container2.pack()  # Empaqueta el contenedor en la ventana

        self.potencia_button = tk.Button(button_container2, text="Potencia", command=self.restPot) #Potencia
        self.potencia_button.pack(side="left")

        self.raiz_button = tk.Button(button_container2, text="Raiz", command=self.restRaiz) #Raiz
        self.raiz_button.pack(side="left")

        self.modulo_button = tk.Button(button_container2, text="Modulo", command=self.restModu) #Modulo
        self.modulo_button.pack(side="left")



        button_container3 = tk.Frame(self)
        button_container3.pack()  # Empaqueta el contenedor en la ventana

        self.cos_button = tk.Button(button_container3, text="Cos", command=self.restCos) #Coseno
        self.cos_button.pack(side="left")

        self.cosh_button = tk.Button(button_container3, text="Cosh", command=self.restCosh) #Coseno Hiperbolico
        self.cosh_button.pack(side="left")

        self.expo_button = tk.Button(button_container3, text="e", command=self.restExpo) #Exponencial
        self.expo_button.pack(side="left")

        self.facto_button = tk.Button(button_container3, text="Factorial", command=self.restFact) #Factorial
        self.facto_button.pack(side="left")

        self.loga_button = tk.Button(button_container3, text="Log", command=self.restLoga) #Logaritmo
        self.loga_button.pack(side="left")



        button_container4 = tk.Frame(self)
        button_container4.pack()  # Empaqueta el contenedor en la ventana

        self.seno_button = tk.Button(button_container4, text="Sen", command=self.restSen) #Seno
        self.seno_button.pack(side="left")

        self.senoh_button = tk.Button(button_container4, text="Senh", command=self.restSenh)   #Senh
        self.senoh_button.pack(side="left")

        self.tan_button = tk.Button(button_container4, text="Tan", command=self.restTan)   #Tangente
        self.tan_button.pack(side="left")

        self.tanh_button = tk.Button(button_container4, text="Tanh",command=self.restTanh)   #Tangente Hiperbolica
        self.tanh_button.pack(side="left")



    def restSuma(self):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/suma?num1={num1}&num2={num2}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restResta(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/resta?numeroUno={num1}&numeroDos={num2}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restMulti(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/multiplicacion?numeroUno={num1}&numeroDos={num2}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restDivi(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/division?numero_1={num1}&numero_2={num2}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restCos(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/cos?cos={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restCosh(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/cosh?cosh={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restExpo(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/e?e={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restFact(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/factorial?base={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restLoga(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/logaritmo?log={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restModu(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/modulo?num1={num1}&num2={num2}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restPot(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/potencia?num1={num1}&num2={num2}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restRaiz(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/raizCuadrada?raiz={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restSen(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/sin?seno={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restSenh(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/sinh?senoh={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restTan(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/tan?tan={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)

    def restTanh(self):
        num1 = float(self.num1_entry.get())
        print(num1)
        num2 = float(self.num2_entry.get())
        print(num2)
        url = f"http://{SERVIDOR}:{PUERTO}/elRest/webresources/webresources/tanh?tanh={num1}&tcliente={CLIENTE}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                resultado = response.json()  # Suponiendo que el servidor REST devuelve un JSON con el resultado
                self.resultado_label.config(text=f"Resultado: {resultado}")
                print("Resultado:", resultado)
            else:
                print("Error en la solicitud al servidor:", response.status_code)
        except Exception as e:
            print("Error:", e)



if __name__ == "__main__":
    app = CalculadoraGUI()  # Crea una instancia de la clase CalculadoraGUI
    app.mainloop()  # Inicia el bucle principal de la interfaz gráfica
