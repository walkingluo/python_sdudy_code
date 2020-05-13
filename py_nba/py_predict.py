# -*- coding:utf-8 -*-

import pandas as pd
import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

base_elo = 1600
team_elos = {}

def init_data(Mstat, Ostat, Tstat):
    new_Mstat = Mstat.drop(['Rk', 'Arena'], axis=1)
    new_Ostat = Ostat.drop(['Rk', 'G', 'MP'], axis=1)
    new_Tstat = Tstat.drop(['Rk', 'G', 'MP'], axis=1)

    team_stats1 = pd.merge(new_Mstat, new_Ostat, how='left', on='Team')
    team_stats1 = pd.merge(team_stats1, new_Tstat, how='left', on='Team')
    return team_stats1.set_index('Team', inplace=False, drop=True)


def get_elo(team):
    try:
        return team_elos[team]
    except:
        team_elos[team] = base_elo
        return team_elos[team]


def calc_elo(win_team, lose_team):
    winner_rank = get_elo(win_team)
    loser_rank = get_elo(lose_team)

    rank_diff = winner_rank - loser_rank
    exp = (rank_diff * -1) / 400
    odds = 1 / (1 + math.pow(10, exp))

    if winner_rank <= 2100:
        k = 32
    elif winner_rank > 2100 and winner_rank < 2400:
        k = 24
    else:
        k = 16

    new_winner_rank = round(winner_rank + (k * (1- odds)))
    new_loser_rank = round(loser_rank + (k * (0 - odds)))

    return new_winner_rank, new_loser_rank


def build_dataSet(data):
    print("Building data set...")
    X = []
    y = []
    for _, row in data.iterrows():
        Wteam = row['WTeam']
        Lteam = row['LTeam']

        team1_elo = get_elo(Wteam)
        team2_elo = get_elo(Lteam)
        # Add 100 to Host team
        if row['WLoc'] == 'H':
            team1_elo += 100
        else:
            team2_elo += 100

        team1_features = [team1_elo]
        team2_features = [team2_elo]

        for _, value in team_stats.loc[Wteam].iteritems():
            team1_features.append(value)
        for _, value in team_stats.loc[Lteam].iteritems():
            team2_features.append(value)

        if random.random() > 0.5:
            X.append(team1_features + team2_features)
            y.append(0)
        else:
            X.append(team2_features + team1_features)
            y.append(1)

        #update elos
        new_winner_rank, new_loser_rank = calc_elo(Wteam, Lteam)
        team_elos[Wteam] = new_winner_rank
        team_elos[Lteam] = new_loser_rank

    return np.nan_to_num(X), y


def predict_winner(team1, team2, model):
    features = []

    features.append(get_elo(team1))
    for _, value in team_stats.loc[team1].iteritems():
        features.append(value)

    features.append(get_elo(team2) + 100)
    for _, value in team_stats.loc[team2].iteritems():
        features.append(value)

    features = np.nan_to_num(features)

    return model.predict_proba([features])


def predict_1617(data, model):
    result = []

    for _, row in data.iterrows():
        team1 = row['Vteam']
        team2 = row['Hteam']
        pred = predict_winner(team1, team2, model)
        prob = pred[0][0]

        if prob > 0.5:
            winner = team1
            loser = team2
            result.append([winner, loser, prob])
        else:
            winner = team2
            loser = team1
            result.append([winner, loser, 1 - prob])

    return result


if __name__ == '__main__':

    Mstat = pd.read_csv('data/15-16Miscellaneous_Stat.csv')
    Ostat = pd.read_csv('data/15-16Opponent_Per_Game_Stat.csv')
    Tstat = pd.read_csv('data/15-16Team_Per_Game_Stat.csv')

    team_stats = init_data(Mstat, Ostat, Tstat)
    '''
    print(len(team_stats))
    print(len(team_stats.loc['Golden State Warriors']))
    '''
    result_data = pd.read_csv('data/2015-2016_result.csv')
    X, y = build_dataSet(result_data)

    print("Fitting on %d game samples..." % len(X))

    model = linear_model.LogisticRegression()
    model.fit(X, y)

    print("Doing cross-validdation...")
    accuracy = cross_val_score(model, X, y, cv=10, scoring='accuracy', n_jobs=-1).mean()
    print(accuracy)

    print("Predicting on new schedule...")

    schedule1617 = pd.read_csv('data/16-17Schedule.csv')
    result = predict_1617(schedule1617, model)

    with open('16-17result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['win', 'lose', 'probability'])
        writer.writerows(result)
        print('done...')
