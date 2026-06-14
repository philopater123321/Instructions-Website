import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r"events.xlsx")


topic_popularity = df.groupby('topic')['attendance'].sum()
topic_popularity = topic_popularity.sort_values(ascending= False)
print('\n Total Attendance By Topic')
print(topic_popularity)
plt.figure(figsize=(10, 6))
plt.bar(topic_popularity.index, topic_popularity.values, color=['#4C72B0', '#DD8452', '#55A868', '#C44E52'])
plt.title('1: Topics Popularity by attendance')
plt.xlabel('Topics')
plt.ylabel('attendance')
plt.show()
print('--------------------------------------------------------------')

events_popularity = df.groupby('event_type')['attendance'].sum()
events_popularity = events_popularity.sort_values(ascending= False)
print('\nMost event type popular:')
print(events_popularity)
plt.figure(figsize = (10,6))
plt.bar(events_popularity.index, events_popularity.values, color = ['#4C72B0', '#DD8452', '#55A868'])
plt.title('2: Event type popularity by attendance:')
plt.xlabel('Event type name')
plt.ylabel('Attendance')
plt.show()

print('--------------------------------------------------------------')

feedback_average = df.groupby('event_type')['feedback_rating'].mean()
feedback_average = feedback_average.sort_values(ascending= False)
print('\nThe most rated event type')
print(feedback_average)
df['date']= pd.to_datetime(df['date'])

plt.figure(figsize= (10,6))
plt.bar(feedback_average.index, feedback_average.values, color = ['#4C72B0', '#DD8452', '#55A868'])
plt.title('3: Feedback averages for each event type:')
plt.xlabel('Event name')
plt.ylabel('Feedback rating')
plt.show()
for event in df['event_type'].unique():
    event_data = df[df['event_type'] == event]
    plt.plot(event_data['date'], event_data['feedback_rating'], marker = 'o', label = event)
plt.title('Feedback ratings by passing time')
plt.xlabel('Date')
plt.ylabel('feedback Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

print('--------------------------------------------------------------')

topic_stats = df.groupby('topic')[['difficulty', 'feedback_rating']].mean()
topic_stats = topic_stats.sort_values(by= 'difficulty', ascending= False)
print('\n Topic difficulty VS its rating')
print(topic_stats) 

plt.figure(figsize = (10,6))

plt.scatter(df['difficulty'], df['feedback_rating'], alpha = 0.5, color = 'purple')
plt.title('4: Topics difficulty VS its ratings')
plt.xlabel('difficulty from 1 to 5')
plt.ylabel('ratings out of 5')
plt.show()

plt.figure(figsize = (12,6))
for topic in df['topic'].unique():
    topic_data = df[df['topic'] == topic]
    plt.plot(topic_data['date'], topic_data['feedback_rating'], marker = 'o', label = topic)

plt.title('4: Topics ratings over time')
plt.xlabel('Date')
plt.ylabel('Feedback rating')
plt.legend()
plt.show()


print('--------------------------------------------------------------')

duration_stats = df.groupby('duration_hours')['attendance'].mean()
duration_stats = duration_stats.sort_values(ascending = False)
print('\n 6: Average attendance according to duration status')
print(duration_stats)

plt.figure(figsize = (10,6))

plt.scatter(df['duration_hours'], df['attendance'], color = 'purple', alpha = 0.5)

plt.title('6: Attraction of students compared to the duration time')
plt.xlabel('Duration hours')
plt.ylabel('Attendance')
plt.tight_layout()
plt.show()

print('--------------------------------------------------------------')

most_popular = df.groupby('topic')['attendance'].sum()
most_popular = most_popular.sort_values(ascending = False)
print('\nThe most popular topics by attendance')
print(most_popular)
most_topic = most_popular.index[0]
attendance_no = most_popular.values[0]
print(f'The most popular topic is: {most_topic}, with number of attendees of: {attendance_no}')

print('--------------------------------------------------------------')

most_rated = df.groupby('topic')['feedback_rating'].mean()
most_rated = most_rated.sort_values(ascending=False)
print('\nThe most rated topics descendingly')
print(most_rated)
most_topic = most_rated.index[0]
most_rate = most_rated.values[0]
print(f'The most rated topic is {most_topic}, with average feedback rating of {most_rate}')

print('--------------------------------------------------------------')

df['efficiency'] = df['attendance'] / df['duration_hours']

topic_efficiency = df.groupby('topic')['efficiency'].mean()
topic_efficiency = topic_efficiency.sort_values(ascending = False)

print("\nEach topic's attendance and duration")
print(topic_efficiency)

plt.figure(figsize =(10,6))
plt.bar(topic_efficiency.index, topic_efficiency.values, color = 'blue')
plt.title('Efficiency or Attendance per Hour')
plt.xlabel('Topic name')
plt.ylabel('efficieny or attendance per duration in hours')
plt.show()



