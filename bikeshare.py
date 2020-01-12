import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington', 'all']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all' ]

USERS = ['subscribers', 'customers', 'dependents']

CUSTOMER_RESPONSE: ['yes', 'no']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter the city with which you would like to go ahead: Chicago, New York City or Washington? \n> ').lower()
        if city not in CITIES:
           print("Invalid data! Please try again.")
           continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month with which you would like to filter: January, February, March, April, May, June or type 'all' if you do not have any preference? \n ").lower()
        if month not in MONTHS:
            print("Invalid data! Please try again.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day with which you would like to filter: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference? \n ").lower()
        if day not in DAYS:
            print("Invalid data! Please try again.")
        else:
            break

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
    # load data file into a dataframe 
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    """The mode of a set of values is the value that appears most often. It can be multiple values. The axis to iterate over while searching for the mode: 0 or 'index' : get mode of each column.
    """
    common_month = df['month'].mode().values[0]
    print('The most common month would be: {}'.format(common_month))
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode().values[0]
    print('The most common day would be: {}'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode().values[0]
    print('The most common hour would be: {}'.format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode().values[0]
    print('The most commonly used start station would be: {}'.format(commonly_used_start_station))

    # TO DO: display most commonly used end station
    commonly_used_end_station = df['End Station'].mode().values[0]
    print('\n The Most commonly used end station would be: {}'.format(commonly_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_start_end_stations'] = df['Start Station'] + '  and  ' +  df['End Station']
    print("\n The most frequest combination of start and end station would be: {}".format(
        df['combination_start_end_stations'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time would be: {}".format(str(total_travel_time)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time would be: {}".format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user = df['User Type'].value_counts()
        print("\nUser Types \n{} users subscribers, customers, or dependents".format(user))
    except:
        print("Sorry! No User Type data available")
        
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nGender Data\n {} ".format(gender))
    except:
        print("Sorry! The gender data is not available.")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = np.int(min(df['Birth Year']))
        print("\nThe earliest year of birth would be {}.".format(earliest_year_of_birth))

        most_recent_year_of_birth = np.int(max(df['Birth Year']))
        print("\nThe most recent year of birth would be {}.".format(most_recent_year_of_birth))

        most_common_year_of_birth = int((df['Birth Year']).mode().values[0])
        print("\nThe most common year of birth would be {}.".format(most_common_year_of_birth))
    except:
        print("\nSorry! The data is not available.")                     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    customer_response = input('Would you like some raw data to be displayed? Yes/No? \n> ').lower()
    if customer_response == 'yes':
        customer_response = True
    elif customer_response == 'no':
        customer_response = False
    else:
        print("Invalid data! Please try again.")
        return
            
    if customer_response:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            customer_response = input('Would you like the next 5 lines of raw data to be displayed? Yes/No ').lower()
            if customer_response=='yes':
                continue
            elif customer_response=='no':
                break
            else:
                print("Invalid data! Please try again.")
                return            
    
    
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
