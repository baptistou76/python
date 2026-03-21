import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    The main program opens two csv file, extracts their DataFrame,
    creates and displays a scatter graph to show a correlation between the
    life expectancy and the gross domestic product.
    """
    try:
        income_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_df = load("life_expectancy_years.csv")
        if income_df is None or life_df is None:
            exit()
        year = "1900"
        income_1900 = income_df[["country", year]]
        life_1900 = life_df[["country", year]]
        merged = income_1900.merge(life_1900, on="country",
                                   suffixes=("_income", "_life"))
        x = merged[f"{year}_income"]
        y = merged[f"{year}_life"]
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y)
        plt.title(
            "Correlation between life expectancy and gross "
            "domestic product in year '1900'")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    main()
