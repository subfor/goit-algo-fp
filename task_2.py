import sys
import turtle


def draw_branch(t, length, level):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(length)

    # Зберігаємо позицію і напрям
    pos = t.pos()
    angle = t.heading()

    # Ліва гілка
    t.left(45)
    draw_branch(t, length * 0.7, level - 1)

    # Повертаємось
    t.setpos(pos)
    t.setheading(angle)

    # Права гілка
    t.right(45)
    draw_branch(t, length * 0.7, level - 1)

    # Повертаємось назад
    t.setpos(pos)
    t.setheading(angle)


def main():
    if len(sys.argv) < 2:
        print("Вкажіть рівень рекурсії (наприклад: `python tree.py 8`)")
        sys.exit(1)

    level = int(sys.argv[1])

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.hideturtle()

    # Початкове положення
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    draw_branch(t, 100, level)
    screen.mainloop()


if __name__ == "__main__":
    main()
