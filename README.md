
# SSH BRUTE FORCE LOGIN PROGRAMI

## Açıklama

Bu Python programı, kullanıcıdan bir **hostname** (bilgisayar adı) değeri alır ve  username.txt ve pass.txt dosyalarındaki giriş bilgilerini kombinleyerek bir bruteforce saldırısı yapar. (tamamen eğitim amaçladır. kötü kullanımdan sorumlu değilim.)


Program, basit bir **input()** fonksiyonu ile kullanıcıdan veri alır ve ardından **socket** modülü ile yerel sistemin hostname bilgisini elde eder.

## Kullanım

1.  Program çalıştırıldığında, kullanıcıdan bir ip adresi ve port girilmesi istenir.
2.  Çıkan sonuç eğer başarılıysa program başarılı olarak  sonuç verir ve programı kapatır.

### Örnek Çıktı:


Ip adresi girin: 192.168.1.7
Port girin: 22
Deniyorum: pi / admin
Başarısız giriş: pi / admin
Deniyorum: pi / 123
Başarısız giriş: pi / 123
Deniyorum: pi / raspberry
Başarılı giriş: pi / raspberry

### Gereksinimler

-   pip install paramiko


# SSH BRUTE FORCE LOGIN PROGRAM

## Description

This Python program takes a **hostname** (computer name) value from the user and performs a bruteforce attack by combining the login information in the username.txt and pass.txt files. (It is purely for educational purposes. I am not responsible for any misuse.)

The program takes data from the user with a simple **input()** function and then obtains the hostname information of the local system with the **socket** module.

## Usage

1. When the program is run, the user is asked to enter an IP address and port.

2. If the result is successful, the program returns the result as successful and closes the program.

### Sample Output:

Enter IP address: 192.168.1.7
Enter Port: 22
Trying: pi / admin
Failed login: pi / admin
Trying: pi / 123
Failed login: pi / 123
Trying: pi / raspberry
Successful login: pi / raspberry

### Requirements

- pip install paramiko