from pyrogram import Client, filters
from datetime import datetime, timedelta
import asyncio
from database.iklandb import db  # Import file database
from info import ADMINS

# Command untuk menambahkan iklan
@Client.on_message(filters.private & filters.command("add_ad") & filters.user(ADMINS))
async def add_ad(client, message):
    try:
        command_args = message.text.split(maxsplit=1)[1]
        if '#' not in command_args or len(command_args.split('#')) < 3:
            await message.reply_text(
                "Gunakan format: /add_ad {nama_iklan}#{durasi/tayangan}#{URL}\n"
                "Contoh: /add_ad PromoDiskon#d7#http://example.com"
            )
            return

        name, duration_or_impression, url = command_args.split('#', 2)
        name = name.strip()
        url = url.strip()

        if len(name) > 35:
            await message.reply_text("Nama iklan tidak boleh lebih dari 35 karakter.")
            return

        expiry_date = None
        impression_count = None

        if duration_or_impression.startswith('d'):
            duration = duration_or_impression[1:]
            if not duration.isdigit():
                await message.reply_text("Durasi harus berupa angka.")
                return
            expiry_date = datetime.utcnow() + timedelta(days=int(duration))
        elif duration_or_impression.startswith('i'):
            impression = duration_or_impression[1:]
            if not impression.isdigit():
                await message.reply_text("Jumlah tayangan harus berupa angka.")
                return
            impression_count = int(impression)
        else:
            await message.reply_text("Gunakan 'd' untuk durasi atau 'i' untuk jumlah tayangan.")
            return

        reply = message.reply_to_message
        if not reply or not reply.text:
            await message.reply_text("Balas pesan teks untuk menjadikan iklan.")
            return

        content = reply.text
        await db.add_advertisement(name, content, expiry_date, impression_count, url)
        await message.reply_text(f"Iklan '{name}' berhasil ditambahkan.")
    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {e}")


# Command untuk menghapus iklan
@Client.on_message(filters.private & filters.command("delete_ad") & filters.user(ADMINS))
async def delete_ad(client, message):
    try:
        command_args = message.text.split(maxsplit=1)
        if len(command_args) < 2:
            await message.reply_text("Gunakan format: /delete_ad {nama_iklan}")
            return

        name = command_args[1].strip()
        deleted = await db.delete_advertisement(name)
        if deleted:
            await message.reply_text(f"Iklan '{name}' berhasil dihapus.")
        else:
            await message.reply_text(f"Iklan '{name}' tidak ditemukan.")
    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {e}")


# Command untuk melihat semua iklan
@Client.on_message(filters.private & filters.command("list_ads") & filters.user(ADMINS))
async def list_ads(client, message):
    try:
        ads = await db.get_all_advertisements()
        if not ads:
            await message.reply_text("Tidak ada iklan yang aktif saat ini.")
            return

        text = "Daftar Iklan Aktif:\n\n"
        for ad in ads:
            name = ad["name"]
            expiry = ad["expiry_date"].strftime('%Y-%m-%d %H:%M:%S') if ad["expiry_date"] else "Tidak ada"
            impressions = ad["impression"] if ad["impression"] is not None else "Tak Terbatas"
            url = ad["url"] if ad["url"] else "Tidak ada URL"
            text += f"Nama: {name}\nKedaluwarsa: {expiry}\nTayangan: {impressions}\nURL: {url}\n\n"

        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"Terjadi kesalahan: {e}")


# Kirim iklan setiap 1 jam
async def send_ads_to_all_users(client):
    while True:
        try:
            ads = await db.get_all_advertisements()
            if not ads:
                await asyncio.sleep(3600)
                continue

            users = await db.get_all_users()
            async for user in users:
                for ad in ads:
                    if ad["impression"] == 0:
                        continue

                    try:
                        await client.send_message(user["id"], ad["content"])
                        if ad["impression"] is not None:
                            await db.update_advertisement_impressions(ad["name"], ad["impression"] - 1)
                    except Exception as e:
                        print(f"Gagal mengirim iklan ke {user['id']}: {e}")

            expired_ads = await db.get_expired_advertisements()
            for expired_ad in expired_ads:
                await db.delete_advertisement(expired_ad["name"])

        except Exception as e:
            print(f"Terjadi kesalahan saat mengirim iklan: {e}")
        await asyncio.sleep(3600)


# Command untuk memulai pengiriman iklan otomatis (khusus admin)
@Client.on_message(filters.private & filters.command("start_ads") & filters.user(ADMINS))
async def start_ads(client, message):
    await message.reply_text("Pengiriman iklan otomatis telah dimulai.")
    asyncio.create_task(send_ads_to_all_users(client))
