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

# Домашнее задание 4.

Задание 1:Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.
То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние образовательные платформы или личные сайты — нельзя.
Создайте отдельный файл validators.py, реализуйте валидатор, проверяющий ссылку, которую пользователь хочет записать в поле урока с помощью класса или функции.
Интегрируйте валидатор в сериализатор.
Если вы используете функцию-валидатор — указанием валидаторов для поля сериализатора validators=[ваш_валидатор].
Если вы используете класс-валидатор — указанием валидаторов в class Meta:
validators = [ваш_валидатор(field='поле_которое_валидируем')].

Задание 2: Добавьте модель подписки на обновления курса для пользователя.
Модель подписки должна содержать следующие поля: «пользователь» (FK на модель пользователя), «курс» (FK на модель курса). Можете дополнительно расширить модель при необходимости.
Вам необходимо реализовать эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.
Подсказка: Воспользуйтесь APIView и реализуйте логику метода post, который будет отдавать ответ в зависимости от действия.
Пример кода метода post для управления подпиской:
def post(self, *args, **kwargs):
    user = получаем пользователя из self.requests
    course_id = получаем id курса из self.reqests.data
    course_item = получаем объект курса из базы с помощью get_object_or_404
    subs_item = получаем объекты подписок по текущему пользователю и курса
# Если подписка у пользователя на этот курс есть - удаляем ее
    if subs_item.exists():
        ...
        message = 'подписка удалена'
# Если подписки у пользователя на этот курс нет - создаем ее
    else:
        ...
        message = 'подписка добавлена'
		# Возвращаем ответ в API
    return Response({"message": message})
Зарегистрируйте новый контроллер в url и проверьте его работоспособность в Postman. При этом при выборке данных по курсу пользователю необходимо присылать признак подписки текущего пользователя на курс. То есть давать информацию, подписан пользователь на обновления курса или нет.
Подсказка: Чтобы реализовать это, используйте SerializerMethodField() с соответсвующим методом или вложенный сериализатор для подписки.
 
Задание 3: Реализуйте пагинацию для вывода всех уроков и курсов.
Пагинацию реализуйте в отдельном файле paginators.py. Можно реализовать один или несколько классов пагинатора. Укажите параметры page_size,  page_size_query_param, max_page_size для класса PageNumberPagination. Количество элементов на странице выберите самостоятельно. Интегрируйте пагинатор в контроллеры, используя параметр pagination_class.

Задание 4: Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.
В тестах используйте метод setUp для заполнения базы данных тестовыми данными. Обработайте возможные варианты взаимодействия с контроллерами пользователей с разными правами доступа. Для аутентификации пользователей используйте self.client.force_authenticate(). Документацию к этому методу можно найти тут. https://www.django-rest-framework.org/api-guide/testing/#forcing-authentication
Сохраните результат проверки покрытия тестами.

*Дополнительное задание (желательно, но не обязательно выполнять).
Напишите тесты на все имеющиеся эндпоинты в проекте.

# Домашнее задание 5.

Задание 1: Подключить и настроить вывод документации для проекта. 
Убедиться, что каждый из реализованных эндпоинтов описан в документации верно, при необходимости описать вручную.
Для работы с документацией проекта воспользуйтесь библиотекой drf-yasg или drf-spectacular.
Как вручную можно сформировать документацию в drf-yasg можно почитать тут, в drf-spectacular — тут или тут.

Задание 2: Подключить возможность оплаты курсов через https://stripe.com/docs/api.
Доступы можно получить напрямую из документации, а также пройти простую регистрацию по адресу https://dashboard.stripe.com/register.
Для работы с учебным проектом достаточно зарегистрировать аккаунт и не подтверждать его — аккаунт будет находиться в тестовом режиме.
Для работы с запросами вам понадобится реализовать обращение к эндпоинтам:
https://stripe.com/docs/api/products/create — создание продукта;
https://stripe.com/docs/api/prices/create — создание цены;
https://stripe.com/docs/api/checkout/sessions/create — создание сессии для получения ссылки на оплату.
При создании цены и сессии обратите внимание на поля, которые вы передаете в запросе. Внимательно изучите значение каждого поля и проанализируйте ошибки при их возникновении, чтобы создать корректную запись.
При создании сессии нужно передавать id цены, которая соответствует конкретному продукту.
Для тестирования можно использовать номера карт из документации:
https://stripe.com/docs/terminal/references/testing#standard-test-cards.
Примечание:
Подключение оплаты лучше всего рассматривать как обычную задачу подключения к стороннему API.
Основной путь: запрос на покупку → оплата. Статус проверять не нужно.
Каждый эквайринг предоставляет тестовые карты для работы с виртуальными деньгами.
Подсказка:
Необходимо связать данные от сервиса платежей со своим приложением. Все взаимодействия с платежным сервисом опишите в сервисных функциях. Сервисные функции взаимодействуют с платежным сервисом (Stripe) и отдают ответы в виде JSON. Далее результаты работы сервисных функций мы используем в соответствующих View: при создании платежа в нашей системе мы должны создать продукт, цену и сессию для платежа в Stripe, сохранить ссылку на оплату в созданном платеже в нашей системе и отдать пользователю в ответе на POST-запрос ссылку на оплату или данные о платеже (которые будут включать ссылку на оплату).
При необходимости проверки статуса платежа можно реализовать дополнительную View, которая будет обращаться на Session Retrieve (https://stripe.com/docs/api/checkout/sessions/retrieve) по id созданной в Stripe сессии и отдавать пользователю данные о статусе платежа. Статус платежа также можно дополнительно хранить в модели платежей в нашей системе.
Перед созданием сессии необходимо создать продукт и цену. Все эти данные мы можем получить из модели платежа (модель платежа связана с продуктом, в продукте есть название и цена).
Обратите внимание, что цены при передаче в Strip указываются в копейках (то есть текущую цену продукта нужно умножить на 100).
 
*Дополнительное задание (желательно, но не обязательно выполнять).
Реализуйте проверку статуса с помощью эндпоинта https://stripe.com/docs/api/checkout/sessions/retrieve — получение данных о сессии по идентификатору.

# Домашнее задание 6.

Задание 1: Настройте проект для работы с Celery. 
Также настройте приложение на работу с celery-beat для выполнения периодических задач.
Не забудьте вынести настройки Redis в переменные окружения.

Задание 2: Ранее вы реализовали функционал подписки на обновление курсов. 
Теперь добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.
Подсказка: Чтобы реализовать асинхронную рассылку, вызывайте специальную задачу по отправке письма в коде контроллера.
То есть вызов задачи на отправку сообщения должен происходить в контроллере обновления курса: когда курс обновлен — тем, кто подписан на обновления именно этого курса, отправляется письмо на почту.

*Дополнительное задание (желательно, но не обязательно выполнять).
Пользователь может обновлять каждый урок курса отдельно. Добавьте проверку на то, что уведомление отправляется только в том случае, если курс не обновлялся более четырех часов.

Задание 3: С помощью celery-beat реализуйте фоновую задачу, которая будет проверять пользователей по дате последнего входа по полю 
last_login и, если пользователь не заходил более месяца, блокировать его с помощью флага is_active.
Задачу сделайте периодической и запланируйте расписание в настройках celery-beat.
Обратите внимание на timezone вашего приложения и timezone в настройках celery: важно, чтобы они были одинаковыми, чтобы задачи запускались в корректное время.