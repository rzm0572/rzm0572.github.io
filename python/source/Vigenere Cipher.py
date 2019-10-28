# -*- coding: utf-8
# author: rzm
# time: 2019/10/27

def main():
	print("欢迎使用维热纳尔密码加密解密工具.\n")
	while True:
		res1=input("加密(e) , 解密(d) or 退出(q)? ")
		if res1=="e":  # 加密
			ret=""
			text1=input("请输入用于加密的明文: ")
			text2=input("密钥: ")
			i=0
			for ch in text1:
				if not ch.isalpha():  # 如果不是英文字符，就直接输出
					ret+=ch
					continue
				tmp1=ord(ch.lower())-ord('a')  # 明文中字符的序号
				tmp2=ord(text2[i].lower())-ord('a')  # 密室中字符的序号
				if ord(ch)>=ord('a') and ord(ch)<=ord('z'):  # 如果是小写字母
					ret+=chr((tmp1+tmp2)%26+ord('a'))
				elif ord(ch)>=ord('A') and ord(ch)<=ord('Z'):  # 如果是大写字母
					ret+=chr((tmp1+tmp2)%26+ord('A'))
				# print(str(tmp1)+" "+str(tmp2)+" "+ret[len(ret)-1])
				if i<len(text2)-1:  # 循环密钥的指针
					i+=1
				else:
					i=0
			print("加密文本: "+ret)
		if res1=="d":  # 解密
			ret=""
			text1=input("请输入用于解密的密文: ")
			text2=input("密钥: ")
			i=0
			for ch in text1:
				if not ch.isalpha():
					ret+=ch
					continue
				tmp1=ord(ch.lower())-ord('a')
				tmp2=ord(text2[i].lower())-ord('a')
				if ord(ch)>=ord('a') and ord(ch)<=ord('z'):
					ret+=chr((tmp1-tmp2)%26+ord('a'))
				elif ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
					ret+=chr((tmp1-tmp2)%26+ord('A'))
				if i<len(text2)-1:
					i+=1
				else:
					i=0
			print("解密文本: "+ret)
		if res1=="q":  # 退出
			break

if __name__=="__main__":
	main()
