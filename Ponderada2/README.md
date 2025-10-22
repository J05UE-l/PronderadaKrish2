# Ponderada de Programação – LED Interno (Arduino UNO)

## Introdução
&emsp;Nesta atividade, o objetivo foi compreender o funcionamento básico do Arduino UNO e aplicar conceitos de lógica de programação para controlar um LED.
A proposta consistia em fazer o LED acender e apagar em intervalos definidos, simulando o efeito de piscar.
Posteriormente, o mesmo código foi adaptado para um LED externo, conectado em um protoboard e simulado no Tinkercad.

# Circuito RC (Arduino + Python) — Aquisição de dados e visualização

Este repositório contém um experimento simples de circuito RC (resistor-capacitor) em que um sketch compatível com Arduino transmite medições de tensão pela porta serial e um script Python interpreta essa saída e produz as visualizações mostradas na figura.

O que este projeto faz
- O código Arduino (fornecido aqui em um arquivo de formato Python chamado `import matplotlib.py`) roda em um Arduino UNO ou placa compatível. Ele mede tensões relacionadas ao carregamento/descarga de um capacitor em um pequeno circuito RC e imprime valores com timestamp no monitor serial.
- O script Python incluído lê a saída serial (ou um log serial colado), analisa as colunas de tempo e tensão e gera gráficos mostrando: a tensão do capacitor durante a carga, a tensão no resistor durante a descarga e um gráfico comparativo.

Arquivos neste repositório
- `import matplotlib.py` — contém o sketch Arduino (exportado ou armazenado neste arquivo). Trate-o como o código-fonte a ser carregado no Arduino IDE. O arquivo também pode conter o script de visualização em Python (veja abaixo) — se você separar os arquivos, mantenha o sketch para o Arduino e o script Python para a visualização.
- `demo.mp4` — vídeo curto demonstrando o circuito em funcionamento e a saída serial sendo registrada. O vídeo está incorporado abaixo.
- `README.md` — este arquivo.

Como o experimento está organizado (resumo)
- Circuito: Arduino UNO, capacitor (10 µF / 25 V), um resistor grande (Re = 1 MΩ) para o caminho de carga lento e um resistor de descarga pequeno (Rd = 100 Ω). Um botão ou chave é usado para alternar entre carga e descarga.
- Medições: o Arduino lê tensões analógicas e as imprime com timestamps (milissegundos). A saída serial é uma tabela em texto simples com tempo e tensões medidas (formato tipo CSV ou delimitado por espaços).

Formato esperado da saída serial
Use um destes formatos simples que o parser Python aceita (linhas de exemplo):

    0, 0.12, 4.88
    100, 0.14, 4.86

Onde as colunas são: timestamp_ms, Vr (tensão no resistor), Vc (tensão no capacitor)

Como executar (Windows PowerShell)
1) Carregue o sketch Arduino no seu Arduino UNO usando o Arduino IDE. Se o código estiver em `import matplotlib.py`, abra-o e cole a parte Arduino em um sketch `.ino`.
2) Opção A — Usar a porta serial ao vivo:
   - Abra um terminal serial (Serial Monitor do Arduino IDE ou outro terminal serial) com a taxa de transmissão (baud) que o sketch usa (comumente 9600 ou 115200).
   - Copie a saída serial para um arquivo de texto (por exemplo `serial_log.txt`). Se usar o Serial Monitor do Arduino, selecione todo o texto e salve.
3) Opção B — Use o `demo.mp4` fornecido para inspecionar o comportamento gravado ou para extrair o texto serial manualmente.


Processamento e plotagem com Python
O repositório inclui o script `Data.py`, que:
- lê um arquivo de log serial ou texto copiado do monitor serial;
- analisa as colunas de tempo e tensão;
- produz três gráficos: carga do capacitor (Vc vs tempo), descarga no resistor (Vr vs tempo) e um gráfico comparativo.

Para um script Python independente, recomenda-se criar `plot_serial.py` com comportamento análogo.

Requisitos
- Python 3.8+
- matplotlib
- pandas (opcional)

Instalação de dependências (PowerShell):

```powershell
python -m pip install --user matplotlib pandas
```

Execução
- Executar o script com os dados embutidos (exemplo):

```powershell
python Data.py
```

- Processar um arquivo de log `serial_log.txt`: coloque o arquivo na mesma pasta e edite `Data.py` para carregar o arquivo ou adapte o script para aceitar um argumento de linha de comando com o caminho do arquivo.

Saída do script
- O script exibe uma janela com os gráficos de Vr e Vc versus tempo. É recomendado salvar as figuras em PNG para documentação e comparação entre ensaios.

Imagens e vídeo
- `Figure_1.png` contém uma visualização de exemplo. Para atualizar a figura com novos dados, execute o script e salve a saída em PNG substituindo este arquivo.
- `Recording 2025-10-22 004704.mp4` demonstra o experimento em funcionamento e a saída do monitor serial.

Respostas às etapas do exercício
- Copiar valores do monitor serial e colar no Python: gere um arquivo `serial_log.txt` a partir do Monitor Serial e processe-o com `Data.py` ou `plot_serial.py`.
- Gerar o gráfico da carga no capacitor: o script plota `Vc` vs tempo.
- Gerar o gráfico da descarga no resistor: o script plota `Vr` vs tempo.
- Comparar os dois gráficos: o gráfico combinado mostra ambas as curvas com legenda e rótulos.

Sugestões de melhorias (opções implementáveis)
1) Adicionar suporte a leitura de arquivo `serial_log.txt` via argumento de linha de comando com parsing robusto (ignorar linhas não numéricas).
2) Adicionar leitura direta da porta serial (opção `--serial COMx`) com parâmetro de baud rate.
3) Gerar e salvar automaticamente `Figure_1.png` a partir dos dados atuais.
4) Traduzir e melhorar rótulos do gráfico (legenda, título, unidades) e ajustar layout.

Verificação rápida
- `Data.py` contém dados de exemplo e um plot funcional.
- `Figure_1.png` e `Recording 2025-10-22 004704.mp4` existem na pasta do projeto.

Próximo passo (implementação)
- Implementar uma ou mais das sugestões acima conforme necessidade do projeto.
```powershell

