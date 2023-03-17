# theEnd, goodending, home  - не сделано
define c = Character("Кот", color ="#9c690a")
define y = Character("Вы", color ="#000000" )

default maxLove = 5
default minLove = 0

default love = 1

screen loveMeter:
    bar:
        xsize 350
        ysize 50
        xpos 50
        ypos 50
        value AnimatedValue (value = love, range = maxLove, delay = 1.0 )
        left_bar Frame("gui/bar/left.png", 10, 10)
        right_bar Frame("gui/bar/right.png", 10, 10)

#if love == 0:
#    window hide
#    scene the_End with Fade(1.0, 1.5, 1.0)
#    with Pause(10)
#    return 

#if love == 5:
#   scene home
#  show playfullCat
# "* котенок счастливо прильнул к вам *"
    #"* вы больше никогда не будите одиноки *"
    #c " мр-мяу "
    #y "да-да, мяу"
    #window hide
    
#    scene good_End with Fade(1.0, 1.5, 1.0)

#    with Pause(10)


label start:

    scene images_BlackScreen

    "* вы возвращаетесь домой *"
    "* но вдруг вы услышали тихое мяуканье в коробке * "

    scene Street
    with Fade(1.0, 1.5, 1.0, color ="#8f8f8f" )

    menu firstChoice:
        "* забрать котенка домой? "
        "да":
            jump main_choice
        "нет":
            jump choice_refuse
        
    return
 
label choice_refuse:

    scene Street

    "* вы решили не брать такую ответственность на себя *"

    c "мяу?"

    window hide
    
    scene the_End with Fade(1.0, 1.5, 1.0)

    with Pause(10)
    
    return 

label main_choice: 
    scene Street
     
    "* вы решили, что вам слишком одиноко в квартире и забрали кота *"

    scene home

    show screen loveMeter

    show mainCat

    "* спустя долгий рабочий день и одну неожиданную встречу вы наконец-то дома *"
    "* ваш гость с интересом принюхивается и разглядывает окружение, сидя у вас на руках *"

    menu secondChoice:
        "что вы сейчас будете делать?"

        "помыть котенка":
            jump bad_bathing
        "покормить": 
            jump Food
    return

label bad_bathing:

    scene GrayScreen

    show catThinks

    "* вы долго настраивали температуру воды, чтобы вашему новому другу было как можно приятнее *"
    "* решив для себя что все готово, вы осторожно взяли на руки котенка и опустили его в теплую ванночку *"
    "* ... *"

    show madCat
    с "МРР-А-РР"

    y "Ай! "

    "* однако он, кажется, не оценил это"

    $ love -= 1

    window hide
    scene the_End with Fade(1.0, 1.5, 1.0)
    with Pause(10)
    return 

    return

label Food:
    scene GrayScreen

    "* вы нашли у себя в холодильнике наполовину полную банку тунца *"

    "* кот нетерпеливо веритится у вас под ногами, жалобно мяукая *"

    show mainCat

    $ love += 2
    
    "* кот с аппетитом доел консерву и теперь мурчал *"

    "* кажется, вы заполучили доверие вашего маленького друга *"

    show playfullCat

    "* выкинув жестяную консерву в мусорку,\n вы вернулись к котенку, довольно вылизывавшего себе лапки и усы *"
    show sleepyCat
    "* вы потрепали котенка между ушек, вздохнув"

    menu: 
        y "и что же мне с тобой делать, таким грязным?"
        "все-таки помыть":
            jump good_bathing
        "поиграть":
            jump playng

    return
label playng: 
    scene home 
    show mainCat
    "* вы ласково трогаете котенка за животик"
    "* он игриво отгоняет лапками вашу руку, энергично извиваясь на диване *"
    $ love += 2
    "* котенок счастливо прильнул к вам *"
    c " мр-мяу "
    y "да-да, мяу"
    "* вы больше никогда не будите одиноки *"
    window hide
    scene good_End with Fade(1.0, 1.5, 1.0)
    with Pause(10)
    return
label good_bathing:
    scene home 
    show CatThinks
    "* вы долго настраивали температуру воды, чтобы вашему новому другу было как можно приятнее *"
    "* решив для себя что все готово, вы осторожно взяли на руки котенка и опустили его в теплую ванночку *"
    "* ... *"
    "* коту все равно, тунец задобрил его и он флегматично наблюдает как вы вымываете его шерсть *"
    jump playng
    return
