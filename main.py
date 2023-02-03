import time
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")
MSG = "{}, что будем готовить?"

bot = Bot("TOKEN")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Привет, {user_full_name}")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=5)
    btn1 = types.KeyboardButton('/Omlet')
    btn2 = types.KeyboardButton('/Blini')
    btn3 = types.KeyboardButton('/Onigiri')
    btn4 = types.KeyboardButton('/KornDog')
    btn5 = types.KeyboardButton('/Raratui')
    btn6 = types.KeyboardButton('/SnailsInFranch')
    btnOut = types.KeyboardButton('/quit')
    btns.add(btn1, btn2, btn3, btn4, btn5, btn6, btnOut)
    await bot.send_message(user_id, MSG.format(user_full_name), reply_markup=btns)

@dp.message_handler(commands=['quit'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Спасибо, досвидания!',
                           reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['Omlet'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Поиск")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Ингредиенты:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Яйца - 4 шт. \nМолоко - 100 мл \nСоль - 0,25 ч. ложки (по вкусу) \nМасло растительное (для жарки) - 1 ст. ложка (10-15 мл)")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Рецепт:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "1. В глубокую миску вбиваем яйца. Добавляем к яйцам немного соли. Уже в самом начале можно включить духовку и разогреть ее до температуры 190 градусов.\n2. Затем сразу же вливаем необходимое количество молока. Желательно, чтобы молоко было комнатной температуры. Один из секретов приготовления пышного...\n3. Перемешиваем все ингредиенты кухонным венчиком. Использовать миксер нет необходимости.")

@dp.message_handler(commands=['Blini'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Поиск")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Ингредиенты:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id,
                           "Яйца - 2 шт \nМолоко - 250 мл (1 стакан)\nВода (кипяток) - 250 мл (1 стакан)\nМасло растительное - 3 ст. ложки\nМука - 200 г\nСахар - 3 ст. ложки\nСоль - 0,5 ч. ложки")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Рецепт:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Взбиваем яйца с сахаром и солью.\nДобавляем молоко, перемешиваем.\nВсыпаем просеянную муку. Перемешиваем тесто до однородности.\nЗатем вливаем кипяток, перемешивая тесто, и растительное масло.\nЗаварное тесто для блинов готово.\nЖарим тонкие блины на разогретой сковороде, до румяности с двух сторон.")

@dp.message_handler(commands=['Onigiri'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Поиск")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Ингредиенты:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "рис 	400	г \nкреветки отварные очищенные 	200	г \nкапуста морская консервированная 	50	г \nморковь маринованная острая	50	г \nлук маринованный жемчужный	50	г \nспаржа консервированая 	50	г \nсемя кунжута 	1	ст. ложка \nперец 	 	по вкусу \nсоль 	 	по вкусу")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Рецепт:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Креветки мелко нарезать, посолить, поперчить. \nСформовать из риса колобки треугольной формы, положив в середину каждого начинку из креветок. \nОбернуть онигири полосками морской капусты, выложить на тарелку, посыпать семенами кунжута. \nОформить маринованным луком, морковью и спаржей.")

@dp.message_handler(commands=['KornDog'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Поиск")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Ингредиенты:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Мука пшеничная (высшего сорта) - 100 г + для обваливания \nМука кукурузная - 100 г \nПаприка сладкая - 2 ч. л. \nРазрыхлитель теста - 2 ч. л. \nЯйца - 1 шт. \nМолоко ~ 200 мл \nСахар - 2 ч. л. \nСосиски - 10 шт. \nСоль - по вкусу и желанию \nМасло рстительное рафинированное - для жарки")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Рецепт:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "В первую очередь смешайте в глубокой таре яйцо с молоком. Присолите, подсыпьте любимые специи, тщательно размешайте.\n"\
                                                 "Дальше просеянную муку соедините с разрыхлителем и введите в яично-молочную смесь. В таком случае воспользуйтесь венчиком для лучшего результата.\n"\
                                                 "Обратите внимание, что тесто для корн-догов по консистенции должно получиться, как густая сметана, и легко стекать с венчика.\n"\
                                                 "Возьмите высокую тару, например, стакан и вылейте туда кляр.\n"\
                                                 "Затем сосиску освободите от пленки и оберните сырной пластинкой.\n"\
                                                 "Далее насадите изделие на деревянную шпажку. Кстати, благодаря ей корн-доги удобно кушать и макать в соус.\n"\
                                                 "Погрузите заготовку в тестовую массу таким образом, чтобы она была полностью в кляре.\n"\
                                                 "Вдобавок к этому, чтобы обжарить сосиски в тесте возьмите глубокую сковородку. Налейте в нее масло и хорошо раскалите.\n"\
                                                 "Итак, выложите аппетитные заготовки и жарьте со всех сторон до золотистого равномерного покрытия на среднем нагреве.\n"\
                                                 "В конце процесса готовые изделия переложите на бумажное полотенце, чтобы стек лишний жир.")

@dp.message_handler(commands=['Ratatui'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Поиск")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Ингредиенты:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Баклажаны - 600 г (2 шт.)\n" \
                                                 "Кабачки - 600 г (2 шт.)\n" \
                                                 "Помидоры - 1 кг (7 шт.)\n" \
                                                 "Лук репчатый - 150 г (2 шт.)\n" \
    
                                                "Перец болгарский - 400 г (4 шт.)\n" \
                                                "Чеснок - 4 зубчика\n" \
                                                "Масло оливковое - 100 мл\n"
                                                "Паприка молотая - 1 ч. ложка\n" \
                                                "Травы прованские сушёные - по вкусу\n" \
                                                "Зелень петрушки (для подачи) - по вкусу\n" \
                                                "Соль - по вкусу")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Рецепт:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Мелко нарезанный лук обжарить до прозрачности на 2 ст. ложках оливкового масла, посолить.\n" \
                                                 "С 3-х помидоров снять кожицу.\n" \
                                                 "У болгарского перца удалить плодоножки и семена. Помидоры и перец нарезать кубиками и добавить к луку. Обжаривать овощи в течение 10-ти минут. Затем измельчить обжаренные овощи блендером до желаемой консистенции.\n" \
                                                 "Готовый соус ровным слоем выложить на дно формы для запекания.\n" \
                                                 "Включить духовку и разогреть до 180°С.\n" \
                                                 "Вымытые и очищенные от кожицы кабачки и баклажаны, а также оставшиеся помидоры нарезать кружочками толщиной 5 мм и выложить сверху на соус, чередуя. Посолить.\n"\
                                                 "Сверху смазать оливковым маслом, смешанным с измельчённым чесноком, молотой паприкой и прованскими травами.\n" \
                                                 "Накрыть форму фольгой и отправить в духовку, нагретую до 180°С, на 30 минут.\n" \
                                                 "Затем фольгу снять, запекать ещё 20 минут.\n" \
                                                 "Готовый рататуй посыпать мелко нарезанной свежей зеленью.")


@dp.message_handler(commands=['SnailsInFranch'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Поиск")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Ингредиенты:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "филе виноградных улиток \nчеснок \nлимон \nсливочное масло \nсоль \nприправы (по вкусу) \nзелень петрушки \nрастительное масло")
    time.sleep(1)
    await bot.send_message(message.from_user.id, "Рецепт:")
    time.sleep(0.5)
    await bot.send_message(message.from_user.id, "Первым делом размораживают мясо улиток естественным способом. Затем на сковороду наливают растительное масло. Бросают в него моллюски, после чего поджаривают деликатесный продукт.\n" \
                                                 "В отдельной емкости готовят соус. Чеснок натирают на мелкой терке или режут ножом. Смешивают его со сливочным маслом, мелко нарубленной петрушкой, солью, приправами, лимонным соком.\n"\
                                                 "Полученный соус разделяют на несколько частей и наполняют небольшие огнеупорные формы или раковины моллюсков. Сверху кладут обжаренный продукт. Отправляют в духовку на 5 минут. Французское блюдо из улиток готово. Его подают в горячем виде, поэтому запекают непосредственно перед предполагаемой трапезой.")


if __name__ == '__main__':
    executor.start_polling(dp)

