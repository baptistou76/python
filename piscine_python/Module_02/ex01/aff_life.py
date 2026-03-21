from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Main program that uses the load function from the
    previous exercise to open the life_expectancy.csv file,
    extracts the DataFrame, creates a graph, and use the
    matplotlib to displays it with a title and legends for
    the X and Y axes.
    """
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
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
