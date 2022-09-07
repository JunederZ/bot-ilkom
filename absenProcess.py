import requests

def submit_form(nama, nim, hp, seksi, pekan, pertemuan):
    mk = mkmap[seksi]
    link = f'https://docs.google.com/forms/d/e/1FAIpQLSeQ65nn1sxI2nrLP-CpDL0YnsfPNWMaJUaAJQgSCDtYfbLFPA/formResponse?entry.608390691={nama}&entry.1579586451={nim}&entry.1079795373={hp}&entry.1067113942=S1&entry.1315756331=Fakultas+Matematika+dan+Ilmu+Pengetahuan+Alam&entry.1812004147=(S1)+Sistem+Komputer&entry.1263835528={mk[1]}&entry.{mk[0]}={mk[2]}&entry.148101967={mk[2]}&entry.865534847={seksi}&entry.820195671={mk[3]}&entry.496196548={mk[4]}&entry.644590421={pekan}&entry.73141647={pertemuan}submit=Submit'
    res = requests.get(link)
    print(res.text)
    print(link)


pekan = [
    'Minggu Ke -1',
    'Minggu Ke -2',
    'Minggu Ke - 3',
    'Minggu Ke - 4',
    'Minggu Ke - 5',
]

pertemuan = [
    'Pertemuan Ke-1',
    'Pertemuan Ke-2',
    'Pertemuan Ke-3',
    'Pertemuan Ke-4',
    'Pertemuan Ke-5',
    'Pertemuan Ke-6',
    'Pertemuan Ke-7',
    'Pertemuan Ke-8',
    'Pertemuan Ke-9',
    'Pertemuan Ke-10',
    'Pertemuan ke – 11',
    'Pertemuan ke – 12',
    'Pertemuan ke – 13',
    'Pertemuan ke - 14',
    'Pertemuan ke - 15',
    'Pertemuan ke – 16',
    'Pertemuan ke – 17',
    'Pertemuan ke – 18',
    'Pertemuan ke – 19',
    'Pertemuan ke – 20',
    'Pertemuan ke – 21',
    'Pertemuan ke – 22',
    'Pertemuan ke – 23',
    'Pertemuan ke – 24',
    'Pertemuan ke – 25',
    'Pertemuan ke – 26',
    'Pertemuan ke – 27',
    'Pertemuan ke – 28',
    'Pertemuan ke – 29',
    'Pertemuan ke – 30',
]

mkmap = {
    '1313600003': ['655789696', 'A', "Ari Hendarno, M.Kom", 'Dasar-dasar Pemrograman', 3],
    '1313600006': ['1264841064', 'F', "Ir. Fariani Hermin Indiyah, M.T.", 'Statistika dan Probabilitas', 3],
    '1313600004': ['54974004', 'L', "Dr. Lukman El Hakim, M.Pd.", 'Olimpisme', 1],
    '1313600002': ['935837216', 'M', "Dr. Meiliasari, S.Pd., M.Sc.", 'Bahasa Inggris', 2],
    '1313600007': ['935837216', 'M', "Med Irzal, S.Kom., M.Kom", 'Pengantar TIK', 2],
    '1313600005': ['669808987', 'R', "Ria Arafiyah, S.Si. M.Si.", 'Matematika Diskrit', 3],
    '1000000009': ['1756380006', 'T', "Dr. Tjipto Sumadi, M.Si., M.Pd.", 'Pendidikan Pancasila', 2],
    '1313600001': ['1756380006', 'T', "Drs. Tri Murdiyanto, M.Si.", 'Kalkulus Diferensial', 3],
    '1000000233': ['929135864', 'V', "Venus Khasanah, S.S., M.Pd.", 'Bahasa Indonesia', 2],
}

# submit_form('Kaisan Tsabit', '1313622020','085155488272', '1313600004', pekan[1], pertemuan[1])