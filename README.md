# DZ_7_DRF

# Домашнее задание 1.

Задание 1: Создайте новый Django-проект, подключите DRF в настройках проекта.

Задание 2: Создайте следующие модели.
- Пользователь:
  -- все поля от обычного пользователя, но авторизацию заменить на email;
  -- телефон;
  -- город;
  -- аватарка.
  Модель пользователя разместите в приложении users
- Курс:
  -- название,
  -- превью (картинка),
  -- описание.
- Урок:
  -- название,
  -- описание,
  -- превью (картинка),
  --ссылка на видео.
  Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков.
  Реализуйте связь между ними.
  Модель курса и урока разместите в отдельном приложении. Название для приложения выбирайте такое, чтобы оно описывало
  то, с какими сущностями приложение работает. Например, lms или materials - отличные варианты.

Задание 3: Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока -
Generic-классы.
Для работы контроллеров опишите простейшие сериализаторы.
При реализации CRUD для уроков реализуйте все необходимые операции (получение списка, получение одной сущности,
создание, изменение и удаление).
Для работы контроллеров опишите простейшие сериализаторы.
Работу каждого эндпоинта необходимо проверять с помощью Postman.
Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже самой
простой авторизацией.

*Дополнительное задание (желательно, но не обязательно выполнять).
Реализуйте эндпоинт для редактирования профиля любого пользователя на основе более привлекательного подхода для личного
использования: Viewset или Generic.

# Домашнее задание 2.

Задание 1: Для модели курса добавьте в сериализатор поле вывода количества уроков.
Поле реализуйте с помощью SerializerMethodField().

Задание 2: Добавьте новую модель в приложение users:
- Платежи
  -- пользователь,
  -- дата оплаты,
  -- оплаченный курс или урок,
  -- сумма оплаты,
  -- способ оплаты: наличные или перевод на счет.
  Поля пользователь, оплаченный курс и отдельно оплаченный урок должны быть ссылками на соответствующие модели.
  Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.
  Если вы забыли как работать с фикстурами или кастомной командой - можете вернуться к уроку 20.1 Работа с ORM в Django
  чтобы вспомнить материал.

Задание 3: Для сериализатора для модели курса реализуйте поле вывода уроков.
Вывод реализуйте с помощью сериализатора для связанной модели.
Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

Задание 4: Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:
- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

*Дополнительное задание (желательно, но не обязательно выполнять).
Для профиля пользователя сделайте вывод истории платежей, расширив сериализатор для вывода списка платежей/

# Домашнее задание 3.

Задание 1: Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, настройте в проекте использование
JWT-авторизации и закройте каждый эндпоинт авторизацией.
Эндпоинты для авторизации и регистрации должны остаться доступны для неавторизованных пользователей.

Задание 2: Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, но без возможности их
удалять и создавать новые.
Заложите функционал такой проверки в контроллеры.
Подсказка: Модератор может просматривать и редактировать любые уроки и курсы, но не может удалять и создавать уроки и
курсы. Каждая операция — это определенный контроллер (часть ViewSet или отдельный Generic).
Заведите отдельный класс для определения, является ли пользователь модератором в permissions.py, для проверки прав
используйте метод
has_permission()
и проверку принадлежности пользователя определенной группе. Сделать это можно с помощью проверки пользователя:
request.user.groups.filter(name='имя_группы').exists()
Группы назначайте пользователям через админ-панель.
Создайте фикстуру или кастомную команду для заполнения созданных вами групп в базе данных.
Фикстуры можно снять командой, например:
python manage.py dumpdata auth.group --indent 2 > users/fixtures/groups.json
Определите права на контроллеры.
Для ViewSet разделяем права по action.
Список action и их названия можно найти тут: https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
Для разграничения прав доступа во вьюсетах используйте метод
get_permissions().
Ссылка на документацию: https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions
Внутри метода формируйте список прав для определенного action (или нескольких сразу).
Например, если нам необходимо ограничить доступ к эндпоинту создания и для вывода списка:
def get_permissions(self)
if self.action == 'create':
self.permission_classes = [список пермишенов для этого эндпоинта]
elif self.action == 'list':
self.permission_classes = [список пермишенов для этого эндпоинта]
return [permission() for permission in permission_classes]
Для Generics разделяем права с помощью указания premission_classes в контроллере.
Ссылка на документацию: https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
Например, для закрытия контроллера вывода списка объектов для неавторизованных пользователей:
class SomeListAPIView(generics.ListAPIView):
...
permission_classes = [IsAuthenticated]
Или для разрешения доступа только модераторам:
class SomeListAPIView(generics.ListAPIView):
...
permission_classes = [IsAuthenticated, Название_пермишена_для_модераторов]
Не забудьте проверить работоспособность ограничений через Postman.

Задание 3:Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов,
могли видеть, редактировать и удалять только свои курсы и уроки.
Подсказка:
Пользователь-немодератор - это любой другой авторизованный пользователь. Определите контроллеры, на которые необходимо
добавить новые права доступа.
Важно, что пользователи имеют право просматривать и редактировать только свои объекты. Чтобы это реализовать, привяжите
объект при создании к определенному пользователю.
Для этого добавьте в модель поле владельца и свяжите его с моделью пользователя. Не забудьте выполнить и запушить
миграции.
В контроллере создания объекта используйте метод
perform_create()
для управления созданием объекта и автоматической привязки создаваемого объекта к авторизованному пользователю.
Ссылка на документацию —https://www.django-rest-framework.org/api-guide/generic-views/#methods раздел Save and deletion
hooks.
Пример использования метода для создания урока и привязки его к авторизованному пользователю:
class LessonCreateAPIView(generics.CreateAPIView):
...
def perform_create(self, serializer):
serializer.save(название_поля_владельца=self.request.user)
Этот метод также можно использовать и во ViewSet для управления созданием объекта. Логика применения метода идентична
применению в Generics.
Права доступа можно объединять между собой и динамически управлять доступом к определенному контроллеру.
Для этого в DRF используются специальные символы — & (логическое И), | (логическое ИЛИ), ~ (логическое отрицание).
Например, нам необходимо, чтобы контроллер был доступен авторизованным пользователям и тем, кто не входит в группу
модераторов:
class SomeListAPIView(generics.ListAPIView):
...
permission_classes = [IsAuthenticated, ~IsModer]
Или контроллер должен быть доступен авторизованным пользователям и ЛИБО модераторам, ЛИБО владельцам объектов.
class SomeListAPIView(generics.ListAPIView):
...
permission_classes = [IsAuthenticated, IsModer | IsOwner]
Не забудьте проверить работоспособность ограничений через Postman.
Примечание: Заводить группы лучше через админку и не реализовывать для этого дополнительных эндпоинтов.

*Дополнительное задание (желательно, но не обязательно выполнять).
Для профиля пользователя введите ограничения, чтобы авторизованный пользователь мог просматривать любой профиль, но
редактировать только свой. При этом для просмотра чужого профиля должна быть доступна только общая информация, в которую
не входят: пароль, фамилия, история платежей.
