import pygame
import sys
import random

window_width = 1400
window_height = 800
arr = []
block_size = 40

# white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (105, 105, 105)
pink = (255, 182, 193)
purple = (128, 0, 128)
sky_blue = (135, 206, 250)
e_colour = (51, 51, 51)
back_col = (255, 255, 0)
above_col = (248, 255, 255)
white = above_col


def main():
    global screen, clock, arr, block_size
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    new_array()

    screen.fill(white)
    drawgrid()
    col_all()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 0 <= pos[1] <= 40:
                    if 100 <= pos[0] <= 435:
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, red)
                    elif 881 <= pos[0] <= 934:
                        block_size = 5
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 934 <= pos[0] <= 986:
                        block_size = 10
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 986 <= pos[0] <= 1037:
                        block_size = 15
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 1037 <= pos[0] <= 1087:
                        block_size = 20
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 1087 <= pos[0] <= 1142:
                        block_size = 25
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 1142 <= pos[0] <= 1193:
                        block_size = 30
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 1193 <= pos[0] <= 1245:
                        block_size = 35
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                    elif 1245 <= pos[0] <= 1300:
                        block_size = 40
                        screen.fill(white)
                        new_array()
                        drawgrid()
                        col_all()
                        draw_box(100, 0, 335, 40, black)
                        draw_box(575, 0, 725, 40, black)
                elif 53 <= pos[1] <= 98:
                    if 50 <= pos[0] <= 260:
                        bubblesort()
                        drawgrid()
                        col_all()
                        draw_back(50, 53, 210, 45)
                        draw_box(50, 53, 210, 45, red)
                    elif 320 <= pos[0] <= 580:
                        selectionsort()
                        drawgrid()
                        col_all()
                        draw_back(320, 53, 260, 45)
                        draw_box(320, 53, 260, 45, red)
                    elif 640 <= pos[0] <= 845:
                        mergeSort(0, len(arr) - 1)
                        drawgrid()
                        col_all()
                        draw_back(320, 53, 260, 45)
                        draw_box(320, 53, 260, 45, red)
                    elif 900 <= pos[0] <= 1105:
                        quicksort(0, len(arr) - 1)
                        drawgrid()
                        col_all()
                        draw_back(900, 53, 205, 45)
                        draw_box(900, 53, 205, 45, red)
                    elif 1160 <= pos[0] <= 1365:
                        heapsort(len(arr))
                        drawgrid()
                        col_all()
                        draw_back(1160, 53, 205, 45)
                        draw_box(1160, 53, 205, 45, red)
            pygame.display.update()


def new_array():
    global arr, block_size
    arr = []
    for x in range(0, window_width, block_size):
        temp = random.randrange(20, window_height - 100, block_size)
        arr.append(temp)


def bubblesort():
    global arr, screen, clock, vis
    clock = pygame.time.Clock()
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            for eve in pygame.event.get():
                if eve.type == pygame.WINDOWCLOSE:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            screen.fill(white)
            drawgrid()
            col_all()
            draw_block(j * block_size, 100, block_size, arr[j])
            draw_block((j + 1) * block_size, 100, block_size, arr[j + 1])
            draw_back(50, 53, 210, 45)
            draw_box(50, 53, 210, 45, red)
            pygame.display.update()
            pygame.time.delay(block_size)


def selectionsort():
    global arr, screen
    for i in range(0, len(arr)):
        ind = i
        for j in range(i + 1, len(arr)):
            if arr[ind] > arr[j]:
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]
        for eve in pygame.event.get():
            if eve.type == pygame.WINDOWCLOSE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        screen.fill(white)
        drawgrid()
        col_all()
        draw_block(i * block_size, 100, block_size, arr[i])
        draw_block(ind * block_size, 100, block_size, arr[ind])
        draw_back(320, 53, 260, 45)
        draw_box(320, 53, 260, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size * 10)


def mergeSort(l, r):
    if l < r:
        mid = l + ((r - l) // 2)
        mergeSort(l, mid)
        mergeSort(mid + 1, r)
        merge(l, mid, r)
        for eve in pygame.event.get():
            if eve.type == pygame.WINDOWCLOSE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()


def merge(l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = []
    R = []
    for i in range(0, n1):
        L.append(arr[l + i])
    for i in range(0, n2):
        R.append(arr[m + 1 + i])

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            for eve in pygame.event.get():
                if eve.type == pygame.WINDOWCLOSE:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            screen.fill(white)
            drawgrid()
            col_all()
            draw_block(k * block_size, 100, block_size, arr[k])
            draw_back(640, 53, 205, 45)
            draw_box(640, 53, 205, 45, red)
            pygame.display.update()
            pygame.time.delay(block_size)
        else:
            arr[k] = R[j]
            j += 1
            for eve in pygame.event.get():
                if eve.type == pygame.WINDOWCLOSE:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            screen.fill(white)
            drawgrid()
            col_all()
            draw_block(k * block_size, 100, block_size, arr[k])
            draw_back(640, 53, 205, 45)
            draw_box(640, 53, 205, 45, red)
            pygame.display.update()
            pygame.time.delay(block_size)
        k += 1

    while i < n1:
        arr[k] = L[i]
        for eve in pygame.event.get():
            if eve.type == pygame.WINDOWCLOSE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        screen.fill(white)
        drawgrid()
        col_all()
        draw_block(k * block_size, 100, block_size, arr[k])
        draw_back(640, 53, 205, 45)
        draw_box(640, 53, 205, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size)
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        for eve in pygame.event.get():
            if eve.type == pygame.WINDOWCLOSE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        screen.fill(white)
        drawgrid()
        col_all()
        draw_block(k * block_size, 100, block_size, arr[k])
        draw_back(640, 53, 205, 45)
        draw_box(640, 53, 205, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size)
        j += 1
        k += 1


def quicksort(l, r):
    if l < r:
        m = partition(l, r)
        quicksort(l, m - 1)
        quicksort(m + 1, r)


def partition(l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            for eve in pygame.event.get():
                if eve.type == pygame.WINDOWCLOSE:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
            screen.fill(white)
            drawgrid()
            col_all()
            draw_block(i * block_size, 100, block_size, arr[i])
            draw_block(j * block_size, 100, block_size, arr[j])
            draw_back(900, 53, 205, 45)
            draw_box(900, 53, 205, 45, red)
            pygame.display.update()
            pygame.time.delay(block_size)
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    for eve in pygame.event.get():
        if eve.type == pygame.WINDOWCLOSE:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    screen.fill(white)
    drawgrid()
    col_all()
    draw_block((i + 1) * block_size, 100, block_size, arr[i + 1])
    draw_block(r * block_size, 100, block_size, arr[r])
    draw_back(900, 53, 205, 45)
    draw_box(900, 53, 205, 45, red)
    pygame.display.update()
    pygame.time.delay(block_size)
    return i + 1


def heapsort(n):
    for i in range((n // 2) - 1, -1, -1):
        heapify(n, i)
        for eve in pygame.event.get():
            if eve.type == pygame.WINDOWCLOSE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        screen.fill(white)
        drawgrid()
        col_all()
        draw_back(1160, 53, 205, 45)
        draw_box(1160, 53, 205, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        screen.fill(white)
        drawgrid()
        col_all()
        draw_back(1160, 53, 205, 45)
        draw_box(1160, 53, 205, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size)
        heapify(i, 0)
        for eve in pygame.event.get():
            if eve.type == pygame.WINDOWCLOSE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        screen.fill(white)
        drawgrid()
        col_all()
        draw_back(1160, 53, 205, 45)
        draw_box(1160, 53, 205, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size)
    screen.fill(white)
    drawgrid()
    col_all()
    draw_back(1160, 53, 205, 45)
    draw_box(1160, 53, 205, 45, red)
    pygame.display.update()
    pygame.time.delay(block_size)


def heapify(n, i):
    ind = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[ind]:
        ind = l
    if r < n and arr[r] > arr[ind]:
        ind = r
    if ind != i:
        arr[i], arr[ind] = arr[ind], arr[i]
        screen.fill(white)
        drawgrid()
        col_all()
        draw_block(i * block_size, 100, block_size, arr[i])
        draw_block(ind * block_size, 100, block_size, arr[ind])
        draw_back(1160, 53, 205, 45)
        draw_box(1160, 53, 205, 45, red)
        pygame.display.update()
        pygame.time.delay(block_size)
        heapify(n, ind)
    for eve in pygame.event.get():
        if eve.type == pygame.WINDOWCLOSE:
            pygame.display.quit()
            pygame.quit()
            sys.exit()


def draw_block(x, y, a, b):
    rect = pygame.Rect(x, y, a, b)
    pygame.draw.rect(screen, pink, rect)
    pygame.draw.rect(screen, sky_blue, rect, 1)


def drawgrid():
    global arr, block_size
    rect = pygame.Rect(0, 0, window_width, 100)
    pygame.draw.rect(screen, above_col, rect)

    for x in range(0, window_width, block_size):
        rect = pygame.Rect(x, 100, block_size, arr[x // block_size])
        pygame.draw.rect(screen, purple, rect)
        pygame.draw.rect(screen, sky_blue, rect, 1)

    font = pygame.font.SysFont('centaur', 40, bold=True)
    s = "BubbleSort" + '     ' + "SelectionSort" + '     ' + "MergeSort" + '     ' + "QuickSort" + '     ' + "HeapSort"
    text = font.render(s, True, green)
    text_rect = text.get_rect()
    text_rect.center = (window_width // 2, 75)
    screen.blit(text, text_rect)

    font = pygame.font.SysFont('centaur', 35, bold=True)
    s = "Generate New Array" + '             ' + "Set Size and Speed 05 10 15 20 25 30 35 40"
    text = font.render(s, True, green)
    text_rect = text.get_rect()
    text_rect.center = (window_width // 2, 20)
    screen.blit(text, text_rect)


def draw_box(x, y, a, b, col):
    rect = pygame.Rect(x, y, a, b)
    pygame.draw.rect(screen, col, rect, 2)


def col_all():
    draw_box(100, 0, 335, 40, black)
    draw_box(575, 0, 725, 40, black)

    draw_box(881, 0, 53, 40, black)
    draw_box(986, 0, 51, 40, black)
    draw_box(1087, 0, 55, 40, black)
    draw_box(1193, 0, 52, 40, black)

    draw_box(50, 53, 210, 45, black)
    draw_box(320, 53, 260, 45, black)
    draw_box(640, 53, 205, 45, black)
    draw_box(900, 53, 205, 45, black)
    draw_box(1160, 53, 205, 45, black)


def draw_back(x, y, a, b):
    rect = pygame.Rect(x, y, a, b)
    pygame.draw.rect(screen, back_col, rect)
    font = pygame.font.SysFont('centaur', 40, bold=True)
    s = "BubbleSort" + '     ' + "SelectionSort" + '     ' + "MergeSort" + '     ' + "QuickSort" + '     ' + "HeapSort"
    text = font.render(s, True, green)
    text_rect = text.get_rect()
    text_rect.center = (window_width // 2, 75)
    screen.blit(text, text_rect)

    font = pygame.font.SysFont('centaur', 35, bold=True)
    s = "Generate New Array" + '             ' + "Set Size and Speed 05 10 15 20 25 30 35 40"
    text = font.render(s, True, green)
    text_rect = text.get_rect()
    text_rect.center = (window_width // 2, 20)
    screen.blit(text, text_rect)


if __name__ == "__main__":
    main()
