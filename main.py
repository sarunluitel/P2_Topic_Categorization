import pandas as pd


def main():
    print("Hello world")
    trainingData = pd.read_csv("data/testing.csv", nrows=5)
    print(trainingData)


if __name__ == "__main__":
    main()
