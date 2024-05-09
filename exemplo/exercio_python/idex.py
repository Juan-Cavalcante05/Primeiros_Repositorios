import time

nome = str(input('Digite seu nome completo: ')).strip().upper()
print('o programa ira verificar se voçe tem -silva no nome- ....')
time.sleep(1)
if 'silva' in nome:
    print('seu nome contem: silva')
else:
    print('seu nome não contem: silva')