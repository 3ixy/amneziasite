# Установка AmneziaVPN на Linux

## Поддерживаемые дистрибутивы:
Мы можем гарантировать работу только базовых версий дистрибутивов
перечисленных ниже (*из коробки). Другие дистрибутивы так же могут
поддерживать приложение, но мы не можем этого гарантировать.

**Debian 11 (x64)** (не работает на wayland)

**Debian 12 (x64)**

**Ubuntu 22.04.5 (x64)**

**Ubuntu 24.04.1 (x64)**

**Fedora 40 (x64)**

**Fedora 41 (x64)**

AmneziaVPN не работает на Debian 13

### Debian 12 (x64)

Для установки AmneziaVPN, помимо административных прав пользователя, нужно
установить следующие библиотеки и компоненты:

    
    
    sudo apt install libxcb-xinerama0  
    

без этого, не запускается GUI установщика

    
    
    sudo apt install libxcb-cursor0  
    

без этого не запускается GUI AmneziaVPN, необходим также, если используется
Xorg вместо Wayland, или если выполнить sudo AmneziaVPN

    
    
    sudo apt install iptables  
    

используйте перед обращением в поддержку. Без установки, лог Amnezia-service
наполнен ошибками об отсутствия iptables

Если на этапе установки ОС, задать пароль суперпользователя, то ваш
собственный пользователь (пример"user1") создаётся без административных прав.

Как исправить проблему:

  1. под "user1" открыть терминал

  2. "повысить" терминал до root, с указанием пароля от root:

    
    
    su root  
    

  3. включите "user1" в группу sudo:

    
    
    sudo usermod -aG sudo user1  
    

### Debian 11 (x64)[​](installing-app-on-linux.html#debian-11-x64 "Прямая
ссылка на Debian 11 \(x64\)")

Из коробки не работает на wayland: "undefined symbol: wl_proxy_marshal_flags"
Необходимо выбрать архитектуру отличную от Wayland

Для установки AmneziaVPN, помимо административных прав пользователя, нужно
установить следующие библиотеки и компоненты:

    
    
    sudo apt install libxcb-xinerama0  
    

без этого, не запускается GUI установщика

    
    
    sudo apt install libopengl0  
    

без этого, не запускается GUI AmneziaVPN

    
    
    sudo apt install libxcb-cursor0  
    

без этого, не запускается GUI AmneziaVPN, так как используется архитектура
отличная от Wayland

### Ubuntu 22.04.5 (x64)

для установки AmneziaVPN, помимо административных прав пользователя, нужны:

    
    
    sudo apt install libxcb-xinerama0  
    

без этого, не запускается GUI установщика

    
    
    sudo apt install libxcb-cursor0  
    

без этого, не запускается GUI AmneziaVPN, если используется Xorg вместо
Wayland, (или если выполнить sudo AmneziaVPN))

### Ubuntu 24.04.1 (x64)

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