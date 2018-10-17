import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Hello world")
    trainingData = pd.read_csv("data/testing.csv", nrows=5)
    print(dir(plt))


if __name__ == "__main__":
    main()
