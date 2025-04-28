  #2.uzd
from skolens.py import  skolens
class Skola:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.skoleni = []
    
    def pievienot_skolenu(self, skolens):
      self.skoleni.append(skolens)
      
      def paradit_visus_skolenus(self):
         for skolens in self.skoleni:
             print(skolens)
             
      def labakais(self):
          if not self.skoleni:
              return None
          
          labakais_skolens = max(self.skoleni, key=lambda s: s. videja_atzime())
          return labakais_skolens
      
#3.uzd

skola = Skola("Mana skola")
