import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import joblib

st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    return pd.read_csv('student-mat.csv')

def load_data2():
    return pd.read_csv('data_cleaned.csv')

def main():
    st.title('Prediksi Prestasi Nilai Siswa Berdasarkan Faktor-Faktor Yang Mempengaruhi Menggunakan Model Supervised Learning')
    st.sidebar.title("Selamat Datang!")
    df = load_data2()
    data = load_data()
    with st.sidebar:
        page = option_menu("Pilih Halaman", ["Informasi Dasar","Distribusi", "Pie Chart", "Bar Chart", "Box Plot", "Model Prediksi"])
    if page == "Informasi Dasar":
        st.subheader("Informasi Dasar Dataset yang digunakan")
        st.write(data.head())
        st.write("**Deskripsi Kolom Dataset:**")
        st.write("- **Sekolah (school):** Nama sekolah tempat siswa belajar, dengan nilai 'GP' untuk Gabriel Pereira atau 'MS' untuk Mousinho da Silveira.")
        st.write("- **Jenis Kelamin (sex):** Jenis kelamin siswa, dengan nilai 'F' untuk perempuan atau 'M' untuk laki-laki.")
        st.write("- **Usia (age):** Usia siswa dalam rentang 15 hingga 22 tahun.")
        st.write("- **Alamat (address):** Tipe alamat rumah siswa, dengan nilai 'U' untuk perkotaan atau 'R' untuk pedesaan.")
        st.write("- **Ukuran Keluarga (famsize):** Ukuran keluarga siswa, dengan nilai 'LE3' untuk kurang atau sama dengan 3 orang atau 'GT3' untuk lebih dari 3 orang.")
        st.write("- **Status Tinggal Orang Tua (Pstatus):** Status tinggal bersama orang tua, dengan nilai 'T' untuk tinggal bersama atau 'A' untuk terpisah.")
        st.write("- **Pendidikan Ibu (Medu):** Tingkat pendidikan ibu siswa, dengan nilai numerik dari 0 (tidak ada) hingga 4 (pendidikan tinggi).")
        st.write("- **Pendidikan Ayah (Fedu):** Tingkat pendidikan ayah siswa, dengan nilai numerik dari 0 (tidak ada) hingga 4 (pendidikan tinggi).")
        st.write("- **Pekerjaan Ibu (Mjob):** Pekerjaan ibu siswa, termasuk 'guru', 'perawatan kesehatan', 'layanan sipil', 'di rumah', atau 'lainnya'.")
        st.write("- **Pekerjaan Ayah (Fjob):** Pekerjaan ayah siswa, dengan nilai yang sama seperti Mjob.")
        st.write("- **Alasan Memilih Sekolah (reason):** Alasan siswa memilih sekolah tersebut, termasuk 'dekat dengan rumah', 'reputasi sekolah', 'preferensi kursus', atau 'lainnya'.")
        st.write("- **Wali (guardian):** Wali siswa, dengan nilai 'ibu', 'ayah', atau 'lainnya'.")
        st.write("- **Waktu Tempuh (traveltime):** Waktu tempuh dari rumah ke sekolah dalam rentang waktu tertentu.")
        st.write("- **Waktu Belajar (studytime):** Waktu belajar mingguan siswa dalam jam, dengan rentang tertentu.")
        st.write("- **Kegagalan (failures):** Jumlah kegagalan kelas masa lalu, dengan nilai spesifik yang menunjukkan rentang.")
        st.write("- **Dukungan Pendidikan Tambahan (schoolsup):** Dukungan pendidikan tambahan di luar sekolah, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Dukungan Pendidikan Keluarga (famsup):** Dukungan pendidikan dari keluarga, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Kelas Tambahan (paid):** Kelas tambahan yang dibayar dalam mata pelajaran tertentu, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Aktivitas Ekstrakurikuler (activities):** Keterlibatan dalam aktivitas ekstrakurikuler, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Taman Kanak-kanak (nursery):** Partisipasi dalam taman kanak-kanak, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Pendidikan Tinggi (higher):** Keinginan untuk melanjutkan pendidikan tinggi, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Akses Internet (internet):** Akses internet di rumah, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Hubungan Romantis (romantic):** Kehadiran hubungan romantis, dengan nilai 'ya' atau 'tidak'.")
        st.write("- **Hubungan Keluarga (famrel):** Kualitas hubungan keluarga, dengan nilai dari 1 (sangat buruk) hingga 5 (sangat baik).")
        st.write("- **Waktu Luang (freetime):** Waktu luang setelah sekolah, dengan nilai dari 1 (sangat sedikit) hingga 5 (sangat banyak).")
        st.write("- **Bersenang-senang dengan Teman (goout):** Aktivitas bersosialisasi dengan teman, dengan nilai dari 1 (sangat sedikit) hingga 5 (sangat banyak).")
        st.write("- **Konsumsi Alkohol pada Hari Kerja (Dalc):** Tingkat konsumsi alkohol pada hari kerja, dengan nilai dari 1 (sangat sedikit) hingga 5 (sangat banyak).")
        st.write("- **Konsumsi Alkohol pada Akhir Pekan (Walc):** Tingkat konsumsi alkohol pada akhir pekan, dengan nilai dari 1 (sangat sedikit) hingga 5 (sangat banyak).")
        st.write("- **Kesehatan (health):** Status kesehatan saat ini, dengan nilai dari 1 (sangat buruk) hingga 5 (sangat baik).")
        st.write("- **Absensi (absences):** Jumlah absensi sekolah, dengan nilai dari 0 hingga 93.")
        st.write("- **Nilai Periode Pertama (G1):** Nilai siswa pada periode pertama, dengan nilai dari 0 hingga 20.")
        st.write("- **Nilai Periode Kedua (G2):** Nilai siswa pada periode kedua, dengan nilai dari 0 hingga 20.")
        st.write("- **Nilai Akhir (G3):** Nilai akhir siswa, dengan nilai dari 0 hingga 20.")

    elif page == "Distribusi":
        st.subheader("Distribusi Gender")
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x='sex', palette='coolwarm')
        plt.xlabel('Gender')
        plt.ylabel('Jumlah')
        plt.title('Distribusi Gender')
        st.pyplot()
        st.write("Berdasarkan data di atas, jumlah siswa pria dan wanita hampir seimbang dan tidak memiliki perbedaan yang signifikan.")

        st.subheader("Distribusi Usia")
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x='age', palette='coolwarm')
        plt.xlabel('Usia')
        plt.ylabel('Jumlah')
        plt.title('Distribusi Usia')
        st.pyplot()
        st.write("Dari data di atas, dapat dilihat bahwa rentang usia siswa berkisar antara 16 hingga 22 tahun, dengan mayoritas siswa berusia 16 hingga 17 tahun.")

    elif page == "Pie Chart":
        st.subheader('Distribusi Ukuran Keluarga (famsize)')
        famsize_counts = data['famsize'].value_counts()
        st.write(famsize_counts)
        fig, ax = plt.subplots()
        ax.pie(famsize_counts, labels=famsize_counts.index, autopct='%1.1f%%', startangle=90, colors=['pink', 'lightblue'])
        ax.axis('equal')  
        st.pyplot(fig)
        st.write("Mayoritas siswa berasal dari keluarga dengan ukuran lebih dari 3 orang (GT3), dengan jumlah sebanyak 281 siswa.")
        st.write("Sementara itu, hanya ada 114 siswa yang berasal dari keluarga dengan ukuran kurang atau sama dengan 3 orang (LE3).")
        st.write("Hal ini menunjukkan bahwa mayoritas siswa dalam sampel memiliki ukuran keluarga yang lebih besar dari 3 orang.")

        # Visualisasi untuk kolom 'address'
        st.subheader('Distribusi Alamat')
        address_counts = data['address'].value_counts()
        st.write(address_counts)
        fig, ax = plt.subplots()
        ax.pie(address_counts, labels=address_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
        ax.axis('equal')  
        st.pyplot(fig)
        st.write("Dari distribusi ini, dapat disimpulkan bahwa mayoritas siswa dalam dataset tinggal di perkotaan (U), sementara jumlah siswa yang tinggal di pedesaan (R) lebih sedikit.")

    elif page == "Bar Chart":
        st.subheader('Distribusi Pendidikan Ibu')
        medu_counts = data['Medu'].value_counts().sort_index()
        st.bar_chart(medu_counts)
        st.write("Mayoritas siswa memiliki ibu dengan tingkat pendidikan kategori 2 (103 siswa) dan kategori 4 (131 siswa), yang mungkin mencerminkan tingkat pendidikan menengah hingga tinggi di antara ibu siswa. Jumlah siswa dengan ibu yang memiliki tingkat pendidikan di kategori 0 (tidak ada) dan kategori 1 adalah yang terendah, dengan hanya 3 dan 59 siswa, berturut-turut.")

        # Visualisasi untuk kolom 'Fedu' (tingkat pendidikan ayah)
        st.subheader('Distribusi Pendidikan Ayah')
        fedu_counts = data['Fedu'].value_counts().sort_index()
        st.bar_chart(fedu_counts)
        st.write("Mayoritas siswa memiliki ayah dengan tingkat pendidikan kategori 2 (115 siswa), yang juga menunjukkan tingkat pendidikan menengah yang signifikan di antara ayah siswa. Sementara itu, tidak ada siswa yang dilaporkan memiliki ayah dengan tingkat pendidikan di kategori 0 (tidak ada). Jumlah siswa dengan ayah yang memiliki tingkat pendidikan di kategori 1 dan kategori 4 hampir sama, yaitu 82 dan 96 siswa, berturut-turut.")

        # Visualisasi untuk kolom 'Mjob' (pekerjaan ibu)
        st.subheader('Distribusi Pekerjaan Ibu')
        mjob_counts = data['Mjob'].value_counts()
        st.bar_chart(mjob_counts)
        st.write("Pekerjaan ibu yang paling umum adalah 'other' (lainnya), dengan 141 siswa memiliki ibu dengan pekerjaan ini. Sedangkan pekerjaan ibu yang paling jarang terjadi adalah 'health' (perawatan kesehatan), dengan hanya 34 siswa memiliki ibu dengan pekerjaan ini.")

        # Visualisasi untuk kolom 'Fjob' (pekerjaan ayah)
        st.subheader('Distribusi Pekerjaan Ayah')
        fjob_counts = data['Fjob'].value_counts()
        st.bar_chart(fjob_counts)
        st.write("Pekerjaan ayah yang paling umum adalah 'other' (lainnya), dengan 217 siswa memiliki ayah dengan pekerjaan ini. Sedangkan pekerjaan ayah yang paling jarang terjadi adalah 'health' (perawatan kesehatan), dengan hanya 18 siswa memiliki ayah dengan pekerjaan ini.")
    elif page == "Box Plot":
        st.subheader('Distribusi Waktu Belajar')
        studytime_boxplot = sns.boxplot(x='studytime', y='G3', data=data)
        st.pyplot()
        st.write("Kelompok pertama terdiri dari 105 siswa, dengan rata-rata nilai akhir sebesar 10.05 dan rata-rata waktu belajar sekitar 4.96.")
        st.write("Kelompok kedua memiliki 198 siswa, dengan rata-rata nilai akhir sebesar 10.17 dan rata-rata waktu belajar sekitar 4.22.")
        st.write("Kelompok ketiga memiliki 65 siswa, dengan rata-rata nilai akhir sebesar 11.40 dan rata-rata waktu belajar sekitar 4.64.")
        st.write("Kelompok keempat terdiri dari 27 siswa, dengan rata-rata nilai akhir sebesar 11.26 dan rata-rata waktu belajar sekitar 5.28.")

        # Distribusi Waktu Luang
        st.subheader('Distribusi Waktu Luang')
        freetime_boxplot = sns.boxplot(x='freetime', y='G3', data=data)
        st.pyplot()
        st.write("Kelompok pertama terdiri dari 19 siswa, dengan rata-rata nilai akhir sebesar 9.84 dan rata-rata waktu belajar sekitar 4.75.")
        st.write("Kelompok kedua memiliki 64 siswa, dengan rata-rata nilai akhir sebesar 11.56 dan rata-rata waktu belajar sekitar 4.22.")
        st.write("Kelompok ketiga memiliki 157 siswa, dengan rata-rata nilai akhir sebesar 9.78 dan rata-rata waktu belajar sekitar 4.79.")
        st.write("Kelompok keempat terdiri dari 115 siswa, dengan rata-rata nilai akhir sebesar 10.43 dan rata-rata waktu belajar sekitar 4.33.")
        st.write("Kelompok kelima memiliki 40 siswa, dengan rata-rata nilai akhir sebesar 11.30 dan rata-rata waktu belajar sekitar 4.62.")

    elif page == "Model Prediksi":
        st.header("Model Prediksi")
        file_path = 'gnb.pkl'
        clf = joblib.load(file_path)

        school = st.selectbox('Sekolah', ['Gabriel Pereira (GP)', 'Mousinho da Silveira (MS)'], index=0)
        if school == 'Gabriel Pereira (GP)':
            school = 0
        else:
            school = 1

        sex = st.selectbox('Jenis Kelamin', ['Perempuan', 'Laki-laki'], index=0)
        if sex == 'Perempuan':
            sex = 0
        else:
            sex = 1

        age = st.number_input('Usia', min_value=15, max_value=22, value=15)  

        Medu = st.selectbox('Pendidikan Orang Tua', ['Tidak Ada', 'SD', 'SMP', 'SMA', 'Pendidikan Tinggi'], index=0)
        if Medu == 'Tidak Ada':
            Medu = 0
        elif Medu == 'SD':
            Medu = 1
        elif Medu == 'SMP':
            Medu = 2
        elif Medu == 'SMA':
            Medu = 3
        else:
            Medu = 4

        Fedu = st.selectbox('Pendidikan Ayah', ['Tidak Ada', 'SD', 'SMP', 'SMA', 'Pendidikan Tinggi'], index=0)
        if Fedu == 'Tidak Ada':
            Fedu = 0
        elif Fedu == 'SD':
            Fedu = 1
        elif Fedu == 'SMP':
            Fedu = 2
        elif Fedu == 'SMA':
            Fedu = 3
        else:
            Fedu = 4

        traveltime = st.number_input('Waktu Tempuh', value=0)  
        failures = st.number_input('Kegagalan', value=0)  
        famrel = st.number_input('Hubungan Keluarga', min_value=1, max_value=5, value=1)  
        freetime = st.number_input('Waktu Luang', min_value=1, max_value=5, value=1)  
        goout = st.number_input('Bersenang-senang dengan Teman', min_value=1, max_value=5, value=1)  
        Dalc = st.number_input('Konsumsi Alkohol pada Hari Kerja', min_value=1, max_value=5, value=1)  
        Walc = st.number_input('Konsumsi Alkohol pada Akhir Pekan', min_value=1, max_value=5, value=1)  
        health = st.number_input('Kesehatan', min_value=1, max_value=5, value=1)  
        absences = st.number_input('Absensi', min_value=0, max_value=93, value=0)  
        G1 = st.number_input('Nilai Periode Pertama', min_value=0, max_value=20, value=0)  
        G2 = st.number_input('Nilai Periode Kedua', min_value=0, max_value=20, value=0)  

        address = st.selectbox('Alamat', ['Pedesaan', 'Perkotaan'], index=0)
        if address == 'Pedesaan':
            address_R = True
            address_U = False
        else:
            address_R = False
            address_U = True

        famsize = st.selectbox('Ukuran Keluarga', ['Kurang dari 3', 'Lebih dari atau sama dengan 3'], index=0)
        if famsize == 'Kurang dari 3':
            famsize_GT3 = False
            famsize_LE3 = True
        else:
            famsize_GT3 = True
            famsize_LE3 = False

        Pstatus = st.selectbox('Status Tinggal Orang Tua', ['Terpisah', 'Bersama'], index=0)
        if Pstatus == 'Terpisah':
            Pstatus_A = True
            Pstatus_T = False
        else:
            Pstatus_A = False
            Pstatus_T = True

        Mjob = st.selectbox('Pekerjaan Ibu', ['Di Rumah', 'Perawatan Kesehatan', 'Layanan Sipil', 'Guru', 'Lainnya'], index=0)
        if Mjob == 'Di Rumah':
            Mjob_at_home = True
            Mjob_health = False
            Mjob_other = False
            Mjob_services = False
            Mjob_teacher = False
        elif Mjob == 'Perawatan Kesehatan':
            Mjob_at_home = False
            Mjob_health = True
            Mjob_other = False
            Mjob_services = False
            Mjob_teacher = False
        elif Mjob == 'Layanan Sipil':
            Mjob_at_home = False
            Mjob_health = False
            Mjob_other = False
            Mjob_services = True
            Mjob_teacher = False
        elif Mjob == 'Guru':
            Mjob_at_home = False
            Mjob_health = False
            Mjob_other = False
            Mjob_services = False
            Mjob_teacher = True
        else:
            Mjob_at_home = False
            Mjob_health = False
            Mjob_other = True
            Mjob_services = False
            Mjob_teacher = False

        Fjob = st.selectbox('Pekerjaan Ayah', ['Di Rumah', 'Perawatan Kesehatan', 'Layanan Sipil', 'Guru', 'Lainnya'], index=0)
        if Fjob == 'Di Rumah':
            Fjob_at_home = True
            Fjob_health = False
            Fjob_other = False
            Fjob_services = False
            Fjob_teacher = False
        elif Fjob == 'Perawatan Kesehatan':
            Fjob_at_home = False
            Fjob_health = True
            Fjob_other = False
            Fjob_services = False
            Fjob_teacher = False
        elif Fjob == 'Layanan Sipil':
            Fjob_at_home = False
            Fjob_health = False
            Fjob_other = False
            Fjob_services = True
            Fjob_teacher = False
        elif Fjob == 'Guru':
            Fjob_at_home = False
            Fjob_health = False
            Fjob_other = False
            Fjob_services = False
            Fjob_teacher = True
        else:
            Fjob_at_home = False
            Fjob_health = False
            Fjob_other = True
            Fjob_services = False
            Fjob_teacher = False

        reason = st.selectbox('Alasan Memilih Sekolah', ['Dekat dengan Rumah', 'Reputasi Sekolah', 'Preferensi Kursus', 'Lainnya'], index=0)
        if reason == 'Dekat dengan Rumah':
            reason_course = False
            reason_home = True
            reason_other = False
            reason_reputation = False
        elif reason == 'Reputasi Sekolah':
            reason_course = False
            reason_home = False
            reason_other = False
            reason_reputation = True
        elif reason == 'Preferensi Kursus':
            reason_course = True
            reason_home = False
            reason_other = False
            reason_reputation = False
        else:
            reason_course = False
            reason_home = False
            reason_other = True
            reason_reputation = False

        guardian = st.selectbox('Wali', ['Ibu', 'Ayah', 'Lainnya'], index=0)
        if guardian == 'Ibu':
            guardian_father = False
            guardian_mother = True
            guardian_other = False
        elif guardian == 'Ayah':
            guardian_father = True
            guardian_mother = False
            guardian_other = False
        else:
            guardian_father = False
            guardian_mother = False
            guardian_other = True

        studytime = st.selectbox('Waktu Belajar', ['2 to 5 hours', '5 to 10 hours', '<2 hours'], index=0)
        if studytime == '2 to 5 hours':
            studytime_2to5 = True
            studytime_5to10 = False
            studytime_less2 = False
        elif studytime == '5 to 10 hours':
            studytime_2to5 = False
            studytime_5to10 = True
            studytime_less2 = False
        else:
            studytime_2to5 = False
            studytime_5to10 = False
            studytime_less2 = True

        schoolsup = st.selectbox('Dukungan Pendidikan Tambahan', ['Ya', 'Tidak'], index=0)
        if schoolsup == 'Ya':
            schoolsup_no = False
            schoolsup_yes = True
        else:
            schoolsup_no = True
            schoolsup_yes = False

        famsup = st.selectbox('Dukungan Pendidikan Keluarga', ['Ya', 'Tidak'], index=0)
        if famsup == 'Ya':
            famsup_no = False
            famsup_yes = True
        else:
            famsup_no = True
            famsup_yes = False

        paid = st.selectbox('Kelas Tambahan', ['Ya', 'Tidak'], index=0)
        if paid == 'Ya':
            paid_no = False
            paid_yes = True
        else:
            paid_no = True
            paid_yes = False

        activities = st.selectbox('Aktivitas Ekstrakurikuler', ['Ya', 'Tidak'], index=0)
        if activities == 'Ya':
            activities_no = False
            activities_yes = True
        else:
            activities_no = True
            activities_yes = False

        nursery = st.selectbox('Taman Kanak-kanak', ['Ya', 'Tidak'], index=0)
        if nursery == 'Ya':
            nursery_no = False
            nursery_yes = True
        else:
            nursery_no = True
            nursery_yes = False

        higher = st.selectbox('Pendidikan Tinggi', ['Ya', 'Tidak'], index=0)
        if higher == 'Ya':
            higher_no = False
            higher_yes = True
        else:
            higher_no = True
            higher_yes = False

        internet = st.selectbox('Akses Internet', ['Ya', 'Tidak'], index=0)
        if internet == 'Ya':
            internet_no = False
            internet_yes = True
        else:
            internet_no = True
            internet_yes = False

        romantic = st.selectbox('Hubungan Romantis', ['Ya', 'Tidak'], index=0)
        if romantic == 'Ya':
            romantic_no = False
            romantic_yes = True
        else:
            romantic_no = True
            romantic_yes = False

        kategori = st.selectbox('Kategori Usia', ['Dewasa', 'Lansia'], index=0)
        if kategori == 'Dewasa':
            kategori_Adult = True
            kategori_Elderly = False
        else:
            kategori_Adult = False
            kategori_Elderly = True

    if st.button('Predict'):
        input_data = [[school, sex, age, Medu, Fedu, traveltime, failures, famrel, freetime, goout, Dalc, Walc, health, absences, 
                        G1, G2, address_R, address_U, famsize_GT3, famsize_LE3, Pstatus_A, Pstatus_T, Mjob_at_home, Mjob_health,
                        Mjob_other, Mjob_services, Mjob_teacher, Fjob_at_home, Fjob_health, Fjob_other, Fjob_services, Fjob_teacher,
                        reason_course, reason_home, reason_other, reason_reputation, guardian_father, guardian_mother, guardian_other,
                        studytime_2to5, studytime_5to10, studytime_less2, schoolsup_no, schoolsup_yes, famsup_no, famsup_yes, paid_no,
                        paid_yes, activities_no, activities_yes, nursery_no, nursery_yes, higher_no, higher_yes, internet_no,
                        internet_yes, romantic_no, romantic_yes, kategori_Adult, kategori_Elderly]]
        result = clf.predict(input_data)
        st.write('Hasil prediksi skor G3 adalah:', result[0])
main()
