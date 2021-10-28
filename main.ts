controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    music.beamUp.play()
    mySprite.startEffect(effects.fire, 200)
    projectile2 = sprites.createProjectileFromSprite(assets.image`Key Blast`, mySprite, 100, 1)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.zapped.play()
    projectile = sprites.createProjectileFromSprite(assets.image`Final Flash`, mySprite, 100, 0)
    mySprite.startEffect(effects.fire, 200)
})
info.onLifeZero(function () {
    game.over(false)
})
sprites.onDestroyed(SpriteKind.Player, function (sprite) {
    myEnemy = sprites.create(assets.image`Frezzer ship`, SpriteKind.Enemy)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.ashes, 500)
    info.changeScoreBy(2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    mySprite.destroy(effects.confetti, 500)
    scene.cameraShake(20, 500)
    info.changeLifeBy(-1)
})
let myEnemy: Sprite = null
let projectile: Sprite = null
let projectile2: Sprite = null
let mySprite: Sprite = null
info.setLife(1)
mySprite = sprites.create(assets.image`ssj2 Vegeta`, SpriteKind.Player)
mySprite.setStayInScreen(true)
game.setDialogTextColor(6)
game.showLongText("Welcome Z Fighter, this world is cursed by the frezzer force and I need your help to stop them. Will you except this parallel quest?", DialogLayout.Top)
game.setDialogFrame(img`
    a a a a a a a a a a a a a a a 
    a a a 5 c c 5 5 c c 5 a a a a 
    a a 5 c a 5 5 5 5 a c 5 a a a 
    a a c c 5 3 c c 3 5 c c a a a 
    a a c c 5 3 c c 3 5 c c a a a 
    a a 5 c a 5 5 5 5 a c 5 a a a 
    a a a 5 c c 5 5 c c 5 a a a a 
    a a c 5 a a 5 5 a a 5 c a a a 
    a a 5 5 a a 5 5 a a 5 5 a a a 
    c 5 5 c c c 5 5 c c c 5 5 a a 
    5 5 a a a c 5 5 c a a a 5 5 c 
    5 a a 5 5 5 5 5 5 5 5 a a 5 5 
    c a a c 5 5 5 5 5 5 c a a a 5 
    a a a a a 5 5 5 5 a a a a a c 
    a a a a a c 5 5 c a a a a a a 
    `)
scene.cameraShake(8, 5000)
scene.setBackgroundImage(assets.image`Destroyed Namek`)
info.setScore(0)
controller.moveSprite(mySprite)
game.onUpdateInterval(1000, function () {
    myEnemy = sprites.create(assets.image`Frezzer ship`, SpriteKind.Enemy)
    myEnemy.setVelocity(-100, 0)
    myEnemy.setPosition(160, randint(5, 115))
    myEnemy.setFlag(SpriteFlag.AutoDestroy, true)
})
forever(function () {
    music.playMelody("C5 F A G E D A B ", 125)
})
