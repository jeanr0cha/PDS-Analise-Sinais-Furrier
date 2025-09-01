
import numpy as np
import matplotlib.pyplot as plt

# Frequência do sinal senoidal
frequencia_sinal = 5  # Hz

# Tempo total do sinal
tempo_total = 1  # segundos

# Taxa de amostragem
taxa_amostragem = 100 # amostras por segundo

# Crie o vetor de tempo
tempo = np.linspace(0, tempo_total, int(taxa_amostragem * tempo_total))

# Gere o sinal senoidal contínuo
sinal_continuo = np.sin(2 * np.pi * frequencia_sinal * tempo)

# Plote o sinal contínuo
plt.figure(figsize=(10, 4))
plt.plot(tempo, sinal_continuo)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal Senoidal Contínuo (5 Hz)')
plt.grid(True)
plt.show()

# Taxa de amostragem
taxas_amostragem = [100, 50, 25]  # amostras por segundo

#Criando vetor para cada taxa de amostragem

for taxa in taxas_amostragem:
  tempo_amostrado = np.linspace(0, tempo_total, int(taxa * tempo_total))
  sinal_amostrado = np.sin(2 * np.pi * frequencia_sinal * tempo_amostrado)

  # Crie o vetor de tempo para a taxa atual
  tempo = np.linspace(0, tempo_total, int(taxa * tempo_total))

  # Gere o sinal senoidal contínuo
  sinal_continuo = np.sin(2 * np.pi * frequencia_sinal * tempo)

  # Plote o sinal contínuo usando stem
  plt.figure(figsize=(10, 4))
  plt.plot(tempo, sinal_continuo)
  plt.stem(tempo, sinal_continuo, linefmt='r-', basefmt='k-')
  plt.xlabel('Tempo (s)')
  plt.ylabel('Amplitude')
  plt.title('Sinal Senoidal Contínuo (5 Hz)')
  plt.grid(True)
  plt.show()