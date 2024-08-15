import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Classe para a equação do 2º grau
class Equacao:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b

     def get_c(self):
        return self.c

    def set_c(self, c):
        self.c = c    
    
    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def x1(self):
        d = self.delta()
        if d < 0:
            return None  # Não existem raízes reais
        return (-self.b + np.sqrt(d)) / (2 * self.a)

    def x2(self):
        d = self.delta()
        if d < 0:
            return None  # Não existem raízes reais
        return (-self.b - np.sqrt(d)) / (2 * self.a)

    def y(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def __str__(self):
        return f"Equação: {self.a}x^2 + {self.b}x + {self.c} = 0"

# Interface em Streamlit
st.title("Calculadora de Equação do 2º Grau")

# Entrada dos coeficientes
a = st.number_input("Coeficiente a", value=1.0)
b = st.number_input("Coeficiente b", value=0.0)
c = st.number_input("Coeficiente c", value=0.0)

# Criar a equação
equacao = Equacao(a, b, c)

# Calcular delta e raízes
delta_val = equacao.delta()
x1_val = equacao.x1()
x2_val = equacao.x2()

# Exibir os resultados
st.write(f"**Delta (Δ):** {delta_val}")

if delta_val < 0:
    st.write("A equação não possui raízes reais.")
else:
    st.write(f"**Raíz:** X1 = {x1_val}")
    st.write(f"**Raiz:** X2 = {x2_val}")

# Plotar o gráfico da equação
x_vals = np.linspace(-10, 10, 400)
y_vals = equacao.y(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label=f'{a}x² + {b}x + {c}')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.scatter([x1_val, x2_val], [0, 0], color='red')  # Mostrar as raízes no gráfico
plt.title('Gráfico da Equação do 2º Grau')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
st.pyplot(plt)
