def find_poisoned_duration(timeSeries: list, duration: int) -> int:
    total_seconds = 0
    if duration == 0:
        return 0

    for idx in range(len(timeSeries) - 1):
        if timeSeries[idx + 1] - timeSeries[idx] < duration:
            total_seconds += timeSeries[idx + 1] - timeSeries[idx]
        else:
            total_seconds += duration
    total_seconds += duration
    return total_seconds

    # total_seconds  = len(timeSeries) * duration
    # reset_seconds = sum([duration - (timeSeries[x + 1] - timeSeries[x])
    #                      for x in range(len(timeSeries) - 1)
    #                      if timeSeries[x + 1] - timeSeries[x] < duration])
    # total_seconds -= reset_seconds
    # print(total_seconds, reset_seconds)
    # return total_seconds


time_series1 = [1,2 ]
duration1 = 2
print(find_poisoned_duration(time_series1, duration1))