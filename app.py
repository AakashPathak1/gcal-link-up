import urllib.parse
from datetime import datetime, timedelta
import pytz

# Set the timezone to PST
timezone = pytz.timezone("America/Los_Angeles")

while True:
    try:
        # Ask user for event details
        event_name = input("Enter the event name: ")

        # Ask user for event start date and time
        event_days_input = input("Enter how many days from today: ")
        event_days = int(event_days_input)
        event_time_input = input("Enter the event start time (HH:MMam/pm): ")
        event_time = datetime.strptime(event_time_input, "%I:%M%p")

        # Calculate event start datetime by adding days and time to today's date
        event_datetime = datetime.now(timezone) + timedelta(days=event_days)
        event_datetime = event_datetime.replace(
            hour=event_time.hour, minute=event_time.minute
        )

        # Ask user for event duration
        event_duration_input = input("Enter the event duration in minutes: ")
        duration = int(event_duration_input)

        # Calculate end datetime by adding duration to start datetime
        end_datetime = event_datetime + timedelta(minutes=duration)

        # Ask user for event location
        location = input("Enter the event location: ")

        # Ask user for attendees' email addresses
        attendees_input = input(
            "Enter the email addresses of attendees (comma-separated): "
        )
        attendees = attendees_input.split(",")

        # Create dictionary of URL parameters
        parameters = {
            "action": "TEMPLATE",
            "text": event_name,
            "dates": event_datetime.strftime("%Y%m%dT%H%M%S")
            + "/"
            + end_datetime.strftime("%Y%m%dT%H%M%S"),
            "location": location,
            "add": ",".join(attendees),  # Add attendees to the event
        }

        # Encode the parameters
        encoded_parameters = urllib.parse.urlencode(
            parameters, quote_via=urllib.parse.quote
        )

        # Create Google Calendar link
        link = "https://www.google.com/calendar/render?" + encoded_parameters

        # Print link
        print("\n Here is your Google calendar link:", link, "\n")

        # Exit the loop if all inputs are valid
        break

    except ValueError:
        print("Invalid input. Please try again.")
