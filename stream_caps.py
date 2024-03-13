# Mengimpor modul-modul yang dibutuhkan
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(
    page_title = 'Belajar Streamlit',
    layout='wide'
)

# Mengatur tata letak judul ke tengah dengan CSS
st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 1000px;
            padding-top: 5rem;
            padding-right: 3rem;
            padding-left: 3rem;
            padding-bottom: 5rem;
        }}
        h1 {{
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Kasus Kejahatan Pada Negara US (Los Angeles)')

# Tag Penulis
stringHeader = 'Penulis : **Syarifudin Jaelani**'
st.markdown(stringHeader)

# image = Image.open('dataset_caps/crime2.jpg')
# st.image(image, caption='', use_column_width=True)

# ---------------------------------------------------------------

# Sidebar Content
stringInfo1 = '''
            ### Dataset 
            
           Dataset yang digunakan dalam artikel ini bersumber dari :
            
            1. [Data.gov - Crime Data from 2020 to Present](https://catalog.data.gov/dataset/crime-data-from-2020-to-present)
            
            2. [LA City - Crime Data](https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data)
            '''
st.sidebar.info(stringInfo1)

stringInfo2 = '''
            **Penjelasan Mengenai Dataset Tindak Kriminal**
            
            Kumpulan data ini mencerminkan insiden kejahatan di Kota Los Angeles sejak tahun 2020 hingga saat ini. Data ini ditranskrip dari laporan kejahatan asli yang diketik di atas kertas dan oleh karena itu mungkin ada beberapa ketidakakuratan dalam data. Beberapa bidang lokasi dengan data yang hilang dicatat sebagai (0°, 0°). Kolom alamat hanya disediakan hingga seratus blok terdekat untuk menjaga privasi. Data ini seakurat data yang ada di database.
            '''
st.sidebar.info(stringInfo2)

stringInfoAuthor = '''
            **Kontak Saya:**
            
            📬 syarifudinjaelani@gmail.com\n
            📲 [LinkedIn](https://www.linkedin.com/in/syarifudin-jaelani-b956761b3/)\n
            📰 [Medium](https://medium.com/@syarifudinjaelani)\n
            📑 [GitHub](https://github.com/RIFF7)\n
            🧾 [Instagram](https://www.instagram.com/paper.curt/)
            '''
st.sidebar.info(stringInfoAuthor)

# GAMBAR
col1, col2 = st.columns(2)

with col1:
    # Penjelasan Singkat Mengenai Tidak Kriminal
    string1 = '''
                Di era digital yang penuh teka-teki ini, data bagaikan kunci yang membuka gerbang pemahaman terhadap misteri kriminalitas. Melalui artikel ini, mari kita selami lautan data laporan kriminalitas sejak tahun 2020, menguak pola tersembunyi, dan menemukan jawaban atas pertanyaan-pertanyaan yang membingungkan. Berbekal dataset kaya informasi, kita akan menjelajahi lorong-lorong waktu, menguak tren dan pola kriminalitas yang tak terduga. Dari tanggal kejadian hingga lokasi, jenis kejahatan hingga karakteristik korban, data menjadi kompas yang menuntun kita dalam petualangan ini.\n

                Lebih dari sekadar statistik, analisis mendalam akan membawa kita pada wawasan yang tak ternilai. Kita akan melihat melampaui permukaan, menemukan benang merah yang menghubungkan berbagai kejadian, dan menguak faktor-faktor yang berkontribusi pada maraknya kriminalitas. Namun, perjalanan ini bukan hanya tentang memahami, di akhir petualangan, kita akan menemukan solusi. Data menjadi peta yang menunjukkan jalan menuju penegakan hukum yang lebih efektif dan terciptanya lingkungan yang lebih aman bagi semua.\n

                Mari kita bersama-sama membuka lembaran baru dalam memerangi kriminalitas. Bergabunglah dalam petualangan data ini, demi masa depan yang lebih damai dan terhindar dari rasa was-was.\n
            '''
    st.write(string1)

with col2:
    image = Image.open('dataset_caps/crime2.jpg')
    st.image(image, caption='', use_column_width='auto')

# Tambahkan garis batas horizontal
st.markdown("---")

# ---------------------------------------------------------------

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Tren Waktu Kriminal')

# Membuat Columns Grafik
yearLpr_col, monthLpr_col = st.columns(2)
yearOcc_col, monthOcc_col = st.columns(2)

# Membuat Column Analisa
analisa_col1, analisa_col2 = st.columns(2)

# ---------------------------------------------------------------

# Import Dataset
data_yearLpr = pd.read_csv('dataset_caps/yearLpr_report_count.csv')
data_monthLpr = pd.read_csv('dataset_caps/monthLpr_report_count.csv')
data_yearOcc = pd.read_csv('dataset_caps/yearOcc_report_count.csv')
data_monthOcc = pd.read_csv('dataset_caps/monthOcc_report_count.csv')
data_reportLpr = pd.read_csv('dataset_caps/reportLpr_count.csv')
data_reportOcc = pd.read_csv('dataset_caps/reportOcc_count.csv')
data_crime_day = pd.read_csv('dataset_caps/crime_by_day.csv')
data_crime_count = pd.read_csv('dataset_caps/crime_count_sort.csv')
data_crime_area = pd.read_csv('dataset_caps/crime_by_area.csv')
data_crime_lokasi = pd.read_csv('dataset_caps/crime_by_location.csv')
data_gender = pd.read_csv('dataset_caps/gender_counts.csv')

# ---------------------------------------------------------------

with yearLpr_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_yearLpr).mark_line(point=True).encode(
        x=alt.X('Year_Lpr:O', title='Tahun', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Year_Lpr', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Laporan Kriminal dari Tahun ke Tahun'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

with monthLpr_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_monthLpr).mark_line(point=True).encode(
        x=alt.X('Month_Lpr:O', title='Bulan', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Month_Lpr', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Laporan Kriminal dari Bulan ke Bulan'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

with yearOcc_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_yearOcc).mark_line(point=True).encode(
        x=alt.X('Year_Occ:O', title='Tahun', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Year_Occ', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Kejadian Kriminal dari Tahun ke Tahun'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

with monthOcc_col:
    # Buat plot menggunakan Altair
    chart = alt.Chart(data_monthOcc).mark_line(point=True).encode(
        x=alt.X('Month_Occ:O', title='Bulan', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Jml_Kejahatan:Q', title='Jumlah Laporan Kriminalitas'),
        tooltip=['Month_Occ', 'Jml_Kejahatan']
    ).properties(
        width=600,
        height=400,
        title='Tren Jumlah Kejadian Kriminal dari Bulan ke Bulan'
    ).interactive()

    # Tampilkan plot di aplikasi Streamlit
    st.altair_chart(chart, use_container_width=True)

# Bagian Analisa pada chart
with analisa_col1:
    st.markdown('#### Analisa Tren Tahun Laporan dan Kejadian Kriminal')
    string2 = '''
                - Terdapat peningkatan jumlah kejahatan yang dilaporkan dari tahun 2020 hingga 2022, diikuti dengan sedikit penurunan pada tahun 2023.
                
                - Perbandingan antara jumlah kejahatan yang dilaporkan dan kejadian menunjukkan adanya perbedaan, dengan jumlah kejahatan yang dilaporkan cenderung sedikit lebih rendah daripada jumlah kejahatan yang terjadi pada tahun-tahun tertentu.
                
                - Meskipun terdapat perbedaan antara jumlah kejahatan yang dilaporkan dan yang terjadi, terdapat konsistensi yang cukup besar dalam tren kejahatan dari tahun ke tahun.
            '''
    st.write(string2)
    
    stringInfo8 = '''
                Analisis ini menunjukkan adanya tren peningkatan jumlah kejahatan dari tahun ke tahun, meskipun terdapat perbedaan antara jumlah kejahatan yang dilaporkan dan yang terjadi. Perbedaan ini menunjukkan adanya potensi untuk meningkatkan akurasi dan keandalan data kejahatan di masa mendatang. Evaluasi lebih lanjut terhadap proses pelaporan kejahatan mungkin diperlukan untuk memastikan akurasi dan konsistensi dalam pelaporan kejahatan.

                Analisis ini bertujuan juga untuk memberikan wawasan tentang tren kejahatan dan menyoroti pentingnya evaluasi dan perbaikan terus-menerus terhadap sistem pelaporan kejahatan untuk meningkatkan akurasi dan keandalan data kejahatan.
                '''
    st.info(stringInfo8)
    
with analisa_col2:
    st.markdown('#### Analisa Tren Bulan Laporan dan Kejadian Kriminal')
    string3 = '''
                1. **Trend**
                - Jumlah kriminalitas (baik laporan maupun kejadian) relatif stabil dari bulan ke bulan, tanpa fluktuasi signifikan.
                - Polanya serupa, meningkat di awal tahun mencapai puncak di pertengahan tahun, dan turun di akhir tahun.
                
                2. **Perbedaan Kecil**
                - Terdapat perbedaan kecil dalam jumlah antara bulan laporan dan bulan kejadian, namun tidak signifikan
                - Contoh: Penurunan pada bulan ke-8 di kedua grafik tidak terlalu signifikan.
                
                3. **Penurunan di Akhir Tahun**
                - Penurunan konsisten pada bulan November dan Desember.
                - Kemungkinan terkait peningkatan keamanan menjelang liburan atau perubahan perilaku masyarakat.
            '''
    st.write(string3)

# Tambahkan garis batas horizontal
st.markdown("---")

# ---------------------------------------------------------------

# TREN JUMLAH PELAPORAN TINDAK KRIMINAL

# Menampilkan judul dengan fungsi st.title()
st.title('Analisa Tren Musiman Tindak Kriminal')
st.markdown('### Tren Musiman Jumlah Pelaporan Tindak Kriminal')

# Membuat Column Report
reportLpr_col1, reportLpr_col2 = st.columns(2)
reportLpr_col3, reportLpr_col4 = st.columns(2)

with reportLpr_col1:
    # Grafik Interaktif untuk Analisis Lebih Lanjut
    # interactive_chart = alt.Chart(data_reportLpr).mark_line().encode(
    #     x=alt.X('Month_Lpr:O', axis=alt.Axis(title='Bulan', labelAngle=0)),
    #     y='Jumlah Laporan:Q',
    #     color='Year_Lpr:N',
    #     tooltip=['Year_Lpr', 'Month_Lpr', 'Jumlah Laporan']
    # ).properties(
    #     width=600,
    #     height=400,
    #     title='Tren Musiman Jumlah Laporan Kriminal (Interaktif)'
    # ).interactive()
    
    # interactive_chart
    
    # Ganti Menjadi Penjelasan
    st.markdown('##### Analisa Tren Musiman Laporan Kriminal')
    string4 = '''
                1. **Tren Umum**\n
                Tren umum dari tahun 2020 hingga 2023 menunjukkan fluktuasi dalam jumlah laporan kejahatan dari bulan ke bulan, dengan beberapa puncak dan lembah yang terlihat di sepanjang periode tersebut.
                
                2. **Tren Tahunan**\n
                Secara umum, jumlah laporan kejahatan cenderung mengalami peningkatan dari tahun 2020 hingga 2022, kemudian mengalami sedikit penurunan pada tahun 2023. Hal ini mencerminkan pola umum peningkatan atau penurunan tingkat kejahatan dari tahun ke tahun.
                
                3. **Perbedaan Musiman**\n
                Ada pola musiman yang terlihat dalam data, di mana jumlah laporan kejahatan cenderung naik atau turun pada bulan-bulan tertentu dalam setiap tahunnya. Misalnya, puncak laporan kejahatan terlihat pada bulan Juli di semua tahun, sementara penurunan terlihat pada bulan April.
                
            '''
    st.write(string4)
    
with reportLpr_col2:
    # Heatmap untuk Melihat Pola
    heatmap = alt.Chart(data_reportLpr).mark_rect().encode(
        x=alt.X('Month_Lpr:O', axis=alt.Axis(title='Bulan', labelAngle=0)),
        y=alt.Y('Year_Lpr:O', axis=alt.Axis(title='Tahun Laporan')),
        color='Jumlah Laporan:Q'
    ).properties(
        width=700,
        height=500,
        title='Heatmap Pola Musiman Jumlah Laporan Kriminal'
    )
    
    heatmap
    
# with reportLpr_col3:
#     st.markdown('##### Analisa Tren Musiman Laporan Kriminal')
#     string4 = '''
#                 1. **Tren Menurun pada Tahun 2024**: Terdapat penurunan yang signifikan dalam jumlah laporan kejahatan pada tahun 2024, terutama pada bulan Januari, dibandingkan dengan tahun-tahun sebelumnya. Ini menunjukkan adanya perubahan yang mungkin signifikan dalam situasi keamanan atau perubahan dalam kebijakan penegakan hukum yang berdampak pada tingkat kejahatan.
                
#                 2. **Fluktuasi Tren Tahunan**: Secara umum, terlihat fluktuasi dalam jumlah laporan kejahatan dari bulan ke bulan dalam setiap tahun. Meskipun ada peningkatan dan penurunan yang terjadi dari bulan ke bulan, tetapi secara keseluruhan, trennya cenderung stabil atau menurun dari tahun ke tahun.
                
#                 3. **Pola Musiman**: Terlihat pola musiman dalam jumlah laporan kejahatan, dengan biasanya terjadi peningkatan selama beberapa bulan tertentu dalam setahun. Hal ini mungkin berkaitan dengan faktor-faktor musiman seperti liburan, cuaca, atau peristiwa-peristiwa khusus yang mempengaruhi tingkat kejahatan.
#             '''
#     st.write(string4)

# with reportLpr_col4:
#     # Layout
#     st.markdown('##### Tren Jumlah Perbandingan Berdasarkan Tahun')

#     # Buat daftar tahun unik
#     tahun_unik = list(data_reportLpr['Year_Lpr'].unique())

#     # Buat pilihan dropdown untuk tahun pertama
#     tahun_pertama = st.selectbox('Pilih Tahun Pertama:', tahun_unik)

#     # Buat pilihan dropdown untuk tahun kedua
#     tahun_kedua = st.selectbox('Pilih Tahun Kedua:', tahun_unik)

#     # Filter data berdasarkan tahun yang dipilih
#     data_reportLpr_filtered1 = data_reportLpr[data_reportLpr['Year_Lpr'] == tahun_pertama]
#     data_reportLpr_filtered2 = data_reportLpr[data_reportLpr['Year_Lpr'] == tahun_kedua]

#     # Buat plot dengan Altair untuk perbandingan antara tahun pertama dan tahun kedua
#     chart = alt.Chart(data_reportLpr_filtered1).mark_line().encode(
#         x=alt.X('Month_Lpr', title='Bulan'),
#         y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
#         color=alt.value('blue'),
#         tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
#     ).properties(
#         width=600,
#         height=400
#     )

#     chart += alt.Chart(data_reportLpr_filtered2).mark_line().encode(
#         x=alt.X('Month_Lpr', title='Bulan'),
#         y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
#         color=alt.value('red'),
#         tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
#     )

#     # Tambahkan titik pada setiap lekukan grafik
#     chart += alt.Chart(data_reportLpr_filtered1).mark_circle(color='blue').encode(
#         x=alt.X('Month_Lpr', title='Bulan'),
#         y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
#         tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun
#     )

#     chart += alt.Chart(data_reportLpr_filtered2).mark_circle(color='red').encode(
#         x=alt.X('Month_Lpr', title='Bulan'),
#         y=alt.Y('Jumlah Laporan', title='Jumlah Kejahatan'),
#         tooltip=['Year_Lpr:N', 'Jumlah Laporan:Q']  # Menambahkan tooltip untuk tahun
#     )

#     # Tampilkan plot menggunakan Streamlit
#     st.altair_chart(chart, use_container_width=True)
    
#     # Menggunakan widget bar Altair untuk memilih tahun
#     year_selected = alt.binding_select(options=sorted(data_reportLpr['Year_Lpr'].unique()), name='Tahun  ')
#     year_selection = alt.selection_single(fields=['Year_Lpr'], bind=year_selected)

# TREN KEJADIAN TINDAK KRIMINAL 
st.markdown('### Tren Musiman Jumlah Kejadian Tindak Kriminal')

# Membuta Column Report
reportOcc_col1, reportOcc_col2 = st.columns(2)
reportOcc_col3, reportOcc_col4 = st.columns(2)

with reportOcc_col1:
    # Grafik Interaktif untuk Analisis Lebih Lanjut
    # interactive_chart2 = alt.Chart(data_reportOcc).mark_line().encode(
    #     x=alt.X('Month_Occ:O', axis=alt.Axis(title='Bulan', labelAngle=0)),
    #     y='Jumlah Kejadian:Q',
    #     color='Year_Occ:N',
    #     tooltip=['Year_Occ', 'Month_Occ', 'Jumlah Kejadian']
    # ).properties(
    #     width=600,
    #     height=400,
    #     title='Tren Musiman Jumlah Kejadian Kriminal (Interaktif)'
    # ).interactive()
    
    # interactive_chart2
    
    # Ganti Menjadi Penjelasan
    st.markdown('##### Analisa Tren Musiman Kejadian Kriminal')
    string4 = '''
                1. **Tren Umum**\n
                Dari tahun 2020 hingga 2023, terlihat fluktuasi dalam jumlah kejadian tindak kriminal dari bulan ke bulan, dengan beberapa bulan menunjukkan peningkatan dan penurunan.
                
                2. **Tren Tahunan**\n
                Secara keseluruhan, tren tahunan menunjukkan adanya pola peningkatan jumlah kejadian tindak kriminal dari tahun 2020 hingga 2022, dengan sedikit penurunan pada tahun 2023. Namun, perbedaan ini mungkin tidak signifikan.
                
                3. **Perbandingan dengan Pelaporan**\n
                Ada perbedaan antara tren kejadian tindak kriminal dengan tren pelaporan tindak kriminal. Meskipun tren umumnya serupa, terdapat fluktuasi yang berbeda dari bulan ke bulan antara kedua set data.
                
                4. **Analisis Musiman**\n
                Pola musiman juga terlihat dalam data, dengan bulan-bulan tertentu menunjukkan peningkatan atau penurunan dalam jumlah kejadian tindak kriminal setiap tahunnya.
            '''
    st.write(string4)
    
    # KESIMPULAN TREN MUSIMAN
    stringInfo3 = '''
                    Perhatikan bahwa dalam data kejahatan yang dilaporkan (tren pelaporan) dan kejadian yang sebenarnya (tren kejadian), terdapat perbedaan dalam jumlah laporan dan jumlah kejadian pada tahun dan bulan yang sama. Ini menunjukkan bahwa proses pelaporan kejahatan tidak selalu mencerminkan secara akurat jumlah kejadian yang sebenarnya terjadi.
                    
                    1. **Kesenjangan antara Laporan dan Kejadian**\n
                    
                    Perbedaan antara jumlah laporan dan kejadian pada tahun dan bulan yang sama menunjukkan adanya kesenjangan antara apa yang dilaporkan oleh masyarakat atau pihak berwenang, dengan apa yang sebenarnya terjadi di lapangan.
                    
                    2. **Kemungkinan Penyebab Kesenjangan**\n
                    
                    Kesenjangan ini bisa disebabkan oleh beberapa faktor, termasuk:

                    - Underreporting: Tindak kriminal yang sebenarnya terjadi namun tidak dilaporkan kepada pihak berwenang.
                    - Overreporting: Laporan palsu atau kejadian yang dianggap sebagai kejahatan namun sebenarnya bukan kejahatan.
                    - Proses Pelaporan: Kesalahan dalam proses pelaporan atau pengolahan data.
                    - Perubahan Kebijakan: Perubahan dalam kebijakan pelaporan atau definisi kejahatan.
                    
                    3. **Implikasi dan Rekomendasi**\n
                    
                    Kesenjangan antara laporan dan kejadian dapat memiliki dampak pada analisis keamanan dan kebijakan penegakan hukum. Oleh karena itu, penting untuk memahami penyebab kesenjangan ini dan mengambil langkah-langkah untuk memperbaiki atau mengurangi kesenjangan tersebut. Ini bisa meliputi peningkatan kesadaran masyarakat tentang pentingnya pelaporan kejahatan, peningkatan transparansi dan akurasi dalam proses pelaporan, serta evaluasi dan perbaikan terus-menerus terhadap sistem pelaporan dan analisis kejahatan.
                '''
    st.info(stringInfo3)
    
with reportOcc_col2:
    # Heatmap untuk Melihat Pola
    heatmap2 = alt.Chart(data_reportOcc).mark_rect().encode(
        x=alt.X('Month_Occ:O', axis=alt.Axis(title='Bulan', labelAngle=0)),
        y=alt.Y('Year_Occ:O', axis=alt.Axis(title='Tahun Kejadian')),
        color='Jumlah Kejadian:Q'
    ).properties(
        width=700,
        height=500,
        title='Heatmap Pola Musiman Jumlah Kejadian Kriminal'
    )
    
    heatmap2

# with reportOcc_col3:
#     st.markdown('##### Analisa Tren Musiman Kejadian Kriminal')
#     string4 = '''
#                 1. **Pola Musiman**: Terdapat pola musiman dalam jumlah kejadian tindak kriminal, dengan terjadinya fluktuasi yang berulang dari bulan ke bulan. Misalnya, terlihat peningkatan yang konsisten pada bulan Juli di setiap tahun, yang mungkin dapat dijelaskan oleh faktor-faktor seperti cuaca atau perubahan perilaku masyarakat selama musim liburan.
                
#                 2. **Tren Tahunan**: Meskipun terjadi fluktuasi bulanan, tren keseluruhan dari tahun ke tahun juga bisa diamati. Perhatikan bahwa jumlah kejadian tindak kriminal cenderung naik dari tahun 2020 hingga 2022, namun mengalami penurunan yang signifikan pada tahun 2024.
                
#                 3. **Perubahan Signifikan pada Tahun 2024**: Terdapat penurunan yang drastis dalam jumlah kejadian tindak kriminal pada tahun 2024. Ini bisa menjadi subjek penelitian lebih lanjut untuk memahami penyebabnya. Kemungkinan faktor yang berkontribusi meliputi peningkatan keamanan, perubahan sosial, atau kebijakan penegakan hukum yang baru, atau bisa jadi pada tahun baru di bulan baru ini tindak kejahatan masih minim terjadi.
#             '''
#     st.write(string4)
    
#     # KESIMPULAN TREN MUSIMAN
#     stringInfo3 = '''
#                     ##### Kesimpulan Analisa Tren Musiman Tindak Kriminal
                    
#                     Meskipun laporan tindak kriminal menunjukkan penurunan dari tahun 2020 hingga 2024, jumlah kejadiannya menunjukkan fluktuasi, dengan peningkatan di 2020-2022 dan penurunan di 2024. Perbedaan ini, serta pola musiman yang terlihat pada data, menunjukkan kompleksitas pola kejahatan.
                    
#                     Tantangan dalam memahami dan mengatasi kejahatan masih ada, namun data ini juga menawarkan peluang untuk analisis lebih lanjut dan pengembangan strategi yang lebih efektif dalam penegakan hukum dan pencegahan. Upaya ini dapat dilakukan dengan meningkatkan kualitas pelaporan, memperkuat kerjasama masyarakat dan penegakan hukum, serta mengembangkan program pencegahan yang tepat sasaran.
#                 '''
#     st.info(stringInfo3)

# with reportOcc_col4:
#     # Layout
#     st.markdown('##### Tren Jumlah Perbandingan Berdasarkan Tahun')

#     # Buat daftar tahun unik
#     tahun_unik2 = list(data_reportOcc['Year_Occ'].unique())

#     # Buat pilihan dropdown untuk tahun pertama
#     tahun_pertama2 = st.selectbox('Pilih Tahun Pertama:', tahun_unik2, key='tahun_pertama2')

#     # Buat pilihan dropdown untuk tahun kedua
#     tahun_kedua2 = st.selectbox('Pilih Tahun Kedua:', tahun_unik2, key='tahun_kedua2')

#     # Filter data berdasarkan tahun yang dipilih
#     data_reportOcc_filtered1 = data_reportOcc[data_reportOcc['Year_Occ'] == tahun_pertama2]
#     data_reportOcc_filtered2 = data_reportOcc[data_reportOcc['Year_Occ'] == tahun_kedua2]

#     # Buat plot dengan Altair untuk perbandingan antara tahun pertama dan tahun kedua
#     chart = alt.Chart(data_reportOcc_filtered1).mark_line().encode(
#         x=alt.X('Month_Occ', title='Bulan'),
#         y=alt.Y('Jumlah Kejadian'),
#         color=alt.value('blue'),
#         tooltip=['Year_Occ:N', 'Jumlah Kejadian:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
#     ).properties(
#         width=600,
#         height=400
#     )

#     chart += alt.Chart(data_reportOcc_filtered2).mark_line().encode(
#         x=alt.X('Month_Occ', title='Bulan'),
#         y=alt.Y('Jumlah Kejadian'),
#         color=alt.value('red'),
#         tooltip=['Year_Occ:N', 'Jumlah Kejadian:Q']  # Menambahkan tooltip untuk tahun dan jumlah kejahatan
#     )

#     # Tambahkan titik pada setiap lekukan grafik
#     chart += alt.Chart(data_reportOcc_filtered1).mark_circle(color='blue').encode(
#         x=alt.X('Month_Occ', title='Bulan'),
#         y=alt.Y('Jumlah Kejadian'),
#         tooltip=['Year_Occ:N', 'Jumlah Kejadian:Q']  # Menambahkan tooltip untuk tahun
#     )

#     chart += alt.Chart(data_reportOcc_filtered2).mark_circle(color='red').encode(
#         x=alt.X('Month_Occ', title='Bulan'),
#         y=alt.Y('Jumlah Kejadian'),
#         tooltip=['Year_Occ:N', 'Jumlah Kejadian:Q']  # Menambahkan tooltip untuk tahun
#     )

#     # Tampilkan plot menggunakan Streamlit
#     st.altair_chart(chart, use_container_width=True)
    
#     # Menggunakan widget bar Altair untuk memilih tahun
#     year_selected2 = alt.binding_select(options=sorted(data_reportOcc['Year_Occ'].unique()), name='Tahun  ')
#     year_selection2 = alt.selection_single(fields=['Year_Occ'], bind=year_selected2)

st.markdown("---")

# ---------------------------------------------------------------

# Chart Kejadian Kejahatan Hari dalam Seminggu

st.title('Tingkat Kejadian Kriminalitas per Hari')

crimeDay_col1, crimeDay_col2 = st.columns(2)

with crimeDay_col1:
    string5 = '''
                #### Analisa Kejadian Kejahatan Hari dalam Seminggu
                
                Berdasarkan hasil analisis data pada bar chart, berikut beberapa insight yang dapat ditarik:

                **Tren Kejahatan Mingguan**
                - Hari dengan Kejahatan Tertinggi:
                    - Jumat: Memiliki jumlah kejahatan paling tinggi (98.546)\n
                    - Sabtu: Memiliki jumlah kejahatan kedua tertinggi (96.889)\n
                    - Senin: Memiliki jumlah kejahatan ketiga tertinggi (92.511)\n
                
                - Hari dengan Kejahatan Terendah:
                    - Selasa: Memiliki jumlah kejahatan paling rendah (89.434)
                    
                **Pola Aktivitas Kejahatan**
                - **Peningkatan Kejahatan di Akhir Pekan**: Terjadi peningkatan signifikan pada jumlah kejahatan di hari Jumat, Sabtu, dan Minggu dibandingkan hari Selasa. Hal ini menunjukkan kemungkinan korelasi antara aktivitas akhir pekan dan peningkatan peluang terjadinya kejahatan.
                
                - **Penurunan Kejahatan di Awal Pekan**: Jumlah kejahatan pada hari Selasa relatif lebih rendah dibandingkan hari lain. Hal ini dapat dikaitkan dengan aktivitas masyarakat yang umumnya lebih fokus pada pekerjaan di awal pekan.
            '''
    st.write(string5)
    
with crimeDay_col2:
    # chart_day = alt.Chart(data_crime_day).mark_bar().encode(
    #     x=alt.X('Hari:O', axis=alt.Axis(title='Hari', labelAngle=0)),
    #     y=alt.Y('Jumlah Kejahatan:Q', title='Jumlah Kejahatan'),
    #     tooltip=['Hari', 'Jumlah Kejahatan'],
    #     color=alt.Color('Hari:O', scale=alt.Scale(type='ordinal', range=['#0072B2', '#E64A19', '#F9A825', '#79C75F', '#48A9A6', '#EBEB02', '#C75FB4']))
    # ).properties(
    #     width=600,
    #     height=600,
    #     title='Jumlah Kriminalitas per Hari'
    # )

    # # Tampilkan chart
    # chart_day
    
    # Urutan Chart    
    chart_day = alt.Chart(data_crime_day).mark_bar().encode(
        x=alt.X('Hari:O', sort=alt.EncodingSortField(field="Jumlah Kejahatan", op="sum", order='ascending'), axis=alt.Axis(title='Hari', labelAngle=0)),
        y=alt.Y('Jumlah Kejahatan:Q', title='Jumlah Kejahatan'),
        tooltip=['Hari', 'Jumlah Kejahatan'],
        color=alt.Color('Hari:O', scale=alt.Scale(type='ordinal', range=['#0072B2', '#E64A19', '#F9A825', '#79C75F', '#48A9A6', '#EBEB02', '#C75FB4']))
    ).properties(
        width=600,
        height=600,
        title='Jumlah Kriminalitas per Hari'
    )

    # Tampilkan chart
    chart_day

st.markdown("---")

# ---------------------------------------------------------------

st.title('Identifikasi 10 Tindak Kriminal Paling Umum')

crimeCount_col1, crimeCount_col2 = st.columns(2)

with crimeCount_col1:
    string5 = '''
                #### Analisa 10 Tindak Kriminal Paling Umum 
                
                **Kejahatan Paling Umum**:

                - **Kekerasan**: Tiga kejahatan teratas terkait dengan kekerasan fisik, yaitu BATTERY - SIMPLE ASSAULT, ASSAULT WITH DEADLY WEAPON / AGGRAVATED ASSAULT, dan INTIMATE PARTNER - SIMPLE ASSAULT. Ini menunjukkan prevalensi yang mengkhawatirkan dari kekerasan di wilayah kejadian.
                
                - **Pencurian**: THEFT OF IDENTITY dan THEFT PLAIN - PETTY ($950 & UNDER) menempati peringkat kedua dan ketujuh, menyoroti masalah pencurian properti dan identitas.
                
                - **Kerusakan**: VANDALISM - FELONY ($400 & OVER, ALL CHURCH VA...) berada di peringkat keenam, menunjukkan tingkat vandalisme yang cukup tinggi.
                
                **Tren dan Pola**:

                - **Kekerasan**: Adalah kategori dominan dengan jumlah kejadian hampir dua kali lipat dari kategori lainnya. Ini dapat menunjukkan masalah serius terkait kekerasan fisik dan memerlukan penelitian lebih lanjut.
                
                - **Pencurian**: Dua jenis pencurian masuk dalam lima besar, namun jarak jumlah kejadiannya dengan kategori kekerasan cukup jauh. Namun ini perlu dilihat lebih jauh apakah termasuk tren umum atau ada fluktuasi antar periode.
                
                - **Kerusakan**: Meskipun tidak seumum kategori lain, tingkat vandalisme yang cukup tinggi perlu perhatian juga untuk mengurangi tingkat kriminalitas dari poin ini.
            '''
    st.write(string5)
    
    # Implikasi
    stringInfo4 = '''
                **Analisa Gender Korban**

                - Data menunjukkan bahwa jumlah kriminalitas yang dialami oleh laki-laki (333,887) sedikit lebih tinggi daripada yang dialami oleh perempuan (320,277).
                
                - Meskipun perbedaannya mungkin tidak signifikan, perhatian terhadap pola ini dapat membantu dalam penentuan kebijakan penegakan hukum yang lebih efisien dan efektif.
                '''
    st.info(stringInfo4)

with crimeCount_col2:
    # Bar Chart Data Tindak Kejahatan
    # bar_chart = alt.Chart(data_crime_count.head(10)).mark_bar().encode(
    #     x='Jumlah',
    #     y=alt.Y('Deskripsi Kejahatan').sort('-x'),
    #     color=alt.value('#0072B2'),
    # ).properties(
    #     width=600,
    #     height=500,
    #     title='10 Jenis Kejahatan Paling Umum'
    # )

    # bar_chart
    
    # TRY CHART
    color_map = {
        'BATTERY - SIMPLE ASSAULT': '#0072B2',
        'THEFT OF IDENTITY': '#E64A19',
        'BURGLARY FROM VEHICLE': '#F9A825',
        'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT': '#79C75F',
        'INTIMATE PARTNER - SIMPLE ASSAULT': '#48A9A6',
        'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)': '#EBEB02',
        'THEFT PLAIN - PETTY ($950 & UNDER)': '#C75FB4',
        'BURGLARY': '#33A02C',
        'THEFT FROM MOTOR VEHICLE - GRAND ($950.01 AND OVER)': '#A6CEE3',
        'ROBBERY': '#B2DF8A',
    }

    # Extract the list of color values from the dictionary
    color_list = list(color_map.values())

    bar_chart = alt.Chart(data_crime_count.head(10)).mark_bar().encode(
        x='Jumlah',
        y=alt.Y('Deskripsi Kejahatan').sort('-x'),
        color=alt.Color('Deskripsi Kejahatan', scale=alt.Scale(range=color_list)),
    ).properties(
        width=700,
        height=500,
        title='10 Jenis Kejahatan Paling Umum'
    )

    # Tampilkan Chart
    bar_chart

    chart_gender = alt.Chart(data_gender).mark_bar().encode(
        x=alt.X('JenisKelKor:O', axis=alt.Axis(title='Jenis Kelamin', labelAngle=0)),
        y=alt.Y('Jml_Total:Q', title='Total'),
        tooltip=['JenisKelKor', 'Jml_Total'],
        color=alt.Color('JenisKelKor:O', scale=alt.Scale(type='ordinal', range=['#0072B2', '#E64A19']))
    ).properties(
        width=600,
        height=400,
        title='Banyak Gender Korban'
    )
    
    chart_gender
    
st.markdown("---")

# ---------------------------------------------------------------

st.title('Analisa Area dan Lokasi Kejadian')

crimeArea_col1, crimeArea_col2 = st.columns(2)

with crimeArea_col1:
    string6 = '''
                #### Insight Berdasarkan Analisa Data
                
                **Distribusi Kriminalitas**:

                - **Konsentrasi**: Mayoritas area dengan tingkat kriminalitas tinggi terkonsentrasi di Central, Southwest, dan Hollywood.
                
                - **Perbedaan Signifikan**: Terdapat perbedaan signifikan antara area dengan tingkat kriminalitas tertinggi dan terendah (Central vs. Foothill).
                
                **Lokasi Tindak Kriminal**:

                - **Lokasi Berulang**: Beberapa lokasi muncul beberapa kali dalam daftar 10 lokasi dengan kejadian terbanyak, menunjukkan kemungkinan hotspot kejahatan.
                
                - **Faktor Risiko**: Perlu dikaji faktor-faktor di sekitar lokasi-lokasi tersebut (seperti infrastruktur, kegiatan ekonomi, dll.) untuk memahami faktor risiko yang berkontribusi.
                
                **Perbandingan**:

                - **Perbedaan Antar Area**: Perbandingan antar area dapat menunjukkan disparitas tingkat keamanan dan membantu menentukan prioritas dalam penanganan kriminalitas.
                
                - **Perubahan Pola**: Perbandingan data historis dapat menunjukkan perubahan pola dan tren kejahatan di area tertentu.
            '''
    st.write(string6)
    
    # Analisa Lainnya
    stringInfo5 = '''
                **Analisa Lainnya Mungkin Dapat Ditambahkan**:

                - **Jenis Kejahatan Dominan**: Analisis jenis kejahatan di area dan lokasi tertentu dapat memberikan informasi tentang fokus penegakan hukum dan pencegahan.
                
                - **Analisis Demografis**: Menghubungkan data kriminalitas dengan data demografi dapat membantu memahami faktor-faktor yang berpengaruh pada tingkat kriminalitas.
                
                - **Pendekatan Komprehensif**: Perlu dipertimbangkan berbagai faktor dan pendekatan untuk memahami akar masalah kriminalitas dan merumuskan solusi yang tepat.
                '''
    st.info(stringInfo5)

with crimeArea_col2:
    # Buat bar chart AREA menggunakan Altair dengan pengurutan data di dalam visualisasi
    bar_chart = alt.Chart(data_crime_area).transform_window(
        rank='rank(Jumlah Kejahatan)',
        sort=[alt.SortField('Jumlah Kejahatan', order='descending')]
    ).transform_filter(
        alt.datum.rank <= 10  # Hanya ambil 10 area dengan jumlah kejahatan tertinggi
    ).mark_bar(color='#0072B2').encode(
        x=alt.X('NmArea:N', title='Area', sort='-y'),
        y=alt.Y('Jumlah Kejahatan:Q', title='Jumlah Kriminal')
    ).properties(
        width=600,
        height=400,
        title='Jumlah Tindak Kriminalitas Berdasarkan 10 Area'
    ).configure_axis(
        labelAngle=45
    )

    # Tampilkan bar chart
    bar_chart
    
    # Buat bar chart LOKASI menggunakan Altair dengan pengurutan data di dalam visualisasi
    bar_chart2 = alt.Chart(data_crime_lokasi).transform_window(
        rank='rank(Jumlah Kejahatan)',
        sort=[alt.SortField('Jumlah Kejahatan', order='descending')]
    ).transform_filter(
        alt.datum.rank <= 10  # Hanya ambil 10 area dengan jumlah kejahatan tertinggi
    ).mark_bar(color='#48A9A6').encode(
        x=alt.X('LokKej:N', title='Lokasi Kejadian', sort='-y'),
        y=alt.Y('Jumlah Kejahatan:Q', title='Jumlah Kriminal')
    ).properties(
        width=600,
        height=500,
        title='Jumlah Tindak Kriminalitas Berdasarkan 10 Lokasi'
    ).configure_axis(
        labelAngle=45
    )

    # Tampilkan bar chart
    bar_chart2

st.markdown("---")

# ---------------------------------------------------------------

st.title('Kesimpulan dari Analisa Data Kriminalitas')

conclusion1, conclusion2 = st.columns(2)

with conclusion1:
    # KESIMPULAN
    stringInfo6 = '''
                    ##### Tren Kriminalitas

                    **Tren**

                    - Peningkatan jumlah kejahatan yang dilaporkan dari tahun 2020 hingga 2022.
                    - Penurunan sedikit pada tahun 2023.
                    - Konsistensi tren kejahatan dari tahun ke tahun.
                    
                    **Perbedaan**

                    - Jumlah kejahatan yang dilaporkan lebih rendah daripada yang terjadi.
                    
                    **Implikasi**

                    - Potensi untuk meningkatkan akurasi data kejahatan.
                    - Pentingnya evaluasi dan perbaikan sistem pelaporan.
                    
                    ##### Tingkat Kejadian

                    - **Hari dengan Kejahatan Tertinggi**: Jumat, Sabtu, dan Minggu.
                    
                    - **Hari dengan Kejahatan Terendah**: Selasa.
                    
                    - **Peningkatan di Akhir Pekan**: Peningkatan signifikan pada jumlah kejahatan di akhir pekan.
                    
                    - **Penurunan di Awal Pekan**: Jumlah kejahatan pada hari Senin dan Selasa relatif lebih rendah.
                    '''
    st.info(stringInfo6)

with conclusion2:
    stringInfo7 = '''
                    ##### 10 Tindak Kriminal Paling Umum

                    - **Kekerasan**: Dominan dengan jumlah kejadian hampir dua kali lipat dari kategori lainnya.
                    
                    - **Pencurian**: Dua jenis pencurian masuk dalam lima besar.
                    
                    - **Kerusakan**: Tingkat vandalisme cukup tinggi.
                    
                    ##### Implikasi

                    - Fokus pada pencegahan dan penanganan kejahatan kekerasan.
                    
                    - Meningkatkan kesadaran masyarakat tentang keamanan digital dan perlindungan identitas.
                    
                    - Mencegah perusakan properti.
                    
                    ##### Area dan Lokasi Kejadian

                    - **Konsentrasi**: Mayoritas area dengan tingkat kriminalitas tinggi terkonsentrasi di Central, Southwest, dan Hollywood.
                    
                    - **Lokasi Berulang**: Beberapa lokasi muncul beberapa kali dalam daftar 10 lokasi dengan kejadian terbanyak.
                    
                    - **Perbandingan**: Perbedaan antar area menunjukkan disparitas tingkat keamanan.
                    
                    Hasil analisis menunjukkan bahwa tingkat kriminalitas di wilayah tersebut mengalami penurunan dari tahun 2020 hingga 2024. Namun, terdapat beberapa area dengan tingkat kriminalitas yang tinggi dan jenis kejahatan yang perlu diprioritaskan untuk penanganannya.
                    '''
    st.info(stringInfo7)