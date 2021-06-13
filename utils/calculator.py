import PySimpleGUI as sg
import numpy as np

from predicter import predict
from errors import check, error_msg

def prob_msg(p):
    if p >= 0 and p < 0.25:
        return "Muy improbable"
    elif p >= 0.25 and p < 0.5:
        return "Improbable"
    if p >= 0.5 and p < 0.75:
        return "Probable"
    if p >= 0.75 and p <= 1:
        return "Muy probable"

layout = [[sg.Text('Edad                       '), sg.InputText(size=(8,))],
          [sg.Text('Sexo                       '), sg.InputText(size=(8,))],
          [sg.Text('Tipo de dolor pectoral'), sg.InputText(size=(8,))],
          [sg.Text('Tension en reposo    '), sg.InputText(size=(8,))],
          [sg.Text('Colesterol                '), sg.InputText(size=(8,))],
          [sg.Text('Glucemia en ayunas '), sg.InputText(size=(8,))],
          [sg.Text('Electrocardiograma   '), sg.InputText(size=(8,))],
          [sg.Text('PPM maximas         '), sg.InputText(size=(8,))],
          [sg.Text('Angina inducida       '), sg.InputText(size=(8,))],
          [sg.Text('Depresion ST           '), sg.InputText(size=(8,))],
          [sg.Text('Pendiente                '), sg.InputText(size=(8,))],
          [sg.Text('no vasos mayores    '), sg.InputText(size=(8,))],
          [sg.Text('Thal                        '), sg.InputText(size=(8,))],
          [sg.Button('Calcular', button_color='sea green', key='submit')],
          [sg.Text('', key='output', size=(30,2))],
          #[sg.Button('Info', key='info')],
          #[sg.Button('Ayuda', key='help')],
          [sg.Button('Cerrar', button_color='indian red', key='q')]]

main_window = sg.Window('Calculadora riesgo cardiovascular', layout, disable_close=False,
                        disable_minimize=False)

while True:
    event, value = main_window.Read()
    if event == 'submit':
        sample = [value[0],value[1],value[2],value[3],value[4],value[5],
                  value[6],value[7],value[8],value[9],value[10],value[11],
                  value[12]]
        if check(sample):
            sample = [float(value[0]),float(value[1]),float(value[2]),
                      float(value[3]),float(value[4]),float(value[5]),
                      float(value[6]),float(value[7]),float(value[8]),
                      float(value[9]),float(value[10]),float(value[11]),
                      float(value[12])]
            prob = predict(np.array(sample).reshape(1,-1))
            
            main_window.Element('output').Update("Probabilidad de enfermedad: " + 
                                                 str(round(prob[0][1],2)) + '\n' +
                                                 prob_msg(round(prob[0][1],2)), 
                                                 text_color='black')
        else:
            main_window.Element('output').Update('La entrada es incorrecta. ' +
                                              error_msg(sample),
                                              text_color='red')
    elif event == 'q':
        break
main_window.Close()

'''    
def help_window():
    layout_ayuda = [[sg.Text('Edad: Medida en años')],
          [sg.Text('Sexo: 0:mujer 1:varon ')],
          [sg.Text('Tipo de dolor pectoral:' + '\n'+
                   '1:angina pectoral tipica' + '\n'+
                   '2:angina pectoral tipica' + '\n'+
                   '3:no producido por angina' + '\n'+
                   '0:asintomatico')],
          [sg.Text('Tension en reposo    ')],
          [sg.Text('Colesterol                ')],
          [sg.Text('Glucemia en ayunas ')],
          [sg.Text('Electrocardiograma   ')],
          [sg.Text('PPM maximas         ')],
          [sg.Text('Angina inducida       ')],
          [sg.Text('Depresion ST           ')],
          [sg.Text('Pendiente                ')],
          [sg.Text('no vasos mayores    ')],
          [sg.Text('Thal                        ')],
          [sg.Button('Volver', button_color='indian red', key='q')]]
    return sg.Window('Ayuda', layout_ayuda)
'''
