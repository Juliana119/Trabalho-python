import os
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# -------------- PDF ----------------
class PDF(FPDF):
    def header(self):
        self.image('kick.png', 150, 10, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(
            30, 10, 'PROJETO PYTHON', 0, 0, 'C')
        self.ln(10)
        self.line(75, 20, 135, 20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 20, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

dadosEstado = pd.read_excel(r'Dados-covid-19-estado.xlsx')
totalDeCasos = dadosEstado["Total de casos"]
casosDia = dadosEstado["Casos por dia"]

pdf = PDF()
pdf.add_page()
texto_1 = "Covid-19"
pdf.image(name='covid_19.png', x=83, y=140, w=90)
pdf.cell(w=0, h=120, txt=texto_1, align='C')
pdf.set_font('Times', '', 17)

# ----------- Text -------------
pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.set_margins(20, 40, 0)
texto =  "As pessoas podem ser reinfectadas mesmo que tenham tido a doença anteriormente ou tenham sido vacinadas; A replicação do vírus acontece no trato respiratório superior (diferentemente da delta e outras variantes, que o fazem na parte inferior), facilitando a propagação" "O 1º caso de COVID-19, a infecção viral pelo novo coronavírus, foi diagnosticado em 24 de fevereiro de 2020 pelo Hospital Israelita Albert Einstein. Dias depois,em 26 de fevereiro, o exame foi confirmado pelo Ministério da Saúde." "Co significa corona, vi vem de vírus, e d representa doença. O número 19 indica o ano de sua aparição, 2019. Esse nome substitui o de 2019-nCoV, decidido provisoriamente após o surgimento da doença respiratória. O novo nome foi escolhido por ser fácil de pronunciar e não ter referência estigmatizante a um país ou a uma população em particular"

pdf.multi_cell(w=165, h=8, txt=texto, align='J')

plt.plot(totalDeCasos)
plt.xlabel('Total de casos')
plt.savefig("exemplo.png")
plt.close()
pdf.image(x=20, y=135, w=175, h=75, name='exemplo.png')

plt.plot(casosDia)
plt.xlabel('Casos por dia')
plt.savefig("exemplo2.png")
plt.close()
pdf.image(x=20, y=215, w=175, h=75, name='exemplo2.png')


pdf.output('teste.pdf')

os.system("pause")