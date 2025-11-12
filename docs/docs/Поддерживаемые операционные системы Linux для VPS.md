# Поддерживаемые операционные системы Linux для VPS

**Минимальные системные требования для VPS:**  
Операционная система - Linux, подходит Ubuntu 22.04 или Debian 11.  
Поддерживаемая архитектура процессора - x86-64  
Виртуализация - KVM.  
Адрес сервера c интернет-протоколом IPv4  
Оперативная память (RAM) - рекомендуемая 2 Гб, но не меньше 1 Гб.  
Предустановленное ПО и панель управления не требуются.

Ниже представлены другие варианты операционных систем, поддерживаемые
AmneziaVPN.  
KVM - рекомендуемый тип виртуализации. При виртуализации OpenVZ, протоколы
WireGuard и AmneziaWG не поддерживаются.

### Debian

| Debian 12| Debian 11| Debian 10  
---|---|---|---  
IKEv2| ✔*| ✔*| ✔*  
AmneziaWG| ✔| ✔| ✔  
WireGuard| ✔| ✔| —*  
OpenVPN| ✔| ✔| ✔  
OpenVPN+Cloak| ✔| ✔| ✔  
ShadowSocks| ✔| ✔| ✔  
  
### Ubuntu

| Ubuntu 22.04| Ubuntu 20.04| Ubuntu 18.04| Ubuntu 16.04  
---|---|---|---|---  
IKEv2| ✔*| ✔*| ✔*| ✔*  
AmneziaW| ✔| ✔| ✔| ✔  
WireGuard| ✔| ✔| —*| —  
OpenVPN| ✔| ✔| ✔| ✔  
OpenVPN+Cloak| ✔| ✔| ✔| ✔  
ShadowSocks| ✔| ✔| ✔| ✔  
  
### Fedora

| Fedora 26-29| Fedora 30  
---|---|---  
IKEv2| ✔*| ✔*  
AmneziaWG| ✔| ✔  
WireGuard| —| ✔  
OpenVPN| ✔| ✔  
OpenVPN+Cloak| ✔| ✔  
ShadowSocks| ✔| ✔  
  
### CentOS

| CentOS 7  
---|---  
IKEv2| ✔*  
AmneziaWG| ✔  
WireGuard| —  
OpenVPN| ✔  
OpenVPN+Cloak| ✔  
ShadowSocks| ✔  
  
**✔** * - Для IPSec (IKEv2) в настоящий момент, последняя рабочая версия -
AmneziaVPN 2.0.10. После перезагрузки сервера, требуется переустановка
контейнера. В случае downgrade-обновления, на версию AmneziaVPN более раннюю,
чем 2.1.2, необходимо предварительно сделать backup настроек AmneziaVPN на
устройстве.

**—** * - Для серверов с Ubuntu 18.04 и Debain 10, существует возможность
обновление ядра Linux, с 4-й до 5-й версии, для поддержки протокола WireGuard.

**—** \- Протокол не поддерживается.

Для любых ОС на серверах, кроме Ubuntu 22 / 20, Debian 12 / 11, настоятельно
рекомендуется выполнить предварительное обновление ОС, с последующей
перезагрузкой сервера.

### Обновление Ubuntu / Debian

    
    
    sudo apt update && sudo apt upgrade  
    

Вариант, допустимый для root

    
    
    apt update && apt upgrade  
    

Перезагрузка

    
    
    sudo reboot  
    

Вариант, допустимый для root

    
    
    reboot  
    

### Обновление CentOS 7

    
    
    sudo yum check-update && sudo yum update  
    

Вариант, допустимый для root

    
    
    yum check-update && yum update  
    

Перезагрузка

    
    
    sudo reboot  
    

Вариант, допустимый для root

    
    
    reboot  
    

### Обновление Fedora 26-30

    
    
    sudo dnf check-update && sudo dnf update  
    

Вариант, допустимый для root

    
    
    dnf check-update && dnf update  
    

Перезагрузка

    
    
    sudo reboot  
    

Вариант, допустимый для root

    
    
    reboot  