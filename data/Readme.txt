Tren Musiman: Identifikasi musim puncak dan sepi untuk persewaan sepeda berdasarkan musim dan bulan. Ini membantu manajemen armada dan alokasi sumber daya.
Hari Kerja vs. Akhir Pekan: Analisis perbedaan sewa antara hari kerja (hari kerja) dan akhir pekan menggunakan hari kerja. Hal ini dapat memandu keputusan kepegawaian dan kampanye pemasaran untuk hari-hari tertentu.
Dampak Cuaca: Jelajahi bagaimana kondisi cuaca (lokasi cuaca, suhu, suhu, dengungan, kecepatan angin) memengaruhi persewaan. Anda dapat mengidentifikasi pola cuaca yang menguntungkan dan berpotensi menyesuaikan harga atau promosi.
Dampak Liburan : Menganalisis pengaruh hari libur (holiday) terhadap persewaan. Anda mungkin melihat peningkatan permintaan selama liburan dan menyesuaikan staf atau menawarkan promosi khusus.
Tren Berbasis Waktu: Selidiki variasi persewaan sepanjang jam (jam) dalam sehari. Hal ini dapat membantu mengoptimalkan ketersediaan sepeda pada waktu yang berbeda.
Segmentasi pelanggan:

Pengguna Biasa vs. Pengguna Terdaftar: Bandingkan perilaku pengguna biasa (casual) dan pengguna terdaftar (terdaftar). Hal ini dapat membantu menyesuaikan strategi pemasaran untuk setiap kelompok. Misalnya, menawarkan program loyalitas atau diskon untuk pengguna terdaftar.
Memahami Preferensi Pengguna: Analisis pola pengguna berdasarkan berbagai faktor seperti cuaca, musim, waktu, atau lokasi (jika tersedia di data Anda) untuk memahami preferensi mereka. Hal ini dapat menginformasikan strategi penempatan dan pemeliharaan sepeda di masa depan.
Pemodelan Prediktif:

Peramalan Permintaan: Membangun model prediktif berdasarkan data historis untuk mengantisipasi permintaan di masa depan. Hal ini membantu penjadwalan staf, perencanaan perawatan sepeda, dan strategi penetapan harga yang berpotensi dinamis.
Promosi Bertarget: Kembangkan kampanye pemasaran bertarget untuk segmen pengguna tertentu berdasarkan perilaku dan preferensi persewaan mereka.

#-------variabel-------#

instant: record index
dteday : date
season : season (1:springer, 2:summer, 3:fall, 4:winter)
yr : year (0: 2011, 1:2012)
mnth : month ( 1 to 12)
hr : hour (0 to 23)
holiday : weather day is holiday or not 	- 
weekday : day of the week
workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
weathersit : 	1: Clear, Few clouds, Partly cloudy, Partly cloudy
		2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp : Normalized temperature in Celsius.41 (max)
atemp: Normalized feeling temperature in Celsius 50 (max)
hum: Normalized humidity 100 (max)
windspeed: Normalized wind speed. The values are divided to 67 (max)
casual: count of casual users
registered: count of registered users
cnt: count of total rental bikes including both casual and registered
	
