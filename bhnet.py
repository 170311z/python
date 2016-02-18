# -*- coding: utf-8 -*-

import sys
import socket
import getopt
import threading 
import subprocess


# グローバル変数の定義
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


# もし定義していないコマンドラインパラメーターが指定されていた場合は，このスクリプトの使い方を表示する
def usage():
	print "BHP Net Tool"
	print
	print "Usage: bhpnet.py -t target_host -p port"
	print "-l --listen              - listen on [host] : [port] for"
	print "                           incoming connections"
	print "-e --execute=file_to_run - execute the given file upon"
	print "                           receiving a connection"
	print "-c --command             - initialize a command shell"
	print "-u --upload=destination  - upon receiving connection upload a"
	print "                           file and write to [destination]"
	print
	print
	print "Examples: "
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u c:\\target.exe"
	print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e \"cat /etc/passwd\""
	print "echo 'ABCEDFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
	sys.exit(0)

def main():
	gloal listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):
		usage()

	# コマンドラインオプションの読み込み
	try:
		opts, args = getopt.getopt(
			sys.argv[1:],
			"hle:t:p:cu:",
			["help", "listen", "execute=", "target=",port=", "command", "upload="])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h", "--help"):
			usage()
		elif.o in ("-l", "--listen"):
			listen = True
		elif p in ("-e", "--execute"):
			execute = a
		elif o in ("-c", "--commandshell"):
			command = True
		elif o in ("-u", "--upload"):
			upload_destination = a
		elif o in ("-t", "--target"):
			target = a
		elif o in ("-p", "--port"):
			port = int(a)
		else:
			assert False, "Unhandled Option"
	# 接続を待機する? それとも標準入力からデータを受け取って送信する?
	if not listen and len (target) and port > 0:

		# コマンドラインからの入力を'buffer'に格納する．
		# 入力がこないと処理が継続されないので標準入力にデータを送らない場合は Ctrl-D を入力すること．
		buffer = sys.stdin.read()

		# データ送信
		client_sender(buffer)

	# 接続待機を開始．
	# コマンドラインオプションに応じて，ファイルをアップロード
	# コマンド実行，コマンドシェルの実行を行う．
	if listen:
		server_loop()

main()
def client_sender(buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		# 標的ホストへの接続
		client.connect((target, port))

		# 標準入力からの入力を受け取ったかどうかを確認する．
		if len(buffer):
			client.send(buffer)

		while True:
			# 標的ホストからのデータを待機
			recv_len = 1
			response = ""

			while recv_len:
				data      = client.recv(4096)
				recv_len  = len(data)
				response += data

				if recv_len < 4096:
					break

				print response,

				# 追加の入力を待機
				buffer = raw_input("")
				buffer += "\n"

				# データの送信
				client.send(buffer)

			except:
				print "[*] Exception! Exiting."

				# 接続の終了
				client.close()
	
def server_loop():
	global target

	# 待機するIPアドレスが指定されていない場合はすべてのインターフェースで接続を待機
	if not len (target):
		target = "0.0.0.0"

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	server.bind((target,port))

	server.listen(5)

	while:
		client_socket, addr = server.accept()

		# クライアントからの新しい接続を処理するスレッドの起動
		client_thread = threading.Thread(target=client_handler, args=(client_socket,))
		client_thread.start()

def run_command(command):
	# 文字列の末尾の改行を削除
	command = command.rstrip()

	# コマンドを実行し出力結果を取得
	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
