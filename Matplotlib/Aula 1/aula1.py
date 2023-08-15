import matplotlib.pyplot as plt

idade = [14, 15, 16, 18, 22, 25, 28, 29, 30, 31, 33, 35, 38, 40, 45, 55, 50]
salario = [1100, 1350, 1350, 1400, 2100, 2500, 2580, 3000, 3000, 3300, 3580, 10000, 
           14258, 15500, 15500, 16000, 16500]

salario_python = [1100, 1350, 1350, 1400, 2100, 2500, 2580, 3500, 3600, 3700, 3880, 11000, 
           14258, 16000, 17500, 18500, 20500]

plt.style.use('classic')

plt.title("Salario de Desenvolvedores")

plt.plot(idade, salario, color = 'red', 
         marker = 'o', linestyle = '--', label = 'Salário Geral')

plt.plot(idade, salario_python, color = 'black',
         marker = '*', label = 'Salário Python')

plt.xlabel("Idade")
plt.ylabel("Salário")
plt.legend()
plt.tight_layout()

plt.grid(True)
plt.show()

# print(plt.style.available)