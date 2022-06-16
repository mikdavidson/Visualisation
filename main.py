import pickle
import numpy as np
import pandas as pd


def initialiseAdj(array, df):
    k = 0
    for i in array:
        max = np.abs(i).max()
        if str(np.where(array == max)[0]) == '[]':
            coords = np.where(array == (max * -1))

            target = int(str(coords[1]).replace('[', '').replace(']', ''))
        else:
            coords = np.where(array == max)
            target = int(str(coords[1]).replace('[', '').replace(']', ''))
        dict = {'Node': k,
                'Target': int(target),
                'Weight': max}
        df = df.append(dict, ignore_index=True)
        k += 1

    return df


if __name__ == "__main__":

    for i in range(27):
        outFile = 'WGN/Graph Files/graph_' + str(i) + '.csv'
        dataFrame = pd.DataFrame(columns=['Node', 'Target', 'Weight'])
        file = 'WGN/Matrices/adjacency_matrix_' + str(i) + '.csv'
        with open(file, 'rb') as f:
            data = pickle.load(f)

        print(data)
        # data = pd.read_csv(file)
        # data = data.drop(['Unnamed: 0'], axis=1)
        adp = np.array(data)
        # adp = adp * (1 / np.max(adp))
        dataFrame = initialiseAdj(adp, dataFrame)
        coordinateFrame = pd.read_csv('SARIMAmap.csv')
        lat_col = coordinateFrame[['Latitude']]
        long_col = coordinateFrame[['Longitude']]

        df = pd.concat([dataFrame, lat_col, long_col], axis=1)
        df['Node'] = df['Node'].astype('int')
        df['Target'] = df['Target'].astype('int')
        df.to_csv(outFile)
