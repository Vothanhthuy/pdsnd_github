import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, Washington\n").lower()
        cities= ['chicago','new york city','washington']
        if city in cities:
            break
        else:
            print("Invalid input. Please try again")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Would you like to explore the data for month? (January, February, March, April, May, June, All\n)").lower()
        months = ['january','february','march','april','june','may','all']
        if month in months:
            break
        else:
            print("Invalid input. Please try again")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to explore for day? (all, monday,tuesday,etc,)\n").lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday','all']
        if day in days:
            break
        else:
            print("Invalid input. Please try again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) #load data file to dataframe
    df["Start Time"] = pd.to_datetime(df["Start Time"]) #convert start time to datetime
    df["month"] = df["Start Time"].dt.month_name() #create column month 
    df["day"] = df["Start Time"].dt.day_name() #create column name
    if month != "all":
        df = df[df["month"].str.startswith(month.title())] #filter by month 
    if day != "all":
        df = df[df["day"].str.startswith(day.title())] #filter by day

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    print(f"The most common month is {common_month}")

    # display the most common day of week
    common_day = df["day"].mode()[0]
    print(f"The most commond day is {common_day}")

    # display the most common start hour
    df["Start_hour"] = df["Start Time"].dt.hour
    common_hour = df["Start_hour"].mode()[0]
    print(f"The most common start hour is {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f"The most commonly used start station is {common_start_station}")

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f"The most commonly used end station {common_end_station}")

    # display most frequent combination of start station and end station trip
    df["Start To End"] = df["Start Station"].str.cat(df["End Station"],sep="to")
    combine = df["Start To End"].mode()[0]
    print(f"The most frequent combination of start station and end station trip {combine}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum() # this number is total of mins and seconds
    min , sec = divmod(total_travel_time,60) # time in minutes and seconds
    hrs , min = divmod(min , 60) # time in hour and minute
    print(f"The total travel time is {hrs} hour(s) , {min} minute(s) and {sec} second(s)")

    # display mean travel time
    mean_travel_time = round(df["Trip Duration"].mean())
    minute , second = divmod(mean_travel_time, 60)
    hour , minute = divmod(minute, 60)
    print(f"The average travel time is {hour} hour(s), {minute} minute(s) and {second} second(s)")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_subscriber = df["User Type"].value_counts()["Subscriber"] 
    count_customer = df["User Type"].value_counts()["Customer"]
    print(f"Subscribers : {count_subscriber} , Customer : {count_customer}")

    # Display counts of gender
    try:
        count_gender_male = df["Gender"].value_counts()["Male"]
        count_gender_female = df["Gender"].value_counts()["Female"]
        print(f"There are {count_gender_male} male and {count_gender_female} female users ")
    except:
        print("There is no data for Gender")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df["Birth Year"].min()
        most_reccent_birth = df["Birth Year"].max()
        most_common = df["Birth Year"].mode()[0]
        print(f"The earliest year of birth is {earliest_birth}\nThe most recent year of birth is {most_reccent_birth}\nThe most common year of birth is {most_common}")
    except:
        print("There is no data for Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Display draw data for user to view
def display_data(df):
    while True:
        choices = ["yes", "no"]
        choice_1 = input("Do you wish to view draw data (5 rows)? Type 'yes' or 'no'").lower()
        if choice_1 in choices:
            if choice_1 == "yes":
                start = 0
                end = 5
                data = df.iloc[start : end]
                print(data)
            break
        else:
            print("Invalid input. Please try again 😇")

    if choice_1 == "yes":
        while True:
            choice_2 = input("Do you wish to view more draw data (5 rows)? Type 'yes' or 'no'").lower()
            if choice_2 == "yes":
                start +=5
                end +=5
                data = df.iloc[start : end]
                print(data)
            elif choice_2 == "no":
                break
            else:
                print("Invalid input. Please try again 😇")

#Put all fuction above into main()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
