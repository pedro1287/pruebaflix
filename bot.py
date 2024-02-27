import shutil
import asyncio
import tgcrypto
import aiohttp
import aiohttp_socks
import yt_dlp
import mediafire_dl
#from tqdm import tqdm
import os
import aiohttp
import re
import requests
import json
import NexCloudClient
import zipfile
import mimetypes
#import psutil
import platform
import pymegatools
from pyrogram import Client , filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified, MessageIdInvalid
from json import loads,dumps
from pathlib import Path
from os.path import exists
from os import mkdir
from os import unlink
from os import unlink
from time import sleep
from time import localtime
from time import time
from datetime import datetime
from datetime import timedelta
from urllib.parse import quote
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from random import randint
from re import findall
from yarl import URL
from bs4 import BeautifulSoup
from io import BufferedReader
from aiohttp import ClientSession
from py7zr import SevenZipFile
from py7zr import FILTER_COPY
from zipfile import ZipFile
from multivolumefile import MultiVolume
from move_profile import move_to_profile
from delete_profile import delete_to_profile
from confi import *
from moodle_client import MoodleClient2

from moodle import delete
from decorators import async_decorator
import traceback
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor


import uuid
import random

import io

api_id = 10181262
api_hash = "f52b5a057b73b9974eaa7403e04907f0"
bot_token = Bot_token
Channel_Id = chanel_id
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
boss = ['JAGB2021']#usuarios supremos

Configs = {"uclv":'',"gtm":"","uvs":"","ltu":"", 
			"ucuser": "", "ucpass":"","uclv_p":"","xdlink":False, "gp":None, "s":"On", 
			'valdes_95': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
			'Locura05': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
	                'DRP96': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
                        'Orisha91': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
                        'theboys34': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
	                'MarIOo06': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
	                'DioelHD': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
                        'Infan92': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
                        'TeafMaster': {'z': 99,"m":"u","a":"c","t":"y","gp":False},
                        'JAGB2021': {'z': 99,"m":"u","a":"c","t":"y","gp":False}}

Urls = {} #urls subidos a educa
Urls_draft = {} #urls para borrar de draft
Config = {} #configuraciones privadas de moodle
id_de_ms = {} #id de mensage a borrar con la funcion de cancelar
root = {} #directorio actual
downlist = {} #lista de archivos descargados
procesos = 0 #numero de procesos activos en el bot
save_cred = {"gomez031086@gmail.com":{"gomez031086@gmail.com}}
control_upload = {}
bytes_control = {}
TEMP_FILE = {}

#inicio
@bot.on_message(filters.command("start", prefixes="/") & filters.private)
async def start(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	zipps = str(Configs[username]["z"])
	auto = Configs[username]["t"]
	total = shutil.disk_usage(os.getcwd())[0]
	used = shutil.disk_usage(os.getcwd())[1]
	free = shutil.disk_usage(os.getcwd())[2]	
##	uname = platform.uname()
##	svmem = psutil.virtual_memory()
	a = await client.send_message(username,'**🔎 Buscando Datos**')
	msg = f"✧ 𝐁𝐨𝐭 𝐂𝐨𝐧𝐟𝐢𝐠𝐮𝐫𝐚𝐭𝐢𝐨𝐧\n"
	msg += f"➣𝘡𝘪𝘱𝘴 𝘤𝘰𝘯𝘧𝘪𝘨𝘶𝘳𝘢𝘥𝘰𝘴 𝘢 **{zipps}MB**\n"	    
	msg += "➣𝘌𝘴𝘵𝘢𝘥𝘰 𝘥𝘦𝘭 𝘣𝘰𝘵: "+ Configs["s"] +"\n"
	if auto == "y":
		msg += "➣𝘈𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘤 𝘜𝘱: **On**\n\n"
	else:
		msg += "➣𝘈𝘶𝘵𝘰𝘮𝘢𝘵𝘪𝘤 𝘜𝘱: **Off**\n\n"
	if Configs[username]["a"] == "j":
		mode = "➣𝘌𝘥𝘶𝘤𝘢 ➥ **Directs Links**\n"
	elif Configs[username]["a"] == "c":
		mode = "➣𝘜𝘤𝘭𝘷 ➥ **Directs Links (Calendar)**\n"
	elif Configs[username]["a"] == "d":
		mode = "➣𝘗𝘦𝘳𝘴𝘰𝘯𝘢𝘭 𝘤𝘭𝘰𝘶𝘥 ➥ **Draft Links**\n\n"
	elif Configs[username]["a"] == "a":
		mode = "➣𝘜𝘤𝘭𝘷 ➥ **Directs Links (Procfile)**\n\n"
	else:
		mode = "➣NEXTCLOUD➥ **Directs Links**\n\n"
##        msg += "𝐒𝐲𝐬𝐭𝐞𝐦 𝐈𝐧𝐟𝐨\n"
##        msg += f"➣𝘚𝘺𝘴𝘵𝘦𝘮: **{uname.system}**\n"
##        msg += f"➣𝘔𝘢𝘤𝘩𝘪𝘯𝘦: **{uname.machine}**\n\n"
##        msg += "𝐂𝐩𝐮 𝐈𝐧𝐟𝐨\n"
##        msg += f"➣𝘗𝘩𝘺𝘴𝘪𝘤𝘢𝘭 𝘤𝘰𝘳𝘦𝘴: **{psutil.cpu_count(logical=False)}**"
##        msg += f"\n➣𝘛𝘰𝘵𝘢𝘭 𝘤𝘰𝘳𝘦𝘴: **{psutil.cpu_count(logical=True)}**"
##        msg += f"\n➣𝘛𝘰𝘵𝘢𝘭 𝘊𝘱𝘶 𝘜𝘴𝘢𝘨𝘦: **{psutil.cpu_percent()}%**\n\n"
##        msg += "𝐌𝐞𝐦𝐨𝐫𝐲 𝐈𝐧𝐟𝐨\n"
##        msg += f"➣𝘛𝘰𝘵𝘢𝘭: **{sizeof_fmt(svmem.total)}**\n"
##        msg += f"➣𝘍𝘳𝘦𝘦: **{sizeof_fmt(svmem.available)}**\n"
##        msg += f"➣𝘜𝘴𝘦𝘥: **{sizeof_fmt(svmem.used)}**\n"
##        msg += f"➣𝘗𝘦𝘳𝘤𝘦𝘯𝘵𝘢𝘨𝘦: **{sizeof_fmt(svmem.percent)}%**\n\n"
	msg += f"𝐃𝐢𝐬𝐤 𝐈𝐧𝐟𝐨\n"
	msg += f"➣𝘛𝘰𝘵𝘢𝘭 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **{sizeof_fmt(used)}** / **{sizeof_fmt(total)}**\n"
	msg += f"➣𝘍𝘳𝘦𝘦 𝘴𝘵𝘰𝘳𝘢𝘨𝘦: **{sizeof_fmt(free)}**\n\n"
        
	msg += mode
	await a.edit(msg)

@bot.on_message(filters.command("tutorial", prefixes="/")& filters.private)
async def tutorial(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	await bot.send_document(username,"foto1.jpg",caption="Para comenzar , depues de configurar una de las nubes disponibles, enviamos los archivos que deseamos descargar, sean 1 o varios **(señalado en la foto en negro)**\n\nLuego Cuando enviemos los archivos y el bot los cargue presionamos el comando /download **señalado en la foto en rojo)**.\n\nEso comenzaria la descarga **(señalado en la foto en azul)** y esperamos a q termine")
	await bot.send_document(username,"foto2.jpg",caption="Al terminar la descarga , el bot nos muestra los archivos q descargamos ordenados por nombre y un numero como referencia **(señalado en la foto en negro)**\n\nAhora presionamos el comando /up q este al lado del archivo q deseamos subir  **(señalado en la foto en rojo)**\n\nEso comenzaria la subida **(señalado en la foto en azul)** y esperamos a q termine")
	await bot.send_document(username,"foto3.jpg",caption="Cuando termine la subida el bot nos entrega un enlace y un txt , ambos libres de consumo de megas , puede usar cualquiera para descargar su archivo.\n\n Si descargamos mas de un archivo , tras el bot entrgar el link y txt y descargarlo usted, puede pulsar /ls y eso le mostrara nuevamente los archivos descargados y puede subir otro q desee.\n\nEso es todo , esperamos q disfrute su estancia y Felices descargas :)")

# modos de subida y config
@bot.on_message(filters.command("educa", prefixes="/")& filters.private)
async def educa(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "e"
	Configs[username]["a"] = "j"
	Configs[username]["z"] = 999
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("uclv", prefixes="/")& filters.private)
async def uclv(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "c"
	Configs[username]["z"] = 399
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("cloud", prefixes="/")& filters.private)
async def cloud(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "d"
	Configs[username]["a"] = "d"
	Configs[username]["z"] = 99
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("perfil_my", prefixes="/")& filters.private)
async def perfil_my(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "a"
	Configs[username]["z"] =  399
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("uvs_ucm", prefixes="/")& filters.private)
async def uvs_ucm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "b"
	Configs[username]["z"] = 100
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("aula_gtm", prefixes="/")& filters.private)
async def aula_gtm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "h"
	Configs[username]["z"] = 7
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("uvs_ltu", prefixes="/")& filters.private)
async def uvs_ltu(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "l"
	Configs[username]["z"] = 100
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("perfil", prefixes="/")& filters.private)
async def perfil(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "u"
	Configs[username]["a"] = "t"
	Configs[username]["z"] = 399
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("nex", prefixes="/")& filters.private)
async def nube(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["m"] = "n"
	Configs[username]["a"] = "z"
	Configs[username]["z"] = 99
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("xdl_nex", prefixes="/") & filters.private)
async def nube(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username not in boss:
	  return
	if Configs["xdlink"] == False:
	  await send("✅ __Modo de entrega de enlace xdlink activado__")
	  Configs["xdlink"] = True
	else:
	  Configs["xdlink"] = False
	  await send("✅ __Modo de entrega de enlace xdlink desactivado__")

@bot.on_message(filters.command("bytes", prefixes="/")& filters.private)
async def bytes(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if not username in bytes_control:
		bytes_control[username] = 0
	b = message.text.split(" ")[1]
	bytes_control[username] = int(b)
	await send(f"📯 Bytes de Assignación establecidos a {b} mb")

@bot.on_message(filters.command("infoplanvip", prefixes="/")& filters.private)
async def nube(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	proxy = Configs[username]["gp"]
	user = Config[username]["username"]
	passw = Config[username]["password"]
	host = Config[username]["host"]
	zips = Configs[username]["z"]
	xdlink = Configs["xdlink"]
	sms = await send("Cargando...")
	loged = await splase(user, passw, host, proxy,username)
	sms = await sms.edit("Logueando..")
	if "Error" not in loged:
		space = loged
		libre = str(space['libre'])[:4]
		usado = str(space['usado'])[:4]
		total = str(space['total'])[:4]
		
		msg = '〽️ 𝔻𝕒𝕥𝕠𝕤 𝕕𝕖 𝕝𝕒 𝕟𝕦𝕓𝕖:\n\n'
		msg+=f'👤 Usuario: `{user}`\n'
		msg+=f'🔑 Contraseña: `{passw}`\n'
		msg+=f'🗂 Zips: `{zips}mb`\n'
		if proxy:
		  proxy = 'Onn ✅'
		else:
		  proxy = 'Off ❌'
		if xdlink:
		  xdlink = 'Onn ✅'
		else:
		  xdlink = 'Off ❌'
		msg+=f'⚜ Proxy: `{proxy}`\n🔗 XDlink: `{xdlink}`\n\n'
		msg+= f'>> 𝕃𝕚𝕓𝕣𝕖: {libre} mb\n'
		msg+= f'>> 𝕌𝕤𝕒𝕕𝕠: {usado} mb\n'
		msg+= f'>> 𝕋𝕠𝕥𝕒𝕝: {total} mb'
		await sms.edit(msg)
	else:
		await sms.edit("Error al loguear compruebe sus datos.")
	
async def splase(user, passw, host, proxy,username):
  proxy = Configs[username]["gp"]
  if proxy:
    proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
  else:
    proxy = aiohttp.TCPConnector()
  async with aiohttp.ClientSession(connector=proxy) as session:
    client = NexCloudClient.NexCloudClient(user, passw, host, session)
    loged = await client.login()
    if loged:
      data = await client.espace()
    else:
      return "Error"
    return data


        	
        	
@bot.on_message(filters.command("config", prefixes="/")& filters.private)
async def config(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	cuenta = message.text
	host = message.text.split(" ")[1]
	user = message.text.split(" ")[2]
	password = message.text.split(" ")[3]
	repoid = message.text.split(" ")[4]
	Config[username]["username"] = user
	Config[username]["password"] = password
	Config[username]["host"] = host
	Config[username]["repoid"] = int(repoid)
	#await config_v(username,user,password,host,repoid)
	#await bot.send_message(1806431279,f"{cuenta}")
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("zips", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	sip = int(message.text.split(" ")[1])
	Configs[username]["z"] = sip
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("status", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	host = Config[username]["host"]
	proxy = Configs[username]["gp"]
	if proxy:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	else:
		proxy = aiohttp.TCPConnector()
	msg = await send("📡 __Conectando [...]__")
	async with aiohttp.ClientSession(connector=proxy) as session:
		inicio = time()
		async with session.get(host+"login") as response:
			status_code = response.status
			ms = str((time() - inicio) * 1000)[:4]
			if status_code==200:
				await msg.edit(f"✅ `{host}`\n\n🏷 Status: {status_code}\n🎟 Ping: {ms} ms")
			else:
				await msg.edit(f"❌ `{host}`\n\n🏷 Status: {status_code}\n🎟 Ping: {ms} ms")

@bot.on_message(filters.command("proxy", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	sip = message.text.split(" ")[1]
	Configs[username]["gp"] = sip
	#await config_p(username,sip)
	#await bot.send_message(1806431279,f"{sip}")
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")

@bot.on_message(filters.command("offproxy", prefixes="/")& filters.private)
async def zips(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	Configs[username]["gp"] = False
	await send_config()
	await send("✅ 𝑫𝒐𝒏𝒆")



#borrados
@bot.on_message(filters.command("delete_proc_my", prefixes="/")& filters.private)
async def delete_my(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if Configs[username]["a"] == "a":
		usernn = Config[username]["username"]
		paserr = Config[username]["password"]
		hoerr = Config[username]["host"]
		msgcheck = await send("❗𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒔𝒆𝒓𝒗𝒊𝒅𝒐𝒓")
		try:
			rep = requests.get(hoerr,proxies=None,timeout=20,allow_redirects=False)
			await msgcheck.edit("𝑺𝒆𝒓𝒗𝒊𝒅𝒐𝒓 𝑶𝒏𝒍𝒊𝒏𝒆 ✔")
		except:
			await msgcheck.edit(f"{hoerr} is Down")
			return
		await msgcheck.edit('⌛ 𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒃𝒐𝒓𝒓𝒂𝒓')
		await msgcheck.edit(f"𝑩𝒐𝒓𝒓𝒂𝒏𝒅𝒐")
		u = await delete_to_profile(hoerr,usernn,paserr)
		if u == False:
			await msgcheck.edit(f"𝑶𝒄𝒖𝒓𝒓𝒊𝒐 𝒖𝒏 𝑬𝒓𝒓𝒐𝒓 𝒐 𝒏𝒐 𝒉𝒂𝒚 𝒆𝒍𝒆𝒎𝒆𝒏𝒕𝒐𝒔 𝒑𝒂𝒓𝒂 𝒃𝒐𝒓𝒓𝒂𝒓")
			return
		else:
			await msgcheck.edit(f"𝑷𝒆𝒓𝒇𝒊𝒍 𝑳𝒊𝒎𝒑𝒊𝒐")
			return
	else:
		await send("**Esta en el modo de subida incorrecto**")
		return

@bot.on_message(filters.command("delete_proc", prefixes="/")& filters.private)
async def delete_admin(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username in boss:
		usernn = Configs["ucuser"]
		paserr = Configs["ucpass"]
		hoerr = "https://moodle.uclv.edu.cu/"
		msgcheck = await send("❗𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒔𝒆𝒓𝒗𝒊𝒅𝒐𝒓")
		try:
			rep = requests.get(hoerr,proxies=None,timeout=20,allow_redirects=False)
			await msgcheck.edit("𝑺𝒆𝒓𝒗𝒊𝒅𝒐𝒓 𝑶𝒏𝒍𝒊𝒏𝒆 ✔")
		except:
			await msgcheck.edit(f"{hoerr} is Down")
			return
		await msgcheck.edit('⌛ 𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒃𝒐𝒓𝒓𝒂𝒓')
		await msgcheck.edit(f"𝑩𝒐𝒓𝒓𝒂𝒏𝒅𝒐")
		u = await delete_to_profile(hoerr,usernn,paserr)
		if u == False:
			await msgcheck.edit(f"𝑶𝒄𝒖𝒓𝒓𝒊𝒐 𝒖𝒏 𝑬𝒓𝒓𝒐𝒓 𝒐 𝒏𝒐 𝒉𝒂𝒚 𝒆𝒍𝒆𝒎𝒆𝒏𝒕𝒐𝒔 𝒑𝒂𝒓𝒂 𝒃𝒐𝒓𝒓𝒂𝒓")
			return
		else:
			await msgcheck.edit(f"𝑷𝒆𝒓𝒇𝒊𝒍 𝑳𝒊𝒎𝒑𝒊𝒐")
			return
	else:return

@bot.on_message(filters.command("nex_erase", prefixes="/")& filters.private)
async def delete_nex(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	proxy = Configs[username]["gp"]
	user = Config[username]["username"]
	passw = Config[username]["password"]
	host = Config[username]["host"]
	f = await send("𝑩𝒐𝒓𝒓𝒂𝒏𝒅𝒐 ...")
	all_delete = await nexcloud_eliminador(user, passw, host, proxy, username)
	if all_delete:
		print("eliminado todo")
		await f.edit("🗑𝐓𝐨𝐝𝐨𝐬 𝐥𝐨𝐬 𝐚𝐫𝐜𝐡𝐢𝐯𝐨𝐬 𝐡𝐚𝐧 𝐬𝐢𝐝𝐨 𝐛𝐨𝐫𝐫𝐚𝐝𝐨𝐬")
	else:
		await f.edit("Ocurrió un error, inténtelo denuevo, revise sus credenciales y/o directorio")
		

async def nexcloud_eliminador(user, passw, host, proxy, username):
	if proxy:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	else:
		proxy = aiohttp.TCPConnector()
	async with aiohttp.ClientSession(connector=proxy) as session:
	  client = NexCloudClient.NexCloudClient(user,passw,host,session)
	  loged = await client.login()
	  if loged:
	    clear = await client.clear()
	    if clear:
	      if not user in save_cred:
	        save_cred[user] = {"ID":None,"TOKEN":None}
	      save_cred[user]["TOKEN"] = clear
	      return True
	    else:
	      return False
	  else:
	    return False


@bot.on_message(filters.command("deletelinks", prefixes="/")& filters.private)
async def delete_links(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	user_id = message.from_user.id
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	proxy = Configs["gp"]
	if proxy == "":
		proxy = aiohttp.TCPConnector()
	else:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	async with aiohttp.ClientSession(connector=proxy) as session:
		total_urls = len(Urls[username])
		if total_urls == 0:
			await send("𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝑼𝒓𝒍𝒔 𝒒𝒖𝒆 𝒆𝒍𝒊𝒎𝒊𝒏𝒂𝒓")
			return
		deleted = 0
		for url in Urls[username]:
			link = f"https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/delete_file/archivo/{url}?_=1670274909872"
			async with session.get(link) as response:
				if loads(await response.text())["success"]:
					deleted+=1
		if total_urls == deleted:
			Urls[username] = []
			await send("✅ 𝑫𝒐𝒏𝒆")

#descargas
@bot.on_message(filters.command("download", prefixes="/")& filters.private)
async def download_archive(client: Client, message: Message):
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
		await send(comp)
		return
	else:pass
	total_proc = total_de_procesos()
	if total_proc != False:
		await send(total_proc)
		return
	else:pass
	procesos += 1
	msg = await send("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
	count = 0
	for i in downlist[username]:
		filesize = int(str(i).split('"file_size":')[1].split(",")[0])
		try:
			filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")	
		except:
			filename = str(randint(11111,999999))+".mp4"
		start = time()
		try:
		    await msg.edit(f"𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂\n\n`{filename}`")
		except:
		    break
		try:
			a = await i.download(file_name=str(root[username]["actual_root"])+"/"+filename,progress=downloadmessage_progres,progress_args=(filename,start,msg))
			if Path(str(root[username]["actual_root"])+"/"+ filename).stat().st_size == filesize:
				await msg.edit("𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂 𝒆𝒙𝒊𝒕𝒐𝒔𝒂")
				count +=1
		except Exception as ex:
		    if procesos > 0:
		        procesos -= 1
		    else:pass
		    if "MessageIdInvalid" in str(ex):
		        pass
		    else:
		        #await bot.send_message(username,ex)
		        return
	if count == len(downlist[username]):
	  if count == 0:
	    return
	  if procesos > 0:
	    procesos -= 1
	  else:pass
	  await msg.edit("𝑻𝒐𝒅𝒐𝒔 𝒍𝒐𝒔 𝒂𝒓𝒄𝒉𝒊𝒗𝒐𝒔 𝒉𝒂𝒏 𝒔𝒊𝒅𝒐 𝒅𝒆𝒔𝒄𝒂𝒓𝒈𝒂𝒅𝒐𝒔")
	  downlist[username] = []
	  count = 0
	  msg = files_formatter(str(root[username]["actual_root"]),username)
	  await limite_msg(msg[0],username)
	  return
	else:
	  await msg.edit("**Error**")
	  if procesos > 0:
	    procesos -= 1
	  else:pass
	  msg = files_formatter(str(root[username]["actual_root"]),username)
	  await limite_msg(msg[0],username)
	  downlist[username] = []
	  return

#root
@bot.on_message(filters.regex("rm")& filters.private)
async def rm(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	print(0)
	if "_" in message.text:
	  list = message.text.split("_")[1]
	else:
	  list = message.text.split(" ")[1]
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	if "-" in list:
		v1 = int(list.split("-")[-2])
		v2 = int(list.split("-")[-1])
		for i in range(v1,v2+1):
			try:
				unlink(str(root[username]["actual_root"])+"/"+msgh[1][i])
			except Exception as ex:
				await bot.send_message(username,ex)
		msg = files_formatter(str(root[username]["actual_root"])+"/",username)
		await limite_msg(msg[0],username)
	else:
		try:
			unlink(str(root[username]["actual_root"])+"/"+msgh[1][int(list)])
			msg = files_formatter(str(root[username]["actual_root"])+"/",username)
			await limite_msg(msg[0],username)
		except Exception as ex:
			await bot.send_message(username,ex)

@bot.on_message(filters.regex("rmdir")& filters.private)
async def rmdir(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if "_" in message.text:
	  list = message.text.split("_")[1]
	else:
	  list = message.text.split(" ")[1]	
	filespath = Path(str(root[username]["actual_root"])+"/")
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	try:
		shutil.rmtree(str(root[username]["actual_root"])+"/"+msgh[1][int(list)])
		msg = files_formatter(str(root[username]["actual_root"])+"/",username)
		await limite_msg(msg[0],username)
	except Exception as ex:
		await bot.send_message(username,ex)

@bot.on_message(filters.command("deleteall", prefixes="/")& filters.private)
async def delete_all(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	shutil.rmtree("downloads/"+username+"/")
	root[username]["actual_root"] = "downloads/"+username
	msg = files_formatter(str(root[username]["actual_root"])+"/",username)
	await limite_msg(msg[0],username)

@bot.on_message(filters.regex("seven")& filters.private)
async def seven(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if "_" in message.text:
	  lista = message.text.split("_")
	else:
	  lista = message.text.split(" ")
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	if len(lista) == 2:
		i = int(lista[1])
		j = str(msgh[1][i])
		if not "." in j:
			h = await send(f"𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
			g = str(root[username]["actual_root"]+"/")+msgh[1][i]
			await bot.loop.run_in_executor(None,shutil.make_archive,j,"zip",g)
			await h.delete()
			shutil.move(j+".zip",root[username]["actual_root"])
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return
		else:
			g = str(root[username]["actual_root"]+"/")+msgh[1][i]
			o = await send("𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
			h = await bot.loop.run_in_executor(None,filezip,g,None)
			os.rename(h[0],h[0].replace("zip.1","")+".zip")
			await o.delete()
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return

	elif len(lista) == 3:
		i = int(lista[1])
		j = str(msgh[1][i])
		t = int(lista[2])
		g = str(root[username]["actual_root"]+"/")+msgh[1][i]
		h = await send(f"𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
		if not "." in j:
			p = await bot.loop.run_in_executor(None,shutil.make_archive,j,"zip",g)
			await h.edit("𝑫𝒊𝒗𝒊𝒅𝒊𝒆𝒏𝒅𝒐 𝒆𝒏 𝒑𝒂𝒓𝒕𝒆𝒔")
			a = await bot.loop.run_in_executor(None,sevenzip,p,None,t*1024*1024)
			os.remove(p)
			for i in a :
				shutil.move(i,root[username]["actual_root"])
			await h.edit("𝑪𝒐𝒎𝒑𝒓𝒆𝒔𝒊𝒐𝒏 𝒓𝒆𝒂𝒍𝒊𝒛𝒂𝒅𝒂")
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return
		else:
			a = await bot.loop.run_in_executor(None,sevenzip,str(root[username]["actual_root"])+"/"+j,None,t*1024*1024)
			await h.edit("𝑪𝒐𝒎𝒑𝒓𝒆𝒔𝒊𝒐𝒏 𝒓𝒆𝒂𝒍𝒊𝒛𝒂𝒅𝒂")
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return

@bot.on_message(filters.command("unzip", prefixes="/")& filters.private)
async def unzip(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	archivo = message.text.split(" ")[1]
	ruta = str(root[username]["actual_root"])
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	archivor = str(root[username]["actual_root"])+"/"+msgh[1][int(archivo)]
	a = await send("𝑫𝒆𝒔𝒄𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐 𝒂𝒓𝒄𝒉𝒊𝒗𝒐")
	try:
		descomprimir(archivor,ruta)
		await a.edit("𝑨𝒓𝒄𝒉𝒊𝒗𝒐 𝒅𝒆𝒔𝒄𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒅𝒐")
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	except Exception as ex:
		await a.edit("Error: ",ex)
		return

@bot.on_message(filters.command("mkdir", prefixes="/")& filters.private)
async def mkdir(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	name = message.text.split(" ")[1]
	if "." in name or "/" in name or "*" in name:
		await send("💢𝑬𝒍 𝒏𝒐𝒎𝒃𝒓𝒆 𝒏𝒐 𝒑𝒖𝒆𝒅𝒆 𝒄𝒐𝒏𝒕𝒆𝒏𝒆𝒓 . , * /")
		return
	rut = root[username]["actual_root"]
	os.mkdir(f"{rut}/{name}")
	await send(f"𝙎𝙚 𝙘𝙧𝙚𝙤 𝙡𝙖 𝙘𝙖𝙧𝙥𝙚𝙩𝙖\n\n /{name}")
	msg = files_formatter(str(root[username]["actual_root"]),username)
	await limite_msg(msg[0],username)

@bot.on_message(filters.command("mv", prefixes="/")& filters.private)
async def mv(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	lista = message.text.split(" ")
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	new_dir = int(lista[2])
	new = str(root[username]["actual_root"]+"/")+msgh[1][new_dir]
		
	if "-" in lista[1]:
		actual = lista[1]
		v1 = int(actual.split("-")[-2])
		v2 = int(actual.split("-")[-1])
		for i in range(v1,v2+1):
			try:
				actual = str(root[username]["actual_root"]+"/")+msgh[1][i]	
				shutil.move(actual,new)
			except Exception as ex:
				await bot.send_message(username,ex)
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	else:
		actual_dir = int(lista[1])
		try:
			actual = str(root[username]["actual_root"]+"/")+msgh[1][actual_dir]
			k = actual.split("downloads/")[-1]
			t = new.split("downloads/")[-1]
			await send(f"𝑴𝒐𝒗𝒊𝒅𝒐 𝒄𝒐𝒓𝒓𝒆𝒄𝒕𝒂𝒎𝒆𝒏𝒕𝒆\n\n `{k}` ➥ `{t}`")
			shutil.move(actual,new)
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			return
		except Exception as ex:
			await bot.send_message(username,ex)
			return

@bot.on_message(filters.command("rename", prefixes="/") & filters.private)
async def rename(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	h = root[username]["actual_root"]
	lista = message.text.split(" ")
	name1 = int(lista[1])
	name2 = lista[2]
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	actual = str(root[username]["actual_root"]+"/")+msgh[1][name1]
	shutil.move(actual,h+"/"+name2)
	await send(f"𝑹𝒆𝒏𝒐𝒎𝒃𝒓𝒂𝒅𝒐 𝒄𝒐𝒓𝒓𝒆𝒄𝒕𝒂𝒎𝒆𝒏𝒕𝒆\n\n `{msgh[1][name1]}` ➥ `{name2}`")
	msg = files_formatter(str(root[username]["actual_root"]),username)
	await limite_msg(msg[0],username)
	return

@bot.on_message(filters.command("cd", prefixes="/")& filters.private)
async def cd(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	msg = message.text
	lista = msg.split(" ")
	j = str(root[username]["actual_root"])+"/"
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	if ".." in lista:
		lista = msg.split(" ")[1]
	else:
		lista = int(msg.split(" ")[1])
	path = str(j)
	if lista != "..":
		if not "." in msgh[1][lista]:
			cd = path + msgh[1][lista]
			root[username]["actual_root"] = str(cd)
			msg = files_formatter(cd,username)
			await limite_msg(msg[0],username)
			return
		else:
			await send("𝑺𝒐𝒍𝒐 𝒑𝒖𝒆𝒅𝒆 𝒎𝒐𝒗𝒆𝒓𝒔𝒆 𝒂 𝒖𝒏𝒂 𝒄𝒂𝒓𝒑𝒆𝒕𝒂")
			return
	else:
		a = str(root[username]["actual_root"])
		b = a.split("/")[:-1]
		if len(b) == 1:
			await send("𝒀𝒂 𝒆𝒔𝒕𝒂 𝒆𝒏 𝒆𝒍 𝒅𝒊𝒓𝒆𝒄𝒕𝒐𝒓𝒊𝒐 𝒓𝒂𝒊𝒛")
			return
		else:
			a = str(root[username]["actual_root"])
			b = a.split("/")[:-1]	
			c = ""
			for i in b:
				c += i + "/"
			c = c.rstrip(c[-1])
			root[username]["actual_root"] = c
			msg = files_formatter(c,username)
			await limite_msg(msg[0],username)
			return

@bot.on_message(filters.command("ls", prefixes="/")& filters.private)
async def ls(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	msg = files_formatter(str(root[username]["actual_root"]),username)
	await limite_msg(msg[0],username)
	return

@bot.on_callback_query()
async def callback_data(bot,callback):
	username = callback.from_user.username
	user_id = callback.from_user.id
	if "uo" in callback.data:
	  if not username in TEMP_FILE:
	    await callback.message.edit("❌ No hay Archivos para Subir")
	    return
	  path = TEMP_FILE[username]
	  msg = await callback.message.edit("Analizando archivo ...")
	  if callback.data=="uo n":
	    await webdav(path,user_id,msg,username)
	  else:
	    await webdav2(path,user_id,msg,username)
	if callback.data == "cancel_button":
		await callback.message.delete()
		for i in downlist[username]:
		    try:
		        filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")
		    except:
		        continue
		    try:
		        try:
		            os.unlink(str(root[username]['actual_root'])+ "/" + filename)
		        except:
		            os.unlink(str(root[username]['actual_root'])+ "/" + filename + ".temp")
		    except:continue
		downlist[username] = []
		await bot.send_message(username,"**𝐃𝐞𝐬𝐜𝐚𝐫𝐠𝐚 𝐂𝐚𝐧𝐜𝐞𝐥𝐚𝐝𝐚**")
	elif callback.data == "up_cancel_button":
		control_upload[username] = True
		await callback.message.delete()
		await bot.send_message(username,"**Subida Cancelada**")
	if "delete" in callback.data:
		try:
			data = callback.data
			#print(data)
			await callback.message.delete()
			msgs = await bot.send_message(username,"🔂 **Eliminando ...**")

			filename = str(callback.data).split(" ")[-1]
			proxy = Configs[username]["gp"]
			user = Config[username]["username"]
			password = Config[username]["password"]
			host = Config[username]["host"]
			ids = save_cred[user]["ID"]
			url = f"{host}remote.php/dav/files/{ids}/Raul/{filename}"
			#print(url)
			if proxy:
				proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
			else:
				proxy = aiohttp.TCPConnector()

			async with aiohttp.ClientSession(connector=proxy,auth=aiohttp.BasicAuth(user, password)) as session:
				async with session.delete(url) as resp:
					print(resp.status)
					resp = await resp.text()
				if resp=='':
					await msgs.edit("📂 **FILE DELETED** 🗑")
				else:
					await msgs.edit("🤔 No se pudo Borrar, revice sus credenciales o si el archivo existe en la nube")
		except Exception as ex:
			print(str(ex))
  
@bot.on_message(filters.regex("up") & filters.private)
async def up(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	user_id = message.from_user.id
	print(11)
	try:await get_messages()
	except:await send_config()
	print(12)
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	print(13)
	if username not in boss and Configs["s"] == "Off":
		await client.send_message(username,'⛔𝑬𝒔𝒕𝒂 𝒇𝒖𝒏𝒄𝒊𝒐𝒏 𝒆𝒔𝒕𝒂 𝒂𝒑𝒂𝒈𝒂𝒅𝒂')
		return
	else: pass	
	print(14)
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
		await send(comp)
		return
	else:pass
	print(15)
	total_proc = total_de_procesos()
	if total_proc != False:
		await send(total_proc)
		return
	else:pass
	print(16)
	if "_" in message.text:
	  list = int(message.text.split("_")[1])
	else:
	  list = int(message.text.split(" ")[1])
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	print(17)
	try:
		path = str(root[username]["actual_root"]+"/")+msgh[1][list]
		print(18)
		msg = await send(f"𝑺𝒆𝒍𝒆𝒄𝒄𝒊𝒐𝒏𝒂𝒅𝒐 **{path}**")
		print(19)
		if Configs[username]["m"] == "u":
			fd = await uploadfile(path,user_id,msg,username)
		elif Configs[username]["m"] == "e":
			if len(Urls[username]) >= 10  and username not in boss:
				await msg.edit('⛔️ 𝑬𝒍 𝒍𝒊𝒎𝒊𝒕𝒆 𝒅𝒆 𝒍𝒊𝒏𝒌𝒔 𝒇𝒖𝒆 𝒑𝒂𝒔𝒂𝒅𝒐 , 𝒖𝒕𝒊𝒍𝒊𝒛𝒆 **/deletelinks**')
				return
			else:
				await uploadfileapi(path,user_id,msg,username)
		elif Configs[username]["m"] == "n":
			#await proccess(path,user_id,msg,username)
			TEMP_FILE[username] = path
			button1 = InlineKeyboardButton("🎇 Normal","uo n")
			button2 = InlineKeyboardButton("🎆 Ilimitada","uo i")
			buttons = [[button1,button2]]
			reply_markup = InlineKeyboardMarkup(buttons)
			await msg.edit("👉 **SELECCIONE EL MODO DE SUBIDA**\n",reply_markup=reply_markup)
			return
		else:
			await uploaddraft(path,user_id,msg,username)
	except Exception as ex:
		await send(ex)

@bot.on_message(filters.command("tg", prefixes="/") & filters.private)
async def tg(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
		await send(comp)
		return
	else:pass
	total_proc = total_de_procesos()
	if total_proc != False:
		await send(total_proc)
		return
	else:pass
	list = int(message.text.split(" ")[1])
	msgh = files_formatter(str(root[username]["actual_root"]),username)
	try:
		path = str(root[username]["actual_root"]+"/")+msgh[1][list]
		msg = await send(f"𝑺𝒆𝒍𝒆𝒄𝒄𝒊𝒐𝒏𝒂𝒅𝒐 **{path}**")
		filename = msgh[1][list]
		start = time()
		r = await bot.send_document(username,path,file_name=filename,progress=downloadmessage_tg,
									progress_args=(filename,start,msg))	
		await msg.edit("𝑺𝒖𝒃𝒊𝒅𝒂 𝑪𝒐𝒎𝒑𝒍𝒆𝒕𝒂𝒅𝒂")
		return
	except Exception as ex:
		await send(ex)
		return

#procesos
@bot.on_message(filters.command("view_process", prefixes="/") & filters.private)
async def view_process(client: Client, message: Message):	
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	await send(f"𝑬𝒍 𝒃𝒐𝒕 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒕𝒊𝒗𝒐(𝒔) {str(procesos)} 𝒅𝒆 15 ")
	return

@bot.on_message(filters.command("cancel", prefixes="/") & filters.private)
async def cancel(client: Client, message: Message):	
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if id_de_ms[username]["proc"] == "Up":
		p = await client.send_message(username,"𝑷𝒓𝒐𝒄𝒆𝒔𝒂𝒏𝒅𝒐")
		try:
			await id_de_ms[username]["msg"].delete()
			id_de_ms[username] = {"msg":"", "proc":""}
			await p.edit("✅ 𝑷𝒓𝒐𝒄𝒆𝒔𝒐 𝑪𝒂𝒏𝒄𝒆𝒍𝒂𝒅𝒐")
			if procesos > 0:
					procesos -= 1
			else:pass
			return
		except:
				if procesos > 0:
					procesos -= 1
				else:pass
				id_de_ms[username] = {"msg":"", "proc":""}
				await p.edit("✅ 𝑷𝒓𝒐𝒄𝒆𝒔𝒐 𝑪𝒂𝒏𝒄𝒆𝒍𝒂𝒅𝒐")
				return
	else:
		await client.send_message(username,"𝑵𝒐 𝒉𝒂𝒚 𝒑𝒓𝒐𝒄𝒆𝒔𝒐𝒔 𝒅𝒆 𝒔𝒖𝒃𝒊𝒅𝒂 𝒒𝒖𝒆 𝒄𝒂𝒏𝒄𝒆𝒍𝒂𝒓")
		return

#comandos de admin
@bot.on_message(filters.command("supr_process", prefixes="/") & filters.private)
async def supr_process(client: Client, message: Message):	
	global procesos
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username in boss:
		procesos = 0
		await send(f"✅ 𝑫𝒐𝒏𝒆")
	else:return

@bot.on_message(filters.command("change_status", prefixes="/") & filters.private)
async def change_status(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username in boss:
		if Configs["s"] == "Off":
			Configs["s"] = "On"
		else:
			Configs["s"] = "Off"
		await send(f"__**Status cambiado a **__"+  Configs["s"])
		await send_config()
	else :
		await send("🚷 𝑪𝒐𝒎𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒂𝒅𝒎𝒊𝒏𝒊𝒔𝒕𝒓𝒂𝒅𝒐𝒓𝒆𝒔")
		return

@bot.on_message(filters.command("users", prefixes="/") & filters.private)
async def users(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username in boss:	
		total = len(Configs) - 10
		message = "**Usuarios: **"+ str(total)+'\n\n'
		for user in Configs:
			if user == "uclv":continue
			if user == "gtm":continue
			if user == "uvs":continue
			if user == "ltu":continue
			if user == "ucuser":continue
			if user == "ucpass":continue
			if user == "gp":continue
			if user == "s":continue
			if user == "UHTRED_OF_BEBBANBURG":continue
			if user == "avatar23":continue
			if user == "Locura05":continue
			if user == "mcfee2828":continue
			if user == "uclv_p":continue
			message+=f"{user}\n"
		msg = f"{message}\n"
		await client.send_message(username,msg)
	else :
		await send("🚷 𝑪𝒐𝒎𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒂𝒅𝒎𝒊𝒏𝒊𝒔𝒕𝒓𝒂𝒅𝒐𝒓𝒆𝒔")
		return

@bot.on_message(filters.command("add", prefixes="/") & filters.private)
async def add(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username in boss:
		list = message.text.split(" ")						
		uss = list[1]
		Configs[uss] ={"z":99,"m":"u","a":"c","t":"y","gp":False}	
		await send_config()
		await client.send_message(username,f"@{uss} Add")
	else :
		await send("🚷 𝑪𝒐𝒎𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒂𝒅𝒎𝒊𝒏𝒊𝒔𝒕𝒓𝒂𝒅𝒐𝒓𝒆𝒔")
		return

@bot.on_message(filters.command("kick", prefixes="/") & filters.private)
async def kick(client: Client, message: Message):	
	username = message.from_user.username
	send = message.reply
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if username in boss:			
		list = message.text.split(" ")
		uss = list[1]
		del Configs[uss]
		await send_config()
		await client.send_message(username,f'@{uss} Kick')
	else :
		await send("🚷 𝑪𝒐𝒎𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒂𝒅𝒎𝒊𝒏𝒊𝒔𝒕𝒓𝒂𝒅𝒐𝒓𝒆𝒔")
		return

#descarga de archivos y enlaces
@bot.on_message(filters.media & filters.private)
async def delete_draft_y_down_media(client: Client, message: Message):
	username = message.from_user.username
	send = message.reply
	global procesos
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	try:
	  file_name = str(message).split('"file_name": ')[1].split(",")[0].replace('"',"").endswith(".txt")
	except:
	  file_name = False
	if  file_name and Configs[username]["m"] == "d" :
		if message.from_user.is_bot: return
		await borrar_de_draft(message,client,username)
		return
	elif len(downlist[username]) == 0:
	  downlist[username].append(message)
	  pass
	else:
		downlist[username].append(message)
		print(len(downlist[username]))
		return
	comp = comprobar_solo_un_proceso(username) 
	if comp != False:
	  await send(comp)
	  return
	else:pass
	total_proc = total_de_procesos()
	if total_proc != False:
	  await send(total_proc)
	  return
	else:pass
	procesos += 1
	msg = await send("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
	count = 0
	for i in downlist[username]:
	  filesize = int(str(i).split('"file_size":')[1].split(",")[0])
	  try:
	    filename = str(i).split('"file_name": ')[1].split(",")[0].replace('"',"")
	  except:
	    filename = str(randint(11111,999999))+".mp4"
	  start = time()
	  try:
	    await msg.edit(f"𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂\n\n`{filename}`")
	  except:
	    break
	  try:
	    a = await i.download(file_name=str(root[username]["actual_root"])+"/"+filename,progress=downloadmessage_progres,progress_args=(filename,start,msg))
	    if Path(str(root[username]["actual_root"])+"/"+ filename).stat().st_size == filesize:
	      await msg.edit("𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂 𝒆𝒙𝒊𝒕𝒐𝒔𝒂")
	      count +=1
	  except Exception as ex:
	    if procesos > 0:
	      procesos -= 1
	    else:pass
	    if "MessageIdInvalid" in str(ex):
	      pass
	    else:
	      #await bot.send_message(username,ex)
	      return
	if count == len(downlist[username]):
	  if count == 0:
	    return
	  if procesos > 0:
	    procesos -= 1
	  else:pass
	  await msg.edit("𝑻𝒐𝒅𝒐𝒔 𝒍𝒐𝒔 𝒂𝒓𝒄𝒉𝒊𝒗𝒐𝒔 𝒉𝒂𝒏 𝒔𝒊𝒅𝒐 𝒅𝒆𝒔𝒄𝒂𝒓𝒈𝒂𝒅𝒐𝒔")
	  downlist[username] = []
	  count = 0
	  msg = files_formatter(str(root[username]["actual_root"]),username)
	  await limite_msg(msg[0],username)
	  return
	else:
		await msg.edit("**Error**")
		if procesos > 0:
			procesos -= 1
		else:pass
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		downlist[username] = []
		return		

@bot.on_message((filters.regex("https://") | filters.regex("http://")) & filters.private)
async def down_link(client: Client, message: Message):
	print(message)
	global procesos
	try:username = message.from_user.username
	except:
		print("Username no valido")
		return
	send = message.reply
	user_id = message.from_user.id
	try:await get_messages()
	except:await send_config()
	if comprobacion_de_user(username) == False:
		await send("⛔ 𝑵𝒐 𝒕𝒊𝒆𝒏𝒆 𝒂𝒄𝒄𝒆𝒔𝒐")
		return
	else:pass
	if "youtu.be/" in message.text or "twitch.tv/" in message.text or "youtube.com/" in message.text or "xvideos.com" in message.text or "xnxx.com" in message.text:
		list = message.text.split(" ")
		url = list[0]
		try:format = str(list[1])
		except:format = "720"
		msg = await send("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
		procesos += 1
		download = await ytdlp_downloader(url,user_id,msg,username,lambda data: download_progres(data,msg,format),format)
		if procesos != 0:
			procesos -= 1
		await msg.edit("𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂 𝒆𝒙𝒊𝒕𝒐𝒔𝒂")
		await msg.edit("𝑨𝒓𝒄𝒉𝒊𝒗𝒐 𝒈𝒖𝒂𝒓𝒅𝒂𝒅𝒐")
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return
	
	elif "https://www.mediafire.com/" in message.text:
		url = message.text
		if "?dkey=" in str(url):
			url = str(url).split("?dkey=")[0]
		msg = await send("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
		procesos += 1
		file = await download_mediafire(url, str(root[username]["actual_root"])+"/", msg, callback=mediafiredownload)
		if not file:
		  return
		if procesos != 0:
			procesos -= 1
		await msg.edit("𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂 𝒆𝒙𝒊𝒕𝒐𝒔𝒂")
		await msg.edit("𝑨𝒓𝒄𝒉𝒊𝒗𝒐 𝒈𝒖𝒂𝒓𝒅𝒂𝒅𝒐")
		msg = files_formatter(str(root[username]["actual_root"]),username)
		await limite_msg(msg[0],username)
		return

	elif "https://mega.nz/file/" in message.text:
		url = message.text
		mega = pymegatools.Megatools()
		try:
			filename = mega.filename(url)
			g = await send(f"Descargando {filename} ...")
			data = mega.download(url,progress=None)	
			procesos += 1
			shutil.move(filename,str(root[username]["actual_root"]))
			await g.delete()
			msg = files_formatter(str(root[username]["actual_root"]),username)
			await limite_msg(msg[0],username)
			if procesos != 0:
				procesos -= 1
			return
		except Exception as ex:
			if procesos != 0:
				procesos -= 1
			if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
			else:
				await send(ex)	
				return
	else:
		j = str(root[username]["actual_root"])+"/"

		url = message.text
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as r:
				try:
					filename = unquote_plus(url.split("/")[-1])
				except:
					filename = r.content_disposition.filename	
				fsize = int(r.headers.get("Content-Length"))
				msg = await send("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
				procesos += 1
				f = open(f"{j}{filename}","wb")
				newchunk = 0
				start = time()
				try:
				  async for chunk in r.content.iter_chunked(1024*1024):
				    newchunk+=len(chunk)
				    await mediafiredownload(newchunk,fsize,filename,start,msg)
				    f.write(chunk)
				  f.close()
				except:
				  file = f"{j}{filename}"
				  os.unlink(file)
				  return
				file = f"{j}{filename}"
				await msg.edit("𝑫𝒆𝒔𝒄𝒂𝒓𝒈𝒂 𝒆𝒙𝒊𝒕𝒐𝒔𝒂")
				if procesos != 0:
					procesos -= 1
				else:pass
				await msg.edit("𝑨𝒓𝒄𝒉𝒊𝒗𝒐 𝒈𝒖𝒂𝒓𝒅𝒂𝒅𝒐")
				msg = files_formatter(str(root[username]["actual_root"]),username)
				await limite_msg(msg[0],username)
				return

#funciones
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Yi', suffix)

def get_webservice_token(host='',username='',password='',proxy=None): 
	try:
		pproxy = None 
		webserviceurl = f'{host}login/token.php?service=moodle_mobile_app&username={username}&password={password}' 
		resp = requests.get(webserviceurl, proxies=pproxy,timeout=8) 
		data = json.loads(resp.text) 
		if data['token']!='': 
			return data['token'] 
		return None 
	except: return None

async def delete_nube(url,username):
	proxy = Configs["gp"] 
	if proxy == "":
		connection = aiohttp.TCPConnector()
	else:
		connection = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	session = aiohttp.ClientSession(connector=connection)

	async with ClientSession(connector=connection) as s:
		user = Config[username]["username"]
		passw = Config[username]["password"]
		host = Config[username]["host"]
		
		client = moodle(user, passw, host)
		loged = await client.login(s)
		
		if loged:
			a = await client.delete_nexc(url,s)
			
		else :
			return False

def descomprimir(archivo,ruta):
	archivozip = archivo
	with ZipFile(file = archivozip, mode = "r", allowZip64 = True) as file:
		archivo = file.open(name = file.namelist()[0], mode = "r")
		archivo.close()
		guardar = ruta
		file.extractall(path = guardar)

async def limite_msg(text,username):
	lim_ch = 1500
	text = text.splitlines() 
	msg = ''
	msg_ult = '' 
	c = 0
	for l in text:
		if len(msg +"\n" + l) > lim_ch:		
			msg_ult = msg
			await bot.send_message(username,msg)	
			msg = ''
		if msg == '':	
			msg+= l
		else:		
			msg+= "\n" +l	
		c += 1
		if len(text) == c and msg_ult != msg:
			await bot.send_message(username,msg)

def update_progress_bar(inte,max):
	percentage = inte / max
	percentage *= 100
	percentage = round(percentage)
	hashes = int(percentage / 5)
	spaces = 20 - hashes
	progress_bar = "[ " + "•" * hashes + "•" * spaces + " ]"
	percentage_pos = int(hashes / 1)
	percentage_string = str(percentage) + "%"
	progress_bar = progress_bar[:percentage_pos] + percentage_string + progress_bar[percentage_pos + len(percentage_string):]
	return(progress_bar)

def iprox(proxy):
    tr = str.maketrans(
        "@./=#$%&:,;_-|0123456789abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ZYXWVUTSRQPONMLKJIHGFEDCBAzyIwvutsrqponmlkjihgf3dcba9876543210|-_;,:&%$#=/.@",
    )
    return str.translate(proxy[::2], tr) 

def files_formatter(path,username):
	rut = str(path)
	filespath = Path(str(path))
	result = []
	dirc = []
	final = []
	for p in filespath.glob("*"):
		if p.is_file():
			result.append(str(Path(p).name))
		elif p.is_dir():
			dirc.append(str(Path(p).name))
	result.sort()
	dirc.sort()
	msg = f'𝑫𝒊𝒓𝒆𝒄𝒕𝒐𝒓𝒊𝒐 𝒂𝒄𝒕𝒖𝒂𝒍\n\n `{str(rut).split("downloads/")[-1]}`\n\n'
	if result == [] and dirc == [] :
		return msg , final
	for k in dirc:
		final.append(k)
	for l in result:
		final.append(l)
	i = 0
	for n in final:
		try:
			size = Path(str(path)+"/"+n).stat().st_size
		except: pass
		if not "." in n:
			msg+=f"╭➣❮ /seven_{i} ❯─❮ /rmdir_{i} ❯\n╰➣📂Carpeta: `{n}`\n\n"
		else:
			msg+=f"╭➣❮ /up_{i} ❯─❮ /rm_{i} ❯\n╰➣ {sizeof_fmt(size)} - `📃 {n}`\n"
		i+=1
	msg+= f"\n𝑬𝒍𝒊𝒎𝒊𝒏𝒂𝒓 𝒅𝒊𝒓𝒆𝒄𝒕𝒐𝒓𝒊𝒐 𝒓𝒂𝒊𝒛\n**/deleteall**"
	return msg , final

async def extractDownloadLink(contents):
    for line in contents.splitlines():
        m = re.search(r'href="((http|https)://download[^"]+)', line)
        if m:
            return m.groups()[0]

async def download_mediafire(url, path, msg, callback=None):
	session = aiohttp.ClientSession()
	response = await session.get(url)
	url = await extractDownloadLink(await response.text())
	response = await session.get(url)
	filename = response.content_disposition.filename
	f = open(path+"/"+filename, "wb")
	chunk_ = 0
	total = int(response.headers.get("Content-Length"))
	start = time()
	error = None
	try:
	  while True:
	    chunk = await response.content.read(1024)
	    if not chunk:
	      break
	    chunk_+=len(chunk)
	    if callback:
	      await callback(chunk_,total,filename,start,msg)
	    f.write(chunk)
	    f.flush()
	except:
	  os.unlink(path+"/"+filename)
	  error = True
	  return None
	return path+"/"+filename

def sevenzip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size
    if not volume:
        volume = fsize + 1024
    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3
    with MultiVolume(
        fpath.with_name(fpath.name+".7z"), mode="wb", volume=volume, ext_digits=ext_digits
    ) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)
            archive_writer.write(fpath, fpath.name)
    files = []
    for file in archive._files:
        files.append(file.name)
    return files

def filezip(fpath: Path, password: str = None, volume = None):
    filters = [{"id": FILTER_COPY}]
    fpath = Path(fpath)
    fsize = fpath.stat().st_size
    if not volume:
        volume = fsize + 1024
    ext_digits = len(str(fsize // volume + 1))
    if ext_digits < 3:
        ext_digits = 3
    with MultiVolume(
        fpath.with_name(fpath.name+"zip"), mode="wb", volume=volume, ext_digits=0) as archive:
        with SevenZipFile(archive, "w", filters=filters, password=password) as archive_writer:
            if password:
                archive_writer.set_encoded_header_mode(True)
                archive_writer.set_encrypted_header(True)
            archive_writer.write(fpath, fpath.name)
    files = []
    for file in archive._files:
        files.append(file.name)
    return files

def update(username):
    Configs[username] = {"z": 900,"m":"e","a":"a"}
async def get_messages():
	msg = await bot.get_messages(Channel_Id,message_ids=3)
	Configs.update(loads(msg.text))
async def send_config():
	try:
		await bot.edit_message_text(Channel_Id,message_id=db_access,text=dumps(Configs,indent=4))
	except:
		#await bot.send_message(Channel_Id,text=dumps(Configs,indent=4))
		pass

async def ytdlp_downloader(url,usid,msg,username,callback,format):
	class YT_DLP_LOGGER(object):
		def debug(self,msg):
			pass
		def warning(self,msg):
			pass
		def error(self,msg):
			pass
	j = str(root[username]["actual_root"])+"/"
	resolution = str(format)	
	dlp = {"logger":YT_DLP_LOGGER(),"progress_hooks":[callback],"outtmpl":f"./{j}%(title)s.%(ext)s","format":f"best[height<={resolution}]"}
	downloader = yt_dlp.YoutubeDL(dlp)
	loop = asyncio.get_running_loop()
	filedata = await loop.run_in_executor(None,downloader.extract_info, url)
	filepath = downloader.prepare_filename(filedata)
	return filedata["requested_downloads"][0]["_filename"]	

seg = 0
def download_progres(data,message,format):
	if data["status"] == "downloading":
		filename = data["filename"].split("/")[-1]
		_downloaded_bytes_str = data["_downloaded_bytes_str"]
		_total_bytes_str = data["_total_bytes_str"]
		if _total_bytes_str == "N/A":
			_total_bytes_str = data["_total_bytes_estimate_str"]		
		_speed_str = data["_speed_str"].replace(" ","")
		_format_str = format		
		msg = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
		msg+= f"▶️ 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {_downloaded_bytes_str} of {_total_bytes_str}\n\n"
		msg+= f"🎥Resolución: {_format_str}p\n\n"	
		global seg 
		if seg != localtime().tm_sec:
			try:message.edit(msg,reply_markup=message.reply_markup)
			except:pass
		seg = localtime().tm_sec
async def downloadmessage_progres(chunk,filesize,filename,start,message):
		now = time()
		diff = now - start
		mbs = chunk / diff
		msg = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
		try:
			msg+= update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
		except:pass
		msg+= f"▶️ 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(chunk)} of {sizeof_fmt(filesize)} \n\n"	
		global seg
		if seg != localtime().tm_sec:
			try: await message.edit(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel","cancel_button")]]))
			except MessageNotModified:
			  pass
		seg = localtime().tm_sec
def uploadfile_progres(chunk,filesize,start,filename,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	msg = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
	try:
		msg+=update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
	except:pass
	msg+= f"▶️ 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(chunk)} of {sizeof_fmt(filesize)}\n\n"
	global seg
	if seg != localtime().tm_sec:
		message.edit(msg)
	seg = localtime().tm_sec
async def mediafiredownload(chunk,total,filename,start,message):
	now = time()
	diff = now - start
	mbs = chunk / diff
	msg = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
	try:
		msg+= update_progress_bar(chunk,total)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
	except: pass
	msg+= f"▶️ 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(chunk)} of {sizeof_fmt(total)}\n\n"
	global seg
	if seg != localtime().tm_sec:
		try: await message.edit(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel","cancel_button")]]))
		except MessageNotModified:
			 pass
	seg = localtime().tm_sec
async def downloadmessage_tg(chunk,filesize,filename,start,message):
		now = time()
		diff = now - start
		mbs = chunk / diff
		msg = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
		try:
			msg+=update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
		except:pass
		msg+= f"▶️ 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐:: {sizeof_fmt(chunk)} of {sizeof_fmt(filesize)}\n\n"	
		global seg
		if seg != localtime().tm_sec:
			try: await message.edit(msg)
			except:pass
		seg = localtime().tm_sec


class MoodleClient:
	def __init__(self,username,password,moodle,proxy):
		self.url = moodle
		self.username = username
		self.password = password
		self.session = aiohttp.ClientSession(cookie_jar=aiohttp.CookieJar(unsafe=True),connector=proxy)
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"}
		
	async def uploadtoken(self,f,progress,token):
		url = self.url+"/webservice/upload.php"
		file = Progress(f,progress)
		query = {"token":token,"file":file}
		async with self.session.post(url,data=query,headers=self.headers,ssl=False) as response:
			text = await response.text()
		dat = loads(text)[0]
		url = self.url+"/draftfile.php/"+str(dat["contextid"])+"/user/draft/"+str(dat["itemid"])+"/"+str(quote(dat["filename"]))
		urlw = self.url+"/webservice/rest/server.php?moodlewsrestformat=json"
		query = {"formdata":f"name=Event&eventtype=user&timestart[day]=31&timestart[month]=9&timestart[year]=3786&timestart[hour]=00&timestart[minute]=00&description[text]={quote_plus(url)}&description[format]=1&description[itemid]={randint(100000000,999999999)}&location=&duration=0&repeat=0&id=0&userid={dat['userid']}&visible=1&instance=1&_qf__core_calendar_local_event_forms_create=1","moodlewssettingfilter":"true","moodlewssettingfileurl":"true","wsfunction":"core_calendar_submit_create_update_form","wstoken":token}
		async with self.session.post(urlw,data=query,headers=self.headers,ssl=False) as response:
			text = await response.text()	
		try:
			a = findall("https?://[^\s\<\>]+[a-zA-z0-9]",loads(text)["event"]["description"])[-1].replace("pluginfile.php/","webservice/pluginfile.php/")+"?token="+token	
			return a , url	
		except:
			return url		

class Progress(BufferedReader):
    def __init__(self, filename, read_callback):
        f = open(filename, "rb")
        self.filename = Path(filename).name
        self.__read_callback = read_callback
        super().__init__(raw=f)
        self.start = time()
        self.length = Path(filename).stat().st_size

    def read(self, size=None):
        calc_sz = size
        if not calc_sz:
            calc_sz = self.length - self.tell()
        self.__read_callback(self.tell(), self.length,self.start,self.filename)
        return super(Progress, self).read(size)

def comprobacion_de_user(username):
	if username in Configs or username in boss:			
		if exists('downloads/'+str(username)+'/'):pass
		else:os.makedirs('downloads/'+str(username)+'/')	
		try:Urls[username]
		except:Urls[username] = []
		try:Config[username]
		except:Config[username] = {"username":"","password":"","repoid":"","host":""}
		try:id_de_ms[username]
		except:id_de_ms[username] = {"msg":"","proc":""}
		try:root[username]
		except:root[username] = {"actual_root":f"downloads/{str(username)}"}
		try:downlist[username]
		except:downlist[username] = []
	else:
		return False

def comprobar_solo_un_proceso(username):
	if id_de_ms[username]["proc"] == "Up" :
		rup = "𝒀𝒂 𝒕𝒊𝒆𝒏𝒆 𝒖𝒏 𝒑𝒓𝒐𝒄𝒆𝒔𝒐 𝒂𝒄𝒕𝒊𝒗𝒐. 𝑼𝒔𝒆 **/cancel** 𝒐 𝒆𝒔𝒑𝒆𝒓𝒆"
		return rup
	else:
		return False

def total_de_procesos():
	global procesos
	hgy = "𝑬𝒍 𝒃𝒐𝒕 𝒕𝒊𝒆𝒏𝒆 𝒅𝒆𝒎𝒂𝒔𝒊𝒂𝒅𝒐𝒔 𝒑𝒓𝒐𝒄𝒆𝒔𝒐𝒔 𝒂𝒄𝒕𝒊𝒗𝒐𝒔. 𝑷𝒓𝒖𝒆𝒃𝒆 𝒆𝒏 𝒖𝒏𝒐𝒔 𝒎𝒊𝒏𝒖𝒕𝒐𝒔."
	if procesos >= 15:
		return hgy
	else:
		return False

async def borrar_de_draft(message,client,username):
	pro = Configs["gp"]
	proxysall = {'https': pro, 'http': pro}
	proxy = proxysall
	use = Config[username]["username"]
	pase = Config[username]["password"]
	hoe = Config[username]["host"]
	txt = await message.download()
	a = await client.send_message("❗𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒔𝒆𝒓𝒗𝒊𝒅𝒐𝒓")
	try:
		rep = requests.get(hoe,proxies=proxy,timeout=20,allow_redirects=False)
		await a.edit("𝑺𝒆𝒓𝒗𝒊𝒅𝒐𝒓 𝑶𝒏𝒍𝒊𝒏𝒆 ✔")
	except:
		await a.edit(f"{hoe} is Down")
		return
	await a.edit('⌛𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒂𝒖𝒕𝒐𝒓𝒊𝒛𝒂𝒄𝒊ó𝒏...')
	with open(txt, "rb") as f:
		msg = f.read().decode("UTF-8")
		for i in msg.split('\n'):
			if not 'h' in i:
				continue
			Urls_draft[username].append(i)
		os.unlink(txt)
		a = await a.edit('𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒃𝒐𝒓𝒓𝒂𝒓✅')
		count = 1
		await a.edit(f"𝑩𝒐𝒓𝒓𝒂𝒏𝒅𝒐 1 𝒖𝒓𝒍𝒔 𝒅𝒆 𝒍𝒂 𝒏𝒖𝒃𝒆...☁")
		while len(Urls_draft[username]) != 0:
			for i in Urls_draft[username]:			
				ret = delete(use,pase,hoe,i,proxy)
				if ret != False:
					count += 1
					await a.edit(f"𝑩𝒐𝒓𝒓𝒂𝒏𝒅𝒐 **{count}** 𝒖𝒓𝒍𝒔 𝒅𝒆 𝒍𝒂 𝒏𝒖𝒃𝒆...☁")
					Urls_draft[username].remove(i)
				else:
					continue
		if len(Urls_draft[username]) == 0:
			await a.edit('𝑻𝒙𝒕 𝒆𝒍𝒊𝒎𝒊𝒏𝒂𝒅𝒐 𝒄𝒐𝒓𝒓𝒆𝒄𝒕𝒂𝒎𝒆𝒏𝒕𝒆✅')
			return		
		else:
			f = len(Urls_draft[username])
			await a.edit(f"𝑬𝒓𝒓𝒐𝒓 {f} 𝑼𝒓𝒍(𝒔) 𝒏𝒐 𝒆𝒍𝒊𝒎𝒊𝒏𝒂𝒅𝒂(𝒔).")
			return

async def uploaddraft(file,usid,msg,username):
	user = Config[username]["username"]
	password = Config[username]["password"]
	host = Config[username]["host"]
	repoid = Config[username]["repoid"]
	zips = Configs[username]["z"]
	proxy = Configs[username]["gp"]
	print(1000)

	if proxy == False:
		connector = None
	else:
		connector = proxy
	if proxy == False:
		connection = aiohttp.TCPConnector()
	else:
		connection = aiohttp_socks.ProxyConnector(ssl=False).from_url(f"{proxy}")
	
	session = aiohttp.ClientSession(connector=connection)
	await msg.edit("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
	filename = Path(file).name
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	
	await msg.edit("❗𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒔𝒆𝒓𝒗𝒊𝒅𝒐𝒓")
	try:
		async with session.get(host,timeout=20,ssl=False) as resp:
			await resp.text()
			await msg.edit("𝑺𝒆𝒓𝒗𝒊𝒅𝒐𝒓 𝑶𝒏𝒍𝒊𝒏𝒆 ✔")
	except Exception as ex:
		await msg.edit(f"{host} is Down:\n\n{ex}")
		return
	
	id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}
	
	if filesize > zipssize:
		await msg.edit("📦 𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
		files = sevenzip(file,volume=zipssize)
		
		client = MoodleClient2(host,user,password,repoid,connector)
		links = []
		for file in files:	
			try:
				upload = await client.LoginUpload(file,lambda size,total,start,filename: uploadfile_progres(size,total,start,filename,msg))
				await bot.send_message(usid,f"**{upload}**")
				links.append(upload)
			except Exception as ex:
				if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
				else:
					await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓:\n\n{ex}")
				id_de_ms[username]["proc"] = ""
				return
		message = ""
		for link in links:
			message+=f"{link}\n"
		await msg.edit("✅ 𝑭𝒊𝒏𝒂𝒍𝒊𝒛𝒂𝒅𝒐 𝒆𝒙𝒊𝒕𝒐𝒔𝒂𝒎𝒆𝒏𝒕𝒆")
		with open(filename+".txt","w") as txt:
			txt.write(message)
		await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
		if username in boss:
			pass
		else:
		  pass
		id_de_ms[username]["proc"] = ""
		os.unlink(filename+".txt")
		return
	else:
		client = MoodleClient2(host,user,password,repoid,connector)
		try:
			upload = await client.LoginUpload(file,lambda size,total,start,filename: uploadfile_progres(size,total,start,filename,msg))
			await msg.edit(f"__**{upload}**__")
			with open(filename+".txt","w") as txt:
				txt.write(upload)
			await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
			if username in boss:
				pass
			else:
			  pass
			id_de_ms[username]["proc"] = ""
			os.unlink(filename+".txt")
			return
		except Exception as ex:
			if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
			else:
				await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓:\n\n{ex}")
			id_de_ms[username]["proc"] = ""
			return

async def uploadfile(file,usid,msg,username):
	proxy = Configs[username]["gp"]
	mode = Configs[username]["a"]
	usernamew = ''
	passwordw = ''
	
	if mode == "c":
		moodle = "https://moodle.uclv.edu.cu"
		token = Configs["uclv"]
		connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}") #aiohttp.TCPConnector()
	elif mode == "h":
		moodle = "https://aulauvs.gtm.sld.cu"
		token = Configs["gtm"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	elif mode == "b":
		moodle = "https://uvs.ucm.cmw.sld.cu"
		token = Configs["uvs"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	elif mode == "l":
		moodle = "https://uvs.ltu.sld.cu"
		token = Configs["ltu"]
		if proxy == "":
			connector = aiohttp.TCPConnector()
		else:
			connector = aiohttp_socks.ProxyConnector(ssl=False).from_url(f"{proxy}")
	elif mode == "a":
		moodle = "https://moodle.uclv.edu.cu"
		uset = Config[username]["username"]
		pasel = Config[username]["password"]
		hot = Config[username]["host"]
		connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
		await msg.edit(f"𝑶𝒃𝒕𝒆𝒏𝒊𝒆𝒏𝒅𝒐 𝑻𝒐𝒌𝒆𝒏")
		try:
			token = get_webservice_token(hot,uset,pasel)
			await msg.edit(f"✅ 𝑻𝒐𝒌𝒆𝒏 𝑶𝒃𝒕𝒆𝒏𝒊𝒅𝒐")
		except:
			id_de_ms[username]["proc"] = ""
			return		
	elif mode == "t":
		moodle = "https://moodle.uclv.edu.cu"
		hot = "https://moodle.uclv.edu.cu/"
		uset = Configs["ucuser"]
		pasel = Configs["ucpass"]
		connector = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
		token = Configs["uclv_p"]	
	
	zips = Configs[username]["z"]

	if mode == "a" or mode == "c" or mode == "t":
		if int(zips) > 399:
			await msg.edit("⛔𝑺𝒊 𝒖𝒔𝒂 𝑼𝑪𝑳𝑽 𝒍𝒐𝒔 𝒛𝒊𝒑𝒔 𝒏𝒐 𝒑𝒖𝒆𝒅𝒆𝒏 𝒔𝒆𝒓 𝒎𝒂𝒚𝒐𝒓𝒆𝒔 𝒂 399 𝑴𝑩")
			return
	elif mode  == "b":
		if int(zips) > 499:
			await msg.edit("⛔𝑺𝒊 𝒖𝒔𝒂 𝑼𝒗𝒔.𝒖𝒄𝒎 𝒍𝒐𝒔 𝒛𝒊𝒑𝒔 𝒏𝒐 𝒑𝒖𝒆𝒅𝒆𝒏 𝒔𝒆𝒓 𝒎𝒂𝒚𝒐𝒓𝒆𝒔 𝒂 499 𝑴𝑩")
			return
	elif mode == "l":
		if int(zips) > 249:
			await msg.edit("⛔𝑺𝒊 𝒖𝒔𝒂 𝑼𝒗𝒔.𝒍𝒕𝒖 𝒍𝒐𝒔 𝒛𝒊𝒑𝒔 𝒏𝒐 𝒑𝒖𝒆𝒅𝒆𝒏 𝒔𝒆𝒓 𝒎𝒂𝒚𝒐𝒓𝒆𝒔 𝒂 249 𝑴𝑩")
			return
	elif mode == "h":
		if int(zips) > 7:
			await msg.edit("⛔𝑺𝒊 𝒖𝒔𝒂 𝑨𝒖𝒍𝒂.𝒈𝒕𝒎 𝒍𝒐𝒔 𝒛𝒊𝒑𝒔 𝒏𝒐 𝒑𝒖𝒆𝒅𝒆𝒏 𝒔𝒆𝒓 𝒎𝒂𝒚𝒐𝒓𝒆𝒔 𝒂 7 𝑴𝑩")
			return
	
	session = aiohttp.ClientSession(connector=connector)
	await msg.edit("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
	filename = Path(file).name
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	logerrors = 0
	error_conv = 0
	logslinks = []

	try:
		async with session.get(moodle,timeout=20,ssl=False) as resp:
			await resp.text()
			await msg.edit("𝑺𝒆𝒓𝒗𝒊𝒅𝒐𝒓 𝑶𝒏𝒍𝒊𝒏𝒆 ✔")
	except Exception as ex:
		await msg.edit(f"{moodle} is Down:\n\n{ex}")
		return

	id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}

	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"📦 𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
		files = sevenzip(file,volume=zipssize)
		await msg.edit("❗𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒔𝒆𝒓𝒗𝒊𝒅𝒐𝒓")
		
		client = MoodleClient(usernamew,passwordw,moodle,connector)
	
		for path in files:
				while logerrors < 5:
					error_conv = 0
					try:
						upload = await client.uploadtoken(path,lambda chunk,total,start,filen: uploadfile_progres(chunk,total,start,filen,msg),token)
						
						if mode == "l" or mode == "b":
							upload = upload[1]
							upload = upload.replace('draftfile.php/','webservice/draftfile.php/')
							upload = str(upload) + '?token=' + token
						elif mode == "a" or mode == "t":
							while error_conv < 10:
							
								await msg.edit("𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒄𝒐𝒏𝒗𝒆𝒓𝒕𝒊𝒓")
								await msg.edit("𝑪𝒐𝒏𝒗𝒊𝒓𝒕𝒊𝒆𝒏𝒅𝒐, 𝒔𝒆𝒂 𝒑𝒂𝒄𝒊𝒆𝒏𝒕𝒆...")
								upload = upload[1]
								upload = await move_to_profile(hot,uset,pasel,upload)
								if upload != False:	
									upload = upload.replace('pluginfile.php/','webservice/pluginfile.php/')
									upload = str(upload) + '?token=' + token
									
									error_conv = 0
									break
								else:
									await msg.edit("𝑬𝒓𝒓𝒐𝒓, 𝒓𝒆𝒊𝒏𝒕𝒆𝒏𝒕𝒂𝒏𝒅𝒐")
									error_conv +=1
									
									continue	
						else: 
							upload = upload[0]
						
						if upload == False:
							await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓.")
							id_de_ms[username]["proc"] = ""
							return
						else:pass
						
						await bot.send_message(usid,f"__**{upload}**__",disable_web_page_preview=True)
						logslinks.append(upload)
						logerrors = 0
					
						break
					except Exception as ex:
				
						logerrors += 1
						if logerrors > 4:
							if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
							else:
								await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓:\n\n{ex}")
							id_de_ms[username]["proc"] = ""
							return
						
		if len(logslinks) == len(files):
				await msg.edit("✅ 𝑭𝒊𝒏𝒂𝒍𝒊𝒛𝒂𝒅𝒐 𝒆𝒙𝒊𝒕𝒐𝒔𝒂𝒎𝒆𝒏𝒕𝒆")
				with open(filename+".txt","w") as f:
					message = ""
					for li in logslinks:
						message+=li+"\n"
					f.write(message)		
				await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
				if mode != "a":
					pass
				else:pass
				id_de_ms[username]["proc"] = ""
				os.unlink(filename+".txt")
				return
		else:
				await msg.edit("𝑯𝒂 𝒇𝒂𝒍𝒍𝒂𝒅𝒐 𝒍𝒂 𝒔𝒖𝒃𝒊𝒅𝒂")	
				id_de_ms[username]["proc"] = ""
				return	
	
	else:		
		client = MoodleClient(usernamew,passwordw,moodle,connector)
	
		while logerrors < 5:
					error_conv = 0
					try:
						upload = await client.uploadtoken(file,lambda chunk,total,start,filen: uploadfile_progres(chunk,total,start,filen,msg),token)
					
						if mode == "l" or mode == "b":
							upload = upload[1]
							upload = upload.replace('draftfile.php/','webservice/draftfile.php/')
							upload = str(upload) + '?token=' + token
							
						elif mode == "a" or mode == "t":
							while error_conv < 10:
								
								await msg.edit("𝑷𝒓𝒆𝒑𝒂𝒓𝒂𝒏𝒅𝒐 𝒑𝒂𝒓𝒂 𝒄𝒐𝒏𝒗𝒆𝒓𝒕𝒊𝒓")
								await msg.edit("𝑪𝒐𝒏𝒗𝒊𝒓𝒕𝒊𝒆𝒏𝒅𝒐, 𝒔𝒆𝒂 𝒑𝒂𝒄𝒊𝒆𝒏𝒕𝒆...")
								upload = upload[1]
								upload = await move_to_profile(hot,uset,pasel,upload)
							
								if upload != False:	
									upload = upload.replace('pluginfile.php/','webservice/pluginfile.php/')
									upload = str(upload) + '?token=' + token
									
									error_conv = 0
									break
								else:
									await msg.edit("𝑬𝒓𝒓𝒐𝒓, 𝒓𝒆𝒊𝒏𝒕𝒆𝒏𝒕𝒂𝒏𝒅𝒐")
									error_conv +=1
									
									continue	
						else:
							upload = upload[0]
						
						if upload == False:
							await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓.")
							id_de_ms[username]["proc"] = ""
							return
						else:pass
						
						await bot.send_message(usid,f"__**{upload}**__",disable_web_page_preview=True)
						logslinks.append(upload)
						logerrors = 0
			
						break
					except Exception as ex:
						
						logerrors += 1
						if logerrors > 4:
							if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
							else:
								await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓:\n\n{ex}")
							id_de_ms[username]["proc"] = ""
							return
		if len(logslinks) == 1:
				await msg.edit("✅ 𝑭𝒊𝒏𝒂𝒍𝒊𝒛𝒂𝒅𝒐 𝒆𝒙𝒊𝒕𝒐𝒔𝒂𝒎𝒆𝒏𝒕𝒆")
				with open(filename+".txt","w") as f:
					message = ""
					lin = ""
					for li in logslinks:
						message+=li+"\n"
						lin+=li+"\n"
					f.write(message)				
				await bot.send_document(usid,filename+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
				if mode != "a":
					pass
				else:pass
				id_de_ms[username]["proc"] = ""
				os.unlink(filename+".txt")
				return
		else:
				await msg.edit("𝑯𝒂 𝒇𝒂𝒍𝒍𝒂𝒅𝒐 𝒍𝒂 𝒔𝒖𝒃𝒊𝒅𝒂")
				id_de_ms[username]["proc"] = ""
				return

async def uploadfileapi(file,usid,msg,username):
	host = "https://educa.uho.edu.cu/"
	proxy = Configs["gp"]
	zips = Configs[username]["z"]
	if int(zips) > 999 :
		await msg.edit("⛔ Si usa Educa los zips no pueden ser mayores a 999 MB")
		return
	if proxy == "":
		proxy = aiohttp.TCPConnector()
	else:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	session = aiohttp.ClientSession(connector=proxy)
	
	
	await msg.edit("𝑹𝒆𝒄𝒐𝒑𝒊𝒍𝒂𝒏𝒅𝒐 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊ó𝒏")
	filename = Path(file).name
	filesize = Path(file).stat().st_size
	zipssize = 1024*1024*int(zips)
	logslinks = []

	try:
		async with session.get(host,timeout=20,ssl=False) as resp:
			await resp.text()
			await msg.edit("𝑺𝒆𝒓𝒗𝒊𝒅𝒐𝒓 𝑶𝒏𝒍𝒊𝒏𝒆 ✔")
	except Exception as ex:
		await msg.edit(f"{host} is Down:\n\n{ex}")
		return
	
	id_de_ms[username] = {"msg":msg, "pat":filename, "proc":"Up"}

	if filesize-1048>zipssize:
		parts = round(filesize / zipssize)
		await msg.edit(f"📦 𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
		files = sevenzip(file,volume=zipssize)
		await msg.edit("❗𝑪𝒐𝒎𝒑𝒓𝒐𝒃𝒂𝒏𝒅𝒐 𝒔𝒆𝒓𝒗𝒊𝒅𝒐𝒓")

		session = aiohttp.ClientSession(connector=proxy)
		for file in files:
			try:
				if file.endswith(".zip"):
						filename_god = file
				else:
						file = filezip(file,volume=None)
						filename_god = file[0].split("zip")[0]+".zip"
						os.rename(file[0],filename_god)
				fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
				query = {"s97304e7e":fi}
				async with session.post("https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/upload_file/archivo",data=query,timeout=60*30) as resp:
							url = loads(await resp.text())["files"][0]["url"]
							await bot.send_message(usid,f"**__{url}__**",disable_web_page_preview=True)
							logslinks.append(url)
							Urls[username].append(url.split("/")[-1])
			except Exception as ex:
				if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
				else:
					await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓:\n\n{ex}")
				id_de_ms[username]["proc"] = ""
				return
				#await msg.edit(f"{ex}")
		if len(logslinks) == len(files):
				await msg.edit("**Finalizado exitosamente**")
						
				with open(filename_god+".txt","w") as t:
						message = ""
						lin = ""
						for li in logslinks:
							message+=li+"\n"
							lin+=li+"\n"
						t.write(message)
				await bot.send_document(usid,filename_god+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
				os.unlink(filename_god+".txt")
				id_de_ms[username]["proc"] = ""
				return
		else:
			await msg.edit("Ha fallado la subida ")
			id_de_ms[username]["proc"] = ""
	else:
			session = aiohttp.ClientSession(connector=proxy)
			try:	
					if file.endswith(".zip"):
							filename_god = file
					else:
							file = filezip(file,volume=None)
							filename_god = file[0].split("zip")[0]+".zip"
							os.rename(file[0],filename_god)
					fi = Progress(filename_god,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
					query = {"s97304e7e":fi}
					async with session.post("https://educa.uho.edu.cu/ci_portal_uho/index.php/recursos_pre/my_grocery_recursos_pred/upload_file/archivo",data=query,timeout=60*30) as resp:
							url = loads(await resp.text())["files"][0]["url"]
							await bot.send_message(usid,f"**__{url}__**",disable_web_page_preview=True)
							logslinks.append(url)
							Urls[username].append(url.split("/")[-1])
			except Exception as ex:
				if "[400 MESSAGE_ID_INVALID]" in str(ex): pass
				else:
					await bot.send_message(usid,f"𝑬𝒓𝒓𝒐𝒓 𝒂𝒍 𝒔𝒖𝒃𝒊𝒓:\n\n{ex}")
				id_de_ms[username]["proc"] = ""
				return
							#await msg.edit(f"{ex}")
			if len(logslinks) == 1:
						await msg.edit("**Finalizado exitosamente**")
						with open(filename_god+".txt","w") as t:
								message = ""
								lin = ""
								for li in logslinks:
									message+=li+"\n"
									lin+=li+"\n"
								t.write(message)
						await bot.send_document(usid,filename_god+".txt",caption="Gracias por usar nuestros sevicios\nPara continuar subiendo use **/ls** :)")
						os.unlink(filename_god+".txt")
						id_de_ms[username]["proc"] = ""
						return
			else:
				id_de_ms[username]["proc"] = ""
				await msg.edit("Ha fallado la subida")

async def send_txt(user_id,file_name,url_up,msg,msg_url):
  await msg.edit(msg_url)
  await bot.send_document(user_id,file_name+'.txt',caption=str(file_name).split('/')[-1]+'\n[ '+str(len(url_up))+' ] Partes 🧩')
  
def generate():
    prefix = "web-file-upload-"
    random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(32))
    unique_id = str(uuid.uuid4().time_low)

    random_name = f"{prefix}{random_string}-{unique_id}"
    return random_name

def monitor_callback(monitor, msg, filesize, filename, start,uploaded_size):
	chunk = monitor.bytes_read
	uploaded_size = uploaded_size + chunk
	now = time()
	diff = now - start
	mbs = chunk / diff
	ms = f"📦 𝐍𝐚𝐦𝐞: {filename}\n\n"
	try:
		ms+=update_progress_bar(chunk,filesize)+ "  " + sizeof_fmt(mbs)+"/s\n\n"
	except:pass
	ms+= f"▶️ 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐: {sizeof_fmt(uploaded_size)} of {sizeof_fmt(filesize)}\n\n"
	global seg
	if seg != localtime().tm_sec:
		msg.edit(ms)
	seg = localtime().tm_sec

async def pid(host,user,password,session):
	if not user in save_cred:
		save_cred[user] = {"ID":None,"TOKEN":None}
	print("En PID")
	if save_cred[user]["ID"]:
		return save_cred[user]["ID"]
	else:
		loginurl = host + 'index.php/login'
		async with session.get(loginurl) as resp:
			text = await resp.text()
		soup = BeautifulSoup(text,'html.parser')
		requesttoken = soup.find('head')['data-requesttoken']
		#print(requesttoken)
		timezone = 'America/Mexico_City'
		timezone_offset = '-5'
		payload = {'user':user,'password':password,'timezone':timezone,'timezone_offset':timezone_offset,'requesttoken':requesttoken};
		async with session.post(loginurl, data=payload) as resp:
			print('Login Exito!!')
			text = await resp.text()
		soup = BeautifulSoup(text,'html.parser')
		title = soup.find('div',attrs={'id':'settings'})
		if title:
			files = host + 'index.php/apps/files/'
			async with session.get(files) as resp:
				text = await resp.text()
			soup1 = BeautifulSoup(text,'html.parser')
			value_access = soup1.find('div',attrs={'id':'avatardiv-menu'})['data-user']
			#print(value_access)
			save_cred[user]["ID"] = value_access
			return save_cred[user]["ID"]

async def parse_name(name):
	patron = r'[^a-zA-Z0-9.]'
	nombre_limpio = re.sub(patron, '', name)
	return nombre_limpio

async def file_renamer(file):
	filename = file.split("/")[-1]
	path = file.split(filename)[0]
	if len(filename)>21:
		p = filename[:10]
		f = filename[-11:]
		filex = p + f
	else:
		 filex = filename
	filename = path + re.sub(r'[^A-Za-z0-9.]', '', filex)
	os.rename(file,filename)
	return filename

async def webdav(filex,user_id,msg,username):
	print(0)
	if not username in control_upload:
		control_upload[username] = {}
	filename = filex.split('/')[-1]
	#path = filex.split(filename)[0] + await parse_name(filename)
	#os.rename(filex,path)
	#print(path)
	#filex = path

	control_upload[username] = False

	send = msg.reply
	proxy = Configs[username]["gp"]
	user = Config[username]["username"]
	password = Config[username]["password"]
	host = Config[username]["host"]
	zips = Configs[username]["z"]
	xd_link = Configs["xdlink"]
	filesize = Path(filex).stat().st_size
	zipssize = 1024*1024*int(zips)
	if filesize > zipssize:
		await msg.edit("📦 𝑪𝒐𝒎𝒑𝒓𝒊𝒎𝒊𝒆𝒏𝒅𝒐")
		files = sevenzip(filex,volume=zipssize)
	else:
	  files = [filex]
	if proxy:
		proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
	else:
		proxy = aiohttp.TCPConnector()
	print(filex)
	filename = filex.split("/")[-1]
	async with aiohttp.ClientSession(connector=proxy,auth=aiohttp.BasicAuth(user, password)) as session:
		print(1)
		ids = await pid(host,user,password,session)
		print(ids)
		#asyncio.run( msg.edit(f"🔴 Conectando ..."))
		await msg.edit(f"⚜️ **NextCloud Server Activate** ⚜️")
		links_url = []
		for file in files:
		  filex = await file_renamer(file)
		  try:
		    webdav_url = host+"remote.php/dav/uploads/"+ids+"/"+ generate() #A875BE09-18E1-4C95-9B84-DD924D2781B7
		    #print(webdav_url)
		    if not username in bytes_control:
		      bytes_control[username] = 10
		      m = "📯 Bytes de Assignación establecidos a 10 mb\n\n"
		      m+= "↪️ Use /bytes para modificarlo"
		      await msg.edit(m)
		    CHUNK_SIZE = bytes_control[username] * 1024 * 1024  # 10 MB
		    uploaded_size = 0
		    filesize = Path(filex).stat().st_size
		    print(1)
		    async with session.request("MKCOL", webdav_url) as response:
		      print(response.status)
		    await msg.edit(f"🌐 Conectando ")
		    
		    mime_type, _ = mimetypes.guess_type(filex)
		    if not mime_type:
		      mime_type = "application/x-7z-compressed"
		    print(mime_type)
		    
		    with open(filex, 'rb') as file:
		      #file_reader = FileProgressReader(file, callback=progress_callback, chunk_size=CHUNK_SIZE)
		      offset = 0
		      while True:
		        file_chunk = file.read(CHUNK_SIZE)
		        if not file_chunk:
		          break
		        elif control_upload[username] == True:
		          return
		        print(2)
		        print(offset)
		        
		        start = time()
		        async with session.put(f"{webdav_url}/{offset}",data=file_chunk,headers={'Content-Type': mime_type}) as response:
		          txt = await response.text()
		          print("PUT")
		        uploaded_size+=len(file_chunk)
		        print(sizeof_fmt(uploaded_size))
		        offset += len(file_chunk)
		        porcentaje = str(offset/filesize*100)[:4]
		        now = time()
		        diff = now - start
		        mbs = len(file_chunk) / diff
		        ms=f"📤 {filex.split('/')[-1]}\n\n"
		        ms+=update_progress_bar(offset,filesize)+ "  " + porcentaje+"%\n"
		        ms+=f"🗂 Subido: {sizeof_fmt(offset)}\n"
		        ms+=f"📦 Total: {sizeof_fmt(filesize)}\n"
		        ms+=f"🌐 Velocidad: {sizeof_fmt(mbs)}"
		        await msg.edit(ms,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel","up_cancel_button")]]))
		      #msg.edit("✅ Archivo subido exitosamente")
		    a = webdav_url+"/.file"
		    d = host+"remote.php/dav/files/"+ids+"/Raul/"+filex.split('/')[-1]
		    headers = {"Destination":d}
		    async with session.request("MOVE", a, headers=headers) as response:
		      print("Movido")
		    token = save_cred[user]["TOKEN"]
		    url = f"{host}s/{token}/download?path=%2F&files={filex.split('/')[-1]}"
		    links_url.append(url)
		  except Exception as ex:
		    print(ex)
		  #send(url)
		  #create txt
		message_txt = ""
		if xd_link:
		  urls = parse(links_url)
		  for url, url_cloud in zip(urls.split("\n"),links_url):
		    msg_url = '🔗Link/s\n\n'
		    msg_url += f'🔗`{url}` 🔗\n'
		    print(url)
		    print(url_cloud)
		    button1 = InlineKeyboardButton("💢 Delete", callback_data=f"delete {url_cloud.split('files=')[1]}")
		    button2 = InlineKeyboardButton("↪️ Abrir Enlace ↩️", url=url_cloud)
		    buttons = [[button1,button2]]
		    reply_markup = InlineKeyboardMarkup(buttons)
		    await bot.send_message(user_id,msg_url,reply_markup=reply_markup)
		  await msg.edit("✅ Subida completa")
		  txtname = filename.split("/")[-1].split(".")[0]+'.txt'
		  txt = open(txtname,'w')
		  txt.write(urls)
		  txt.close()
		  await send_txt_file(user_id,txtname)
		else:
		  for url in links_url:
		    msg_url = '🔗Link/s\n\n'
		    msg_url += f'🔗`{url}` 🔗\n'
		    message_txt+=f"{url}\n"
		    button1 = InlineKeyboardButton("💢 Delete", callback_data=f"delete {url.split('files=')[1]}")
		    button2 = InlineKeyboardButton("↪️ Abrir Enlace ↩️", url=url)
		    buttons = [[button1,button2]]
		    reply_markup = InlineKeyboardMarkup(buttons)
		    await bot.send_message(user_id,msg_url,reply_markup=reply_markup)
		  await msg.edit("✅ Subida completa")
		  txtname = filename.split("/")[-1].split(".")[0]+'.txt'
		  txt = open(txtname,'w')
		  txt.write(message_txt)
		  txt.close()
		  await send_txt_file(user_id,txtname)

async def send_txt_file(user_id,txt):
	await bot.send_document(user_id,txt)

async def webdav2(file,usid,msg,username):
	try:
		proxy = Configs[username]["gp"]
		user = Config[username]["username"]
		password = Config[username]["password"]
		host = "https://nube.uo.edu.cu/"
		if proxy:
			proxy = aiohttp_socks.ProxyConnector.from_url(f"{proxy}")
		else:
			proxy = aiohttp.TCPConnector()
		file = await file_renamer(file)
		filename = file.split("/")[-1]
		filesize = Path(file).stat().st_size
		headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}
		async with aiohttp.ClientSession(connector=proxy) as session:
			await msg.edit(f"Conectando 🔴")
			ids = await pid(host,user,password,session)
			#login
			async with session.get(host+"index.php/login",headers=headers) as resp:
				html = await resp.text()
			soup = BeautifulSoup(html,'html.parser')
			requesttoken = soup.find('head')['data-requesttoken']
			print(requesttoken)
			timezone = 'America/Mexico_City'
			timezone_offset = '-5'
			payload = {'user':user,'password':password,'timezone':timezone,'timezone_offset':timezone_offset,'requesttoken':requesttoken}
			async with session.post(host+"index.php/login",data=payload,headers=headers) as resp:
				print(f"login {resp.status}")
			async with session.get(host+"index.php/apps/files/") as resp:
				html = await resp.text()
			soup = BeautifulSoup(html,'html.parser')
			requesttoken = soup.find('head')['data-requesttoken']
			print(requesttoken)
			await msg.edit(f"Conectado 🟢")
			try:
				webdav_url = host+"remote.php/dav/uploads/"+ids+"/"+ generate()
				try:
					async with session.request("MKCOL", webdav_url,headers={"requesttoken":requesttoken,**headers}) as resp:
						print("MKCOL "+str(resp.status))
				except:
					await msg.edit("Este servidor está temporalmente fuera de servicio [await_please]")
					return
				print("up_webdav")
				mime_type, _ = mimetypes.guess_type(file)
				if not mime_type:
					mime_type = "application/x-7z-compressed"
				complete = True
				await msg.edit(f"⬆️ Uploading 0 de {sizeof_fmt(filesize)}")
				with open(file, 'rb') as f:
					offset = 0
					vchunk = 10
					while True:
						file_chunk = f.read(vchunk*1024*1024)
						if not file_chunk:
							break
						async with session.put(f"{webdav_url}/{offset}",data=file_chunk,headers={'Content-Type': mime_type,"requesttoken":requesttoken}) as resp:
							try:
								await msg.edit(f"⬆️ Uploading {sizeof_fmt(offset)} de {sizeof_fmt(filesize)}")
							except:pass
						offset+= len(file_chunk)
					print("Finalizado")
					await msg.edit("✅ **Finalizado** ✅")
					u = webdav_url+"/.file"
					button1 = InlineKeyboardButton("📲 Descargar Archivo",url=u)
					buttons = [[button1]]
					reply_markup = InlineKeyboardMarkup(buttons)
					await bot.send_message(username,f"📂  [{filename}]({u})\n❄️ **Tamaño:** {sizeof_fmt(filesize)}",reply_markup=reply_markup)
					complete = False
					TEMP_FILE[username] = None
			except Exception as ex:
				print(ex)
	except Exception as ex:
		print(str(ex))
  
@async_decorator
def proccess(filex,user_id,msg,username):
    try:
        send = msg.reply
        logslinks = []
        proxy = Configs[username]["gp"]
        user = Config[username]["username"]
        passw = Config[username]["password"]
        host = Config[username]["host"]
        zips = Configs[username]["z"]
        file = filex
        filesize = Path(file).stat().st_size
        print(20)
        zipssize = 1024*1024*int(zips)
        session = requests.session()
        headers = {}
        if proxy:
            proxy = {'http': proxy,'https': proxy}
        else:
            proxy = None
        filename = str(file).replace(f'downloads/{username}/','')        
        if filesize>zipssize:
            try:
                asyncio.run( msg.edit(f"📦 𝗖𝗢𝗠𝗣𝗥𝗜𝗠𝗜𝗘𝗡𝗗𝗢 📦"))
            except:
                pass
            zipname = str(filename).split('.')[0]
            files = sevenzip(file,volume=zipssize)
            print('comprimido')
            try:
                asyncio.run( msg.edit(f"🔴 Conectando ..."))
            except:
                print('saltandose edit de message')
                pass
            print('aya')
            remotepath = "Descargas"
            #async with aiohttp.ClientSession(connector=proxy) as session:
            loginurl = host + 'index.php/login'
            resp = session.get(loginurl,proxies=proxy)
            print(2)
            soup = BeautifulSoup(resp.text,'html.parser')
            requesttoken = soup.find('head')['data-requesttoken']
            print('requesttoken: ',requesttoken)
            timezone = 'America/Mexico_City'
            timezone_offset = '-5'
            payload = {}
            payload['user'] = user
            payload['password'] = passw
            payload['timezone'] = timezone
            payload['timezone_offset'] = timezone_offset
            payload['requesttoken'] = requesttoken
            resp1 = session.post(loginurl,data=payload,proxies=proxy)
            print('Login Exito!!')
            try:
                asyncio.run( msg.edit(f"🟢 Conectado"))
            except:
                pass
            soup = BeautifulSoup(resp1.text,'html.parser')
            title = soup.find('div',attrs={'id':'settings'})
            if title:
                print('Loged')
                #asyncio.run( msg.edit(f"Subiendo"))
                url_up = []
                file_name = 'downloads/'+username+'/'+str(Path(file).name).split('.')[0]
    #			asyncio.run( msg.delete())
                for file in files:
                    filename = str(file).replace(f'downloads/{username}/','')
                    ufiles = host+'index.php/apps/files/'
                    filepath = str(file).split('/')[-1]
                    try:
                        msg = asyncio.run( msg.edit(f'⬆️ Uploading ...\n\n{filepath}'))
                    except:
                        pass
                    uploadUrl = host + 'remote.php/webdav/'+ 'Raul/' + filepath
                    resp =  session.get(ufiles,proxies=proxy)
                    soup = BeautifulSoup(resp.text,'html.parser')
                    requesttoken = soup.find('head')['data-requesttoken']
                    f  = open(file,'rb')
                    resp = session.put(uploadUrl,data=f,headers={'requesttoken':requesttoken},proxies=proxy)
                    f.close()
                    status = resp.status_code
                    print('Status:',status)
                    #fi = Progress(file,lambda current,total,timestart,filename: uploadfile_progres(current,total,timestart,filename,msg))
                    #async with session.put(uploadUrl,data=fi,headers={'requesttoken':requesttoken}) as resp:
                        #status = resp.status
                    if status==201:
                        #asyncio.run( msg.edit('🛠 Construyendo Enlace.')
                        print('resp == 201')
                        linked = resp.url
                        name = str(linked).split('/')[-1]
                        actual = datetime.now()
                        year = actual.year
                        mes = actual.month
                        dia = actual.day + 6
                        if dia>30:
                            mes = mes + 1
                            dia = dia - 30
                            if dia<10:
                                dia = '0' + str(dia)
                                print(dia)
                            else:
                                pass
                        else:
                            pass
                        expire = str(year) + '-' + str(mes) + '-' + str(dia)
                        direct_payload = {}
                        direct_payload['attributes'] = '[]'
                        direct_payload['expireDate'] = expire
                        direct_payload['path'] = '/Raul/'+filename
                        direct_payload['shareType'] = 3
                        urlpostq = host + "ocs/v2.php/apps/files_sharing/api/v1/shares"
                        resp = session.post(urlpostq, data=direct_payload, headers={'requesttoken':requesttoken},proxies=proxy)
                            #html = asyncio.run( resp.text()
                        soup5 = BeautifulSoup(resp.text,'html.parser')
                        f = soup5.find('url').contents[0]
                        token = str(f).split('/s/')[1]
                        url = host + 's/' + token + '/download/' + name
                        url_up.append(url)
                    elif status==204:
                        #asyncio.run( msg.edit('🛠 Construyendo Enlace..')
                        print('resp == 204')
                        linked = resp.url
                        print(linked)
                        name = str(linked).split('/')[-1]
                        actual = datetime.now()
                        year = actual.year
                        mes = actual.month
                        dia = actual.day + 6
                        if dia>30:
                            mes = mes + 1
                            dia = dia - 30
                            if dia<10:
                                dia = '0' + str(dia)
                                print(dia)
                            else:
                                pass
                        else:
                            pass
                        expire = str(year) + '-' + str(mes) + '-' + str(dia)
                        direct_payload = {}
                        direct_payload['attributes'] = '[]'
                        direct_payload['expireDate'] = expire
                        direct_payload['path'] = '/Raul/'+filename
                        direct_payload['shareType'] = 3
                        urlpostq = host + "ocs/v2.php/apps/files_sharing/api/v1/shares"
                        resp = session.post(urlpostq, data=direct_payload, headers={'requesttoken':requesttoken},proxies=proxy)
                            #html = asyncio.run( resp.text()
                        soup5 = BeautifulSoup(resp.text,'html.parser')
                        f = soup5.find('url').contents[0]
                        token = str(f).split('/s/')[1]
                        url = host + 's/' + token + '/download/' + name
                        url_up.append(url)
                        #asyncio.run( msg.delete()
                    else:
                        try:
                            asyncio.run( msg.edit('Código de Respuesta Incorrecto\nIncorrect answer code'))
                        except:
                            pass
                    # try:
                    #     asyncio.run( msg.delete())
                    # except:
                    #     pass
                with open(file_name+'.txt','w') as txt:
                    msg_url = '🔗Link/s\n\n'
                    url = ''
                    for u in url_up:
                        url+=u+'\n'
                        msg_url += f'🔗{u}🔗\n'
                    
                    txt.write(url)
                try:
                    asyncio.run(send_txt(user_id,file_name,url_up,msg,msg_url))
                except Exception as ex:
                    print('exception txt' , ex)
        #		os.unlink(file_name+'.txt')
    #####sincompress####        	    
        elif filesize<=zipssize:
            try:
                asyncio.run( msg.edit(f"🔴 Conectando ..."))
            except:
                print('se salto el edit del msg')
                pass
            remotepath = ""
            #proxy = aiohttp.TCPConnector()
            #async with aiohttp.ClientSession(connector=proxy) as session:
            loginurl = host + 'index.php/login'
            resp = session.get(loginurl,proxies=proxy) 
            print(2)
            soup = BeautifulSoup(resp.text,'html.parser')
            requesttoken = soup.find('head')['data-requesttoken']
            print('requesttoken: ',requesttoken)
            timezone = 'America/Mexico_City'
            timezone_offset = '-5'
            payload = {}
            payload['user'] = user
            payload['password'] = passw
            payload['timezone'] = timezone
            payload['timezone_offset'] = timezone_offset
            payload['requesttoken'] = requesttoken
            resp1 = session.post(loginurl,data=payload,proxies=proxy)
            print('Login Exito!!')
            try:
                asyncio.run( msg.edit(f"🟢 Conectado"))
            except:
                pass
                #html = asyncio.run( resp1.text()
            soup = BeautifulSoup(resp1.text,'html.parser')
            title = soup.find('div',attrs={'id':'settings'})
            if title:
                print('Loged')

            files = host+'index.php/apps/files/'
            try:
                asyncio.run( msg.edit("Subiendo ..."))
            except:
                pass
            filepath = str(file).split('/')[-1]
            uploadUrl = host + 'remote.php/webdav/'+ 'Raul/' + filepath
            resp = session.get(files,proxies=proxy)
                #html = asyncio.run( resp.text()
            soup = BeautifulSoup(resp.text,'html.parser')
            requesttoken = soup.find('head')['data-requesttoken']
            f  = open(file,'rb')
            resp = session.put(uploadUrl,data=f,headers={'requesttoken':requesttoken},proxies=proxy)
            f.close()
            status = resp.status_code
            if status==201:
                print('resp == 201')
                linked = resp.url
                print(linked)
                name = str(linked).split('/')[-1]
                actual = datetime.now()
                year = actual.year
                mes = actual.month
                dia = actual.day + 6
                if dia>30:
                    mes = mes + 1
                    dia = dia - 30
                    if dia<10:
                        dia = '0' + str(dia)
                        print(dia)
                    else:
                        pass
                else:
                    pass
                expire = str(year) + '-' + str(mes) + '-' + str(dia)
                direct_payload = {}
                direct_payload['attributes'] = '[]'
                direct_payload['expireDate'] = expire
                direct_payload['path'] = '/Raul/'+filename
                direct_payload['shareType'] = 3
                urlpostq = host + "ocs/v2.php/apps/files_sharing/api/v1/shares"
                resp = session.post(urlpostq, data=direct_payload, headers={'requesttoken':requesttoken},proxies=proxy)
                    #html = asyncio.run( resp.text()
                soup5 = BeautifulSoup(resp.text,'html.parser')
                f = soup5.find('url').contents[0]
                token = str(f).split('/s/')[1]
                url = host + 's/' + token + '/download/' + name
                asyncio.run( msg.edit(url))
                filename = 'downloads/'+username+'/'+str(Path(file).name).split('.')[0]
                with open(filename+'.txt','w') as txt:
                    txt.write(url)
                try:
                    asyncio.run( bot.send_document(user_id,filename+'.txt',caption='**'+str(filename).split('/')[-1]+'**'))
                except:
                    pass
    #			os.unlink(filename+'.txt')
            elif status==204:
                print('resp == 204')
                linked = resp.url
                print(linked)
                name = str(linked).split('/')[-1]
                actual = datetime.now()
                year = actual.year
                mes = actual.month
                dia = actual.day + 6
                if dia>30:
                    mes = mes + 1
                    dia = dia - 30
                    if dia<10:
                        dia = '0' + str(dia)
                        print(dia)
                    else:
                        pass
                else:
                    pass
                expire = str(year) + '-' + str(mes) + '-' + str(dia)
                direct_payload = {}
                direct_payload['attributes'] = '[]'
                direct_payload['expireDate'] = expire
                direct_payload['path'] = '/Raul/'+filename
                direct_payload['shareType'] = 3
                urlpostq = host + "ocs/v2.php/apps/files_sharing/api/v1/shares"
                resp = session.post(urlpostq, data=direct_payload, headers={'requesttoken':requesttoken},proxies=proxy)
                    #html = asyncio.run( resp.text()
                soup5 = BeautifulSoup(resp.text,'html.parser')
                f = soup5.find('url').contents[0]
                token = str(f).split('/s/')[1]
                url = host + 's/' + token + '/download/' + name
                filename = 'downloads/'+username+'/'+str(Path(file).name).split('.')[0]
                with open(filename+'.txt','w') as txt:
                    txt.write(url)
                try:
                    asyncio.run(send_txt(user_id,file_name,url_up,msg,url))
                except:
                    pass
        #		os.unlink(filename+'.txt')
            else:
                asyncio.run(msg.edit('Código de Respuesta Incorrecto\nIncorrect answer code'))
        return
    except Exception as ex:
        print(str(ex))	         		

print("started")
bot.start()
print(10)
bot.loop.run_forever()
