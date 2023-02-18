import pygame

# define constants for the window size and stack element size
ELEMENT_WIDTH = 50
ELEMENT_HEIGHT = 200

# initialize Pygame
pygame.init()

# create a window
window = pygame.display.set_mode((1000, 500))

# define a font to use for displaying the stack elements
font = pygame.font.Font(None, 36)

# define a stack to hold the operands
stack = []

# define a list of tokens (operators and operands) in RPN
tokens = ["2", "3", "5", "*", "8", "+", "4", "2", "/", "-"]

# iterate through the tokens
for token in tokens:
    # if the token is an operand, push it onto the stack and draw it on the window
    if token.isdigit():
        stack.append(int(token))
        text = font.render(token, True, (255, 255, 255))
        window.blit(text, (10, (len(stack) - 1) * ELEMENT_HEIGHT))
    # if the token is an operator, pop the top two operands from the stack,
    # perform the operation, and push the result back onto the stack
    else:
        right = stack.pop()
        left = stack.pop()
        if token == "+":
            result = left + right
        elif token == "-":
            result = left - right
        elif token == "*":
            result = left * right
        elif token == "/":
            result = left / right
        stack.append(result)
        text = font.render(str(result), True, (255, 255, 255))
        window.blit(text, (10, (len(stack) - 1) * ELEMENT_HEIGHT))
    # update the window to show the new stack element
    pygame.display.update()
    # pause for a moment to allow the user to see the update
    pygame.time.delay(500)

# the final result will be the top item on the stack
result = stack.pop()
text = font.render(str(result), True, (255, 255, 255))
window.blit(text, (10, (len(stack) - 1) * ELEMENT_HEIGHT))
pygame.display.update()

# run the Pygame loop until the user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit Pygame
pygame.quit()
