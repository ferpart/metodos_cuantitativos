""" module containing the markov chains for the homework """

from pathlib import Path
from datascience import Table
from playsound import playsound
import numpy as np

class MarkovChains():
    """ class for using the markov chains """

    def __init__(self, num_notes=20, starting_note="0"):
        """ __init__ """
        self.res_path = str(Path("components/res/"))
        self.data_table = Table.read_table(self.res_path + "/probability_table.csv")
        self.notes = self.data_table.column("octave")
        self.num_notes = num_notes
        self.starting_note = starting_note

    def element_selector(self):
        """ method for selecting elements """
        actual_note = self.notes[self.starting_note]
        note_list = np.array([actual_note])

        for _ in range(self.num_notes):
            change = np.random.choice(self.notes, p=self.data_table.column(actual_note))
            note_list = np.append(note_list, change)
        return note_list

    def sound_player(self, notes):
        """ method used to play sounds according to the a list of notes """
        for i in notes:
            print("Note played: %s" % i)
            playsound(self.res_path + "/%s.mp3" % i)

    def display(self):
        """ method used to display the notes played and play said notes """
        note_list = self.element_selector()
        self.sound_player(note_list)
        print("Complete array of notes played: %s" % str(note_list))
