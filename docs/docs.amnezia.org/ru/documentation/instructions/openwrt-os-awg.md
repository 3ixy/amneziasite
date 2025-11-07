
* * *

## Шаг 4. Настройка файрвола роутера[​](openwrt-os-awg.html#шаг-4-настройка-
файрвола-роутера "Прямая ссылка на Шаг 4. Настройка файрвола роутера")

  1. Перейдите в **Network** → **Firewall**.

![](../../assets/images/openwrt_9-f9b44dad0c8c37d992c0847ca63164c3.png)

  2. Нажмите **Edit** справа от зоны **lan**.

![](../../assets/images/openwrt_10-2b24cd78ad1d014e82f4ca497b8f2158.png)

  3. Нажмите на выпадающий список **Allow forward to destination zones** → поставьте галочку возле ранее созданной файрвол-зоны → нажмите **Save**.

![](../../assets/images/openwrt_11-0f8fdde43f2f3172ec31dea47dcadd76.png)

  4. Поставьте галочку в параметре **Masquerading** возле ранее созданной файрвол-зоны → нажмите **Save & Apply**.

![](../../assets/images/openwrt_12-6320faee413f50ec968c8ce76824ca29.png)

  5. Перейдите в **Network** → **Interfaces**.

![](../../assets/images/openwrt_3-24d46794500c5340738ec38a5e83da3b.png)

  6. Нажмите **Edit** справа от созданного ранее VPN-интерфейса.

![](../../assets/images/openwrt_13-5c8a840dcde3c089ec23ff28cafc08e1.png)

  7. Перейдите на вкладку **Peers** → нажмите **Edit** справа от загруженного ранее файла конфигурации.

![](../../assets/images/openwrt_14-cc51b2b4445a0b4d652de3aaa66603e7.png)

  8. Поставьте галочку у параметра **Route Allowed IPs** → нажмите **Save** → ещё раз **Save**.

![](../../assets/images/openwrt_15-03e5219ab7d3312c10eb58b63b0874c6.png)

  9. В появившемся окне, находясь на вкладке **Interfaces** , нажмите **Save & Apply** → наведите курсор на **System** → нажмите **Reboot**.

![](../../assets/images/openwrt_16-5f73a4f3b3248e3d91032a8bff3ae969.png)

  10. Нажмите **Perform reboot**.

![](../../assets/images/openwrt_17-1e726b8991169c17310e47285fd11c71.png)

После перезагрузки роутера проверьте наличие трафика — интернет должен начать
работать через VPN.

* * *

## Как поменять параметры VPN-подключения на новые из другого файла
конфигурации[​](openwrt-os-awg.html#как-поменять-параметры-vpn-подключения-на-
новые-из-другого-файла-конфигурации "Прямая ссылка на Как поменять параметры
VPN-подключения на новые из другого файла конфигурации")

  1. Перейдите в **Network** → **Interfaces**.

![](../../assets/images/openwrt_3-24d46794500c5340738ec38a5e83da3b.png)

  2. Нажмите **Edit** справа от созданного VPN-интерфейса.

![](../../assets/images/openwrt_13-5c8a840dcde3c089ec23ff28cafc08e1.png)

  3. В появившемся окне нажмите **Load configuration**.

![](../../assets/images/openwrt_5-efa9f0b6d32b9f7e1f806204693d397f.png)

  4. Вставьте всё содержимое файла конфигурации или переместите файл конфигурации в появившееся окно → нажмите **Import settings** → нажмите **OK** , чтобы подтвердить внесение изменений.

![](../../assets/images/openwrt_18-3f956e9fc00221ff7d7176576686d530.png)

  5. На вкладке **Peers** нажмите **Delete** справа от старого файла конфигурации → **Save**.

![](../../assets/images/openwrt_19-cd03876541653ba086db283dad13ef93.png)

  6. Нажмите **Edit** справа от загруженного ранее файла конфигурации → поставьте галочку у параметра **Route Allowed IPs** → нажмите **Save** → ещё раз **Save**.

![](../../assets/images/openwrt_15-03e5219ab7d3312c10eb58b63b0874c6.png)

  7. В появившемся окне, находясь на вкладке **Interfaces** , нажмите **Save & Apply**.

![](../../assets/images/openwrt_20-54812c8984515ae3544fc908c370b83d.png)

[Предыдущая страницаУстановка VPN на роутер Keenetic](keenetic-os-
awg.html)[Следующая страницаПодключение к Amnezia Free](connect-amfree.html)

Обращайтесь в чат за помощью, если что-то не получается

[](https://t.me/amnezia_vpn)

  * [Шаг 1. Установка OpenWrt на роутер](openwrt-os-awg.html#шаг-1-установка-openwrt-на-роутер)
  * [Шаг 2. Установка AmneziaWG на роутер OpenWrt](openwrt-os-awg.html#шаг-2-установка-amneziawg-на-роутер-openwrt)
  * [Шаг 3. Создание VPN-подключения на роутере](openwrt-os-awg.html#шаг-3-создание-vpn-подключения-на-роутере)
  * [Шаг 4. Настройка файрвола роутера](openwrt-os-awg.html#шаг-4-настройка-файрвола-роутера)
  * [Как поменять параметры VPN-подключения на новые из другого файла конфигурации](openwrt-os-awg.html#как-поменять-параметры-vpn-подключения-на-новые-из-другого-файла-конфигурации)

![](../../img/logo-with-a-w-glow.svg)

Продукты

[Amnezia Premium](https://amnezia.org/premium)[Amnezia
Free](https://amnezia.org/free)[Amnezia Self-hosted](https://amnezia.org/self-
hosted)

Ресурсы

[Документация](../../documentation.html)[Решение
проблем](../../troubleshooting.html)[FAQ](../../faq.html)

Контакты

[Github](https://github.com/amnezia-vpn/amnezia-
client)[Telegram](https://t.me/amnezia_vpn)[Reddit](https://reddit.com/r/AmneziaVPN/)

