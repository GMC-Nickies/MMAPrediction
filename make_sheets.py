import pandas as pd
import csv
import re

fighters = pd.read_csv("fighters_2022_06_16_0.csv")
fighters_1 = pd.read_csv("fighters_2022_06_16_1.csv")

dict_list = []
f1_odds_set = []
f2_odds_set = []
genders_list = []

with open('upcoming_test.txt') as f:
    lines = f.readlines()
    for x in lines:
        this_dict = {}
        x_list = x.split()
        fighter1_name = ""
        f1_name_set = []
        fighter2_name = ""
        f2_name_set = []
        f1_odds = ""
        f2_odds = ""
        got_first = 0
        win = x_list[-2]
        gender = x_list[-1]
        genders_list.append(gender)
        for y in x_list[:-1]:
            if y[0] != 'v' and got_first == 0 and y[0] != '(':
                #print("F1 name: " + y)
                f1_name_set.append(y)
            elif y[0] != 'v' and got_first == 0:
                #print("F1 odds: " + y[1:-1])
                f1_odds = y[1:-1]
                got_first = 1
            elif y[0] != 'v' and got_first == 1 and y[0] != '(' and len(y) != 1:
                #print("F2 name: " + y)
                f2_name_set.append(y)
            elif y[0] != 'v' and len(y) != 1:
                #print("F2 odds: " + y[1:-1])
                f2_odds = y[1:-1]
        fighter1_name = " ".join(f1_name_set)
        fighter2_name = " ".join(f2_name_set)

        f1_odds_set.append(f1_odds)
        f2_odds_set.append(f2_odds)

        this_dict['f1_name'] = fighter1_name
        this_dict['f1_odds'] = f1_odds
        this_dict['f2_name'] = fighter2_name
        this_dict['f2_odds'] = f2_odds
        this_dict['win'] = win
        dict_list.append(this_dict)

print(f1_odds_set)
print(f2_odds_set)

df = pd.DataFrame(
    {
    'Name': "",
    'Height': 0,
    'Weight': 0,
    'Reach': 0,
    'Stance': "",
    'DOB': 0,
    'SLpm': 0,
    'SAcc': 0,
    'SApm': 0,
    'StrDef': 0,    
    'TDAvg': 0,
    'TDAcc': 0, 
    'TDDef': 0,
    'SubAvg': 0,
    'Name_1': "",
    'Height_1': 0,
    'Weight_1': 0,
    'Reach_1': 0,
    'Stance_1': "",
    'DOB_1': 0,
    'SLpm_1': 0,
    'SAcc_1': 0,
    'SApm_1': 0,
    'StrDef_1': 0,  
    'TDAvg_1': 0,
    'TDAcc_1': 0,
    'TDDef_1': 0,
    'SubAvg_1': 0,
    'Win': 0
    },
    index=[0],)

f1_df = pd.DataFrame(
    {
    'Name': "",
    'Height': 0,
    'Weight': 0,
    'Reach': 0,
    'Stance': "",
    'DOB': 0,
    'SLpm': 0,
    'SAcc': 0,
    'SApm': 0,
    'StrDef': 0,    
    'TDAvg': 0,
    'TDAcc': 0, 
    'TDDef': 0,
    'SubAvg': 0,
    },
    index=[0],)

f2_df = pd.DataFrame(
    {
    'Name_1': "",
    'Height_1': 0,
    'Weight_1': 0,
    'Reach_1': 0,
    'Stance_1': "",
    'DOB_1': 0,
    'SLpm_1': 0,
    'SAcc_1': 0,
    'SApm_1': 0,
    'StrDef_1': 0,  
    'TDAvg_1': 0,
    'TDAcc_1': 0,
    'TDDef_1': 0,
    'SubAvg_1': 0
    },
    index=[0],)

win_df = pd.DataFrame(
    {
    'Win': 0
    },
    index=[0],)

def rev_sentence(sentence):
 
    # first split the string into words
    words = sentence.split(' ')
 
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
 
    # finally return the joined string
    return reverse_sentence

counter = 1
for x in dict_list:
    f1_name = x['f1_name']
    f2_name = x['f2_name']
    win = x['win']
    this_f1_df = fighters.loc[(fighters["Name"] == f1_name)]
    if this_f1_df.empty == True:
        f1_name = rev_sentence(f1_name)
        this_f1_df = fighters.loc[(fighters["Name"] == f1_name)]
    this_f2_df = fighters_1.loc[(fighters_1["Name_1"] == f2_name)]
    if this_f2_df.empty == True:
        f2_name = rev_sentence(f2_name)
        this_f2_df = fighters_1.loc[(fighters_1["Name_1"] == f2_name)]

    this_win_df = pd.DataFrame(
        {
            'Win': win
    },
    index=[0],)

    print(this_f1_df)
    print(this_f2_df)
    f1_index = this_f1_df.index[0]
    f2_index = this_f2_df.index[0]
    win_index = this_win_df.index[0]

    this_f1_df = this_f1_df.rename(index = {f1_index: counter})
    this_f2_df = this_f2_df.rename(index = {f2_index: counter})
    this_win_df = this_win_df.rename(index = {win_index: counter})

    f1_height = this_f1_df.at[counter, 'Height']
    w1 = f1_height
    w1 = re.sub("""['"]""", "", w1)
    w2 = w1.split()
    w3 = [int(x) for x in w2]
    w4 = w3[0] * 0.3048 + w3[1] * 0.0254
    w4 = str(w4)
    this_f1_df.at[counter, 'Height'] = w4

    f1_weight = this_f1_df.at[counter, 'Weight']
    h1 = f1_weight.split()
    h1 = str(h1[0])
    this_f1_df.at[counter, 'Weight'] = h1

    f1_reach = this_f1_df.at[counter, 'Reach']
    r1 = f1_reach[:-1]
    this_f1_df.at[counter, 'Reach'] = r1

    f1_DOB = this_f1_df.at[counter, 'DOB']
    dob1 = f1_DOB.split('-')
    dob1 = dob1[-1]
    if int(dob1) < 40:
        dob1 = "20" + dob1
    else:
        dob1 = "19" + dob1
    this_f1_df.at[counter, 'DOB'] = dob1

    f2_height = this_f2_df.at[counter, 'Height_1']
    w1 = f2_height
    w1 = re.sub("""['"]""", "", w1)
    w2 = w1.split()
    w3 = [int(x) for x in w2]
    w4 = w3[0] * 0.3048 + w3[1] * 0.0254
    w4 = str(w4)
    this_f2_df.at[counter, 'Height_1'] = w4

    f2_weight = this_f2_df.at[counter, 'Weight_1']
    h1 = f2_weight.split()
    h1 = str(h1[0])
    this_f2_df.at[counter, 'Weight_1'] = h1

    f2_reach = this_f2_df.at[counter, 'Reach_1']
    r1 = f2_reach[:-1]
    this_f2_df.at[counter, 'Reach_1'] = r1

    f2_DOB = this_f2_df.at[counter, 'DOB_1']
    dob1 = f2_DOB.split('-')
    dob1 = dob1[-1]
    if int(dob1) < 40:
        dob1 = "20" + dob1
    else:
        dob1 = "19" + dob1
    this_f2_df.at[counter, 'DOB_1'] = dob1

    this_f2_df = this_f2_df.join(this_win_df)
    this_slice = this_f1_df.join(this_f2_df)

    df = pd.concat([df, this_slice], ignore_index=True)

    counter += 1

df.to_csv('output_fighters.csv')

counter = 0
predicted_wins = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]
outcomes = [1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0]

performance = []

for x in predicted_wins:
    if x == outcomes[counter]:
        performance.append(1)
    else:
        performance.append(0)
    counter += 1

print(performance)
print(sum(performance) / len(performance))

print(genders_list)

counter = 0
with open('output_bets.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)
    row = ['Outcome', 'Odds', 'Gender']
    # write a row to the csv file
    writer.writerow(row)
    for x in performance:
        if x == 1:
            if predicted_wins[counter] == 1:
                row = [1, f1_odds_set[counter], genders_list[counter]]
            else:
                row = [1, f2_odds_set[counter], genders_list[counter]]
        if x == 0:
            if predicted_wins[counter] == 1:
                row = [0, f1_odds_set[counter], genders_list[counter]]
            else:
                row = [0, f2_odds_set[counter], genders_list[counter]]
        counter += 1
        writer.writerow(row)