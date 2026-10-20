age = input("Yaşınız: ")
print("5 ildən sonra " + age + 5 + " yaşınız olacaq")

#input() daxil edilən məlumatı mətn kimi daxil edir. Ona görə yaş int() edilir.
#Printdə dırnaqlrdan sonra + yox, vergül(,) qoyulur.Çünki ayrı ayrı məlumatları print olunur
#Düzgünü:

age = int(input("Yaşınız: "))
print("5 ildən sonra ", age + 5, " yaşınız olacaq")
