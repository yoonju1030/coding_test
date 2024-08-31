#  https://school.programmers.co.kr/learn/courses/30/lessons/42579
import pandas as pd 

def solution(genres, plays):
    df = pd.DataFrame({"genres": genres, "plays": plays})
    inner_rank = df.groupby('genres')['plays'].rank(method='max', ascending=False)
    genres_df = df.groupby('genres').sum().reset_index().rename(columns={'plays': 'total'})
    df = pd.merge(df, genres_df, how='inner', on='genres')
    df['inner_rank'] = list(inner_rank)
    remove_index = df[df['inner_rank'] > 2].index
    df.drop(remove_index, inplace=True)
    ans = list(df.sort_values(by=['total', 'inner_rank'], ascending=[False, True]).index)
    
    return ans

# 프로그래머스의 테스트케이스 입력 시 vscode 에서는 기대값이 제대로 나오는데 프로그래머스에서는 안나오는 이슈 존재