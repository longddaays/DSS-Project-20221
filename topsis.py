import pandas as pd
import os
import sys
import csv
myData = []
hashDishCategory = {} # category, listRestaurant
listAllCategory = []



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
            print("ERROR : Dữ liệu có ít hơn 3 cột thuộc tính")
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
                "ERROR : Số trọng số, số dấu thuộc tính và số cột thuộc tính khác nhau")
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
    
def main2():
    while True:
        string = input("Enter a positive number: ")
        print(string)
        if string in "nướng":
            print("true")
        else:
            print("false")
        if string == "out":
            break

def readData():
    with open('data_test.csv',encoding="utf8") as file:
        myFile = csv.reader(file)
        for row in myFile:
            myData.append(row)
    myData.pop(0)

def readListCategory():
    for dataRestaurant in myData:
        listCategory = dataRestaurant[7].split(", ")
        # print(str(listCategory))
        for category in listCategory:
            if category.lower() in hashDishCategory.keys():
                listRestaurant = hashDishCategory[category.lower()]
                listRestaurant.append(dataRestaurant[0])
            else:
                listRestaurant = [dataRestaurant[0]]
                hashDishCategory[category.lower()] = listRestaurant
                listAllCategory.append(category.lower())

def startRecommend():
     while True:
        categoryInput = input("Nhập tên món ăn bạn muốn tìm : (Hoặc ""end"")")
        
        if categoryInput.lower() == "end":
            return
        categoryInput = categoryInput.lower()
        listRecRestaurant = None

        if categoryInput in listAllCategory:
            listRecRestaurant = processRecommend(hashDishCategory[categoryInput])
        
        if (listRecRestaurant == None):
            #lay danh sach category goi y
            listRecCategory = []
            for category in listAllCategory:
                if categoryInput in category:
                    listRecCategory.append(category)

            if len(listRecCategory) == 0:
                print("Tên món không phù hợp!!")

            print("Gợi ý tên món : " + str(listRecCategory))
            isContinue = input("Bạn có muốn nhập lại tên món theo gợi ý? (Yes / No)")

            if (isContinue.lower() != "yes"):
                listIdRestaurant = []
                for category in listRecCategory:
                    # isDuplicated = False
                    # for id in listIdRestaurant:
                    #     if id == hashDishCategory[category]:
                    #         isDuplicated = True
                    # if isDuplicated:
                    #     continue
                    listIdRestaurant += hashDishCategory[category]
                listIdRestaurant = list(set(listIdRestaurant))
                listRecRestaurant = processRecommend(listIdRestaurant)

        if listRecRestaurant != None:
            print("Các quán ăn phù hợp là : ")
            for idRes in listRecRestaurant:
                restaurantInfo = myData[int(idRes) - 1]
                print("Tên quán : " + restaurantInfo[1] + ", Địa chỉ : " + restaurantInfo[5])


#input : list id restaurant (string)
#output : list id restaurant (string)
def processRecommend(listIdRestaurant):
    #code here
    #end code here
    return listIdRestaurant


def main3():
    readData()
    readListCategory()
    startRecommend()
if __name__ == "__main__":
    main3()