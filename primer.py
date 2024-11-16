#pgzero
import random
import pygame as py

WIDTH = 600  # Anchura de la ventana
HEIGHT = 300  # Altura de la ventana

TITLE = "invacion"  # Título de su proyecto de juego
FPS = 30  # Número de fotogramas por segundo

nave = Actor('nave', (50, 240))
background = Actor("fondo")
mode="game"
enemies = []
enemies2 = []
enemies3 = []
proyectil = []
# bonificaciones
escudos = []
corazones=[Actor("corazon",(60,30)),Actor("corazon",(80,30)),Actor("corazon",(100,30)),Actor("corazon",(120,30)),Actor("corazon",(150,30))]
# Listas para los disparos enemigos
proyectiles_enemies = []
proyectiles_enemies2 = []
proyectiles_enemies3 = []

count = 0
vidas = 5  # Número de vidas

for i in range(4):
    x = random.randint(700, 850)
    y = random.randint(20, 280)
    enemy = Actor("image", (x, y))
    enemy.speed = random.randint(2, 5)
    enemies.append(enemy)
for i in range(3):
    x = random.randint(700, 850)
    y = random.randint(20, 280)
    enemy2 = Actor("image (1)", (x, y))
    enemy2.speed = random.randint(2, 4)
    enemies2.append(enemy2)
for i in range(2):
    x = random.randint(700, 850)
    y = random.randint(20, 280)
    enemy3 = Actor("image (2)", (x, y))
    enemy3.speed = random.randint(2, 3)
    enemies3.append(enemy3)

def draw():
    if mode=="game":
        background.draw()
        nave.draw()
        for i in corazones:
            i.draw()
        for i in proyectil:
            i.draw()
        if count < 15:
            for i in enemies:
                i.draw()
            for i in enemies2:
                i.draw()
        else:
            for i in enemies3:
                i.draw()
        
        # Dibujar proyectiles enemigos
        for p in proyectiles_enemies:
            p.draw()
        for p in proyectiles_enemies2:
            p.draw()
        for p in proyectiles_enemies3:
            p.draw()
    
        screen.draw.text(str(count), pos=(10, 10), color="blue", fontsize=26, bold=True)
    elif mode=="end":
        background.draw()
        screen.draw.text(str("GAME OVER"), pos=(80, 150), color="red", fontsize=70, bold=True)
def movimiento_enemy():
    if count < 15:
        for i in enemies:
            i.x -= i.speed
            if i.x < -50:  # Si el enemigo sale de la pantalla por la izquierda
                i.x = random.randint(700, 850)
                i.y = random.randint(20, 280)
                
        for j in enemies2:
            j.x -= j.speed
            if j.x < -50:  # Si el enemigo sale de la pantalla por la izquierda
                j.x = random.randint(700, 850)
                j.y = random.randint(20, 280)
    else:
        for i in enemies3:
            i.x -= i.speed

def collisions():
    global count, vidas, mode

    # Crear listas temporales para almacenar los elementos que serán eliminados
    proyectiles_a_eliminar = set()

    for i, p in enumerate(proyectil):
        if count < 15:
            for e in enemies:
                if p.colliderect(e):
                    e.x = random.randint(700, 850)
                    e.y = random.randint(20, 280)
                    proyectiles_a_eliminar.add(i)
                    count += 1
                    break
            
            for e2 in enemies2:
                if p.colliderect(e2):
                    e2.x = random.randint(700, 850)
                    e2.y = random.randint(20, 280)
                    proyectiles_a_eliminar.add(i)
                    count += 1
                    break
        else:
            for h, e3 in enumerate(enemies3): 
                if p.colliderect(e3):
                    enemies3.pop(h)
                    proyectiles_a_eliminar.add(i)
                    count += 1
                    break

    for i in sorted(proyectiles_a_eliminar, reverse=True):
        proyectil.pop(i)

    # Colisiones con disparos enemigos
    for p in proyectiles_enemies + proyectiles_enemies2 + proyectiles_enemies3:
        if p.colliderect(nave):
            if vidas > 0:
                vidas -= 1
                corazones[vidas].image = "corazon gris"
            elif vidas<=0:
                mode="end"
            proyectiles_a_eliminar.add(p)

    # Eliminar proyectiles después de recorrer todas las colisiones
    for p in proyectiles_a_eliminar:
        if p in proyectil:
            proyectil.remove(p)
        if p in proyectiles_enemies:
            proyectiles_enemies.remove(p)
        if p in proyectiles_enemies2:
            proyectiles_enemies2.remove(p)
        if p in proyectiles_enemies3:
            proyectiles_enemies3.remove(p)

def movimiento_proyectiles_enemigos():
    for p in proyectiles_enemies:
        p.x -= 5
        if p.x < -50:
            proyectiles_enemies.remove(p)
    
    for p in proyectiles_enemies2:
        p.x -= 5
        if p.x < -50:
            proyectiles_enemies2.remove(p)
    
    for p in proyectiles_enemies3:
        p.x -= 5
        if p.x < -50:
            proyectiles_enemies3.remove(p)

def enemigos_disparan():
    for e in enemies:
        disparo = Actor("disparo4", (e.x, e.y))
        proyectiles_enemies.append(disparo)
    
    for e2 in enemies2:
        disparo2 = Actor("disparo2", (e2.x, e2.y))
        proyectiles_enemies2.append(disparo2)
    
    for e3 in enemies3:
        disparo3 = Actor("disparo3", (e3.x, e3.y))
        proyectiles_enemies3.append(disparo3)

def update(dt):
    movimiento_enemy()
    movimiento_proyectiles_enemigos()
    py.mouse.set_visible(False)
    collisions()
    for i in proyectil:
        if i.x > 630:
            proyectil.remove(i)
            break
        else:
            i.x += 10
    
def on_mouse_move(pos):
    nave.pos = pos    

def on_mouse_enter():
    py.mouse.set_visible(False)

def on_mouse_leave():
    py.mouse.set_visible(True)
    
def on_mouse_down(button, pos):
    if button == mouse.left:
        bullet = Actor("disparo")
        bullet.pos = nave.pos
        proyectil.append(bullet)

clock.schedule_interval(enemigos_disparan, 7.0)



