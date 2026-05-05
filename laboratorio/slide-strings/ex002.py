url = "https://www.exemplo.com.br/produtos/eletronicos"
url1 = url.split('://')
prot = url1[0]
url2 = url1[1].split('/',1)
dom = url2[0]
cam = '/' + url2[1]
print(prot)
print(dom)
print(cam)