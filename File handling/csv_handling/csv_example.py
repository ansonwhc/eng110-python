import csv


def transform_user_details(csv_file_name):
    new_user_data = []

    with open(csv_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data


if __name__ == "__main__":
    print(transform_user_details("user_details.csv"))

