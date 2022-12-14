# Расчет ежемесячных платежей для достижения целевой суммы (пенсии)

from numpy import negative
import numpy_financial as npf

try:
    ставка = float(input("\nВведите процентную ставку [0.05]: "))
    лет = float(input("Введите количество лет: "))
    желаемая_сумма = float(input("Введите желаемую сумму [500000]: "))

    result = npf.pmt(rate=ставка/12, nper=лет*12, pv=0, fv=желаемая_сумма)
    print("="*30)
    print(f"Срок: {лет} лет\nСтавка: {ставка} %\nЖелаемая сумма: {желаемая_сумма} ₽")
    print("-"*30)
    print(f"Ежемесячное внесение: {negative(result):.2f} ₽")
    print("="*30)
except:
    print("Ошибка. Проверьте вводимые значения.")