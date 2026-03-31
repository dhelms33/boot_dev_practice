class Lotr:
    def __init__(self):
        pass
    def calc_total_attack(attack_one, attack_two, attack_three):
        total_attack = attack_one + attack_two + attack_three
        return(total_attack)
    
if __name__ == "__main__":
    obj_instance = Lotr
    result = obj_instance.calc_total_attack(6)
    print(f"Woah that's {result} damage!!!")