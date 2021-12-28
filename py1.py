import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 400
    screen = pygame.display.set_mode(size)
    # screen.fill('purple')

    running = True
    x_pos = 0
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
        x_pos += 10
        if x_pos > 1920:
            x_pos = 0

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()
    pygame.quit()