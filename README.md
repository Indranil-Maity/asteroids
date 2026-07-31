# Asteroids Game

A classic 2D 2D arcade shooter built with Python and Pygame. Navigate your ship, dodge oncoming space debris, and shoot asteroids to split them apart before they destroy your ship!

---

## Features

- **Smooth 2D Physics:** Vector-based movement and velocity rotation.
- **Dynamic Spawning:** An automated `AsteroidField` manager spawns asteroids of varying sizes around the screen edges.
- **Asteroid Splitting:** Shooting large asteroids breaks them down into smaller, faster fragments.
- **Automatic Group Management:** Leverages Pygame sprite containers to streamline rendering, updating, and collision tracking.

---

## Project Structure

```text
├── main.py            # Main game loop, initialization, and collision logic
├── player.py          # Player ship rendering, movement, and shooting controls
├── asteroid.py        # Asteroid sprite with custom drawing and splitting logic
├── asteroidfield.py   # Invisible manager spawning asteroids off-screen
├── shot.py            # Projectile/bullet sprite definitions
├── circleshape.py     # Base class for circular collision handling
├── constants.py       # Configuration variables (screen dimensions, radii, speeds)
└── logger.py          # Logging functions for tracking game states and events
