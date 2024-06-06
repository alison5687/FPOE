import requests
import tkinter.messagebox as alerta

class Comunicacion():
    
    def __init__(self, ventanaPrincipal):
        self.url ='http://localhost:8000/v1/hilo'
        self.ventanaPrincipal= ventanaPrincipal
        pass

    def guardar(self,hilo,elasticidad,suavidad,tenacidad,ductilidad):
        try:
            print(hilo,elasticidad,suavidad,tenacidad,ductilidad)
            data= {
                'hilo':hilo,
                'elasticidad':elasticidad,
                'suavidad': suavidad,
                'tenacidad':tenacidad,
                'ductilidad': ductilidad,
                }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def consultar(self, id):
        try:
            response= requests.get(self.url +'/'+ str(id))
            response.raise_for_status()
            data= response.json()
            if not data:
                raise ValueError("Vacio")
            return data
        except Exception as err:
            if isinstance(err, requests.exceptions.HTTPError):
                print(f"HTTP error occurred: {err}")
                alerta.showerror("Error", f"Error HTTP al consultar el hilo: {err}")
            elif isinstance(err, requests.exceptions.RequestException):
                print(f"Request error occurred: {err}")
                alerta.showerror("Error", f"Error de solicitud al consultar el hilo: {err}")
            elif isinstance(err, ValueError):
                print(f"Error al analizar JSON: {err}")
                alerta.showerror("Error", "Error al consultar el hilo: Respuesta JSON no válida.")
            else:
                print(f"Error al consultar: {err}")
                alerta.showerror("Error", "Error al consultar el hilo.")
        return None
    
    def todos(self):
        print("hola")
        try:
            response= requests.get(self.url)
            if response.status_code==200:
                hilos =response.json()
                return hilos
            else:
                alerta.showerror("Error","Error al consultar los hilos")
        except Exception as e:
            print (f"Error al consultar los hilos: {e}")
            alerta.showerror("Error","Error al consultar los hilos.")
        return []
    def buscar(self,id):
        response = requests.get(f"{self.url}/{str(id)}")
        hilo = response.json()
        if not hilo:
            raise ValueError("Respuesta JSON vacía")
        return hilo
    def actualizar(self,id, hilo, elasticidad, suavidad, tenacidad, ductilidad):
        data = {
            'hilo': hilo,
            'elasticidad': elasticidad,
            'suavidad': suavidad,
            'tenacidad': tenacidad,
            'ductilidad': ductilidad
        }
        print(f"URL: {self.url}/{id}")
        print(f"Data: {data}")
        try:
            response = requests.put(f"{self.url}/{id}/", json=data)
            print(f"Response: {response.text}")  # Imprimir la respuesta del servidor
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as e:
            print(f"Other error occurred: {e}")
            return None