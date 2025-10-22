import matplotlib.pyplot as plt
# Seus dados
dados = [
    (1607, 5.00, 0.00),
    (2010, 4.55, 0.45),
    (2412, 3.04, 1.96),
    (2813, 2.03, 2.97),
    (3216, 1.36, 3.64),
    (3618, 0.91, 4.09),
    (4021, 0.61, 4.39),
    (4423, 0.41, 4.59),
    (4825, 0.27, 4.73),
    (5227, 0.18, 4.82),
    (5629, 0.12, 4.88),
    (6032, 0.08, 4.92),
    (6433, 0.05, 4.95),
    (6836, 0.04, 4.96),
    (7238, 0.02, 4.98),
    (7641, 0.01, 4.99),
    (8043, 0.01, 4.99),
    (8444, 0.01, 4.99),
    (8847, 0.00, 5.00),
 ]
# Separando os dados
x = [item[0] for item in dados]
y1 = [item[1] for item in dados]
y2 = [item[2] for item in dados]
# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Y1')
plt.plot(x, y2, label='Y2')
# Configurando rótulos e título
plt.xlabel('X')
plt.ylabel('Valores')
plt.title('Gráfico de Dispersão')
plt.legend()
# Exibindo o gráfico
plt.grid(True)
plt.show()
