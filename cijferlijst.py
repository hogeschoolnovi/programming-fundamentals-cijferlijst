import random


def read_scores(file_name):
    scores = {}
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            vak = parts[0]
            score = float(parts[1])
            if vak in scores:
                scores[vak].append(score)
            else:
                scores[vak] = [score]
    return scores

def genereer_cijfers(file_name):
    with open(file_name, "w") as file:
        for i in range(10):
            file.write(f"wiskunde,{random.randint(1, 10)}\n")
            file.write(f"nederlands,{random.randint(1, 10)}\n")
            file.write(f"engels,{random.randint(1, 10)}\n")
    file.close()


def print_statestieken(scores):
    print("Statistieken per vak:")
    for vak, scores_list in scores.items():
        gemiddelde = sum(scores_list) / len(scores_list)
        hoogste_score = max(scores_list)
        laagste_score = min(scores_list)
        print(f"Vak: {vak}, Gemiddelde score: {gemiddelde}, Hoogste score: {hoogste_score}, Laagste score: {laagste_score}")


def main():

    file_name = "cijferlijst.txt"
    genereer_cijfers(file_name)
    scores = read_scores(file_name)
    print_statestieken(scores)


if __name__ == "__main__":
    main()
