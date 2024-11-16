import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (800, 600)

# Create screen
screen = pygame.display.set_mode(screen_size)

# Set title
pygame.display.set_caption("Particle Simulation")

# Set frame rate
frame_rate = 60

# Set particle properties
num_particles = 300
particle_size = 3
particle_color = (255, 255, 255)

# Create list to store particles
particles = []

# Create random particles
for i in range(num_particles):
    x = random.uniform(0, screen_size[0])
    y = random.uniform(0, screen_size[1])
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    particle = [x, y, vx, vy]
    particles.append(particle)

# Set repulsion strength
repulsion_strength = 120

# Set attraction strength
attraction_strength = 10

# Set mouse attraction flag to False
mouse_attraction_on = True

# Set mouse position
mouse_pos = (0, 0)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_attraction_on = True
            repulsion_strength=0
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_attraction_on = False
            repulsion_strength=13
    
    # Update mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    # Update particle positions
    for i, particle in enumerate(particles):
        # Calculate repulsive forces between particles
        for j, other_particle in enumerate(particles):
            if i != j:
                # Calculate distance between particles
                dx = particle[0] - other_particle[0]
                dy = particle[1] - other_particle[1]
                distance = math.sqrt(dx**2 + dy**2)
                # Calculate repulsion force
                force = repulsion_strength / distance**1.5
                if distance<60:
                    force=0
                # Calculate acceleration due to repulsion force
                ax = force * dx / distance
                ay = force * dy / distance
                # Update particle velocity
                particle[2] -= ax
                particle[3] -= ay
                particle[2] *= 0.997
                particle[3] *= 0.997
                #print(particle)
    
        # Calculate attractive forces to mouse
        if mouse_attraction_on:
            
            # Calculate distance to mouse
            dx = particle[0] - mouse_pos[0]
            dy = particle[1] - mouse_pos[1]
            distance = math.sqrt(dx**2 + dy**2)
            # Calculate attraction force
            force = attraction_strength / distance**2
            #force *= -1
            # Calculate acceleration due to attraction force
            ax = force * dx / distance
            ay = force * dy / distance
            # Update particle velocity
            particle[2]
        # Update particle position
        particle[0] += particle[2]
        particle[1] += particle[3]
        # Check if particle is outside screen and bounce if necessary
        if particle[0] < 0 or particle[0] > screen_size[0]:
            particle[2] *= -1
        if particle[1] < 0 or particle[1] > screen_size[1]:
            particle[3] *= -1


    # Draw particles
    screen.fill((0, 0, 0))
    for particle in particles:
        pygame.draw.circle(screen, particle_color, (int(particle[0]), int(particle[1])), particle_size)
    
    # Update display
    pygame.display.flip()
    
    # Delay to achieve desired frame rate
    pygame.time.delay(int(1000/frame_rate))
