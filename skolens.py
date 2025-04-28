  #1.uzd
class Skolnieks:
    id_counter = 1

    def __init__(self, vards, uzvards, sekmes):
        self.name = vards
        self.surname = uzvards
        self.sekmes = sekmes
        self.id = Skolens.id_counter
        Skolens.id_counter += 1

        def pievienot_jauno_atzime(self, atzime):
            self.sekmes.append(atzime)
            
            def videja_atzime(self):
                if self.sekmes:
                    return sum(self.sekmes) / len(self.sekmes)
                else:
                    return 0
                
                def __str__(self):
                    return f"{self.id} - {self.name} {self.surname} - {self.sekmes}"
            

