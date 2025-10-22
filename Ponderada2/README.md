# Ponderada de Programação – LED Interno (Arduino UNO)

## Introdução
&emsp;Nesta atividade, o objetivo foi compreender o funcionamento básico do Arduino UNO e aplicar conceitos de lógica de programação para controlar um LED.
A proposta consistia em fazer o LED acender e apagar em intervalos definidos, simulando o efeito de piscar.
Posteriormente, o mesmo código foi adaptado para um LED externo, conectado em um protoboard e simulado no Tinkercad.

# RC Circuit (Arduino + Python) — Data capture and visualization

This repository contains a simple RC (resistor-capacitor) experiment where an Arduino-compatible sketch streams voltage measurements over the serial port and a Python script parses that output and produces the visualization shown in the figure.

What this project does
- The Arduino code (provided here as a Python-format file named `import matplotlib.py`) runs on an Arduino UNO or compatible board. It measures voltages related to charging/discharging a capacitor in a small RC circuit and prints timestamped values to the serial monitor.
- The included Python script reads the serial output (or a pasted serial log), parses the timestamp and voltage columns, and generates plots showing: the capacitor voltage during charge, the resistor voltage during discharge, and a comparison plot.

Files in this repo
- `import matplotlib.py` — contains the Arduino sketch (exported or stored in this file). Treat it as the source code to upload to the Arduino IDE. The file also contains a Python visualization script (see below) — if you split them, keep the Arduino sketch for the board and the Python script for visualization.
- `demo.mp4` — a short video demonstrating the circuit running and the live serial output being recorded. The video is embedded below.
- `README.md` — this file.

How the experiment is organized (brief)
- Circuit: Arduino UNO, capacitor (10 uF / 25 V), a large resistor (Re = 1 MΩ) for the slow charge path and a small discharge resistor (Rd = 100 Ω). A push-button or switch is used to toggle charge/discharge.
- Measurements: The Arduino reads analog voltages and prints them with timestamps (milliseconds). The serial output is a plain-text table of time and measured voltages (CSV-like or whitespace-delimited).

Expected serial output format
Use one of these simple formats the Python parser accepts (example lines):

		0, 0.12, 4.88
		100, 0.14, 4.86

Where columns are: timestamp_ms, Vr (voltage across resistor), Vc (voltage across capacitor)

How to run (Windows PowerShell)
1) Upload the Arduino sketch to your Arduino UNO using the Arduino IDE. If the code is in `import matplotlib.py`, open it and paste the Arduino portion into a `.ino` sketch.
2) Option A — Use the live serial port:
	 - Open a serial terminal (Arduino IDE Serial Monitor or any serial terminal) at the baud rate the sketch uses (commonly 9600 or 115200).
	 - Copy the serial output to a text file (for example `serial_log.txt`). If you use the Arduino Serial Monitor, select all text and save it.
3) Option B — Use the provided `demo.mp4` to inspect the recorded behavior or to extract the serial text manually.

Parsing and plotting with Python
The repository includes a Python script (in the same `import matplotlib.py` file or as a separate script you create) that:
- Reads a serial log file or pasted serial text.
- Parses time and voltage columns.
- Produces three plots: capacitor charge (Vc vs time), resistor discharge (Vr vs time), and a combined comparison.

If you want a minimal standalone Python script (recommended to separate concerns), create `plot_serial.py` with the following behavior:

- Requirements: Python 3.8+ and matplotlib, pandas (optional)

Install dependencies in PowerShell (one-time):

```powershell
python -m pip install --user matplotlib pandas
```

Run the parser (example, for a file called `serial_log.txt`):

```powershell
python plot_serial.py serial_log.txt
```

The script will save PNGs of the three plots and open them interactively (if your platform supports it).

Embedding the demo video
Below is the demo video showing the circuit running and the serial monitor output. If your Markdown viewer supports video embedding, it will show; otherwise open `demo.mp4` in a video player.

<video controls width="640">
	<source src="demo.mp4" type="video/mp4">
	Your browser does not support the video tag. Open `demo.mp4` in your video player.
</video>

Notes and cleanup
- The original slide images and TinkerCAD / Fritzing instructions (intended for in-lab assembly) were removed from this README to keep the repository focused on the code + data workflow.
- If you prefer the Arduino code and the Python plotting code to be in separate files, I can split `import matplotlib.py` into `arduino_sketch.ino` and `plot_serial.py` and add a small test and example serial log.

Troubleshooting
- If your Python script can't parse the log, open the `serial_log.txt` and ensure the data lines match the expected three-column (time, Vr, Vc) format separated by commas or whitespace. If your Arduino sketch prints extra text (headers or prompts), remove them or modify the parser to skip non-numeric lines.

Want me to split files or add the plot script?
# Experimento Circuito RC — Arduino + Python (versão final)

Este repositório contém um experimento de circuito RC (resistor-capacitor). A placa Arduino mede tensões relacionadas ao carregamento/descarga do capacitor e envia valores pelo monitor serial. O arquivo `Data.py` neste repositório contém um exemplo de código Python que gera os gráficos usados para análise (os dados podem vir de um arquivo de log gravado a partir do monitor serial ou ser inseridos manualmente no script).

Resumo do que está no repositório
- `Data.py` — script Python que lê dados (exemplos embutidos) e plota as curvas de tensão. Atualmente contém um vetor de dados de exemplo e gera o gráfico comparativo.
- `Figure_1.png` — figura usada como visualização dos resultados (gerada a partir dos dados). (Se desejar, a figura pode ser substituída por saída nova do `Data.py`).
- `Recording 2025-10-22 004704.mp4` — gravação do experimento e do monitor serial (vídeo demonstrativo).
- `README.md` — este arquivo.

Formato de dados aceito / estrutura
- Cada linha de dado deve ter 3 valores: tempo_em_ms, Vr (tensão no resistor), Vc (tensão no capacitor).
- Exemplo de linha aceita:

		0, 0.12, 4.88

Como `Data.py` está organizado (explicação rápida)
- O arquivo contém um array de tuplas com (timestamp_ms, Vr, Vc). O script separa as colunas e traça dois conjuntos de dados (Vr e Vc) contra o tempo usando matplotlib.
- O código é um bom ponto de partida: você pode substituí-lo por leitura de arquivo (csv/txt) ou por leitura direta da porta serial (COMx).

Instruções para executar (Windows PowerShell)
1) Instale dependências (uma vez):

```powershell
python -m pip install --user matplotlib pandas
```

2) Para executar o `Data.py` que já contém dados de exemplo:

```powershell
python Data.py
```

3) Se preferir processar um arquivo `serial_log.txt` (uma linha por registro):

- Posicione `serial_log.txt` na mesma pasta e edite `Data.py` para carregar os dados desse arquivo (ou solicite que eu faça essa alteração; posso adicionar leitura automática de arquivo). Uma alternativa é executar `python Data.py serial_log.txt` caso eu adicione suporte a argumento de linha de comando.

O que o script gera
- Um gráfico (janela interativa) com as duas curvas (Vr e Vc) e, se desejado, arquivos PNG salvos automaticamente. O exemplo atual desenha o gráfico e chama `plt.show()`.

Imagens e Vídeo (uso no README)
- A figura `Figure_1.png` está disponível no repositório; certifique-se de que ela representa a saída do `Data.py` (se não, posso gerar uma nova imagem a partir dos dados e atualizar o arquivo).
- O vídeo `Recording 2025-10-22 004704.mp4` demonstra a montagem em funcionamento e a saída do monitor serial. Ele já está incluído no repositório; se quiser um nome de arquivo mais curto posso renomeá-lo.

Respostas às perguntas/etapas originais do exercício
- Copiar valores do MONITOR SERIAL e colar no Python: Sim — o `Data.py` já contém um vetor de exemplo com valores. Para usar valores reais, basta gerar `serial_log.txt` a partir do Monitor Serial e processá-lo (posso adicionar essa funcionalidade automaticamente).
- Montar um gráfico da carga no capacitor: Sim — `Data.py` plota `Vc` vs `tempo`.
- Montar um gráfico da descarga no resistor: Sim — `Data.py` plota `Vr` vs `tempo`.
- Comparar os dois gráficos: Sim — o gráfico combinado mostra ambas as curvas; ajustar legendas e cores melhora a comparação (posso atualizar o script para rótulos em Português e salvar as figuras).

Sugestões de melhorias que posso aplicar agora (escolha uma ou mais):
1) Adicionar leitura de arquivo `serial_log.txt` via argumento de linha de comando e parsing robusto (ignorar linhas não-numéricas).
2) Adicionar leitura da porta serial (argumento `--serial COM3`), com escolha de baud rate.
3) Gerar e salvar automaticamente `Figure_1.png` a partir dos dados atuais e substituir o arquivo existente.
4) Traduzir/ajustar rótulos do gráfico para Português e melhorar layout (legenda, título, unidades).

Verificação rápida (estado atual)
- `Data.py` existe e contém dados de exemplo e um plot funcional (já pronto para execução).
- `Figure_1.png` e `Recording 2025-10-22 004704.mp4` existem na pasta do projeto e são referenciados aqui.

Próximo passo (se quiser que eu acrescente):
- Posso implementar a opção 1 (leitura de `serial_log.txt`) e a opção 4 (melhorar rótulos e salvar PNGs). Diga quais opções prefere e eu aplico as mudanças imediatamente.

