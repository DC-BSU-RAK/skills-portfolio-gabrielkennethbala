import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os

class JokeTellingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("skibidi rizzler haha (DONT FORGET TO REPLACE AFTER FINISH)")
        self.root.geometry("900x400")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize pygame mixer for sound
        pygame.mixer.init()
        
        # HARDCODED SOUND PATHS - EDIT THESE TO MATCH YOUR SOUND FILES
        self.sound_paths = {
            'joke_start': "toby fox - UNDERTALE Soundtrack - 23 Shop.flac",      # Edit this path
            'punchline': "LAUGH.mp3",        # Edit this path  
            'drum_roll': "DRUM ROLL.mp3",        # Edit this path
            'laughter': "LAUGH.mp3",          # Edit this path
            'custom': ""         # Edit this path
        }
        
        # Load the sounds
        self.sounds = {}
        self.load_hardcoded_sounds()
        
        # Load jokes
        self.jokes = self.load_jokes()
        self.current_joke = None
        
        self.create_widgets()
    
    def load_hardcoded_sounds(self):
        """Load all the hardcoded sound files"""
        sound_status = []
        for sound_type, filepath in self.sound_paths.items():
            try:
                if os.path.exists(filepath):
                    self.sounds[sound_type] = pygame.mixer.Sound(filepath)
                    sound_status.append(f"✓ {sound_type}")
                else:
                    self.sounds[sound_type] = None
                    sound_status.append(f"✗ {sound_type} (file not found)")
            except Exception as e:
                self.sounds[sound_type] = None
                sound_status.append(f"✗ {sound_type} (error: {str(e)})")
        
        self.sound_status_text = "\n".join(sound_status)
    
    def load_jokes(self):
        """Load jokes from the provided content"""
        joke_content = """Why did the chicken cross the road?To get to the other side.
What happens if you boil a clown?You get a laughing stock.
Why did the car get a flat tire?Because there was a fork in the road!
How did the hipster burn his mouth?He ate his pizza before it was cool.
What did the janitor say when he jumped out of the closet?SUPPLIES!!!!
Have you heard about the band 1023MB?It's probably because they haven't got a gig yet…
Why does the golfer wear two pants?Because he's afraid he might get a "Hole-in-one."
Why should you wear glasses to maths class?Because it helps with division.
Why does it take pirates so long to learn the alphabet?Because they could spend years at C.
Why did the woman go on the date with the mushroom?Because he was a fun-ghi.
Why do bananas never get lonely?Because they hang out in bunches.
What did the buffalo say when his kid went to college?Bison.
Why shouldn't you tell secrets in a cornfield?Too many ears.
What do you call someone who doesn't like carbs?Lack-Toast Intolerant.
Why did the can crusher quit his job?Because it was soda pressing.
Why did the birthday boy wrap himself in paper?He wanted to live in the present.
What does a house wear?A dress.
Why couldn't the toilet paper cross the road?Because it got stuck in a crack.
Why didn't the bike want to go anywhere?Because it was two-tired!
Want to hear a pizza joke?Nahhh, it's too cheesy!
Why are chemists great at solving problems?Because they have all of the solutions!
Why is it impossible to starve in the desert?Because of all the sand which is there!
What did the cheese say when it looked in the mirror?Halloumi!
Why did the developer go broke?Because he used up all his cache.
Did you know that ants are the only animals that don't get sick?It's true! It's because they have little antibodies.
Why did the donut go to the dentist?To get a filling.
What do you call a bear with no teeth?A gummy bear!
What does a vegan zombie like to eat?Graaains.
What do you call a dinosaur with only one eye?A Do-you-think-he-saw-us!
Why should you never fall in love with a tennis player?Because to them... love means NOTHING!
What did the full glass say to the empty glass?You look drunk.
What's a potato's favorite form of transportation?The gravy train
What did one ocean say to the other?Nothing, they just waved.
What did the right eye say to the left eye?Honestly, between you and me something smells.
What do you call a dog that's been run over by a steamroller?Spot!
What's the difference between a hippo and a zippo?One's pretty heavy and the other's a little lighter
Why don't scientists trust Atoms?They make up everything."""
        
        jokes = [line.strip() for line in joke_content.split('\n') if line.strip()]
        return jokes
    
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        # Title
        title_label = tk.Label(self.root, text="Alexa Joke Teller", 
                              font=('Arial', 16, 'bold'), bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=10)
        
        # Sound status
        sound_status = tk.Label(self.root, text="Sound Status:\n" + self.sound_status_text,
                               font=('Arial', 8), bg='#f0f0f0', fg='#666666',
                               justify='left')
        sound_status.pack(pady=5)
        
        # Joke display area
        self.joke_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.joke_frame.pack(pady=20, fill='both', expand=True)
        
        # Setup label
        self.setup_label = tk.Label(self.joke_frame, text="Click 'Tell me a Joke' to start!", 
                                   font=('Arial', 12), bg='#f0f0f0', fg='#555555',
                                   wraplength=400, justify='center')
        self.setup_label.pack(pady=10)
        
        # Punchline label
        self.punchline_label = tk.Label(self.joke_frame, text="", 
                                       font=('Arial', 12, 'italic'), bg='#f0f0f0', 
                                       fg='#FF6600', wraplength=400, justify='center')
        self.punchline_label.pack(pady=10)
        
        # Button frame
        self.button_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.button_frame.pack(pady=20)
        
        # Tell Joke button
        self.tell_joke_btn = tk.Button(self.button_frame, text="Alexa tell me a Joke", 
                                      command=self.tell_joke, font=('Arial', 10),
                                      bg='#4CAF50', fg='white', padx=20, pady=8)
        self.tell_joke_btn.grid(row=0, column=0, padx=5, pady=5)
        
        # Show Punchline button
        self.punchline_btn = tk.Button(self.button_frame, text="Show Punchline", 
                                      command=self.show_punchline, font=('Arial', 10),
                                      bg='#2196F3', fg='white', padx=20, pady=8,
                                      state='disabled')
        self.punchline_btn.grid(row=0, column=1, padx=5, pady=5)
        
        # Next Joke button
        self.next_joke_btn = tk.Button(self.button_frame, text="Next Joke", 
                                      command=self.next_joke, font=('Arial', 10),
                                      bg='#FF9800', fg='white', padx=20, pady=8,
                                      state='disabled')
        self.next_joke_btn.grid(row=0, column=2, padx=5, pady=5)
        
        # Test Sound button
        self.test_sound_btn = tk.Button(self.button_frame, text="Test Sound", 
                                       command=self.test_sound, font=('Arial', 10),
                                       bg='#9C27B0', fg='white', padx=20, pady=8)
        self.test_sound_btn.grid(row=0, column=3, padx=5, pady=5)
        
        # Quit button
        self.quit_btn = tk.Button(self.button_frame, text="Quit", 
                                 command=self.quit_app, font=('Arial', 10),
                                 bg='#f44336', fg='white', padx=20, pady=8)
        self.quit_btn.grid(row=0, column=4, padx=5, pady=5)
        
        # Status label
        self.status_label = tk.Label(self.root, text=f"Loaded {len(self.jokes)} jokes", 
                                    font=('Arial', 8), bg='#f0f0f0', fg='#888888')
        self.status_label.pack(side='bottom', pady=5)
    
    def parse_joke(self, joke_line):
        """Parse a joke line into setup and punchline"""
        separators = ['?', '|', '-']
        
        for separator in separators:
            if separator in joke_line:
                parts = joke_line.split(separator, 1)
                if len(parts) == 2:
                    setup = parts[0].strip()
                    punchline = parts[1].strip()
                    if separator == '?' and not setup.endswith('?'):
                        setup += '?'
                    return setup, punchline
        
        return joke_line, "That's the joke!"
    
    def tell_joke(self):
        """Tell a random joke"""
        if not self.jokes:
            messagebox.showwarning("No Jokes", "No jokes available!")
            return
        
        pygame.mixer.stop()

        # Play joke start sound if loaded
        if self.sounds['joke_start']:
            self.sounds['joke_start'].play()
        
        # Select random joke
        joke_line = random.choice(self.jokes)
        self.current_joke = self.parse_joke(joke_line)
        
        # Display setup
        self.setup_label.config(text=self.current_joke[0], fg='#333333')
        self.punchline_label.config(text="")
        
        # Enable/disable buttons
        self.punchline_btn.config(state='normal')
        self.next_joke_btn.config(state='normal')
        self.tell_joke_btn.config(state='disabled')
    
    def show_punchline(self):
        """Show the punchline of the current joke"""
        if self.current_joke:
            # Play drum roll before punchline if loaded
            if self.sounds['drum_roll']:
                self.sounds['drum_roll'].play()
            
            # Display punchline after a short delay
            self.root.after(1500, self._display_punchline)
    
    def _display_punchline(self):
        """Actually display the punchline (called after delay)"""
        self.punchline_label.config(text=self.current_joke[1], fg='#FF6600')
        self.punchline_btn.config(state='disabled')
        
        # Play laughter or punchline sound after displaying
        if self.sounds['laughter']:
            self.sounds['laughter'].play()
        elif self.sounds['punchline']:
            self.sounds['punchline'].play()
    
    def test_sound(self):
        """Test the custom sound"""
        if self.sounds['custom']:
            self.sounds['custom'].play()
        else:
            messagebox.showinfo("Test Sound", "No custom sound loaded or file not found.")
    
    def next_joke(self):
        """Get the next random joke"""
        self.tell_joke()
    
    def quit_app(self):
        """Quit the application"""
        pygame.mixer.stop()
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = JokeTellingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()