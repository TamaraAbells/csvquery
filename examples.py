import csv_query

def usa_cases_date_range():
    dataset = csv_query.open_csv("example_data/coronavirus_data.csv")
    dataset.index("location", lambda a,b: a<b)
    result = dataset.query({
        "location": {
            csv_query.Operators.equal: "United States"
        },
        "date": {
            csv_query.Operators.greater_than_or_equal: "2020-03-01",
            csv_query.Operators.less_than_or_equal: "2020-03-15",
            csv_query.Operators.comparison: lambda a,b: a<b
        }
    })
    result.print_data()

def more_than_1000_cases_today():
    dataset = csv_query.open_csv("example_data/coronavirus_data.csv")
    result = dataset.query({
        "total_cases": {
            csv_query.Operators.greater_than: 1000,
            csv_query.Operators.comparison: lambda a,b: int(a)<int(b)
        },
        "date": {
            csv_query.Operators.equal: "2020-03-23"
        }
    })
    result.index("total_cases")
    result.print_data()
    return result

def save_more_than_1000_cases_today():
    more_than_1000_cases_today().save_csv("output.csv", ";", ["location","total_cases"])

def print_diversity_info():
    dataset = csv_query.open_csv("example_data/census_diversity.csv", ",")
    dataset.index("totpop10")
    dataset.save_csv(dataset.column_names[2:])

usa_cases_date_range()