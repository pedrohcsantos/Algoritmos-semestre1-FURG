# Faça um programa em python que leia o nome de 4 times de futebol que estão em uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4. Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual time foi campeão (se empatar, perguntar quem foi campeão).

time1 = str(input("Informe o primeiro time: "))
time2 = str(input("Informe o segundo time: "))
time3 = str(input("Informe o terceiro time: "))
time4 = str(input("Informe o quarto time: "))

print(f"Informe os gols do jogo {time1} x {time2}: ")
gols_time1_jogo1 = int(input(f"Gols do {time1}: "))
gols_time2_jogo1 = int(input(f"Gols do {time2}: "))

print(f"Informe os gols do jogo {time3} x {time4}: ")
gols_time3_jogo2 = int(input(f"Gols do {time3}: "))
gols_time4_jogo2 = int(input(f"Gols do {time4}: "))

if gols_time1_jogo1 > gols_time2_jogo1:
	print(f"O {time1} foi para a final! ")
	time_final1 = time1
else:
	if gols_time1_jogo1 == gols_time2_jogo1:
		classificacao1 = str(input(f"Qual time se classificou na partida {time1} x {time2}? "))
		if classificacao1 == time1:
			print(f"O {time1} foi para a final! ")
			time_final1 = time1
		else:
			print(f"O {time2} foi para a final! ")
			time_final1 = time2
	else:
		print(f"O {time2} foi para a final! ")
		time_final1 = time2

if gols_time3_jogo2 > gols_time4_jogo2:
	print(f"O {time3} foi para a final! ")
	time_final2 = time3
else:
	if gols_time3_jogo2 == gols_time4_jogo2:
		classificacao2 = str(input(f"Qual time se classificou {time3} x {time4}? "))
		if classificacao2 == time3:
			print(f"O {time3} foi para a final! ")
			time_final2 = time3
		else:
			print(f"O {time4} foi para a final! ")
			time_final2 = time4
	else:
		print(f"O {time4} foi para a final! ")
		time_final2 = time4
			
print(f"Informe os gols da final {time_final1} x {time_final2}: ")
gols_final1 = int(input(f"Gols do {time_final1}: "))
gols_final2 = int(input(f"Gols do {time_final2}: "))

if gols_final1 > gols_final2:
	print(f"O {time_final1} foi campeão! ")
else:
	if gols_final1 == gols_final2:
		campeao = str(input("Qual time ganhou a partida? "))
		if campeao == time_final1:
			print(f"O {time_final1} foi campeão! ")
		else:
			print(f"O {time_final2} foi campeão! ")
	else:
		print(f"O {time_final2} foi campeão! ")
