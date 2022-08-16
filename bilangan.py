import os,sys
"""
MAU RECODE SILAHKAN TAPI CANTUMKAN NAMA AUTHOR YA AJG :)
"""
def bilangan():
	os.system("clear")
	print("\nTOOLS KALKULATOR\nAuthor : Iwan Dev")
	print("\n1. Pertambahan")
	print("2. perkalian")
	print("3. pengurangan")
	print("4. Pembagian")
	x = input("choose : ")
	if x in[""]:
		print("pilih yang benar")
	elif x in["1","01"]:
		bilangan1 = int(input("\nmasukkan bilangan ke 1 : "))
		bilangan2 = int(input("masukkan bilangan ke 2 : "))
		print(f"Hasil Pertambahan {bilangan1}+{bilangan2} : ",bilangan1+bilangan2)
	elif x in["2","02"]:
		bilangan1 = int(input("\nmasukkan bilangan ke 1 : "))
		bilangan2 = int(input("masukkan bilangan ke 2 : "))
		print(f"Hasil Perkalian {bilangan1}*{bilangan2} : ",bilangan1*bilangan2)
	elif x in["3","03"]:
		bilangan1 = int(input("\nmasukkan bilangan ke 1 : "))
		bilangan2 = int(input("massukan bilangan ke 2 : "))
		print(f"Hasil Pengurangan {bilangan1}-{bilangan2} : ",bilangan1-bilangan2)
	elif x in["4","04"]:
		bilangan1 = int(input("\nmassukan bilangan ke 1 : "))
		bilangan2 = int(input("masukkan bilangan ke 2 : "))
		print(f"Hasil Pembagian {bilangan1}/{bilangan2} : ",bilangan1/bilangan2)
	else:
		print("pilih yang benar")


bilangan()
