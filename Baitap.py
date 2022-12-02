##Câu 1
# t = int(input ("Nhập một số : "))
# if 0<t<100 :
#         for i in range(t):
#                 a=input("Test "+ str(i +1)+": ")
#                 print (a.title())

##Câu 2
# def dem_nguyen_phu(s):
#     nguyenam="ueoaiEUOAI"
#     tongnguyenam=0
#     phuam="qwrtypsdfghjkzxcvbnm"
#     tongphuam = 0
#     for c in nguyenam:
#         tongnguyenam += s.count(c)
#     for z in phuam:
#         tongphuam += s.count(z)
#     return tongnguyenam ,tongphuam, s
# s=input("Nhập vào: ")
# soLuongNguyenAm , soLuongPhuAm , chuoiKetQua = dem_nguyen_phu(s)
# t = int(input("Nhập số: "))
# if 0 <t <100 :
#     for i in range (t):
#         print("Test " + str(i +1) + " là :", chuoiKetQua)
#         print ("Số lượng nguyên âm là : ", soLuongNguyenAm)
#         print ("Số lượng phụ âm là : ", soLuongPhuAm)

##Câu 3
# str1 = input("Nhập vào chuỗi câu: ")
# so_tu=1
#
# for i in range(len(str1)):
#     if(str1[i]==' '):
#         so_tu=so_tu+1
# t = int(input("Nhập số: "))
# if 0 <t <100 :
#       for i in range (t):
#         print ("Test ["+str(i+1)+"] ")
#         print ("Chuỗi kết quả là : ",str1)
#         print ("Số từ trong chuỗi trên là : ",so_tu)

##Câu 5
# t = int(input("Nhập số: "))
# if 0 <t <100 :
#        for i in range (t):
#            str1 = input("Nhập chuỗi vào: ")
#            sub = input("Nhập chuỗi cần tìm vào: ")
#            print ("Test "+ str(i+1)+" : ")
#            print (sub + " Xuất hiện trong " + str1 +"là : ",str1.count(sub))

##Câu 6
# t = int(input ("Số : "))
# if 0 <t<100 :
#     for i in range (t):
#         str2 = input ("Nhập chuỗi 1 : ")
#         sub2 = input("Nhập chuỗi thay thế : ")
#         print ("Test "+str(i+1)+ " là : ")
#         print ("Hàm đã thế là : ",str2.replace(str2,sub2))

##Câu 7


##Câu 8
#t = int(input("Nhập số: "))
#if 0 <t <100 :
#       for i in range (t):
#         dem = {}
#         line = input("Nhập dòng thứ "+str(i + 1)+": " )
#         for a in line.split():
#                 dem[a] = dem.get(a,0)+1
#                 tu = sorted(dem.keys())
#         for w in tu:
#             print ("%s:%d" % (w,dem[w]))
##9
# t = int(input("Nhập số: "))
# if 0 <t <100 :
#        for i in range(t):
#            string = input()
#            count = {}
#            for a in string:
#                if a in count:
#                    count[a] += 1
#                else:
#                    count[a] = 1
#
#            print("Test "+str(i + 1),count)


