import sys
import random

Insultos_flojitos = ['Mongol@', 'Tontorron/Tontorrona', 'Fe@']
Insultos_potentillos = ['Cerradit@ de mente', 'Tont@ de mierda', 'Gilipollas']
Insultos_fuertes = ['Me cago en tu madre', 'Te comes las pollas de 5 en 5 y por el culo te la hinco', 'Eres mas fe@ que las piedras']
Insultos_duros = ['aberracion monocromatica', 'Tu mama en vez de darte el pecho te daba la espalda y te decia, "te quiero, pero como amigo"', 'No te quieren ni los perros callejeros']
Insultos_multiples = ['Fea, malparida, cochina, marrana, peluda, apestosa, maloliente', 'chupacojones, esnifacojones, perrita faldera, zorrita, zorda, estupida']
Insultos_supremos = ['Eres un Dalas', 'Eres un alvaro', 'Eres peor que el salseo de youtube']
Insulto_flojito = random.choice(Insultos_flojitos)
Insulto_potentillo = random.choice(Insultos_potentillos)
Insulto_fuerte = random.choice(Insultos_fuertes)
Insulto_duro = random.choice(Insultos_duros)
Insultos_multiples_v = random.choice(Insultos_multiples)
Insulto_supremo = random.choice(Insultos_supremos)

if __name__ == '__main__':

    if sys.argv[1] == 'help':
        print('Escribe alguno de los siguientes comandos en tu consola: python insultator.py Insulto_flojito, Insulto_potentillo ,     Insulto_fuerte, Insulto_duro, Insultos_multiples, Insulto_supremo')

    if sys.argv[1] == 'Insulto_flojito':
        print(Insulto_flojito)

    if sys.argv[1] == 'Insulto_potentillo':
        print(Insulto_potentillo)

    if sys.argv[1] == 'Insulto_fuerte':
        print(Insulto_fuerte)

    if sys.argv[1] == 'Insulto_duro':
        print(Insulto_duro)

    if sys.argv[1] == 'Insultos_multiples':
        print(Insultos_multiples_v)

    if sys.argv[1] == 'Insulto_supremo':
        print(Insulto_supremo)