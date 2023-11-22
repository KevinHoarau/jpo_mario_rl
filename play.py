"""Super Mario Bros for OpenAI Gym."""
from nes_py.wrappers import JoypadSpace
from play_human import play_human
from gym_super_mario_bros.actions import RIGHT_ONLY, SIMPLE_MOVEMENT, COMPLEX_MOVEMENT
import gym_super_mario_bros

env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')

# wrap the environment with the new action space
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# play the environment with the given mode
infos = play_human(env)
