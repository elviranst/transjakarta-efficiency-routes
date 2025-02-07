def get_route(path = "input.txt"):
    # Fungsi buat baca file dan dapetin koridor, kasus, dan halte transitnya
    koridor = {} # Koridor
    rute = []    # Rute

    f = open(path) # Open file
    halte = []     # Halte yang ada
    for i in range(1, int(f.readline()) + 1):  # Looping sebanyak N koridor
        temp = f.readline().strip().split("-") # Baca perbaris dan split berdasarkan "-" untuk dapetin koridornya
        halte += temp             # Tambahin ke list halte
        koridor[str(i)] = temp    # Update koridor
    
    for _ in range(int(f.readline())):          # Looping sebanyak M kasus
        temp = f.readline().strip().split("-")  # Baca perbaris buat dapetin start dan end dari setipa kasus
        rute.append(temp)                       # Append ke rute
    f.close()   # Close file

    T_halte = [x for x in halte if halte.count(x) > 1] # Pilih halte yang muncul lebih dari 1 kali buat dapetin 
                                                       # Halte transitnya aja
    
    return koridor, rute, T_halte

def get_coridor(koridor, place):
    # Fungsi buat dapetin semua koridor yang lewat di satu halte
    res = []  # Inisiasi list hasil (koridor" yang lewat halte itu)
    for coridor, route in koridor.items(): # Looping setiap koridornya
        if place in route:       # Jika halte di dalam koridor
            res.append(coridor)  # Update res
    return res                   # Return res

def cek_rute(koridor, ranc_rute, tujuan):
    # Fungsi buat ngecek apakah tujuan ada 
    # di dalam koridor di rancangan rute
    for coridor in ranc_rute: # looping koridor di rancangan rute
        if tujuan in koridor[coridor]: # jika tujuan ada di salah satu koridor di rancangan rute
            return True # langsung return True
    return False # Jika sampai akhir loop enggak ada return False


# Main
koridor, rute, T_halte = get_route('input.txt') # Baca input dan dapetin 
                                                # koridor, rute, dan halte transitnya
hasil = "" # Inisiasi Hasil buat nyetor hasil tiap" case

for case, rute in enumerate(rute): # looping sebanyak M casenya
    start, tujuan = rute # Pisahin rute jadi start sma tujuan
    path = [[x] for x in get_coridor(koridor, start)]   # Buat Path awal, path itu adalah list yang isinya 
                                                        # list dari rute yang melewati halte start
    res_rute, kond = None, True  # Inisiasi Rute hasil sebagai None dan Kondisi pengulangan sebagai True
    while kond: # Mulai loop
        # Mengecek apakah tujuan sudah ada di dalam path
        for ranc_rute in path:  # loop rancangan rute di dalam path
            if cek_rute(koridor, ranc_rute, tujuan): # Cek apakah tujuan ada di dalam rancangan rute
                # Jika ada
                kond = False         # Kondisi loop awal jadi False biar bsa keluar dari while
                res_rute = ranc_rute # Rute hasil = rancangan rute
                break                # Break looping for
        
        # Jika gak ada satupun rancangan rute yang memuat tujuan
        temp_rute = [] # inisiasi temp rute kyk tempat buat rancangan rute yang baru
        for ranc_rute in path: # Looping rancangan rute di dalam path
            for halte in koridor[ranc_rute[-1]]: # Looping halte" yang ada di koridor rancangan rute
                if halte in T_halte: # Jika haltenya termasuk halte transit
                    transit = get_coridor(koridor, halte) # Cek koridor apa aja yang ada di situ
                    for c_trans in transit: # Looping koridor" itu
                        if c_trans not in ranc_rute: # kalo koridornya gk ada di rancangan rute sebelumnya
                            temp_rute.append(ranc_rute + [c_trans]) # Isi temp_rute dengan rancangan rute sebelumnya 
                                                                    # Ditambah koridor itu
        
        path = temp_rute # Ganti path yang lama dengan temp_rute (path yang baru)
    
    # Jika udah keluar dari while
    hasil_case = "Case #{} : {}".format(case + 1, " ".join(res_rute))
    hasil += (hasil_case + '\n') # Tambahin Hasil dengan res_rute (tambahin enter jangan lupa)
    print(hasil_case) # print

# Write
w = open("output.txt", "w")
w.write(hasil)
w.close()