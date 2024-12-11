with open ('saida.html', 'w') as arq:
    numero1 = 1
    numero2 = 1
    arq.write('<table border =1>')
    while numero1 <= 10 and numero2 <= 10:
        if numero2 == 1:
            arq.write('<tr>')
        arq.write(f'<td>{numero1} X {numero2}</td>')
        arq.write(f'<td>{numero1*numero2}</td>')
        numero2 += 1
        if numero2 > 10:
            arq.write('</tr>')
            numero1 += 1
            numero2 = 1
    arq.write('</table>')
