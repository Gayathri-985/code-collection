import cv2
import mediapipe as mp
import pyautogui
import pygame
import random
import sys

# Initialize Mediapipe for hand tracking
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize Pygame for the game
pygame.init()

# Screen dimensions for Pygame
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture-Controlled Target Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Ball settings
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 30, 30)

# Target settings
target = pygame.Rect(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), 40, 40)

# Game variables
score = 0
timer = 30  # Game duration in seconds
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

# Webcam setup
cap = cv2.VideoCapture(0)

# Main game loop
while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror view
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Gesture control logic
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw blue hand landmarks on the webcam feed
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),  # Blue outline
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)  # Green connections
            )

            # Extract landmark positions for controlling the ball
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Map hand position to screen coordinates
            ball.centerx = int(index_finger_tip.x * WIDTH)
            ball.centery = int(index_finger_tip.y * HEIGHT)

    # Check for collision between ball and target
    if ball.colliderect(target):
        score += 1
        # Move the target to a new random location
        target.x = random.randint(50, WIDTH - 50)
        target.y = random.randint(50, HEIGHT - 50)

    # Timer logic
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # Convert to seconds
    remaining_time = max(0, timer - int(elapsed_time))

    # Game over
    if remaining_time == 0:
        cap.release()
        cv2.destroyAllWindows()
        pygame.quit()
        print(f"Game Over! Final Score: {score}")
        sys.exit()

    # Draw everything in Pygame
    screen.fill(WHITE)  # Background
    pygame.draw.ellipse(screen, BLUE, ball)  # Ball
    pygame.draw.rect(screen, RED, target)  # Target

    # Draw dotted line (path to target)
    start_pos = ball.center
    end_pos = target.center
    for i in range(0, 101, 10):  # Dotted effect
        dot_x = start_pos[0] + (end_pos[0] - start_pos[0]) * (i / 100)
        dot_y = start_pos[1] + (end_pos[1] - start_pos[1]) * (i / 100)
        pygame.draw.circle(screen, BLACK, (int(dot_x), int(dot_y)), 3)

    # Draw score and timer
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (10, 50))

    pygame.display.flip()

    # Display the webcam feed 
    cv2.imshow("Hand Gesture Control", frame)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            sys.exit()

    # Close webcam window if ESC is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

    clock.tick(30)

# Release resources
cap.release()
cv2.destroyAllWindows()
pygame.quit()

