'''
    вопрос 1) если писать сюда, кто-то прочитает это??
'''
name_elements ='H He Li Be B C N O F Ne Na Mg Al Si P Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nb Pm Sm Sm Eu Gb Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Ti Pb Bi Po At Rn Fr Ra Ac Th Pa U p Pu Am Cm Bk Cf Es Fm Mb No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og UUe Ubn Ubu Ubb Ubt Ubq Ubp Ubh'
sp = name_elements.split()
tabl_mendel = {}
for i in range(len(sp)):
    tabl_mendel[str(i + 1)] = sp[i]

print(tabl_mendel)
a = input('Введите номер элемента (до 128)? ')
print(tabl_mendel[a] if a in tabl_mendel.keys() else 'Я таких элементов не знаю(')