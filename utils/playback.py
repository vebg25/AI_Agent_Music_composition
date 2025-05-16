# utils/playback.py

import pygame

def play_midi(midi_file_path: str):
    pygame.mixer.init()
    pygame.mixer.music.load(midi_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
