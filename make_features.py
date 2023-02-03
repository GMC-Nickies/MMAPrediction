set1 = ['R_odds', 'B_odds', 'R_ev', 'B_ev', 'B_current_lose_streak', 
                'B_current_win_streak','B_draw', 'B_avg_SIG_STR_landed', 'B_avg_SUB_ATT', 
                'B_avg_TD_landed', 'B_avg_TD_pct', 'B_longest_win_streak', 'B_losses',
                'B_total_rounds_fought', 'B_total_title_bouts', 'B_win_by_Decision_Majority', 
                'B_win_by_Decision_Split','B_win_by_Decision_Unanimous', 
                'B_win_by_KO/TKO', 'B_win_by_Submission', 'B_win_by_TKO_Doctor_Stoppage', 
                'B_wins', 'B_Height_cms', 'B_Reach_cms', 'B_Weight_lbs', 'B_age',
                'b_sub_odds', 'b_dec_odds', 'b_ko_odds',
                'R_current_lose_streak', 
                'R_current_win_streak','R_draw', 'R_avg_SIG_STR_landed', 'R_avg_SUR_ATT', 
                'R_avg_TD_landed', 'R_avg_TD_pct', 'R_longest_win_streak', 'R_losses',
                'R_total_rounds_fought', 'R_total_title_bouts', 'R_win_by_Decision_Majority', 
                'R_win_by_Decision_Split','R_win_by_Decision_Unanimous', 
                'R_win_by_KO/TKO', 'R_win_by_Submission', 'R_win_by_TKO_Doctor_Stoppage', 
                'R_wins', 'R_Height_cms', 'R_Reach_cms', 'R_Weight_lRs', 'R_age',
                'r_sub_odds', 'r_dec_odds', 'r_ko_odds']

set2 = []
for x in set1:
    str1 = x + " = tf.feature_column.numeric_column('" + x + "')" + "\n"
    set2.append(str1)
with open('features.txt', 'w') as f:
    f.writelines(set2)
set3 = []
with open('features1.txt') as f:
    lines = f.readlines()
"""
for x in lines:
    y = x.split("=")
    this_str = "'" + y[0].strip() + "',\n"
    if this_str == (",\n"):
        continue
    else:
        set3.append(this_str)
"""
counter = 0
test = [1,1,1,1,45,51,29,34,2,5,18,13,12,21,39,7,8,9,28,22,40,10,55,25
,56,49,47,48,17,23,50,46,65,27,54,11,42,57,16,61,19,37,1,58,31,53,14,33
,3,4,41,6,1,63,44,32,67,38,59,62,15,52,30,1,24,26,20,1,60,64,35,43
,66,36]
print(len(test))
print(len(lines))
for x in lines:
    if test[counter] < 5:
        this_str = x + "\n"
        set3.append(this_str)
    else:
        this_str = "#" + x + "\n"
        set3.append(this_str)
    counter += 1
with open('features_names.txt', 'w') as f:
    f.writelines(set3)


