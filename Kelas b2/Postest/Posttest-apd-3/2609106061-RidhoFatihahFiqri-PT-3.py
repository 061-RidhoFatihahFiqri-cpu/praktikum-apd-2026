username = input("Masukkan username: ").lower().strip()
password = input("Masukkan password: ").lower().strip()

if username == "ridhofatihahfiqri":
    if password == "61":
        print("Login berhasil")
        print("Pilih tingkat kesulitan misi: standard, sulit, kritis, penyelematan bumi:")
        Pemilihan_misi = input("Masukkan level misi (1-4): ").lower().strip()

        if Pemilihan_misi == "1":
            reward = 1000
            bonus = 0.2
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        elif Pemilihan_misi == "2":
            reward = 1000
            bonus = 0.5
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        elif Pemilihan_misi == "3":
            reward = 1000
            bonus = 0.8
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        elif Pemilihan_misi == "4":
            reward = 1000
            bonus = 0.12
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        else:
            print("Pilihan level misi tidak valid. Silakan pilih level misi yang tersedia.")
    else:
        print("Password salah. Silakan coba lagi.")
else:
    print("Username tidak ditemukan. Silakan coba lagi.")