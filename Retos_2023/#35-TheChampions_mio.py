"""
    Sorteo de Champions League
    
    Bombos 2023
Bombo 1
Manchester City (ING) Sevilla (ESP) Barcelona (ESP) Nápoles (ITA) Bayern (ALE) PSG (FRA) Benfica (POR) Feyenoord (NED)

Bombo 2
Real Madrid (ESP) Atlético de Madrid (ESP) Manchester United (ING) Inter (ITA) Borussia Dortmund (ALE) RB Leipzig (ALE) Oporto (POR) Arsenal (ING)

Bombo 3
Shakhtar Dontesk (UKR) Red Bull Salzburgo (AUS) Milan (ITA) Braga (POR) Lazio (ITA) Estrella Roja (SER) Copenhague (DEN) PSV (NED)

Bombo 4
Real Sociedad (ESP) Galatasaray (TUR) Amberes (BEL) Young Boys (SUI) Celtic (ESC) Newcastle (ING) Unión Berlín (ALE) Lens (FRA)

***Reglas***
No podrá haber equipos del mismo país en el mismo bombo
Especial, los grupos ABCD podrán tener una pareja del mismo pais, EFGH ocurrirá lo mismo
    
"""
import random


Pot1 = ["Manchester City (ING)", "Sevilla (ESP)", "Barcelona (ESP)", "Nápoles (ITA)" ,
        "Bayern (ALE)", "PSG (FRA)" ,"Benfica (POR)", "Feyenoord (NED)"]
Pot2 = ["Real Madrid (ESP)", "Atlético de Madrid (ESP)", "Manchester United (ING)", 
        "Inter (ITA)", "Borussia Dortmund (ALE)", "RB Leipzig (ALE)", "Oporto (POR)", "Arsenal (ING)"]
Pot3 = ["Shakhtar Dontesk (UKR)", "Red Bull Salzburgo (AUS)", "Milan (ITA)", "Braga (POR)",
        "Lazio (ITA)", "Estrella Roja (SER)", "Copenhague (DEN)", "PSV (NED)"]
Pot4 = ["Real Sociedad (ESP)", "Galatasaray (TUR)", "Amberes (BEL)", "Young Boys (SUI)",
        "Celtic (ESC)", "Newcastle (ING)", "Unión Berlín (ALE)", "Lens (FRA)"]

Groups = ["A","B","C","D","E","F","G","H"]

GroupA = []
GroupB = []
GroupC = []
GroupD = []
GroupE = []
GroupF = []
GroupG = []
GroupH = []

def presentation(list:list):
    for x in range(0,len(list)):
        print (str(x+1)+"."+list[x])


def election (list:list,pot:int):
    
    for x in range(0,len(list)):
        team = random.choice(list)
        list.remove(team)
        country = team[-5:] #obtiene los últimos 5 caracteres de la cadena
        group_Choice(team,pot,country)
    

def group_Choice (team:str,pot:int,country:str):
   
    round = pot -1
    if list(filter(lambda x: country in x, GroupA))==[] and len(GroupA) == round:
        GroupA.insert(round,team)
       
    elif list(filter(lambda x: country in x, GroupB))==[] and len(GroupB) == round:
        GroupB.insert(round,team)
       
    elif list(filter(lambda x: country in x, GroupC))==[] and len(GroupC) == round:
        GroupC.insert(round,team)
        
    elif list(filter(lambda x: country in x, GroupD))==[] and len(GroupD) == round:
        GroupD.insert(round,team)
       
    elif list(filter(lambda x: country in x, GroupE))==[] and len(GroupE) == round:
        GroupE.insert(round,team)
       
    elif list(filter(lambda x: country in x, GroupF))==[] and len(GroupF) == round:
        GroupF.insert(round,team)
       
    elif list(filter(lambda x: country in x, GroupG))==[] and len(GroupG) == round:
        GroupG.insert(round,team)
       
    elif list(filter(lambda x: country in x, GroupH))==[] and len(GroupH) == round:
        GroupH.insert(round,team)
       

    
    

def main():

    print("---- BOMBOS ----")
    print("Bombo 1:")
    presentation(Pot1)
    print("Bombo 2:")
    presentation(Pot2)
    print("Bombo 3:")
    presentation(Pot3)
    print("Bombo 4:")
    presentation(Pot4)
    print("------ SORTEO ------")
    election(Pot1,1)
    election(Pot2,2)
    election(Pot3,3)
    election(Pot4,4)
   
    print("Group A\n")
    presentation(GroupA)
    print("Group B\n")
    presentation(GroupB)
    print("Group C\n")
    presentation(GroupC)
    print("Group D\n")
    presentation(GroupD)
    print("Group E\n")
    presentation(GroupE)
    print("Group F\n")
    presentation(GroupF)
    print("Group G\n")
    presentation(GroupG)
    print("Group H\n")
    presentation(GroupH)
    
   
if __name__ == "__main__":
    main()  