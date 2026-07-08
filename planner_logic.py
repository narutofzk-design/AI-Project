"""
Study Planner Logic Module
Generates a study schedule by distributing hours across days.
Uses simple proportional allocation based on number of subjects.
"""

import math


def generate_plan(subjects, total_hours, days):
    """
    Generates a study plan that distributes hours across days and subjects.

    Args:
        subjects (list): List of subject names (e.g., ['Math', 'Science', 'English'])
        total_hours (int): Total study hours available
        days (int): Number of days to spread the study over

    Returns:
        dict: A schedule dictionary with day numbers as keys and
              lists of {subject, hours} dicts as values.
              Example: {1: [{'subject': 'Math', 'hours': 2}, ...], 2: [...]}
    """
    if not subjects or total_hours <= 0 or days <= 0:
        return {}

    num_subjects = len(subjects)

    # Calculate hours per day
    hours_per_day = total_hours / days

    # Calculate hours per subject per day
    # Distribute evenly, with slight variation for realism
    hours_per_subject_per_day = hours_per_day / num_subjects

    # Build the schedule
    schedule = {}

    for day in range(1, days + 1):
        day_schedule = []
        remaining_hours = hours_per_day

        for i, subject in enumerate(subjects):
            if i == len(subjects) - 1:
                # Last subject gets whatever remains (avoids rounding errors)
                subject_hours = round(remaining_hours, 1)
            else:
                # Allocate proportional hours
                subject_hours = round(hours_per_subject_per_day, 1)
                # Add slight variation based on day number to make schedule interesting
                # Only apply variation if there's enough room (at least 1.5 hrs per subject)
                if hours_per_subject_per_day >= 1.5:
                    if day % 2 == 0 and i % 2 == 0:
                        subject_hours = round(subject_hours + 0.5, 1)
                    elif day % 2 == 0 and i % 2 != 0:
                        subject_hours = round(subject_hours - 0.5, 1)

            # Make sure hours don't go below 0.5
            subject_hours = max(0.5, subject_hours)

            remaining_hours -= subject_hours

            # Generate a suggested time block
            start_hour = 9 + sum(item['hours'] for item in day_schedule)
            end_hour = start_hour + subject_hours

            day_schedule.append({
                'subject': subject,
                'hours': subject_hours,
                'time_block': f"{format_time(start_hour)} - {format_time(end_hour)}"
            })

        schedule[day] = day_schedule

    return schedule


def format_time(hour_float):
    """
    Converts a decimal hour to a readable time string.

    Args:
        hour_float (float): Hour as decimal (e.g., 9.5 = 9:30 AM)

    Returns:
        str: Formatted time string (e.g., "9:30 AM")
    """
    hour = int(hour_float)
    minutes = int((hour_float - hour) * 60)

    if hour >= 12:
        period = "PM"
        if hour > 12:
            hour -= 12
    else:
        period = "AM"

    if hour == 0:
        hour = 12

    return f"{hour}:{minutes:02d} {period}"
