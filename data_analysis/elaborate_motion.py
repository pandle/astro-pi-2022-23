import pandas as pd
import os

from datetime import datetime
from math import ceil
from matplotlib import pyplot as plt


def dt_object_from_str(dt_string: str) -> datetime:
    return datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S.%f")

def delta_secs(datetime_after, datetime_before):
    return (datetime_after - datetime_before).total_seconds()

def elaborate_corrected_motion(
        path_to_csv, 
        estimated_value: int = 0, 
        new_csv_folder: str = None, 
        show_seconds: bool = False
    ):
    """
    estimated_value is the value to give to all the estimated measurements
    """
    data = pd.read_csv(path_to_csv)
    time_data = data["date_time"]
    motion_data = data["motion_detected"]

    measurement_dt_list = []
    measurement_time_list = [] # Relative time from start
    START_TIME = dt_object_from_str(time_data[0])

    motion_detected_list = []
    bad_measurement_indices = []

    AVG_TIME_US = 115376 # Measured previously
    motion_detected_list.append(motion_data[0])
    measurement_dt_list.append(0)
    measurement_time_list.append(0)

    # 1. Understand average time took for one measurement
    # 2. Understand which holes in the data should be filled
    for i in range(1, len(time_data)):

        dt = dt_object_from_str(time_data[i])

        prev_dt = dt_object_from_str(time_data[i-1])

        # us: microsecond
        delta_us = round(delta_secs(dt, prev_dt)* 1_000_000)
        delta_us_from_start = round(delta_secs(dt, START_TIME) * 1_000_000)

        # Measurement that take more than 1 second are "bad" measurements
        if delta_us < 1_000_000:
            measurement_dt_list.append(delta_us)
            measurement_time_list.append(delta_us_from_start)
            motion_detected_list.append(motion_data[i])
        else:
            bad_measurement_indices.append(i)
            possible_measures = ceil(delta_us / AVG_TIME_US) - 1

            # Last measure data
            final_measure = motion_data[i]
            final_measurement_time = delta_us_from_start

            # Estimated measurement delta, in which motion was not detected
            estimated_delta = delta_us / possible_measures

            # iter from farthest measurement to nearest measurement 
            # before the final measurement in the measurement-less 
            # time window
            for i in range(possible_measures-1, 0, -1):
                # Go back time `i*estimated_delta` us in time
                measurement_time_list.append(
                    final_measurement_time - estimated_delta * i
                )
                
                measurement_dt_list.append(estimated_delta)
                motion_detected_list.append(estimated_value)  

            # Insert final measure data
            measurement_dt_list.append(estimated_delta)
            measurement_time_list.append(final_measurement_time)
            motion_detected_list.append(final_measure)
    
    #avg_time = sum(measurement_time_list)/len(measurement_time_list)

    csv_title = "est_time_microsecs"
    if show_seconds == True:
        measurement_time_list = [round(i / 1_000_000,6) for i in measurement_time_list]
        csv_title = "est_time_secs"

    print(f"""
Avg. measurement time = {AVG_TIME_US} us
    Long measurements = {len(bad_measurement_indices)}
    Estimated motions = {len(motion_data)} -> {len(motion_detected_list)}
         Estimated dt = {len(time_data)} -> {len(measurement_dt_list)}
   Estimate time list = {len(measurement_time_list)}
""")
    # Create CSV File
    df = pd.DataFrame(
        [
            [
                measurement_time_list[i],
                motion_detected_list[i]
            ] for i in range(len(measurement_time_list))
        ],
        columns=[csv_title, "motion_detected"]
    )

    # Determine the CSV file folder and create it if it does not exist
    if new_csv_folder is None:
        new_csv_folder = ".\\data_analysis\\motion_data"
    os.makedirs(new_csv_folder, exist_ok=True)

    # Determine the name of the file
    if show_seconds == True:
        filename = f"estimated_motion_secs_{estimated_value}.csv" 
    else:
        filename = f"estimated_motion_microsecs_{estimated_value}.csv"

    path_for_new_csv = os.path.join(
        new_csv_folder, filename
    )
    # Save the data to the file
    df.to_csv(path_for_new_csv, index=False)

    plt.plot(measurement_time_list, motion_detected_list, "bo:")
    plt.show()
    # TODO: Apply moving average to also determine 
    # periods with high movement which were not captured by the camera

