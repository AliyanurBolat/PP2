import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.current_song_index = 0
        self.load_songs()
        
    def load_songs(self):
        self.songs = [file for file in os.listdir('.') if file.endswith('.mp3')]
        if len(self.songs) == 0:
            pygame.quit()
            quit()

    def play_song(self, index):
        pygame.mixer.music.load(self.songs[index])
        pygame.mixer.music.play()
        self.playing = True

    def stop_song(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_song(self):
        self.stop_song()
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.play_song(self.current_song_index)

    def previous_song(self):
        self.stop_song()
        self.current_song_index = (self.current_song_index - 1) % len(self.songs)
        self.play_song(self.current_song_index)

    def run(self):
        running = True
        self.screen.fill((255, 255, 255))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.playing:
                            self.stop_song()
                        else:
                            self.play_song(self.current_song_index)
                    elif event.key == pygame.K_RIGHT:
                        self.next_song()
                    elif event.key == pygame.K_LEFT:
                        self.previous_song()
        
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
