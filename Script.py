import os
class script(object):
    START_TXT = """<b>ʜᴇʏ {}, {}\n\nɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ !! 😍\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/TMID21">TelMovID</a></blockquote></b>"""
    
    HELP_TXT = """<b>Klik tombol di bawah ini untuk mendapatkan dokumentasi tentang modul tertentu..\n\n<blockquote>🌿 <a href="https://t.me/+6ox6Xi-uqCo3NzFl">👉🏻 Buat Bot Anda Sendiri</a></blockquote></b>"""
    
    TELE_TXT = """<b>/telegraph - kirim saya gambar atau video di bawah (5MB)

Catatan - Perintah ini berfungsi di grup dan PM bot</b>"""
    
    FSUB_TXT = """<b>• Tambahkan saya ke grup Anda dan jadikan saya admin 😗
• Jadikan saya admin di saluran atau grup target force subscribe Anda 😉
• Kirim /fsub id_chat_target_anda
Contoh: <code>/fsub -100xxxxxx</code>

Sekarang sudah selesai. Saya akan memaksa pengguna Anda untuk bergabung dengan saluran/grup Anda, dan saya tidak akan menyediakan file apa pun sampai pengguna Anda bergabung dengan saluran target Anda.

Untuk menonaktifkan fsub di grup Anda, cukup kirim <code>/del_fsub</code>

Untuk memeriksa apakah fsub terhubung atau tidak, gunakan <code>/show_fsub</code></b>"""

    FORCESUB_TEXT = """<b>Untuk mendapatkan film yang diminta oleh Anda.

Anda harus bergabung dengan saluran resmi kami.

Pertama, klik tombol "Gabung Saluran Pembaruan", lalu, klik tombol "Minta Bergabung".

Setelah itu, coba akses film tersebut lalu klik tombol "Coba Lagi".
    </b>"""
    
    TTS_TXT = """<b>Kirim /tts untuk menggunakan fitur ini</b>"""

    DISCLAIMER_TXT = """<b>Ini adalah proyek sumber terbuka.

Semua file dalam bot ini tersedia secara bebas di internet atau diposting oleh orang lain. Untuk pencarian yang mudah, bot ini mengindeks file yang sudah diunggah di Telegram. Kami menghormati semua undang-undang hak cipta dan bekerja sesuai dengan DMCA dan EUCD. Jika ada yang melanggar hukum, silakan hubungi saya agar dapat segera dihapus. Dilarang mengunduh, streaming, mereproduksi, berbagi, atau mengonsumsi konten tanpa izin eksplisit dari pembuat konten atau pemegang hak cipta yang sah. Jika Anda yakin bot ini melanggar hak kekayaan intelektual Anda, hubungi saluran terkait untuk penghapusan. Bot ini tidak memiliki konten ini, hanya mengindeks file dari Telegram.

<blockquote>🌿 Dipelihara oleh: <a href='https://t.me/+6ox6Xi-uqCo3NzFl'>TelMovID</a></b></blockquote>"""
    

    ABOUT_TEXT = """<blockquote><b>‣ Nama saya: Cari Film\n‣ Pembuat: <a href='https://t.me/TMID21'>TelMovID</a>\n‣ Perpustakaan: pyrogram\n‣ Bahasa: Python\n‣ Basis Data: Mongo DB\n‣ Dihosting di: semua web\n‣ Status build: v5.2 [stabil]</b></blockquote>"""    
    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>Hai {}

Saya menemukan {} hasil 🎁,
tapi tidak bisa mengirim file nya 🤞🏻
Anda belum bergabung grup Support Chat ✨</b>'''

    CHANNELS = """<u>Semua grup dan saluran kami</u> 

▫ Semua film & serial terbaru dan lama.
▫ Semua bahasa tersedia.
▫ Dukungan admin selalu ada.
▫ Layanan tersedia 24x7."""

    LOGO = """BOT BERFUNGSI DENGAN BAIK 🔥"""
    
    RESTART_TXT = """<b>Bot Direset Ulang!

📅 Tanggal: <code>{}</code>
⏰ Waktu: <code>{}</code>
🌐 Zona Waktu: <code>Asia/Jakarta</code>
🛠️ Status Build: <code>v4.2 [Stabil]</code>

Oleh TelMovID</b>"""
        
    
    STATUS_TXT = """<b><u>🗃 Basis Data 1 🗃</u>

» Total pengguna - <code>{}</code>
» Total grup - <code>{}</code>
» Penyimpanan yang digunakan - <code>{} / {}</code>

<u>🗳 Basis Data 2 🗳</u></b>

» Total file - <code>{}</code>
» Penyimpanan yang digunakan - <code>{} / {}</code>

<u>🤖 Detail Bot 🤖</u>

» Waktu aktif - <code>{}</code>
» RAM - <code>{}%</code>
» CPU - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#Pengguna_Baru {}

≈ ID:- <code>{}</code>
≈ Nama:- {}</b>"""

    NEW_GROUP_TXT = """#Grup_Baru {}

Nama grup - {}
ID - <code>{}</code>
Nama pengguna grup - @{}
Tautan grup - {}
Total anggota - <code>{}</code>
Pengguna - {}"""

    REQUEST_TXT = """<b>📜 Pengguna - {}
📇 ID - <code>{}</code>

🎁 Permintaan pesan - <code>{}</code></b>"""  
   
    IMDB_TEMPLATE_TXT = """<b>Hai {message.from_user.mention}, berikut adalah hasil untuk permintaan Anda {search}.

🍿 Judul: {title}
🎃 Genre: {genres}
📆 Tahun: {release_date}
⭐ Peringkat: {rating} / 10</b>
"""

    FILE_CAPTION = """<b>{file_name}\n\nBergabung ➥ 「<a href="https://t.me/+6ox6Xi-uqCo3NzFl">Support Chat</a>」</b>"""
    

    ALRT_TXT = """Segera keluar dari sini!"""

    OLD_ALRT_TXT = """Anda menggunakan pesan lama saya.. kirim permintaan baru.."""

    NO_RESULT_TXT = """<b>Pesan ini belum dirilis atau ditambahkan dalam basis data saya 🙄</b>"""
    
    I_CUDNT = """🤧 Halo {}

Saya tidak menemukan film atau serial dengan nama itu.. 😐"""

    I_CUD_NT = """😑 Halo {}

Saya tidak menemukan apa pun terkait itu 😞... periksa ejaan Anda."""
    
    CUDNT_FND = """🤧 Halo {}

Saya tidak menemukan apa pun terkait itu, apakah Anda maksud salah satu dari ini ?? 👇"""
    
    FONT_TXT = """<b>Anda dapat menggunakan mode ini untuk mengubah gaya font Anda, cukup kirim saya dalam format ini

<code>/font hai bagaimana kabarmu</code></b>"""
    
    PLAN_TEXT = """<b>Kami menyediakan premium dengan harga terendah:
    
3.000 rupiah per hari 👻
5.000 rupiah untuk satu bulan 😚
7.000 rupiah untuk dua bulan 😗

Klik tombol di bawah ini untuk melanjutkan pembelian ↡↡↡
</b>"""
    
    VERIFICATION_TEXT = """<b>👋 Hai {} {},

📌 <u>Anda belum terverifikasi hari ini, silakan klik verifikasi & dapatkan akses tak terbatas hingga verifikasi berikutnya</u>

#verifikasi:- 1/3 ✓

Jika Anda ingin langsung mendapatkan file tanpa verifikasi, maka beli langganan bot 😊

💶 Kirim /plan untuk membeli langganan</b>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 Hai {},

Anda telah menyelesaikan verifikasi pertama ✓

Sekarang Anda memiliki akses tak terbatas untuk <code>{}</code></b>"""

    SECOND_VERIFICATION_TEXT = """<b>👋 Hai {} {},

📌 <u>Anda belum terverifikasi, tap link verifikasi dan dapatkan akses tak terbatas hingga verifikasi berikutnya</u>

#verifikasi:- 2/3

Jika Anda ingin langsung mendapatkan file tanpa verifikasi, maka beli langganan bot 😊

💶 Kirim /plan untuk membeli langganan</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 Hai {},

Anda telah menyelesaikan verifikasi kedua ✓

Sekarang Anda memiliki akses tak terbatas untuk <code>{}</code></b>"""

    THIRDT_VERIFICATION_TEXT = """<b>👋 Hai {},

📌 <u>Anda belum terverifikasi hari ini, tap tautan verifikasi & dapatkan akses tak terbatas untuk hari penuh berikutnya.</u>

#verifikasi:- 3/3

Jika Anda ingin langsung mendapatkan file, Anda dapat mengambil layanan premium (tidak perlu verifikasi)</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>👋 Hai {},

Anda telah menyelesaikan verifikasi ketiga ✓

Sekarang Anda memiliki akses tak terbatas untuk hari penuh berikutnya </b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ Pengguna berhasil diverifikasi ☄</u>

⚡️ Nama:- {} [ <code>{}</code> ] 
📆 Tanggal:- <code>{}</code></b>

#verified_{}_completed"""

    MOVIES_UPDATE_TXT = """<b>#File_Baru_Ditambahkan ✅
**🍿 Judul:** {title}
**🎃 Genre:** {genres}
**📆 Tahun:** {year}
**⭐ Peringkat:** {rating} / 10
</b>"""

    PREPLANS_TXT = """<b>👋 Hai {},

<blockquote>🎁 Manfaat fitur premium:</blockquote>

❏ Tidak perlu membuka tautan
❏ Dapatkan file langsung   
❏ Pengalaman bebas iklan 
❏ Tautan unduhan kecepatan tinggi                         
❏ Tautan streaming multi-pemutar                           
❏ Film dan serial tak terbatas                                                                    
❏ Dukungan admin penuh                              
❏ Permintaan akan selesai dalam 1 jam [ jika tersedia ]

⛽️ Periksa paket aktif Anda: /myplan
</b>"""    

    PREPLANSS_TXT = """<b>👋 Hai {},

<blockquote>🎁 Manfaat fitur premium:</blockquote>

❏ Tidak perlu membuka tautan
❏ Dapatkan file langsung   
❏ Pengalaman bebas iklan 
❏ Tautan unduhan kecepatan tinggi                         
❏ Tautan streaming multi-pemutar                           
❏ Film dan serial tak terbatas                                                                    
❏ Dukungan admin penuh                              
❏ Permintaan akan selesai dalam 1 jam [ jika tersedia ]

⛽️ Periksa paket aktif Anda: /myplan
</b>"""

    OTHER_TXT = """<b>👋 Hai {},

🎁 <u>Paket lain</u>
⏰ Hari yang disesuaikan
💸 Sesuai dengan hari yang Anda pilih

🏆 Jika Anda ingin paket baru selain dari paket yang diberikan, maka Anda bisa bicara langsung dengan <a href='https://t.me/+6ox6Xi-uqCo3NzFl'>Admin</a> kami dengan mengklik tombol kontak di bawah ini.

👨‍💻 Hubungi admin untuk mendapatkan paket lainnya.

➛ Gunakan /plan untuk melihat semua paket kami sekaligus.
➛ Periksa paket aktif Anda dengan menggunakan: /myplan</b>"""

    FREE_TXT = """<b>👋 Hai {},

<blockquote>🎖️Paket premium tersedia:</blockquote>

 <code>××××</code> [tap untuk menyalin]
 
⛽️ Periksa paket aktif Anda: /myplan

🏷️ <a href='https://t.me/'>Bukti premium</a>

‼️ Harus kirim tangkapan layar setelah pembayaran.
‼️ Beri kami waktu untuk menambahkan Anda ke daftar premium.
</b>"""

    ADMIN_CMD_TXT = """<b><blockquote>
-------------Pengguna Premium------------
➩ /add_premium {user ID} {Times} - Tambahkan pengguna premium
➩ /remove_premium {user ID} - Hapus pengguna premium
➩ /add_redeem - Buat kode redeem
➩ /premium_users - Daftar semua pengguna premium
➩ /refresh - Segarkan uji coba gratis untuk pengguna
-------------Saluran Pembaruan----------
➩ /set_muc {ID saluran} - Tetapkan saluran pembaruan film
--------------Pencarian PM--------------
➩ /pm_search_on - Aktifkan pencarian PM
➩ /pm_search_off - Nonaktifkan pencarian PM
--------------Verifikasi ID--------------
➩ /verify_id - Buat ID verifikasi hanya untuk penggunaan grup
--------------Tetapkan Iklan----------------
➩ /set_ads {nama iklan}}#{Times}#{URL foto} - <a href="https://t.me/+6ox6Xi-uqCo3NzFl">Penjelasan</a>
➩ /del_ads - Hapus iklan
-------------Top Trending------------
➩ /setlist {Mirzapur, Money Heist} - <a href=https://t.me/+6ox6Xi-uqCo3NzFl>Penjelasan</a>
➩ /clearlist - Hapus semua daftar
</blockquote></b>"""

    ADMIN_CMD_TXT2 = """<b><blockquote>
--------------Indeks File--------------
➩ /index - Indeks semua file
--------------Tautan Keluar--------------
➩ /leave {ID grup} - Keluar dari grup yang ditentukan
-------------Kirim Pesan-------------
➩ /send {nama pengguna} - Gunakan perintah ini sebagai balasan untuk pesan apa pun
----------------Larang Pengguna---------------
➩ /ban {nama pengguna} - Larang pengguna
➩ /unban {nama pengguna} - Batalkan larangan pengguna
--------------Broadcast--------------
➩ /broadcast - Kirim pesan ke semua pengguna
➩ /grp_broadcast - Kirim pesan ke semua grup yang terhubung

</blockquote></b>"""
    
    GROUP_TEXT = """<b><blockquote>
 --------------Setel Verifikasi-------------
/set_verify {{tautan situs web}} {{api situs web}}
/set_verify_2 {{tautan situs web}} {{api situs web}}
/set_verify_3 {{tautan situs web}} {{api situs web}}
-------------Setel Waktu Verifikasi-----------
/set_time_2 {{detik}} Setel waktu verifikasi kedua
/set_time_3 {{detik}} Setel waktu verifikasi ketiga
--------------Verifikasi On Off------------
/verifyoff {{kode verify.off}} - nonaktifkan verifikasi <a href="https://t.me/IM_JISSHU">Hubungi</a> admin bot untuk kode verify.off
/verifyon - aktifkan verifikasi 
------------Setel Keterangan File-----------
/set_caption - setel keterangan file khusus 
-----------Setel Template Imdb-----------
/set_template - setel template IMDb <a href="https://t.me/TMID21">Contoh</a>
--------------Setel Tutorial-------------
/set_tutorial - setel tutorial verifikasi 
-------------Setel Saluran Log-----------
--> Tambahkan saluran log dengan format ini & pastikan bot adalah admin di saluran log Anda 👇

/set_log {{log channel id}}
---------------------------------------
Anda dapat memeriksa semua detail Anda 
dengan perintah /details
</blockquote>
Tambahkan saya ke grup Anda dan jadikan saya admin dan gunakan semua fitur😇</b>"""

    SOURCE_TXT = """<b>CATATAN:
- Oleh ◉› :<blockquote><a href="https://t.me/TMID21">TelMovID</a></blockquote>

pengembang: Mr.Jisshu
</b>""" 
    GROUP_C_TEXT = """<b><blockquote>
 --------------Setel Verifikasi-------------
/set_verify {tautan situs web} {api situs web}
/set_verify_2 {tautan situs web} {api situs web}
/set_verify_3 {tautan situs web} {api situs web}
-------------Setel Waktu Verifikasi-----------
/set_time_2 {detik} Setel waktu verifikasi kedua
/set_time_3 {detik} Setel waktu verifikasi ketiga
--------------Verifikasi On Off------------
/verifyoff {kode verify.off} - nonaktifkan verifikasi <a href="https://t.me/+6ox6Xi-uqCo3NzFl">hubungi</a> admin bot untuk kode verify.off
/verifyon - aktifkan verifikasi 
------------Setel Keterangan File-----------
/set_caption - setel keterangan file khusus 
-----------Setel Template Imdb-----------
/set_template - setel template IMDb <a href="https://t.me/TMID21">Contoh</a>
--------------Setel Tutorial-------------
/set_tutorial - setel tutorial verifikasi 
-------------Setel Saluran Log-----------
--> Tambahkan saluran log dengan format ini & pastikan bot adalah admin di saluran log Anda 👇

/set_log {ID saluran log}
---------------------------------------
Anda dapat memeriksa semua detail Anda 
dengan perintah /details
</blockquote>
Jika Anda memiliki keraguan silakan <a href="https://t.me/+6ox6Xi-uqCo3NzFl">hubungi</a> <a href="https://t.me/+6ox6Xi-uqCo3NzFl">admin</a> saya</b>"""
