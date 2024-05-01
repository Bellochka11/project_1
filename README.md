SQL


CREATE DATABASE IF NOT EXISTS Друзья_человека;
USE Друзья_человека;

CREATE TABLE Animals (
    animal_id INT PRIMARY KEY AUTO_INCREMENT,
    animal_name VARCHAR(50),
    birth_date DATE
);
CREATE TABLE PetAnimals (
    pet_id INT PRIMARY KEY,
    animal_type ENUM('Собака', 'Кошка', 'Хомяк'),
    FOREIGN KEY (pet_id) REFERENCES Animals(animal_id)
);

CREATE TABLE WorkingAnimals (
    work_id INT PRIMARY KEY,
    animal_type ENUM('Лошадь', 'Верблюд', 'Осел'),
    FOREIGN KEY (work_id) REFERENCES Animals(animal_id)
);

INSERT INTO Animals (animal_name, birth_date) VALUES ('Рекс', '2019-03-15');
INSERT INTO PetAnimals (pet_id, animal_type) VALUES (1, 'Собака');

DELETE FROM WorkingAnimals WHERE animal_type = 'Верблюд';

CREATE TABLE HorsesAndDonkeys AS
SELECT * FROM WorkingAnimals WHERE animal_type = 'Лошадь'
UNION
SELECT * FROM WorkingAnimals WHERE animal_type = 'Осел';

CREATE TABLE YoungAnimals AS
SELECT *
FROM Animals
WHERE DATEDIFF(CURDATE(), birth_date) BETWEEN 365 AND 1095;

ALTER TABLE YoungAnimals
ADD COLUMN age_in_months INT;
UPDATE YoungAnimals
SET age_in_months = DATEDIFF(CURDATE(), birth_date) / 30;

CREATE OR REPLACE VIEW AllAnimals AS
SELECT animal_id, animal_name, birth_date, 'Родительский класс' AS animal_group FROM Animals
UNION ALL
SELECT pet_id, animal_name, birth_date, animal_type AS animal_group FROM PetAnimals
UNION ALL
SELECT work_id, animal_name, birth_date, animal_type AS animal_group FROM HorsesAndDonkeys;

LINUX


liza@gb-linux:~$ cat > Домашние животные

cat: животные: Нет такого файла или каталога

liza@gb-linux:~$ cat > Домашние животные!

cat: 'животные!': Нет такого файла или каталога

liza@gb-linux:~$ cat > "Домашние животные"

собаки

кошки

хомяки

liza@gb-linux:~$ cat > "Вьючные животные"

лошади

верблюды

ослы

liza@gb-linux:~$ cat "Домашние животные" "Вьючные животные" > "Общие животные"

liza@gb-linux:~$ cat "Общие животные"

собаки

кошки

хомяки

лошади

верблюды

ослы

liza@gb-linux:~$ mv "Общие животные" "Друзья человека"

liza@gb-linux:~$ mkdir новая_директория

mkdir: невозможно создать каталог «новая_директория»: Файл существует

liza@gb-linux:~$ mkdir новая_директория1

liza@gb-linux:~$ mv "Друзья человека" новая_директория1/

liza@gb-linux:~$ lsb_release -a

No LSB modules are available.

Distributor ID:	Ubuntu

Description:	Ubuntu 22.04.3 LTS

Release:	22.04

Codename:	jammy

liza@gb-linux:~$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.23-1_all.deb

--2024-05-01 22:57:12--  https://dev.mysql.com/get/mysql-apt-config_0.8.23-1_all.deb

Распознаётся dev.mysql.com (dev.mysql.com)… 23.54.13.213, 2001:2030:4f:a8::2e31, 2001:2030:4f:89::2e31

Подключение к dev.mysql.com (dev.mysql.com)|23.54.13.213|:443... соединение установлено.

HTTP-запрос отправлен. Ожидание ответа… 302 Moved Temporarily

Адрес: https://repo.mysql.com//mysql-apt-config_0.8.23-1_all.deb [переход]

--2024-05-01 22:57:12--  https://repo.mysql.com//mysql-apt-config_0.8.23-1_all.deb

Распознаётся repo.mysql.com (repo.mysql.com)… 23.201.249.199, 2a02:26f0:e2:59b::1d68, 2a02:26f0:e2:5a2::1d68

Подключение к repo.mysql.com (repo.mysql.com)|23.201.249.199|:443... соединение установлено.

HTTP-запрос отправлен. Ожидание ответа… 200 OK

Длина: 18028 (18K) [application/x-debian-package]

Сохранение в: ‘mysql-apt-config_0.8.23-1_all.deb.1’



mysql-apt-confi 100%[====>]  17,61K  --.-KB/s    за 0s      



2024-05-01 22:57:12 (56,6 MB/s) - ‘mysql-apt-config_0.8.23-1_all.deb.1’ сохранён [18028/18028]



liza@gb-linux:~$ sudo dpkg -i mysql-apt-config_0.8.23-1_all.deb

[sudo] пароль для liza: 

(Чтение базы данных … на данный момент установлено 230099 файлов и каталогов.)

Подготовка к распаковке mysql-apt-config_0.8.23-1_all.deb …

Распаковывается mysql-apt-config (0.8.23-1) на замену (0.8.23-1) …

Настраивается пакет mysql-apt-config (0.8.23-1) …

Warning: apt-key should not be used in scripts (called from postinst maintainerscript of the package mysql-apt-config)

Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).

OK

liza@gb-linux:~$ sudo apt update

Сущ:1 http://ru.archive.ubuntu.com/ubuntu jammy InRelease

Пол:2 http://ru.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]

Сущ:3 http://ru.archive.ubuntu.com/ubuntu jammy-backports InRelease

Пол:4 http://repo.mysql.com/apt/ubuntu jammy InRelease [25,1 kB]

Игн:5 https://ppa.launchpadcontent.net/nginx/stable/ubuntu jammy InRelease

Сущ:6 https://download.virtualbox.org/virtualbox/debian jammy InRelease

Ошб:7 https://ppa.launchpadcontent.net/nginx/stable/ubuntu jammy Release

  404  Not Found [IP: 185.125.190.80 443]

Сущ:8 http://security.ubuntu.com/ubuntu jammy-security InRelease

Ошб:4 http://repo.mysql.com/apt/ubuntu jammy InRelease

  Следующие подписи не могут быть проверены, так как недоступен открытый ключ: NO_PUBKEY B7B3B788A8D3785C

Чтение списков пакетов… Готово

E: Репозиторий «https://ppa.launchpadcontent.net/nginx/stable/ubuntu jammy Release» не содержит файла Release.

N: Обновление из этого репозитория нельзя выполнить безопасным способом, поэтому по умолчанию он отключён.

N: Информацию о создании репозитория и настройках пользователя смотрите в справочной странице apt-secure(8).

W: Ошибка GPG: http://repo.mysql.com/apt/ubuntu jammy InRelease: Следующие подписи не могут быть проверены, так как недоступен открытый ключ: NO_PUBKEY B7B3B788A8D3785C

E: Репозиторий «http://repo.mysql.com/apt/ubuntu jammy InRelease» не подписан.

N: Обновление из этого репозитория нельзя выполнить безопасным способом, поэтому по умолчанию он отключён.

N: Информацию о создании репозитория и настройках пользователя смотрите в справочной странице apt-secure(8).

liza@gb-linux:~$ sudo apt install mysql-server

Чтение списков пакетов… Готово

Построение дерева зависимостей… Готово

Чтение информации о состоянии… Готово         

Уже установлен пакет mysql-server самой новой версии (8.0.36-0ubuntu0.22.04.1).

Обновлено 0 пакетов, установлено 0 новых пакетов, для удаления отмечено 0 пакетов, и 191 пакетов не обновлено.

liza@gb-linux:~$ wget http://ftp.debian.org/debian/pool/main/t/tree/tree_1.8.0-1_amd64.deb

--2024-05-01 22:57:56--  http://ftp.debian.org/debian/pool/main/t/tree/tree_1.8.0-1_amd64.deb

Распознаётся ftp.debian.org (ftp.debian.org)… 151.101.86.132, 2a04:4e42:14::644

Подключение к ftp.debian.org (ftp.debian.org)|151.101.86.132|:80... соединение установлено.

HTTP-запрос отправлен. Ожидание ответа… 200 OK

Длина: 49316 (48K) [application/vnd.debian.binary-package]

Сохранение в: ‘tree_1.8.0-1_amd64.deb.1’



tree_1.8.0-1_am 100%[====>]  48,16K  --.-KB/s    за 0,02s   



2024-05-01 22:57:56 (1,93 MB/s) - ‘tree_1.8.0-1_amd64.deb.1’ сохранён [49316/49316]



liza@gb-linux:~$ sudo dpkg -i tree_1.8.0-1_amd64.deb

Выбор ранее не выбранного пакета tree.

(Чтение базы данных … на данный момент установлено 230099 файлов и каталогов.)

Подготовка к распаковке tree_1.8.0-1_amd64.deb …

Распаковывается tree (1.8.0-1) …

Настраивается пакет tree (1.8.0-1) …

Обрабатываются триггеры для man-db (2.10.2-1) …

liza@gb-linux:~$ sudo dpkg -r tree

(Чтение базы данных … на данный момент установлено 230107 файлов и каталогов.)

Удаляется tree (1.8.0-1) …

Обрабатываются триггеры для man-db (2.10.2-1) …

liza@gb-linux:~$ ^C



