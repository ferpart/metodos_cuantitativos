""" main module for the generadores_de_melodias homework """
from components import MarkovChains

def main():
    """ main method """
    flag = True
    avaiable_notes = ["c", "d", "e", "f", "g", "a", "b", "c#", "d#", "f#", "g#", "a#"]
    num_notes = int(input("Enter number of notes to be played: "))
    starting_note = input("Enter starting note <%s>: " % str(avaiable_notes).strip("[]"))
    if num_notes < 1:
        print("Please select a number over 1")
        flag = False
    if starting_note not in avaiable_notes:
        print("Please select a real note <%s>" % str(avaiable_notes).strip("[]"))
        flag = False
    if flag:
        starting_note = avaiable_notes.index(starting_note)
        MarkovChains(num_notes=num_notes, starting_note=starting_note).display()

if __name__ == "__main__":
    main()
