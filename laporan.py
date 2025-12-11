def lapor(benar):
    for i, hasil in enumerate(benar, start=1):
        print(f"{i}: " + ("Benar" if hasil == True else "Salah"))
    print(f"Rata-rata nilai Anda adalah: {round(sum(benar) / len(benar) * 100)}")