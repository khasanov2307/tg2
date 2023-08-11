# Телеграм бот для пекарни

***

## Описание:

Бот написан на python c использованием библиотеки aiogram. Бот имеет админку, которой можно управлять через телеграм.
Через админку можно добавлять продукты: фото, название, описание, цена. Продукты разделены по 3 категориям. Реализована
возможность загружать фото в галерею. Также через админку, можно удалять продукты или фото из галереи. График работы
можно загрузить через админку с помощью отдельной кнопки в меню админа. В меню юзера, пользователь может загрузить все
фото из галереи, загрузить продукты из выбранной категории. А также узнать адрес или контакты, предприятия. Вся
необходимая информация записывается в БД Sqlite3.
***

### Пакеты и файлы:

* **data** - пакет для работы с данными, а именно работой с БД и и файлом конфигурации.
    + ***config.py*** -файл конфигурации, в него попадают значения из перменного окружения: API-токен, список админов,
      адрес, телефон и прочее.
    + ***sqlite_db.py*** - файл содержит все необходимые функции для обращения к БД, будь то загрузка из БД, добавление
      или изменение.
* **handlers** - пакет с обработчиками событий (тектовых команд отправляемых в бот, инлайн кнопок)
    + ***admin_handlers*** - файл содержит обработчки админских действий для работы в админке. Только пользователи с id,
      которые прописаны в файле конфигурации config.py могут выполнять эти команды.
    + ***сlient_handlers*** - файл содержит обработчики для юзерских кнопок.
* **keyboards** - пакет для админиских и юзерских клавиатур.
    + ***admin_keyboards*** - файл содержит админские клавиатуры, которые будут отображаться админам для управления
      ботом.
    + ***client_keyboards*** - файл содержит юзерские клавиатуры.
* *.gitignore* - файл игнорирования для GIT.
* *app.py* - основной файл бота, именно он вызывается из файла start.bat при запуске. В нем подключается БД и
  регистрируются дистпетчеры.
* *loader.py* - в файле создается объект бота, объект дистпечера и хранилище storage, для удобного вызова из любого
  места проекта.
* *requirements.txt* - файл содержит список внешних зависимостей проекта.
* *start.bat* - Файл запуска бота. В нем хранится API-токен, список админов, адрес и прочее. Именно этот файл необходимо
  отредактировать под свой проект.

***