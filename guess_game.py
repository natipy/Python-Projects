from random import randint
import sys
class HumanGame:
    def __init__(self, max_val):
        self.max = max_val
        self.rand = randint(1, self.max-1)
        print("WELCOME TO GUESS GAME.\nGUESS THE NUMBER BETWEEN 1 and {max}\nGOOD LUCK !!!!".format(max=self.max))
        self.main()
    
    @property
    def on_max_val(self):
        return self.max

    @on_max_val.setter
    def set_max_val(self, val):
        self.max = val
    
    def main(self):
        while True:
            try:
                get = int(input("> "))
                
                if get > self.rand:
                    print("TO HIGH")
                elif get < self.rand:
                    print("TO LOW")
                
                else:
                    print("CONGRA YOU WON!!")
                    get = input("DO YOU WANT TO PLAY AGAIN? [Y/N]: ")
                    if get == "Y":
                        HumanGame(self.max)
                    else:
                        sys.exit()
            except:continue

class ComputerGuess:
    def __init__(self, min_val, max_val, num):
        self.min = min_val
        self.max = max_val
        self.rand = randint(self.min, self.max-1)
        self.user_num = num
        self.main()


    @property
    def on_min_val(self):
        return self.min
    
    @on_min_val.setter
    def set_min_val(self, min):
        self.min = min
    
    @property
    def on_max_val(self):
        return self.max
    
    @on_max_val.setter
    def set_max_val(self, val):
        self.max = val
    
    @property
    def on_update_rand(self):
        return self.rand
    
    @on_update_rand.setter
    def update_rand(self, val:bool=True):
        if val:
            self.rand = randint(self.min, self.max-1)

        
    def main(self):
        print("[H] - High || [L] - Low || [C] - Won")
        get =  ""
        while get != "C":

            get = input("is the number %d ? "%self.rand)
            if get == "H":

                self.set_max_val = self.rand
                self.update_rand = True

            elif get == "L":
                self.set_min_val = self.rand
                self.update_rand = True

            elif get == "C":
                break
        
        print("CONGRA I WON!!") 

ComputerGuess(1, 1000, 145)