from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            exit()
        country = "France"
        country_data = df[df["country"] == country]
        years = df.columns[1:].astype(int)
        values = country_data.iloc[0, 1:]
        plt.plot(years, values)
        plt.title(f"Life expectancy in {country}")
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
