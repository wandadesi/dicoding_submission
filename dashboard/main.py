import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title = "Bike Dashboard",
    page_icon = ":bike:",
    layout="wide")

st.title('Bike Data Dashboard')
st.caption('by wanda desi')

def load_data(path: str):
  data = pd.read_csv(path)
  # change dteday to datetime
  data['dteday'] = pd.to_datetime(data['dteday'])
  return data

df = load_data('./data/main_data.csv')

# Select tahun
yr_selection = st.sidebar.selectbox(
    'Select Year:',
    ['2011-2012', '2011', '2012']
)

# Filter
if yr_selection == '2011-2012':
    output = df
elif yr_selection == '2011':
    output = df[df['yr'] == 0]
else:
    output = df[df['yr'] == 1]

#-----USER----#
col1, col2, col3 = st.columns(3)

with col1:
    total_cnt = output['cnt'].sum()
    st.metric("Total Rental", total_cnt)

with col2:
    total_registered = output['registered'].sum()
    st.metric("Registered User", total_registered)

with col3:
    total_casual = output['casual'].sum()
    st.metric("Casual User", total_casual)

style_metric_cards(border_left_color="#F08080")
st.divider()

st.header('Bike Rentals Over Time')

#----DAILY----#
with st.container():
  st.subheader(f"Trend Over Time {yr_selection}")
  plt.figure(figsize=(15,5))
  sns.lineplot(x=output["dteday"].dt.date, y=output["cnt"])
  plt.xlabel("Date")
  plt.ylabel("Total Rentals")
  plt.xticks(rotation=45)
  st.pyplot(plt)

st.divider()

#----HOUR----#
with st.container():
  st.subheader(f'Total Bike Rentals by Time of Day {yr_selection}')
  hourly_counts = output.groupby('hr')['cnt'].sum()
  def time_of_day(hour):
      if hour in [23, 0, 1, 2, 3]:
          return 'midnight'
      elif hour in [4, 5, 6, 7, 8, 9]:
          return 'morning'
      elif hour in [10, 11, 12, 13]:
          return 'afternoon'
      elif hour in [14, 15, 16, 17, 18]:
          return 'evening'
      else:
          return 'night'
  output['time'] = output['hr'].apply(time_of_day)
  time_counts = output.groupby('time')['cnt'].sum().sort_index()
  time_order = ['morning', 'afternoon', 'evening', 'night', 'midnight']
  time_counts = time_counts.reindex(time_order)
  plt.figure(figsize=(10, 6))
  max_time = time_counts.idxmax()
  colors = ['gold' if time == max_time else 'lightgrey' for time in time_order]
  ax = sns.barplot(x=time_counts.index, y=time_counts.values, palette=colors)
  # Set labels and title
  plt.xlabel('Time of Day')
  plt.ylabel('Total Rentals')
  # Format y-axis labels to display actual values (remove scientific notation)
  ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
  # Add legend for time periods
  legend_labels = ['morning (4-9 am)', 'afternoon (10 am - 1 pm)', 'evening (2-5 pm)', 'night (6-9 pm)', 'midnight (10 pm - 3 am)']
  plt.legend(labels=legend_labels, loc='upper left')
  # Display the plot
  plt.tight_layout()
  st.pyplot(plt)

st.divider()

#-----MONTH & WEEKDAY-----#
col1, col2 = st.columns(2)

with col1:
  st.subheader(f'Total Bike Rentals by Month {yr_selection}')
  monthly_counts = output.groupby('mnth')['cnt'].sum()
  plt.figure(figsize=(8, 6))
  sns.lineplot(x=monthly_counts.index, y=monthly_counts.values)
  plt.xlabel('Month')
  plt.ylabel('Total Rentals')
  month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  plt.xticks(ticks=range(1, 13), labels=month_names)
  plt.tight_layout()
  st.pyplot(plt)

with col2:
  st.subheader(f'Total Bike Rentals by Weekday {yr_selection}')
  daily_users = output.groupby('weekday')[['registered', 'casual']].sum().reset_index()
  plt.figure(figsize=(8, 6))
  sns.lineplot(x='weekday', y='registered', data=daily_users, color='skyblue', label='Registered')
  sns.lineplot(x='weekday', y='casual', data=daily_users, color='gold', label='Casual')
  plt.xlabel('Day')
  plt.ylabel('Number of Users')
  plt.xticks(range(7), ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  st.pyplot(plt)

st.divider()


#-----HOLIDAY AND WORKINGDAY-----#
st.header('Holiday vs Workingday')

st.caption(f'Percentage of Bike Rentals {yr_selection}')
holiday_counts = output.groupby('holiday')['cnt'].sum()
colors = ['lightgrey', 'gold']
plt.figure(figsize=(8, 6))
plt.pie(holiday_counts, labels=holiday_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.legend(['Workingday', 'Holiday'], loc='best')
st.pyplot(plt)

with st.container():
  workingday_users = output.groupby('workingday')[['registered', 'casual']].sum()
  fig, axes = plt.subplots(1, 2, figsize=(18, 9))
  axes[0].pie(workingday_users.loc[1], labels=['Registered', 'Casual'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'gold'])
  axes[0].set_title(f'User Types on Working Days {yr_selection}')
  axes[1].pie(workingday_users.loc[0], labels=['Registered', 'Casual'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'gold'])
  axes[1].set_title(f'User Types on Holidays {yr_selection}')
  plt.tight_layout()
  st.pyplot(plt)

st.divider()

st.header('Weather Conditions')

#-----SEASON-----#
with  st.container():
  st.subheader(f'Total Bike Rentals by Season {yr_selection}')
  seasonal_counts = output.groupby('season')['cnt'].sum()
  colors = ['lightgreen', 'gold', 'orange', 'lightblue']
  plt.figure(figsize=(8, 4))
  seasonal_counts.plot(kind='bar', color=colors)
  plt.xlabel('Season')
  plt.ylabel('Total Rental')
  plt.xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)
  plt.tight_layout()
  st.pyplot(plt)

st.divider()

with st.container():
  st.subheader('Environmental Factors to Bike Rentals')
  correlation_matrix = output[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
  mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
  plt.figure(figsize=(10, 8))
  sns.heatmap(correlation_matrix, annot=True, cmap=sns.cubehelix_palette(rot=-.2), fmt=".2f", mask=mask)
  st.pyplot(plt)

with st.container():
  fig, axes = plt.subplots(2, 2, figsize=(12, 8))
  sns.scatterplot(x='temp', y='cnt', data=output, ax=axes[0, 0], color='orange')
  axes[0, 0].set_title('Temperature vs Bike Rentals')
  sns.scatterplot(x='atemp', y='cnt', data=output, ax=axes[0, 1], color='skyblue')
  axes[0, 1].set_title('Feeling Temperature vs Bike Rentals')
  sns.scatterplot(x='hum', y='cnt', data=output, ax=axes[1, 0], color='grey')
  axes[1, 0].set_title('Humidity vs Bike Rentals')
  sns.scatterplot(x='windspeed', y='cnt', data=output, ax=axes[1, 1], color='seagreen')
  axes[1, 1].set_title('Windspeed vs Bike Rentals')
  plt.tight_layout()
  st.pyplot(plt)
