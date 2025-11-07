    

без этого, не запускается GUI установщика

    
    
    sudo apt install libopengl0  
    

без этого, не запускается GUI AmneziaVPN

    
    
    sudo apt install libxcb-cursor0  
    

без этого, не запускается GUI AmneziaVPN, так как используется архитектура
отличная от Wayland

### Ubuntu 22.04.5 (x64)[​](installing-app-on-linux.html#ubuntu-22045-x64
"Прямая ссылка на Ubuntu 22.04.5 \(x64\)")

для установки AmneziaVPN, помимо административных прав пользователя, нужны:

    
    
    sudo apt install libxcb-xinerama0  
    

без этого, не запускается GUI установщика

    
    
    sudo apt install libxcb-cursor0  
    

без этого, не запускается GUI AmneziaVPN, если используется Xorg вместо
Wayland, (или если выполнить sudo AmneziaVPN))

### Ubuntu 24.04.1 (x64)[​](installing-app-on-linux.html#ubuntu-24041-x64
"Прямая ссылка на Ubuntu 24.04.1 \(x64\)")

для установки AmneziaVPN, помимо административных прав пользователя, нужны:

    
    
    sudo apt install libxcb-xinerama0  
    

без этого, не запускается GUI установщика

    
    
    sudo apt install libxcb-cursor0  
    

без этого, не запускается GUI AmneziaVPN, если используется Xorg вместо
Wayland, (или если выполнить sudo AmneziaVPN)

### Fedora 40 (x64)[​](installing-app-on-linux.html#fedora-40-x64 "Прямая
ссылка на Fedora 40 \(x64\)")

AmneziaVPN работает сразу после установки.

Возможно понадобиться перезагрузить систему.

### Fedora 41 (x64)[​](installing-app-on-linux.html#fedora-41-x64 "Прямая
ссылка на Fedora 41 \(x64\)")

AmneziaVPN работает сразу после установки.

Возможно понадобиться перезагрузить систему.

На всех Linux, нельзя блокировать подсистему ipv6. В частности, команда: sudo
sysctl -w net.ipv6.conf.all.disable_ipv6=1 ломает работу кнопки
подключения/отключения в AmneziaVPN.

[Предыдущая страницаУстановка APK-файлов на Android](installing-apk-files-for-
android.html)[Следующая страницаX-RAY](xray.html)

Обращайтесь в чат за помощью, если что-то не получается

[](https://t.me/amnezia_vpn)

  * [Поддерживаемые дистрибутивы:](installing-app-on-linux.html#поддерживаемые-дистрибутивы)
    * [Debian 12 (x64)](installing-app-on-linux.html#debian-12-x64)
    * [Debian 11 (x64)](installing-app-on-linux.html#debian-11-x64)
    * [Ubuntu 22.04.5 (x64)](installing-app-on-linux.html#ubuntu-22045-x64)
    * [Ubuntu 24.04.1 (x64)](installing-app-on-linux.html#ubuntu-24041-x64)
    * [Fedora 40 (x64)](installing-app-on-linux.html#fedora-40-x64)
    * [Fedora 41 (x64)](installing-app-on-linux.html#fedora-41-x64)

![](../img/logo-with-a-w-glow.svg)

Продукты

[Amnezia Premium](https://amnezia.org/premium)[Amnezia
Free](https://amnezia.org/free)[Amnezia Self-hosted](https://amnezia.org/self-
hosted)

Ресурсы

[Документация](../documentation.html)[Решение
проблем](../troubleshooting.html)[FAQ](../faq.html)

Контакты

[Github](https://github.com/amnezia-vpn/amnezia-
client)[Telegram](https://t.me/amnezia_vpn)[Reddit](https://reddit.com/r/AmneziaVPN/)

