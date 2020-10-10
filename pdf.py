"""
WELCOME TO MY TOOLS PDF PROGRAMMING DOWNLOADER
          HANYA PROGRAMMER SEJATI
===============================================
Author : Rizky | Aprilia
Support: KangPacman
Team   : XIUZCODE (OPEN SOURCE TEAM)
"""

import requests as _oOooOoo_o
from bs4 import BeautifulSoup as _oooOooOoO_
from os import *
import progressbar as OoooOoOOoOOO, io

hijau, putih, merah, cyan, kuning, biru = '\x1b[1;92m', '\x1b[1;97m', '\x1b[1;91m', '\x1b[1;96m', '\x1b[1;93m', '\x1b[1;94m'
_ = lambda: system('clear')
__ = lambda _OoOOoO_: exit(f"{cyan}[{merah}={cyan}] {putih}ERROR:{merah} {_OoOOoO_}\n")
___ = (f"\n {cyan}╭━<━━╮\n ┃{merah}╭╮╭╮{cyan}┃  {merah}╔═╗{putih}┌┬┐┌─┐  {merah}╔═╗{putih}┌─┐┌┬┐┌─┐┬─┐\n{cyan}┗┫┏━━┓┣┛ {merah}╠═╝{putih} ││├┤{kuning}───{merah}║{putih}  │ │ ││├┤ ├┬┘\n {cyan}┃╰━━╯┃  {merah}╩{putih}  ─┴┘└    {merah}╚═╝{putih}└─┘─┴┘└─┘┴└─\n {cyan}╰┳━━┳╯\n  ┛  ┗   {biru}>> {hijau}https://github.com/hekelpro")
____ = []
_____ = "https://books.goalkicker.com/"


def oOooOo(logo):
	print(putih+logo)
	print(f"{putih}="*42)
	oOo = _oooOooOoO_(_oOooOoo_o.get(_____).text, "html.parser")
	______ = 0
	for ooO in oOo.find_all("div", attrs={"class":"bookContainer grow"}):
		______ += 1
		_oOooOo_ = ooO.text
		print(f"{cyan}[{hijau}"+str(______)+f"{cyan}]{putih} "+_oOooOo_[:30]+f"{merah}....")
		for Ooo in ooO.find_all("a"):
			____.append(Ooo.get("href"))
	print(f"{putih}="*42)
	_o_ = int(input(f"{cyan}[{hijau}•{cyan}]{putih} PILIH:{hijau} ")) - 1
	# print(str(____[_o_])) ~> Menampilkan URL
	_O_ = _oooOooOoO_(_oOooOoo_o.get(_____+str(____[_o_])).text, "html.parser").find("div", id="frontpage").find("a")["href"]
	# print(_O_) ~> Menampilkan Output
	O__ = _oOooOoo_o.get(_____+str(____[_o_])+_O_, stream=True)
	_V_ = io.open(_O_, "wb")
	OooOooO = int(O__.headers.get('content-length'))
	oooOooo = OoooOoOOoOOO.ProgressBar(redirect_stdout=True,redirect_stderr=True,widgets=[OoooOoOOoOOO.Percentage(),OoooOoOOoOOO.Bar(),' (',OoooOoOOoOOO.AdaptiveTransferSpeed(),' ',OoooOoOOoOOO.ETA(),') '])
	oooOooo.start(OooOooO)
	__oooO_ = 0
	for _r_i_z_k_y_ in O__.iter_content(chunk_size=1024):
		if _r_i_z_k_y_:
			__oooO_ += len(_r_i_z_k_y_)
			oooOooo.update(__oooO_)
			_V_.write(_r_i_z_k_y_)
			_V_.flush()
	oooOooo.finish()
	print(f"{putih}="*42)
	exit(f"{cyan}[{hijau}✓{cyan}]{putih} SELESAI {merah}!!\n    {biru}> {putih}OUTPUT: {hijau}{_O_}\n")


if __name__=="__main__":
	try:
		_()
		oOooOo(___)
	except Exception as stack:
		__(str(stack))
