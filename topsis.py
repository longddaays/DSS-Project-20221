import pandas as pd
import os
import sys



def main():
    
    
    if len(sys.argv) != 5:
        print("ERROR : Nhập thiếu tham số")
        print("Cú pháp : python topsis.py inputfile.csv '1,1,1,1' '+,+,-,+' result.csv ")
        exit(1)

    
    elif not os.path.isfile(sys.argv[1]):
        print(f"ERROR : {sys.argv[1]} không tồn tại!!")
        exit(1)

    
    elif ".csv" != (os.path.splitext(sys.argv[1]))[1]:
        print(f"ERROR : {sys.argv[1]} không phải là file csv!!")
        exit(1)

    else:
        dataset, temp_dataset = pd.read_csv(
            sys.argv[1]), pd.read_csv(sys.argv[1])
        nCol = len(temp_dataset.columns.values)

        
        if nCol < 3:
            print("ERROR : Dữ liệu có ít hơn 3 cột")
            exit(1)

        
        for i in range(1, nCol):
            pd.to_numeric(dataset.iloc[:, i], errors='coerce')
            dataset.iloc[:, i].fillna(
                (dataset.iloc[:, i].mean()), inplace=True)

        
        try:
            weights = [int(i) for i in sys.argv[2].split(',')]
        except:
            print("ERROR : Kiểm tra lại trọng số")
            exit(1)
        impact = sys.argv[3].split(',')
        for i in impact:
            if not (i == '+' or i == '-'):
                print("ERROR : Kiếm tra lại dấu thuộc tính")
                exit(1)

        
        if nCol != len(weights)+1 or nCol != len(impact)+1:
            print(
                "ERROR : Số trọng số, số dấu thuộc tính và số cột khác nhau")
            exit(1)

        if (".csv" != (os.path.splitext(sys.argv[4]))[1]):
            print("ERROR : Sai định dạng đầu ra")
            exit(1)
        if os.path.isfile(sys.argv[4]):
            os.remove(sys.argv[4])
        
        topsis_pipy(temp_dataset, dataset, nCol, weights, impact)


def Normalize(temp_dataset, nCol, weights):
    
    
    for i in range(1, nCol):
        temp = 0
        for j in range(len(temp_dataset)):
            temp = temp + temp_dataset.iloc[j, i]**2
        temp = temp**0.5
        for j in range(len(temp_dataset)):
            temp_dataset.iat[j, i] = (
                temp_dataset.iloc[j, i] / temp)*weights[i-1]
    return temp_dataset


def Calc_Values(temp_dataset, nCol, impact):
    
    p_sln = (temp_dataset.max().values)[1:]
    n_sln = (temp_dataset.min().values)[1:]
    for i in range(1, nCol):
        if impact[i-1] == '-':
            p_sln[i-1], n_sln[i-1] = n_sln[i-1], p_sln[i-1]
    return p_sln, n_sln


def topsis_pipy(temp_dataset, dataset, nCol, weights, impact):
    
    temp_dataset = Normalize(temp_dataset, nCol, weights)

    
    p_sln, n_sln = Calc_Values(temp_dataset, nCol, impact)

    
    
    score = []
    for i in range(len(temp_dataset)):
        temp_p, temp_n = 0, 0
        for j in range(1, nCol):
            temp_p = temp_p + (p_sln[j-1] - temp_dataset.iloc[i, j])**2
            temp_n = temp_n + (n_sln[j-1] - temp_dataset.iloc[i, j])**2
        temp_p, temp_n = temp_p**0.5, temp_n**0.5
        score.append(temp_n/(temp_p + temp_n))
    dataset['topsis_score'] = score

    
    dataset['rank'] = (dataset['topsis_score'].rank(
        method='max', ascending=False))
    dataset = dataset.astype({"rank": int})

    
    
    dataset.to_csv(sys.argv[4], index=False)
    


if __name__ == "__main__":
    main()