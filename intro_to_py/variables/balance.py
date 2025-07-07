deposit = 1000
balance = deposit * (1.05**5)
print(f'In five years you will have: ${round(balance, 2):,}')

#Same with augmented assignment
balance2 = 1000
balance2 *= 1.05**5
print(f'In five years you will have: ${round(balance2, 2):,}')


      