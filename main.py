def on_b_pressed():
    global mySprite3
    mySprite3 = sprites.create(assets.image("""
        bomb
    """), SpriteKind.projectile)
    music.pew_pew.play()
    mySprite3.set_velocity(1, 10)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    music.zapped.play()
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 8 . . . . . . . . . 
                    . . . . . 8 . 8 8 8 . . . . . . 
                    . . . . . . . 8 1 1 8 . . . . . 
                    . . . . . . 8 8 9 1 1 9 . . . . 
                    . . . . . 8 8 9 9 9 1 1 9 . . . 
                    . . . . 8 8 6 9 9 9 9 1 9 . . . 
                    . . . 8 8 8 6 9 9 9 9 1 9 . . . 
                    . . . . 8 8 6 9 9 9 9 1 9 . . . 
                    . . . . . 8 6 9 9 9 9 1 9 . . . 
                    . . . . . . 8 9 9 9 1 1 9 . . . 
                    . . . . . . . 8 9 1 1 9 . . . . 
                    . . . . . . . 8 1 1 8 . . . . . 
                    . . . . . . . 8 8 8 . . . . . . 
                    . . . . . 8 8 . . . . . . . . .
        """),
        mySprite,
        100,
        50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.over(False)
    music.play_melody("F D C F D C F E ", 95)
info.on_countdown_end(on_countdown_end)

def on_life_zero():
    global mySprite2
    mySprite2 = sprites.create(assets.image("""
        coke
    """), SpriteKind.enemy)
info.on_life_zero(on_life_zero)

mySprite2: Sprite = None
projectile: Sprite = None
mySprite3: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(assets.image("""
    sprite
"""), SpriteKind.player)
game.set_dialog_text_color(6)
game.show_long_text("Welcome adventurer, this world is cursed by the divine and I need your help to stop them. Will you except this quest?",
    DialogLayout.TOP)
game.set_dialog_frame(img("""
    a a a a a a a a a a a a a a a 
        a a a 5 a a 5 5 a a 5 a a a a 
        a a 5 a a 5 5 5 5 a a 5 a a a 
        a a a a 5 a a a a 5 a a a a a 
        a a a a 5 a a a a 5 a a a a a 
        a a 5 a a 5 5 5 5 a a 5 a a a 
        a a a 5 a a 5 5 a a 5 a a a a 
        a a a 5 a a 5 5 a a 5 a a a a 
        a a 5 5 a a 5 5 a a 5 5 a a a 
        a 5 5 a a a 5 5 a a a 5 5 a a 
        5 5 a a a a 5 5 a a a a 5 5 a 
        5 a a 5 5 5 5 5 5 5 5 a a 5 5 
        a a a a 5 5 5 5 5 5 a a a a 5 
        a a a a a 5 5 5 5 a a a a a a 
        a a a a a a 5 5 a a a a a a a
"""))
scene.camera_shake(8, 5000)
controller.move_sprite(mySprite)
info.set_life(5)
info.set_score(0)
info.change_life_by(-1)
scene.set_background_image(img("""
    ccccccccccccccccccccccccccccccccccccccccccccccc5555555555555555555555555555555555555555555555555555555555ccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccccccccccccccccc555555555555555555555555555555555555555555555555555555555555555cccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccc1cccccccccccccccccccccccccccccccccccc55555555555555555555555555555555555554444444444444444444444555555ccccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccccccccccccccc5555555555555544555555555555555544444444444444444444444444444555555cccccccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccc1cccccccccccccccccc555555555555444444445555555444444444444444444444444444444444444555555ccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccc555555555555444444444444444444444444444444444444444444444444444444555555cc1ccccccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccccccccccc55555555555544444444444444444444444444444444444444444444444444444444455555ccccccccccccccccccc1ccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccc1ccc5555555555444444444444444444444444444444444444444444444444444444444444555555cccccccccccccccccccccccccccccccccc1ccccccccccccc
        cccccccccccccccccccccccccccccccccc55555555554444444444444444444444444444444444444444444444444444444444444445555555cccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccc55555555555444444444444444444444444444444444444444444444444444444444444444445555555ccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccc55555555555444444444444444444444444444444444444444444444444444444444444444444445555555cccccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccc5555555555544444444444444444444444444444444444444444444444444444444444444444444455555555ccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccc555555555444444444444444444444444444444444444444444444444444444444444444444444444455555555cccccccccccccccccccccccccccccccccccccccccc
        ccccccccc1ccccccccccccccccc55555555544444444444444444444444444444444444444444444444444444444444444444444444444455555555ccccccccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccc5555555555544444444444444444444444444444444444444444444444444444444444444444444444444445555555555cccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccc55555555554444444444444444444444444444444444444444444444444444444444444444444444444444444555555555cccccccccccccccccccccccccccccc1ccccccc
        ccccccccccccccccccccccc55555555554444444444444444444444444444444444444aa444444444444444444444444444444444444444445555555555ccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccc555555555544444444444444444444444444444444444444aa4444444444444444444444444444444444444444445555555555cccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccccc555555555544444444444444444444444444444444444444aaaa444444444444444444444444444444444444444444555555555cccccc1ccccccccccccccccccccccccccccc
        ccccccccccccccccccccc55555555544444444444444444444444444444444444444aaaaaaa44444444444444444444444444444444444444444455555555ccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccc55555555544444444444444444444444444444444444444aaaaaaaaaa444444444444444444444444444444444444444445555555ccccccccccccccccccccccccccccccccccc
        ccccccccccccccccccc5555555554444444444444444444444444444444444444aaaaaaaaaaaaa444444444444444444444444444444444444444455555555cccccccccccccccccccccccccccccccccc
        cccccccccccccccccc5555555554444444444444444444444444444444444444aaaaaaaaaaaaaaa444444444444444444444444444444444444444445555555cccccccccccccccc1cccccccccccccccc
        cccccccccccccccccc555555554444444444444444444444444444444444444aaaaaaaaaaaaaaaaa444444444444444444444444444444444444444445555555cccccccccccccccccccccccccccccccc
        ccccccccccccccccc555555555444444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444444444455555555cccccccccccccccccccccccccccccc
        cccccc1ccccccccc555555555444444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444444444455555555cccccccccccccccccccccccccccc
        ccccccccccccccc55555555544444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444444444444444555555555cccccccccccccccccccccccccc
        ccccccccccccccc55555555444444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444444444455555555cccccccccccccccccccccccccc
        cccccccccccccc5555555554444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444444445555555555cccccccccccccccccccccccc
        cccccccccccccc555555554444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444444444555555555ccccccccccccccccccccccc
        ccccccccccccc555555554444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444444444555555555cccccccccccccccccccccc
        cccccccccccc555555555444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444444444555555555cccccccccccccccccccccc
        ccccccccccc555555555444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444444444445555555555ccccccccccccccccccccc
        ccccccccccc55555555444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444445555555555cccccccccccccccccccc
        ccccccccccc55555555444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444445555555555ccccccccccccccccccc
        cccccccccc55555555444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444445555555555ccccccccccccccccccc
        ccccccccc55555555444444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444445555555555cccccccccccccccccc
        ccccccccc5555555544444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444444445555555555cccccccccccccccccc
        cccc1ccc5555555544444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444444555555555cccccccccccccccccc
        cccccccc55555554444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444455555555cccccccccccccccccc
        ccccccc55555554444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444444555555555ccccccccccccccccc
        ccccccc5555554444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444445555555555ccccccccc1cccccc
        ccccccc555555444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444445555555555ccccccccccccccc
        ccccc5555555444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444444555555555ccccccccccccccc
        ccccc555555444444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444444555555555cccccccccccccc
        cccc555555544444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444444555555555ccccccccccccc
        cccc5555554444444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444444555555555ccccccccccccc
        cccc55555544444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444444555555555cccccccccccc
        ccc55555544444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444445555555555ccccccccccc
        ccc5555544444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444445555555555ccccccccccc
        ccc55554444444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444555555555ccccccccccc
        ccc555544444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444555555555ccccccccccc
        ccc5555444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafffffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444455555555ccccccccccc
        cc5555444444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa44444444444444444444444444444555555ccccccccccc
        cc555544444444444444444444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffffffcccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaa4444444444444444444444444444555a55aaaaaaaaaa
        cc555544444444444444444aaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccffffffffffffccccccccccccccccaaaaaaaaaaaaaaaaaaaaaaaaa444444444444444444444444444aaaaaaaaaaaaaaa
        ccc555444444444444444aaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccffffffffffffccccccccccccccccccccccaaaaaaaaaaaaaaaaaaaaafffffff444444444444444aaaaaaaaaaaaaaaaaa
        cccc5544444aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccfffffffffffffffccccccccccccccccccccccccaaaaaaaaaaaaaaaafffffffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        ccccc5aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccffffffffffffffffffcccccccccccccccccccccccaaaaaaaaaaaaafffffffffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccccccccaaaaaaaaafffffffafffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccfffffffffffffffffffffcccccccccccccccccccccccccccccaaaaafffffffaafffffccccccccccccccccccccccccccccccc
        aaaaaaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccffffffffffffffffffffffffccccccccccccccccccccccccccccccccfffffffaffffffccccccccccccccccccccccccccccccc
        aaaaaaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccfffffffffffffffffffffffffcccccccccccccccccccccccccccccccffffffffaffffffccccccccccccccccccccccccccccccc
        aaaaaaaaaaaaaaaaaccccccccccccccccccacccccccccacccccccccccfffffffffffffffffffffffffffccccccccccccccccccccccccccccccffffffffaffffffccccccccccccccccccccccccccccccc
        aaaaaaaaaaacccccccccccccccccccccccccccccccccccccccccccccfffaaaffffffffffffffffafffffccccccccccccccccccccccccccccccffffffffaffffffccccccccccccccccccccccccccccccc
        aaaaaacccccccccccccccccccccccccccccccccccccccccccccccccfffffffaaafffffffffffffafffffcccccccccccccccccccccccccccccfffffffffaffffffccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccacccccccaccccccccccccccccfffffffffffaafffffffffffaffffffcccccccccccccccccccccccccccffffffffffaffffffccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccffffffffffffffaaffffffffaaffffffccccccccccccccccccccccccccfffffffffffafffffffcccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccaccccccccccccccccccccffffffffffffffffaaffffffaaffffffffccccccccccccccccccccccccffffffffffffaffffffffccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccffccccccccccccccaccccccccffffffffffffffffffafffffaaffffffffffccccccccccccccccccccccfffffffffffffafffffffffffcccccccccc4ccccccccccccccc
        ccccccccccccccccccccccccccffffccccccccccccccccccccfffffffffffffffffaffaffffafffffffffffccccccccccccccccccccccfffffffffffffafffffffcfffcccccccccccccccccccccccccc
        cccccccccccccccccccccccccfffffcccccccccccccccccccffffffffffffffffaafffaafffaffffffffffffccccccccccccccccccccccffffffffffffafffffffffcccccccccccccccccccccccccccc
        cccccccccccccccccccccccccfffffccccccccccccccccccfffffffffffffffffaffffffaaaaffffffffffffffcccccccccccccccccccccfffffffffffaafffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccfffffffcccccccfcccccccccffffffffffffffffaaffffffffffaafffffffffffffffcccccccccccccccccccffffffffffffafffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccffffffffccccccfffcccccccfffffffffffffffaffffffffffffffaafffffffffffffffffccccccccccccccfffffffffffffafffffffccccccccccccccccccccccccccccc
        ccccccccccccccccccccccfffffffffccccccffcccccccfffffffffffffffaffffffffffffffffaafffffffffffffffffffcccccccccccfffffffffffffafffffffccccccccccccccccccccccccccccc
        ccccccccccccccccccccccfffffffffcccccfffccccccffffffffffffaaaaffffffffffffffffffaafffffffffffffffffffccccccccccfffffffffffffaffffffffcccccccccccccccccccccccccccc
        cccccccccccccccccccccccffffffffccfffffcccccccffffffffffaafffffffffffffffffffffffaafffffffffffffffffffcccccccccffffffffffffaaffffffffcccccccccccccccccccccccccccc
        ccccccccccccc2cccccccccffffffffffffffccccccffffffffffffaffffffffffffffffffffffffffaffffffffffffffffffcccccccccffffffffffffafffffffffcccccccccccccccccccccccccccc
        cccccccccccccccccccccccffffffffffffffacccccffffffffffffaffffffffffffffffffffffffffaafffffffffffffffffffccccccfffffffffffaaffffffffffccccccccc4cccccc54cccccccccc
        ccccccc2cccccccccccccccfffffffffffffaafcccffffffffffffffffffffffffff5555fffffffffffaffffffffffffffffffffccccfffffffffffaaaffffffffffcccccccccccccccccccccccccccc
        cccccccccccccccccccccccfffffffffffffafffffffffffffffffffffffffffff555ff55ffffffffffffffffffffffffffffffffccffffffffffffafafffffffffccccccccccccccccccccccccccccc
        ccccccccccccccccccccccccfffffffffffafffffffffffffffffffffffffffff5ffffff5fffffffffffffffffffffffffffffffffcfffffffffffaffafffffffffcccccccccccccc2cccccccccccccc
        ccccccccccccccccccccccccffffffffffafffffffffffffffffffffffffffff5ffffffff5fffffffffffffffffffffffffffffffffffffffffffaaffaaafffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccfffffffaafffffffffffffffffffffffffffff5fffffffff5ffffffffffffffffffffffffffffffffcffffffffffafffffaaafffffccccccccccccccccccccccccccccc
        ccccccc2ccccccccccccccccccffffffaffffffffffffffffffffffffffffff55ffffffff5fffffffffffffffffffffffffffffffffffffffffffafffffffafffffcccccccc4cccccccccccccccccccc
        cccccccccccc4cccccccccccccffffffafffffffffffffffffffffffffffffff5ffffffff5ffffffffffffffffffffffffffffffffffffffffffaaffffffffaffffccccccccccccccccccc2ccccccccc
        ccccccccccccccc2ccccccccccffffffaffffffffffffffffffffffffffffffff5ffffff5ffffffffffffffffffffffffffffffffffffffffffaafffffffffaffffccccccccccc5cccc4cccccccccccc
        ccccccccccccccccccccccccccffffffaaffffffffffffffffffffffffffffffff55fff5ffffffffffffffffffffffffffffffffffffffffffaaffffffffffaffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccffffffaafffffffffffffffffffffffffffffffff5555ffffffffffffffffffffffffffffffffffffffffffafffffffffffaffffccccccccc5ccc4ccccccccccccccc
        ccccccccccccccccccccccccccccffffffaafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffaafffffffffffaffffccccccccccccccccccccccccccccc
        cccccccccc2cccccccccccccccccfffffffafffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffafffffcccccccccccc2ccccccccccccccc
        cccccccccccccc4cccccccccccccffffffffafffffffffffffffffffffff5ffffffffffffffff55fffffffffffffffffffffffffffffffffffffffffffffaafffffffccccccc2ccccccccccc5ccccccc
        ccccccccccccccccccccccccccccffffffffafffffffffffffffffffffff5fffffffffffffffff555fffffffffffffffffffffffffffffffffffffffffffaffffffffccccccccccccc5ccccccccccccc
        ccccccccccccccccccccccccccccffffffffaffaaffffffffffffffffff5ffffffffffffffffffff5555fffffffffffffffffffffffffffffffffffaaaaaafffffffffcccccccccccccccccccccccccc
        ccccccccccc5ccccccccccccccccffffffffafaafffffffffffffffffff5ffffffff5ffffffffffffff55fff5fffffffffffffffffffffffffffffaafffaffffffffffcccccccccccccccc4ccccccccc
        ccccc4ccccccccccccccccccccccffffffffaaafffffffffffffffffff5fffffffff5ffffffffffffffff5555ffffffffffffffffffffffffffffafffffafffffffffccccc5ccccccccccccccccccccc
        cccccccccccccc5cccccccccccccffffffffaafffffffffffffffffff5ffffffff55ffffff5fffffffffffffffffffffffffffffffffffffffffaafffffaffffffffccccccccccccc2cccccccccccccc
        ccccccccc5ccccccccccccccccccffffffffaffffffffffffffffff55fffffffff5ffffffff5ffffffffffffffffffffffffffffffffffffffffaffffffaafffffffccccccccccccccccccc2cccccccc
        ccccccccccccccccccccccccccccffffffffafffffffffffffffff55fffffffff5ffffffffff5fffffffffffffffffffffffffffffffffffffffafffffffffffffffcccccccccccccccccccccccccccc
        ccccccccccccccccccccccccccccffffffffafffffffffffffff55ffffffffff55fffffffffff5fffffffffffffffaaaafffffffffffffffffffafffffffffffffffcccccccccccccccccccccccccccc
        cccccccccccccccc4cccccccccccfffffffffaffffffffffff555ffffffffff5ffffff5ffffff5555fffffffffffafffffffffffffffffffffffafffffffffffffffcccccccccccccccccccccccccccc
        ccccccccccccc5ccccccccccccccfffffffffaffffffffff555ffffffffffff5ffffff5fffffffff5555ffffffffaffffffffffffffffffffffaaffffffffffffffffccccaccc2cccccccccccccccccc
        cccccc4cccccccccccccccccccccffffffffaffffffffff5fffffffffffff55fffffff5ffffffffffffffffffffaafffffffffffffffffffffaafffffffffffffffffcccccccccccccccc5cccccccccc
        ccccccccccccccccccccccccccccffffffffafffffffffffffffffffffff55ffffffff5fffffffffffffffffffafffffffffffffffffffffaaaffffffffffffffffffccccccccccccccccccccccccccc
        ccccccccccc5ccccccccccccccccfffffffffffffffffffffffffffffff55fffffffff55ffffffffffffffffffaffffffffffffffffffaaaffffffffffffffffffffffcccccc4ccccccccccccccccccc
        cccccccccccccccccc4ccccccccccfffffcfffffffffffffffffffff555ffffffffffff5fffffffffffffffffaffffffffffffffffffffffffffffffffffffffffffffccccccccccc444cccccccccccc
        cccccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffff5fffffffffffffffffaffffaaaaaffffffffffffffffffffffffffffffcffffccccccccccc444cccccccccccc
        cccccccccc5ccc5ccccccccccccccffffcfffffccffffffffffffffffffffffffffffff5ffffffffffffffffaafffaafffffffffffffffffffffffffffffffffffcffccccccccacc444ccccccccccccc
        ccccccccccccccccccccccccacccccffccfffccccffffffffffffffffffffffffffffff5ffffffffffffffffafffaaffffffffffffffffffffffffffffffffffffcccccccccccccccf4ccccccccccccc
        cccccc2cccc44cccccccccccccccccfcccccccccfffffffffffffffffffffffffffffff5fffffffffffaaaaaaaafafffffffffffffffffffffffffffffffffffffcccccccccccccccfcccccccccccccc
        cccccccccc444cccccccccccccccccccccccccccffffffffffffffffffffffffffffff55fffffffffffafffffffaffffffffffffffffffffffffffffffffffcfffcccccfcccccccccfcccccccccccccc
        cccccccccc44cccccc2ccccccccccacccccccccfffffffffffffffffffffffffffffff555fffffffaaaaffffffaffffffffffffffffffffffffffffffffffccffccfcccccccacccccfcccccccccccccc
        ccccccccc5cfcccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffaffffffffffffffffffffffffffffffffffccccccccccccccccccccfcccccccccccccc
        cccccccccccfcccccccccccccccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffaffffffffffffffffffffffffffffffffffccccccccccccccccccccfcccccccccccccc
        cccccccccccfcccccccccccccccccacccccccfcffffffffffffffffffffffffffffffffffffffffffffffffffafffffffffffffffffffffffffffffffffffccfcccccccccccccccccfcccccccccccccc
        cccccccccccfccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffaafffffffffffffffffffffffffffffffffffccccffcccfccccccccccfcccccccccccccc
        ccccccccccfccccccccccccaccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffaaffffffffffffffffffffffffffffffffffffcccffcfcccccccccccccfcccccccccccccc
        ccccccccccfcccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffaafffffffffffffffffffffffffffffffffffffccfffffcccccccccccccfcccccccccccccc
        ccccccccccfccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffffffffffffffffaaffffffffffffffffffffffffffffffffffffffffffffffffccccccccccfcccccccccccccc
"""))
info.start_countdown(5)

def on_forever():
    music.play_melody("E F A C5 E C5 C A ", 200)
forever(on_forever)

def on_update_interval():
    pass
game.on_update_interval(500, on_update_interval)
