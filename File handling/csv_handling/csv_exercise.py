import csv
from csv_example import transform_user_details


def create_new_user_data_csv(old_user_data_file="user_details.csv",
                             new_file_name="new_user_data.csv"):

    new_user_data = transform_user_details(old_user_data_file)
    new_file = open(new_file_name, 'w')

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


if __name__ == "__main__":
    create_new_user_data_csv()